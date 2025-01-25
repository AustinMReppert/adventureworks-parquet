from pyspark.sql.types import *
from pyspark.sql.types import StructType, StructField

# Auto-generated schema definitions

AdventureWorksDWBuildVersion_schema = StructType([
    StructField('DBVersion', StringType(), True),
    StructField('VersionDate', TimestampType(), True)
])

DatabaseLog_schema = StructType([
    StructField('DatabaseLogID', IntegerType(), False),
    StructField('PostTime', TimestampType(), False),
    StructField('DatabaseUser', StringType(), False),
    StructField('Event', StringType(), False),
    StructField('Schema', StringType(), True),
    StructField('Object', StringType(), True),
    StructField('TSQL', StringType(), False),
    StructField('XmlEvent', StringType(), False)
])

DimAccount_schema = StructType([
    StructField('AccountKey', IntegerType(), False),
    StructField('ParentAccountKey', IntegerType(), True),
    StructField('AccountCodeAlternateKey', IntegerType(), True),
    StructField('ParentAccountCodeAlternateKey', IntegerType(), True),
    StructField('AccountDescription', StringType(), True),
    StructField('AccountType', StringType(), True),
    StructField('Operator', StringType(), True),
    StructField('CustomMembers', StringType(), True),
    StructField('ValueType', StringType(), True),
    StructField('CustomMemberOptions', StringType(), True)
])

DimCurrency_schema = StructType([
    StructField('CurrencyKey', IntegerType(), False),
    StructField('CurrencyAlternateKey', StringType(), False),
    StructField('CurrencyName', StringType(), False)
])

DimCustomer_schema = StructType([
    StructField('CustomerKey', IntegerType(), False),
    StructField('GeographyKey', IntegerType(), True),
    StructField('CustomerAlternateKey', StringType(), False),
    StructField('Title', StringType(), True),
    StructField('FirstName', StringType(), True),
    StructField('MiddleName', StringType(), True),
    StructField('LastName', StringType(), True),
    StructField('NameStyle', BooleanType(), True),
    StructField('BirthDate', DateType(), True),
    StructField('MaritalStatus', StringType(), True),
    StructField('Suffix', StringType(), True),
    StructField('Gender', StringType(), True),
    StructField('EmailAddress', StringType(), True),
    StructField('YearlyIncome', DecimalType(19,4), True),
    StructField('TotalChildren', ByteType(), True),
    StructField('NumberChildrenAtHome', ByteType(), True),
    StructField('EnglishEducation', StringType(), True),
    StructField('SpanishEducation', StringType(), True),
    StructField('FrenchEducation', StringType(), True),
    StructField('EnglishOccupation', StringType(), True),
    StructField('SpanishOccupation', StringType(), True),
    StructField('FrenchOccupation', StringType(), True),
    StructField('HouseOwnerFlag', StringType(), True),
    StructField('NumberCarsOwned', ByteType(), True),
    StructField('AddressLine1', StringType(), True),
    StructField('AddressLine2', StringType(), True),
    StructField('Phone', StringType(), True),
    StructField('DateFirstPurchase', DateType(), True),
    StructField('CommuteDistance', StringType(), True)
])

DimDate_schema = StructType([
    StructField('DateKey', IntegerType(), False),
    StructField('FullDateAlternateKey', DateType(), False),
    StructField('DayNumberOfWeek', ByteType(), False),
    StructField('EnglishDayNameOfWeek', StringType(), False),
    StructField('SpanishDayNameOfWeek', StringType(), False),
    StructField('FrenchDayNameOfWeek', StringType(), False),
    StructField('DayNumberOfMonth', ByteType(), False),
    StructField('DayNumberOfYear', ShortType(), False),
    StructField('WeekNumberOfYear', ByteType(), False),
    StructField('EnglishMonthName', StringType(), False),
    StructField('SpanishMonthName', StringType(), False),
    StructField('FrenchMonthName', StringType(), False),
    StructField('MonthNumberOfYear', ByteType(), False),
    StructField('CalendarQuarter', ByteType(), False),
    StructField('CalendarYear', ShortType(), False),
    StructField('CalendarSemester', ByteType(), False),
    StructField('FiscalQuarter', ByteType(), False),
    StructField('FiscalYear', ShortType(), False),
    StructField('FiscalSemester', ByteType(), False)
])

