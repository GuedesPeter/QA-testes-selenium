from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class FunctionalTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_pagina_inicial(self):
        self.driver.get('http://127.0.0.1:8000/')
        self.assertIn("Lista de Livros", self.driver.title)

    def test_adicao_livro(self):
        self.driver.get('http://127.0.0.1:8000/adicionar/')
        self.driver.find_element(By.ID, 'id_titulo').send_keys("Novo Livro")
        self.driver.find_element(By.ID, 'id_autor').send_keys("Novo Autor")
        self.driver.find_element(By.ID, 'id_data_publicacao').send_keys("2024-06-09")
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Salvar')]").click()
        time.sleep(2)
        self.driver.get('http://127.0.0.1:8000/')
        self.assertIn("Novo Livro", self.driver.page_source)

    def test_atualizacao_livro(self):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.find_element(By.LINK_TEXT, 'Editar').click()
        titulo_field = self.driver.find_element(By.ID, 'id_titulo')
        titulo_field.clear()
        titulo_field.send_keys("Livro Atualizado")
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Salvar')]").click()
        time.sleep(2)
        self.driver.get('http://127.0.0.1:8000/')
        self.assertIn("Livro Atualizado", self.driver.page_source)

    def test_exclusao_livro(self):
        self.driver.get('http://127.0.0.1:8000/')
        excluir_buttons = self.driver.find_elements(By.XPATH, "//form[@method='post']/button[contains(text(), 'Excluir')]")
        if excluir_buttons:
            excluir_buttons[0].click()
            time.sleep(2)
            self.driver.get('http://127.0.0.1:8000/')
            self.assertNotIn("Livro Atualizado", self.driver.page_source)
        else:
            self.fail("Nenhum botão de exclusão encontrado.")

    

if __name__ == "__main__":
    unittest.main()
