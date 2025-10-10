CREATE TABLE  t_vendas (
    id_venda     NUMBER(6)     NOT NULL PRIMARY KEY,
    nm_comprador VARCHAR2(60)  NOT NULL,
    nm_vendedor  VARCHAR2(60)  NOT NULL,
    dt_venda     DATE          NOT NULL,
    ds_produto   VARCHAR2(150) NOT NULL,
    vl_total     NUMBER(8,2)   NOT NULL,
    vl_impostos  NUMBER(8,2)   NOT NULL
);

CREATE SEQUENCE sq_t_vendas START WITH 1 INCREMENT BY 1 NOCYCLE NOCACHE ORDER;

INSERT INTO t_vendas (id_venda, nm_comprador, nm_vendedor, dt_venda, ds_produto, vl_total, vl_impostos) VALUES (
    sq_t_vendas.NEXTVAL, 
    'Johnny', 
    'Luisa', 
    TO_DATE('10-10-2025', 'DD-MM-YYYY'), 
    'Churros sabor chocolate', 
    2000, 
    300
);

SELECT * FROM t_vendas;