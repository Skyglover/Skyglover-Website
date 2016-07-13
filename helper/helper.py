def assert_path_uses_template(test_case, path, template):
    response = test_case.client.get(path)
    test_case.assertTemplateUsed(response, template)
