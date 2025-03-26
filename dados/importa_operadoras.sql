LOAD DATA INFILE '/caminho/para/operadoras_ativas.csv'
INTO TABLE operadoras_ativas
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    id_operadora,
    registro_ans,
    cnpj,
    nome_fantasia,
    modalidade,
    logradouro,
    numero,
    complemento,
    bairro,
    cidade,
    uf,
    cep,
    ddd,
    telefone,
    fax,
    email,
    representante,
    cargo_representante,
    data_registro
);