DimDepartmentGroup_schema = StructType([
    StructField('DepartmentGroupKey', IntegerType(), False),
    StructField('ParentDepartmentGroupKey', IntegerType(), True),
    StructField('DepartmentGroupName', StringType(), True)
])

DimEmployee_schema = StructType([
    StructField('EmployeeKey', IntegerType(), False),
    StructField('ParentEmployeeKey', IntegerType(), True),
    StructField('EmployeeNationalIDAlternateKey', StringType(), True),
    StructField('ParentEmployeeNationalIDAlternateKey', StringType(), True),
    StructField('SalesTerritoryKey', IntegerType(), True),
    StructField('FirstName', StringType(), False),
    StructField('LastName', StringType(), False),
    StructField('MiddleName', StringType(), True),
    StructField('NameStyle', BooleanType(), False),
    StructField('Title', StringType(), True),
    StructField('HireDate', DateType(), True),
    StructField('BirthDate', DateType(), True),
    StructField('LoginID', StringType(), True),
    StructField('EmailAddress', StringType(), True),
    StructField('Phone', StringType(), True),
    StructField('MaritalStatus', StringType(), True),
    StructField('EmergencyContactName', StringType(), True),
    StructField('EmergencyContactPhone', StringType(), True),
    StructField('SalariedFlag', BooleanType(), True),
    StructField('Gender', StringType(), True),
    StructField('PayFrequency', ByteType(), True),
    StructField('BaseRate', DecimalType(19,4), True),
    StructField('VacationHours', ShortType(), True),
    StructField('SickLeaveHours', ShortType(), True),
    StructField('CurrentFlag', BooleanType(), False),
    StructField('SalesPersonFlag', BooleanType(), False),
    StructField('DepartmentName', StringType(), True),
    StructField('StartDate', DateType(), True),
    StructField('EndDate', DateType(), True),
    StructField('Status', StringType(), True),
    StructField('EmployeePhoto', BinaryType(), True)
])

DimGeography_schema = StructType([
    StructField('GeographyKey', IntegerType(), False),
    StructField('City', StringType(), True),
    StructField('StateProvinceCode', StringType(), True),
    StructField('StateProvinceName', StringType(), True),
    StructField('CountryRegionCode', StringType(), True),
    StructField('EnglishCountryRegionName', StringType(), True),
    StructField('SpanishCountryRegionName', StringType(), True),
    StructField('FrenchCountryRegionName', StringType(), True),
    StructField('PostalCode', StringType(), True),
    StructField('SalesTerritoryKey', IntegerType(), True),
    StructField('IpAddressLocator', StringType(), True)
])

DimOrganization_schema = StructType([
    StructField('OrganizationKey', IntegerType(), False),
    StructField('ParentOrganizationKey', IntegerType(), True),
    StructField('PercentageOfOwnership', StringType(), True),
    StructField('OrganizationName', StringType(), True),
    StructField('CurrencyKey', IntegerType(), True)
])

DimProduct_schema = StructType([
    StructField('ProductKey', IntegerType(), False),
    StructField('ProductAlternateKey', StringType(), True),
    StructField('ProductSubcategoryKey', IntegerType(), True),
    StructField('WeightUnitMeasureCode', StringType(), True),
    StructField('SizeUnitMeasureCode', StringType(), True),
    StructField('EnglishProductName', StringType(), False),
    StructField('SpanishProductName', StringType(), False),
    StructField('FrenchProductName', StringType(), False),
    StructField('StandardCost', DecimalType(19,4), True),
    StructField('FinishedGoodsFlag', BooleanType(), False),
    StructField('Color', StringType(), False),
    StructField('SafetyStockLevel', ShortType(), True),
    StructField('ReorderPoint', ShortType(), True),
    StructField('ListPrice', DecimalType(19,4), True),
    StructField('Size', StringType(), True),
    StructField('SizeRange', StringType(), True),
    StructField('Weight', DoubleType(), True),
    StructField('DaysToManufacture', IntegerType(), True),
    StructField('ProductLine', StringType(), True),
    StructField('DealerPrice', DecimalType(19,4), True),
    StructField('Class', StringType(), True),
    StructField('Style', StringType(), True),
    StructField('ModelName', StringType(), True),
    StructField('LargePhoto', BinaryType(), True),
    StructField('EnglishDescription', StringType(), True),
    StructField('FrenchDescription', StringType(), True),
    StructField('ChineseDescription', StringType(), True),
    StructField('ArabicDescription', StringType(), True),
    StructField('HebrewDescription', StringType(), True),
    StructField('ThaiDescription', StringType(), True),
    StructField('GermanDescription', StringType(), True),
    StructField('JapaneseDescription', StringType(), True),
    StructField('TurkishDescription', StringType(), True),
    StructField('StartDate', TimestampType(), True),
    StructField('EndDate', TimestampType(), True),
    StructField('Status', StringType(), True)
])

