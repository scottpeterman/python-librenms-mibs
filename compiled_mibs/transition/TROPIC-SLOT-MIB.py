# SNMP MIB module (TROPIC-SLOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\1830\TROPIC-SLOT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:11 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(tnSlotMIB,
 tnSlotModules,
 tropicEmptyCard) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSlotMIB",
    "tnSlotModules",
    "tropicEmptyCard")

(tnShelfIndex,) = mibBuilder.importSymbols(
    "TROPIC-SHELF-MIB",
    "tnShelfIndex")

(TropicAdminStateType,
 TropicNewResetType,
 TropicOperationalCapabilityType,
 TropicOperationalStateType,
 TropicSlotIndexType,
 TropicStateQualifierType) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "TropicAdminStateType",
    "TropicNewResetType",
    "TropicOperationalCapabilityType",
    "TropicOperationalStateType",
    "TropicSlotIndexType",
    "TropicStateQualifierType")


# MODULE-IDENTITY

tnSlotMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tnSlotMibModule.setRevisions(
        ("2022-07-22 12:00",
         "2021-11-26 12:00",
         "2020-07-24 12:00",
         "2020-05-15 12:00",
         "2020-05-08 12:00",
         "2020-03-20 12:00",
         "2020-02-28 12:00",
         "2019-12-13 12:00",
         "2019-08-02 12:00",
         "2019-01-18 12:00",
         "2019-01-11 12:00",
         "2018-12-21 12:00",
         "2018-09-28 12:00",
         "2018-06-15 12:00",
         "2018-02-23 12:00",
         "2017-11-24 12:00",
         "2016-11-16 12:00",
         "2016-11-07 12:00",
         "2016-10-20 12:00",
         "2016-07-12 12:00",
         "2014-02-26 12:00",
         "2013-12-06 12:00",
         "2013-05-21 12:00",
         "2010-12-09 12:00",
         "2009-06-25 12:00",
         "2008-10-16 12:00",
         "2008-09-26 12:00",
         "2008-07-25 12:00",
         "2008-03-06 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluWdmSlotSubType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("empty", 1),
          ("mSubType", 2),
          ("rSubType", 3),
          ("hSubType", 4),
          ("eSubType", 5),
          ("lSubType", 6),
          ("fSubType", 7),
          ("qSubType", 8),
          ("lPSubType", 9),
          ("bSubType", 10),
          ("unassigned", 9999))
    )



# MIB Managed Objects in the order of their OIDs

_TnSlotConf_ObjectIdentity = ObjectIdentity
tnSlotConf = _TnSlotConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 1)
)
_TnSlotGroups_ObjectIdentity = ObjectIdentity
tnSlotGroups = _TnSlotGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 1, 1)
)
_TnSlotCompliances_ObjectIdentity = ObjectIdentity
tnSlotCompliances = _TnSlotCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 1, 2)
)
_TnSlotObjs_ObjectIdentity = ObjectIdentity
tnSlotObjs = _TnSlotObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2)
)
_TnSlotBasics_ObjectIdentity = ObjectIdentity
tnSlotBasics = _TnSlotBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2)
)
_TnSlotTable_Object = MibTable
tnSlotTable = _TnSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tnSlotTable.setStatus("current")
_TnSlotEntry_Object = MibTableRow
tnSlotEntry = _TnSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1)
)
tnSlotEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnSlotEntry.setStatus("current")
_TnSlotIndex_Type = TropicSlotIndexType
_TnSlotIndex_Object = MibTableColumn
tnSlotIndex = _TnSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 1),
    _TnSlotIndex_Type()
)
tnSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSlotIndex.setStatus("current")


class _TnSlotProgrammedType_Type(ObjectIdentifier):
    """Custom type tnSlotProgrammedType based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 1)


_TnSlotProgrammedType_Type.__name__ = "ObjectIdentifier"
_TnSlotProgrammedType_Object = MibTableColumn
tnSlotProgrammedType = _TnSlotProgrammedType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 2),
    _TnSlotProgrammedType_Type()
)
tnSlotProgrammedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlotProgrammedType.setStatus("current")


class _TnSlotPresentType_Type(ObjectIdentifier):
    """Custom type tnSlotPresentType based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 1)


