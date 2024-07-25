import os
import shutil
from templates import TemplateManager
from questions import QuestionManager

class Domain:
    def __init__(self):
        self.template_manager = TemplateManager()
        self.question_manager = QuestionManager()

    def create_project(self, template_name):
        # create a new project using the specified template
        template = self.template_manager.get_template(template_name)
        if template:
            project_name = input("Enter project name: ")
            project_path = os.path.join(os.getcwd(), project_name)
            shutil.copytree(template.path, project_path)
            print(f"Project created at {project_path}")
        else:
            print("Template not found")

    def save_template(self, template_name, template_path):
        # save a new template
        self.template_manager.save_template(template_name, template_path)

    def create_template_from_questions(self, template_name):
        # create a new template from questions
        questions = self.question_manager.get_questions()
        template = self.template_manager.create_template_from_questions(template_name, questions)
        if template:
            print(f"Template created at {template.path}")
        else:
            print("Failed to create template")

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Domain CLI')
    subparsers = parser.add_subparsers(dest='command')

    create_project_parser = subparsers.add_parser('create', help='Create a new project')
    create_project_parser.add_argument('template_name', help='Template name')

    save_template_parser = subparsers.add_parser('save', help='Save a new template')
    save_template_parser.add_argument('template_name', help='Template name')
    save_template_parser.add_argument('template_path', help='Template path')

    create_template_from_questions_parser = subparsers.add_parser('create-template', help='Create a new template from questions')
    create_template_from_questions_parser.add_argument('template_name', help='Template name')

    args = parser.parse_args()

    domain = Domain()

    if args.command == 'create':
        domain.create_project(args.template_name)
    elif args.command == 'save':
        domain.save_template(args.template_name, args.template_path)
    elif args.command == 'create-template':
        domain.create_template_from_questions(args.template_name)
    else:
        parser.print_help()