DimProductCategory_schema = StructType([
    StructField('ProductCategoryKey', IntegerType(), False),
    StructField('ProductCategoryAlternateKey', IntegerType(), True),
    StructField('EnglishProductCategoryName', StringType(), False),
    StructField('SpanishProductCategoryName', StringType(), False),
    StructField('FrenchProductCategoryName', StringType(), False)
])

DimProductSubcategory_schema = StructType([
    StructField('ProductSubcategoryKey', IntegerType(), False),
    StructField('ProductSubcategoryAlternateKey', IntegerType(), True),
    StructField('EnglishProductSubcategoryName', StringType(), False),
    StructField('SpanishProductSubcategoryName', StringType(), False),
    StructField('FrenchProductSubcategoryName', StringType(), False),
    StructField('ProductCategoryKey', IntegerType(), True)
])

DimPromotion_schema = StructType([
    StructField('PromotionKey', IntegerType(), False),
    StructField('PromotionAlternateKey', IntegerType(), True),
    StructField('EnglishPromotionName', StringType(), True),
    StructField('SpanishPromotionName', StringType(), True),
    StructField('FrenchPromotionName', StringType(), True),
    StructField('DiscountPct', DoubleType(), True),
    StructField('EnglishPromotionType', StringType(), True),
    StructField('SpanishPromotionType', StringType(), True),
    StructField('FrenchPromotionType', StringType(), True),
    StructField('EnglishPromotionCategory', StringType(), True),
    StructField('SpanishPromotionCategory', StringType(), True),
    StructField('FrenchPromotionCategory', StringType(), True),
    StructField('StartDate', TimestampType(), False),
    StructField('EndDate', TimestampType(), True),
    StructField('MinQty', IntegerType(), True),
    StructField('MaxQty', IntegerType(), True)
])

DimReseller_schema = StructType([
    StructField('ResellerKey', IntegerType(), False),
    StructField('GeographyKey', IntegerType(), True),
    StructField('ResellerAlternateKey', StringType(), True),
    StructField('Phone', StringType(), True),
    StructField('BusinessType', StringType(), False),
    StructField('ResellerName', StringType(), False),
    StructField('NumberEmployees', IntegerType(), True),
    StructField('OrderFrequency', StringType(), True),
    StructField('OrderMonth', ByteType(), True),
    StructField('FirstOrderYear', IntegerType(), True),
    StructField('LastOrderYear', IntegerType(), True),
    StructField('ProductLine', StringType(), True),
    StructField('AddressLine1', StringType(), True),
    StructField('AddressLine2', StringType(), True),
    StructField('AnnualSales', DecimalType(19,4), True),
    StructField('BankName', StringType(), True),
    StructField('MinPaymentType', ByteType(), True),
    StructField('MinPaymentAmount', DecimalType(19,4), True),
    StructField('AnnualRevenue', DecimalType(19,4), True),
    StructField('YearOpened', IntegerType(), True)
])

DimSalesReason_schema = StructType([
    StructField('SalesReasonKey', IntegerType(), False),
    StructField('SalesReasonAlternateKey', IntegerType(), False),
    StructField('SalesReasonName', StringType(), False),
    StructField('SalesReasonReasonType', StringType(), False)
])

DimSalesTerritory_schema = StructType([
    StructField('SalesTerritoryKey', IntegerType(), False),
    StructField('SalesTerritoryAlternateKey', IntegerType(), True),
    StructField('SalesTerritoryRegion', StringType(), False),
    StructField('SalesTerritoryCountry', StringType(), False),
    StructField('SalesTerritoryGroup', StringType(), True),
    StructField('SalesTerritoryImage', BinaryType(), True)
])

DimScenario_schema = StructType([
    StructField('ScenarioKey', IntegerType(), False),
    StructField('ScenarioName', StringType(), True)
])