_TnSlotPresentType_Type.__name__ = "ObjectIdentifier"
_TnSlotPresentType_Object = MibTableColumn
tnSlotPresentType = _TnSlotPresentType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 3),
    _TnSlotPresentType_Type()
)
tnSlotPresentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSlotPresentType.setStatus("current")


class _TnSlotAdminState_Type(TropicAdminStateType):
    """Custom type tnSlotAdminState based on TropicAdminStateType"""
    defaultValue = 2


_TnSlotAdminState_Type.__name__ = "TropicAdminStateType"
_TnSlotAdminState_Object = MibTableColumn
tnSlotAdminState = _TnSlotAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 4),
    _TnSlotAdminState_Type()
)
tnSlotAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlotAdminState.setStatus("current")


class _TnSlotOperationalState_Type(TropicOperationalStateType):
    """Custom type tnSlotOperationalState based on TropicOperationalStateType"""
    defaultValue = 2


_TnSlotOperationalState_Type.__name__ = "TropicOperationalStateType"
_TnSlotOperationalState_Object = MibTableColumn
tnSlotOperationalState = _TnSlotOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 5),
    _TnSlotOperationalState_Type()
)
tnSlotOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSlotOperationalState.setStatus("current")


class _TnSlotOperationalCapability_Type(TropicOperationalCapabilityType):
    """Custom type tnSlotOperationalCapability based on TropicOperationalCapabilityType"""
    defaultValue = 1


_TnSlotOperationalCapability_Type.__name__ = "TropicOperationalCapabilityType"
_TnSlotOperationalCapability_Object = MibTableColumn
tnSlotOperationalCapability = _TnSlotOperationalCapability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 6),
    _TnSlotOperationalCapability_Type()
)
tnSlotOperationalCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSlotOperationalCapability.setStatus("current")


class _TnSlotStateQualifier_Type(TropicStateQualifierType):
    """Custom type tnSlotStateQualifier based on TropicStateQualifierType"""
    defaultBinValue = "0000001"


_TnSlotStateQualifier_Type.__name__ = "TropicStateQualifierType"
_TnSlotStateQualifier_Object = MibTableColumn
tnSlotStateQualifier = _TnSlotStateQualifier_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 7),
    _TnSlotStateQualifier_Type()
)
tnSlotStateQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSlotStateQualifier.setStatus("current")


class _TnSlotAlmProfName_Type(OctetString):
    """Custom type tnSlotAlmProfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_TnSlotAlmProfName_Type.__name__ = "OctetString"
_TnSlotAlmProfName_Object = MibTableColumn
tnSlotAlmProfName = _TnSlotAlmProfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 17),
    _TnSlotAlmProfName_Type()
)
tnSlotAlmProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlotAlmProfName.setStatus("current")


class _TnSlotMigrationType_Type(ObjectIdentifier):
    """Custom type tnSlotMigrationType based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 1)


_TnSlotMigrationType_Type.__name__ = "ObjectIdentifier"
_TnSlotMigrationType_Object = MibTableColumn
tnSlotMigrationType = _TnSlotMigrationType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 18),
    _TnSlotMigrationType_Type()
)
tnSlotMigrationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlotMigrationType.setStatus("current")


class _TnSlotProgrammedSubType_Type(AluWdmSlotSubType):
    """Custom type tnSlotProgrammedSubType based on AluWdmSlotSubType"""
    defaultValue = 2


_TnSlotProgrammedSubType_Type.__name__ = "AluWdmSlotSubType"
_TnSlotProgrammedSubType_Object = MibTableColumn
tnSlotProgrammedSubType = _TnSlotProgrammedSubType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 19),
    _TnSlotProgrammedSubType_Type()
)
tnSlotProgrammedSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlotProgrammedSubType.setStatus("current")


class _TnSlotPresentSubType_Type(AluWdmSlotSubType):
    """Custom type tnSlotPresentSubType based on AluWdmSlotSubType"""
    defaultValue = 2


