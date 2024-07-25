import os
import shutil

class TemplateManager:
    def __init__(self):
        self.templates_path = os.path.join(os.getcwd(), "templates")

    def get_template(self, template_name):
        # get a template by name
        template_path = os.path.join(self.templates_path, template_name)
        if os.path.exists(template_path):
            return Template(template_path)
        else:
            return None

    def save_template(self, template_name, template_path):
        # save a new template
        template = Template(template_path)
        template.save(self.templates_path, template_name)

    def create_template_from_questions(self, template_name, questions):
        # create a new template from questions
        template = Template(os.path.join(self.templates_path, template_name))
        template.create_from_questions(questions)
        return template

class Template:
    def __init__(self, path):
        self.path = path

    def save(self, templates_path, template_name):
        # save the template
        shutil.copytree(self.path, os.path.join(templates_path, template_name))

    def create_from_questions(self, questions):
        # create the template from questions
        for question in questions:
            # create a new file based on the question
            file_name = question["file_name"]
            file_path = os.path.join(self.path, file_name)
            with open(file_path, "w") as f:
                f.write(question["content"])