FactAdditionalInternationalProductDescription_schema = StructType([
    StructField('ProductKey', IntegerType(), False),
    StructField('CultureName', StringType(), False),
    StructField('ProductDescription', StringType(), False)
])

FactCallCenter_schema = StructType([
    StructField('FactCallCenterID', IntegerType(), False),
    StructField('DateKey', IntegerType(), False),
    StructField('WageType', StringType(), False),
    StructField('Shift', StringType(), False),
    StructField('LevelOneOperators', ShortType(), False),
    StructField('LevelTwoOperators', ShortType(), False),
    StructField('TotalOperators', ShortType(), False),
    StructField('Calls', IntegerType(), False),
    StructField('AutomaticResponses', IntegerType(), False),
    StructField('Orders', IntegerType(), False),
    StructField('IssuesRaised', ShortType(), False),
    StructField('AverageTimePerIssue', ShortType(), False),
    StructField('ServiceGrade', DoubleType(), False),
    StructField('Date', TimestampType(), True)
])

FactCurrencyRate_schema = StructType([
    StructField('CurrencyKey', IntegerType(), False),
    StructField('DateKey', IntegerType(), False),
    StructField('AverageRate', DoubleType(), False),
    StructField('EndOfDayRate', DoubleType(), False),
    StructField('Date', TimestampType(), True)
])

FactFinance_schema = StructType([
    StructField('FinanceKey', IntegerType(), False),
    StructField('DateKey', IntegerType(), False),
    StructField('OrganizationKey', IntegerType(), False),
    StructField('DepartmentGroupKey', IntegerType(), False),
    StructField('ScenarioKey', IntegerType(), False),
    StructField('AccountKey', IntegerType(), False),
    StructField('Amount', DoubleType(), False),
    StructField('Date', TimestampType(), True)
])

FactInternetSales_schema = StructType([
    StructField('ProductKey', IntegerType(), False),
    StructField('OrderDateKey', IntegerType(), False),
    StructField('DueDateKey', IntegerType(), False),
    StructField('ShipDateKey', IntegerType(), False),
    StructField('CustomerKey', IntegerType(), False),
    StructField('PromotionKey', IntegerType(), False),
    StructField('CurrencyKey', IntegerType(), False),
    StructField('SalesTerritoryKey', IntegerType(), False),
    StructField('SalesOrderNumber', StringType(), False),
    StructField('SalesOrderLineNumber', ByteType(), False),
    StructField('RevisionNumber', ByteType(), False),
    StructField('OrderQuantity', ShortType(), False),
    StructField('UnitPrice', DecimalType(19,4), False),
    StructField('ExtendedAmount', DecimalType(19,4), False),
    StructField('UnitPriceDiscountPct', DoubleType(), False),
    StructField('DiscountAmount', DoubleType(), False),
    StructField('ProductStandardCost', DecimalType(19,4), False),
    StructField('TotalProductCost', DecimalType(19,4), False),
    StructField('SalesAmount', DecimalType(19,4), False),
    StructField('TaxAmt', DecimalType(19,4), False),
    StructField('Freight', DecimalType(19,4), False),
    StructField('CarrierTrackingNumber', StringType(), True),
    StructField('CustomerPONumber', StringType(), True),
    StructField('OrderDate', TimestampType(), True),
    StructField('DueDate', TimestampType(), True),
    StructField('ShipDate', TimestampType(), True)
])

FactInternetSalesReason_schema = StructType([
    StructField('SalesOrderNumber', StringType(), False),
    StructField('SalesOrderLineNumber', ByteType(), False),
    StructField('SalesReasonKey', IntegerType(), False)
])

FactProductInventory_schema = StructType([
    StructField('ProductKey', IntegerType(), False),
    StructField('DateKey', IntegerType(), False),
    StructField('MovementDate', DateType(), False),
    StructField('UnitCost', DecimalType(19,4), False),
    StructField('UnitsIn', IntegerType(), False),
    StructField('UnitsOut', IntegerType(), False),
    StructField('UnitsBalance', IntegerType(), False)
])

