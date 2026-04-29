Feature: Uni search

  Scenario Outline: Buscar informacion academica en universidades
    Given que estoy en la pagina principal de Google
    When busco en Google el termino "<universidad>"
    And abro el primer resultado de la busqueda
    Then debo estar en la pagina oficial de "<dominio>"
    When busco en Google dentro de "<dominio>" el termino "<termino>"
    Then debo ver resultados relacionados con "<termino>"
    And los resultados deben pertenecer a "<dominio>"

    Examples:
      | universidad | dominio    | termino      |
      | iteso       | iteso.mx   | carreras     |
      | iteso       | iteso.mx   | admision     |
      | iteso       | iteso.mx   | posgrados    |
      | universidad une | une.edu.mx | licenciaturas |
      | universidad une | une.edu.mx | admision      |
      | universidad une | une.edu.mx | becas         |
      | udg         | udg.mx     | carreras     |
      | udg         | udg.mx     | admision     |
      | udg         | udg.mx     | posgrados    |