_TnSlotPresentSubType_Type.__name__ = "AluWdmSlotSubType"
_TnSlotPresentSubType_Object = MibTableColumn
tnSlotPresentSubType = _TnSlotPresentSubType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 20),
    _TnSlotPresentSubType_Type()
)
tnSlotPresentSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlotPresentSubType.setStatus("current")
_TnSlotProgrammedGenericType_Type = SnmpAdminString
_TnSlotProgrammedGenericType_Object = MibTableColumn
tnSlotProgrammedGenericType = _TnSlotProgrammedGenericType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 21),
    _TnSlotProgrammedGenericType_Type()
)
tnSlotProgrammedGenericType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlotProgrammedGenericType.setStatus("current")
_TnSlotPresentGenericType_Type = SnmpAdminString
_TnSlotPresentGenericType_Object = MibTableColumn
tnSlotPresentGenericType = _TnSlotPresentGenericType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 22),
    _TnSlotPresentGenericType_Type()
)
tnSlotPresentGenericType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSlotPresentGenericType.setStatus("current")


class _TnSlotProgrammedProductCode_Type(SnmpAdminString):
    """Custom type tnSlotProgrammedProductCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnSlotProgrammedProductCode_Type.__name__ = "SnmpAdminString"
_TnSlotProgrammedProductCode_Object = MibTableColumn
tnSlotProgrammedProductCode = _TnSlotProgrammedProductCode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 23),
    _TnSlotProgrammedProductCode_Type()
)
tnSlotProgrammedProductCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlotProgrammedProductCode.setStatus("current")


class _TnSlotProductCodeSup_Type(Integer32):
    """Custom type tnSlotProductCodeSup based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TnSlotProductCodeSup_Type.__name__ = "Integer32"
_TnSlotProductCodeSup_Object = MibTableColumn
tnSlotProductCodeSup = _TnSlotProductCodeSup_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 24),
    _TnSlotProductCodeSup_Type()
)
tnSlotProductCodeSup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlotProductCodeSup.setStatus("current")


class _TnSlotLifeCycleState_Type(SnmpAdminString):
    """Custom type tnSlotLifeCycleState based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_TnSlotLifeCycleState_Type.__name__ = "SnmpAdminString"
_TnSlotLifeCycleState_Object = MibTableColumn
tnSlotLifeCycleState = _TnSlotLifeCycleState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 25),
    _TnSlotLifeCycleState_Type()
)
tnSlotLifeCycleState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlotLifeCycleState.setStatus("current")


class _TnSlotDueDate_Type(SnmpAdminString):
    """Custom type tnSlotDueDate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TnSlotDueDate_Type.__name__ = "SnmpAdminString"
_TnSlotDueDate_Object = MibTableColumn
tnSlotDueDate = _TnSlotDueDate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 26),
    _TnSlotDueDate_Type()
)
tnSlotDueDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlotDueDate.setStatus("current")


class _TnSlotInsertExtract_Type(Integer32):
    """Custom type tnSlotInsertExtract based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2),
          ("remove", 3))
    )


_TnSlotInsertExtract_Type.__name__ = "Integer32"
_TnSlotInsertExtract_Object = MibTableColumn
tnSlotInsertExtract = _TnSlotInsertExtract_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 27),
    _TnSlotInsertExtract_Type()
)
tnSlotInsertExtract.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlotInsertExtract.setStatus("current")


class _TnSlotMigrationSubType_Type(AluWdmSlotSubType):
    """Custom type tnSlotMigrationSubType based on AluWdmSlotSubType"""
    defaultValue = 9999


_TnSlotMigrationSubType_Type.__name__ = "AluWdmSlotSubType"
_TnSlotMigrationSubType_Object = MibTableColumn
tnSlotMigrationSubType = _TnSlotMigrationSubType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 28),
    _TnSlotMigrationSubType_Type()
)
tnSlotMigrationSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlotMigrationSubType.setStatus("current")


class _TnSlotCustomerLifeCycleState_Type(SnmpAdminString):
    """Custom type tnSlotCustomerLifeCycleState based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_TnSlotCustomerLifeCycleState_Type.__name__ = "SnmpAdminString"
_TnSlotCustomerLifeCycleState_Object = MibTableColumn
tnSlotCustomerLifeCycleState = _TnSlotCustomerLifeCycleState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 29),
    _TnSlotCustomerLifeCycleState_Type()
)
tnSlotCustomerLifeCycleState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlotCustomerLifeCycleState.setStatus("current")
_TnSlotKeyGraceEndTime_Type = Integer32
_TnSlotKeyGraceEndTime_Object = MibTableColumn
tnSlotKeyGraceEndTime = _TnSlotKeyGraceEndTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 30),
    _TnSlotKeyGraceEndTime_Type()
)
tnSlotKeyGraceEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSlotKeyGraceEndTime.setStatus("current")
_TnSlotResetTable_Object = MibTable
tnSlotResetTable = _TnSlotResetTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    tnSlotResetTable.setStatus("current")
_TnSlotResetEntry_Object = MibTableRow
tnSlotResetEntry = _TnSlotResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 2, 1)
)
tnSlotResetEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnSlotResetEntry.setStatus("current")


