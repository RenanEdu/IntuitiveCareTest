-- Cria~ção da tabela para os dados cadastrais das operadoras
CREATE TABLE operadoras_ativas (
    id_operadora INT PRIMARY KEY,
    registro_ans VARCHAR(20),
    cnpj VARCHAR(20),
    razao_social VARCHAR(225),
    nome_fantasia VARCHAR(225),
    modalidade VARCHAR(50),
    logradouro VARCHAR(20),
    numero VARCHAR(20),
    complemento VARCHAR(225),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf CHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(5),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    email VARCHAR(20),
    representante VARCHAR(255),
    cargo_representante VARCHAR(100),
    data_registro DATE
)