FactResellerSales_schema = StructType([
    StructField('ProductKey', IntegerType(), False),
    StructField('OrderDateKey', IntegerType(), False),
    StructField('DueDateKey', IntegerType(), False),
    StructField('ShipDateKey', IntegerType(), False),
    StructField('ResellerKey', IntegerType(), False),
    StructField('EmployeeKey', IntegerType(), False),
    StructField('PromotionKey', IntegerType(), False),
    StructField('CurrencyKey', IntegerType(), False),
    StructField('SalesTerritoryKey', IntegerType(), False),
    StructField('SalesOrderNumber', StringType(), False),
    StructField('SalesOrderLineNumber', ByteType(), False),
    StructField('RevisionNumber', ByteType(), True),
    StructField('OrderQuantity', ShortType(), True),
    StructField('UnitPrice', DecimalType(19,4), True),
    StructField('ExtendedAmount', DecimalType(19,4), True),
    StructField('UnitPriceDiscountPct', DoubleType(), True),
    StructField('DiscountAmount', DoubleType(), True),
    StructField('ProductStandardCost', DecimalType(19,4), True),
    StructField('TotalProductCost', DecimalType(19,4), True),
    StructField('SalesAmount', DecimalType(19,4), True),
    StructField('TaxAmt', DecimalType(19,4), True),
    StructField('Freight', DecimalType(19,4), True),
    StructField('CarrierTrackingNumber', StringType(), True),
    StructField('CustomerPONumber', StringType(), True),
    StructField('OrderDate', TimestampType(), True),
    StructField('DueDate', TimestampType(), True),
    StructField('ShipDate', TimestampType(), True)
])

FactSalesQuota_schema = StructType([
    StructField('SalesQuotaKey', IntegerType(), False),
    StructField('EmployeeKey', IntegerType(), False),
    StructField('DateKey', IntegerType(), False),
    StructField('CalendarYear', ShortType(), False),
    StructField('CalendarQuarter', ByteType(), False),
    StructField('SalesAmountQuota', DecimalType(19,4), False),
    StructField('Date', TimestampType(), True)
])

FactSurveyResponse_schema = StructType([
    StructField('SurveyResponseKey', IntegerType(), False),
    StructField('DateKey', IntegerType(), False),
    StructField('CustomerKey', IntegerType(), False),
    StructField('ProductCategoryKey', IntegerType(), False),
    StructField('EnglishProductCategoryName', StringType(), False),
    StructField('ProductSubcategoryKey', IntegerType(), False),
    StructField('EnglishProductSubcategoryName', StringType(), False),
    StructField('Date', TimestampType(), True)
])

NewFactCurrencyRate_schema = StructType([
    StructField('AverageRate', FloatType(), True),
    StructField('CurrencyID', StringType(), True),
    StructField('CurrencyDate', DateType(), True),
    StructField('EndOfDayRate', FloatType(), True),
    StructField('CurrencyKey', IntegerType(), True),
    StructField('DateKey', IntegerType(), True)
])

ProspectiveBuyer_schema = StructType([
    StructField('ProspectiveBuyerKey', IntegerType(), False),
    StructField('ProspectAlternateKey', StringType(), True),
    StructField('FirstName', StringType(), True),
    StructField('MiddleName', StringType(), True),
    StructField('LastName', StringType(), True),
    StructField('BirthDate', TimestampType(), True),
    StructField('MaritalStatus', StringType(), True),
    StructField('Gender', StringType(), True),
    StructField('EmailAddress', StringType(), True),
    StructField('YearlyIncome', DecimalType(19,4), True),
    StructField('TotalChildren', ByteType(), True),
    StructField('NumberChildrenAtHome', ByteType(), True),
    StructField('Education', StringType(), True),
    StructField('Occupation', StringType(), True),
    StructField('HouseOwnerFlag', StringType(), True),
    StructField('NumberCarsOwned', ByteType(), True),
    StructField('AddressLine1', StringType(), True),
    StructField('AddressLine2', StringType(), True),
    StructField('City', StringType(), True),
    StructField('StateProvinceCode', StringType(), True),
    StructField('PostalCode', StringType(), True),
    StructField('Phone', StringType(), True),
    StructField('Salutation', StringType(), True),
    StructField('Unknown', IntegerType(), True)
])

sysdiagrams_schema = StructType([
    StructField('name', StringType(), False),
    StructField('principal_id', IntegerType(), False),
    StructField('diagram_id', IntegerType(), False),
    StructField('version', IntegerType(), True),
    StructField('definition', BinaryType(), True)
])
