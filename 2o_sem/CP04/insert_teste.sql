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