class _TnSlotReset_Type(TropicNewResetType):
    """Custom type tnSlotReset based on TropicNewResetType"""
    defaultValue = 1


_TnSlotReset_Type.__name__ = "TropicNewResetType"
_TnSlotReset_Object = MibTableColumn
tnSlotReset = _TnSlotReset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 2, 1, 1),
    _TnSlotReset_Type()
)
tnSlotReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlotReset.setStatus("current")


class _TnSlotResetReason_Type(Integer32):
    """Custom type tnSlotResetReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("powerReset", 1),
          ("userReset", 2),
          ("ccActivitySwitch", 3),
          ("softwareTrap", 4),
          ("watchdog", 5),
          ("alarmPanelStartupError", 6),
          ("softwareStartupError", 7),
          ("cardCommsError", 8),
          ("softwareAssert", 9),
          ("subcomponentSoftwareBadCrc", 10),
          ("databaseError", 11),
          ("seepError", 12),
          ("subcomponentReset", 13),
          ("warmReset", 14),
          ("coldReset", 15),
          ("userBootReset", 16),
          ("ntpNotResponding", 17),
          ("cardTookNewShelfSerialNumber", 18),
          ("subcomponentStartupError", 19),
          ("inBootJumperSet", 20),
          ("inBootSeep", 21),
          ("inBootBank0Corrupt", 22),
          ("inBootBank1Corrupt", 23),
          ("inBootAppLoadCorrupt", 24),
          ("inBootCrashCountExceeded", 25),
          ("subcomponentWatchdog", 26),
          ("criticalDatabaseStartupError", 27),
          ("redundancyError", 28),
          ("controlNetworkError", 29),
          ("shelfSerialNumberChanged", 30),
          ("swlDiskTransferFailure", 31),
          ("bitSyncCommsFailure", 32),
          ("diskReformatted", 33),
          ("diskMissing", 34),
          ("diskIoError", 35),
          ("cpuStarvation", 36),
          ("uiStarvation", 37),
          ("sonetSdhModeMismatch", 38),
          ("universalCardTypeMismatch", 39),
          ("boardMgrPowerCycle", 40),
          ("boardMgrProcessorReset", 41),
          ("ecProcessExit", 42),
          ("eventNvramAccessFailure", 43),
          ("userCCActivitySwitch", 44))
    )


_TnSlotResetReason_Type.__name__ = "Integer32"
_TnSlotResetReason_Object = MibTableColumn
tnSlotResetReason = _TnSlotResetReason_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 2, 1, 2),
    _TnSlotResetReason_Type()
)
tnSlotResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSlotResetReason.setStatus("current")


class _TnSlotResetTime_Type(Unsigned32):
    """Custom type tnSlotResetTime based on Unsigned32"""
    defaultValue = 0


_TnSlotResetTime_Type.__name__ = "Unsigned32"
_TnSlotResetTime_Object = MibTableColumn
tnSlotResetTime = _TnSlotResetTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 2, 1, 3),
    _TnSlotResetTime_Type()
)
tnSlotResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSlotResetTime.setStatus("current")

# Managed Objects groups

tnSlotGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 1, 1, 1)
)
tnSlotGroup.setObjects(
      *(("TROPIC-SLOT-MIB", "tnSlotProgrammedType"),
        ("TROPIC-SLOT-MIB", "tnSlotPresentType"),
        ("TROPIC-SLOT-MIB", "tnSlotAdminState"),
        ("TROPIC-SLOT-MIB", "tnSlotOperationalState"),
        ("TROPIC-SLOT-MIB", "tnSlotOperationalCapability"),
        ("TROPIC-SLOT-MIB", "tnSlotStateQualifier"),
        ("TROPIC-SLOT-MIB", "tnSlotAlmProfName"),
        ("TROPIC-SLOT-MIB", "tnSlotMigrationType"),
        ("TROPIC-SLOT-MIB", "tnSlotProgrammedSubType"),
        ("TROPIC-SLOT-MIB", "tnSlotPresentSubType"),
        ("TROPIC-SLOT-MIB", "tnSlotProgrammedGenericType"),
        ("TROPIC-SLOT-MIB", "tnSlotPresentGenericType"),
        ("TROPIC-SLOT-MIB", "tnSlotProgrammedProductCode"),
        ("TROPIC-SLOT-MIB", "tnSlotProductCodeSup"),
        ("TROPIC-SLOT-MIB", "tnSlotLifeCycleState"),
        ("TROPIC-SLOT-MIB", "tnSlotDueDate"),
        ("TROPIC-SLOT-MIB", "tnSlotInsertExtract"),
        ("TROPIC-SLOT-MIB", "tnSlotMigrationSubType"),
        ("TROPIC-SLOT-MIB", "tnSlotCustomerLifeCycleState"),
        ("TROPIC-SLOT-MIB", "tnSlotKeyGraceEndTime"))
)
if mibBuilder.loadTexts:
    tnSlotGroup.setStatus("current")

tnSlotResetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 1, 1, 2)
)
tnSlotResetGroup.setObjects(
      *(("TROPIC-SLOT-MIB", "tnSlotReset"),
        ("TROPIC-SLOT-MIB", "tnSlotResetReason"),
        ("TROPIC-SLOT-MIB", "tnSlotResetTime"))
)
if mibBuilder.loadTexts:
    tnSlotResetGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnSlotCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 1, 2, 1)
)
tnSlotCompliance.setObjects(
      *(("TROPIC-SLOT-MIB", "tnSlotGroup"),
        ("TROPIC-SLOT-MIB", "tnSlotResetGroup"))
)
if mibBuilder.loadTexts:
    tnSlotCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-SLOT-MIB",
    **{"AluWdmSlotSubType": AluWdmSlotSubType,
       "tnSlotMibModule": tnSlotMibModule,
       "tnSlotConf": tnSlotConf,
       "tnSlotGroups": tnSlotGroups,
       "tnSlotGroup": tnSlotGroup,
       "tnSlotResetGroup": tnSlotResetGroup,
       "tnSlotCompliances": tnSlotCompliances,
       "tnSlotCompliance": tnSlotCompliance,
       "tnSlotObjs": tnSlotObjs,
       "tnSlotBasics": tnSlotBasics,
       "tnSlotTable": tnSlotTable,
       "tnSlotEntry": tnSlotEntry,
       "tnSlotIndex": tnSlotIndex,
       "tnSlotProgrammedType": tnSlotProgrammedType,
       "tnSlotPresentType": tnSlotPresentType,
       "tnSlotAdminState": tnSlotAdminState,
       "tnSlotOperationalState": tnSlotOperationalState,
       "tnSlotOperationalCapability": tnSlotOperationalCapability,
       "tnSlotStateQualifier": tnSlotStateQualifier,
       "tnSlotAlmProfName": tnSlotAlmProfName,
       "tnSlotMigrationType": tnSlotMigrationType,
       "tnSlotProgrammedSubType": tnSlotProgrammedSubType,
       "tnSlotPresentSubType": tnSlotPresentSubType,
       "tnSlotProgrammedGenericType": tnSlotProgrammedGenericType,
       "tnSlotPresentGenericType": tnSlotPresentGenericType,
       "tnSlotProgrammedProductCode": tnSlotProgrammedProductCode,
       "tnSlotProductCodeSup": tnSlotProductCodeSup,
       "tnSlotLifeCycleState": tnSlotLifeCycleState,
       "tnSlotDueDate": tnSlotDueDate,
       "tnSlotInsertExtract": tnSlotInsertExtract,
       "tnSlotMigrationSubType": tnSlotMigrationSubType,
       "tnSlotCustomerLifeCycleState": tnSlotCustomerLifeCycleState,
       "tnSlotKeyGraceEndTime": tnSlotKeyGraceEndTime,
       "tnSlotResetTable": tnSlotResetTable,
       "tnSlotResetEntry": tnSlotResetEntry,
       "tnSlotReset": tnSlotReset,
       "tnSlotResetReason": tnSlotResetReason,
       "tnSlotResetTime": tnSlotResetTime}
)
