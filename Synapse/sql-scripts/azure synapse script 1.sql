use gold_db
GO

CREATE OR ALTER PROC CreateSQlServerLessView_gold @ViewName NVARCHAR(100)
AS
BEGIN

DECLARE @statement VARCHAR(MAX)
    SET @statement = N'CREATE OR ALTER VIEW ' + @ViewName + ' AS
        SELECT *
        FROM
        OPENROWSET(
        BULK ''https://project1adlsgen2storage.dfs.core.windows.net/gold/SalesLT/'+ @ViewName + '/'',
        FORMAT = ''DELTA''
    ) AS [result]
    '

EXEC (@statement)

END
GO