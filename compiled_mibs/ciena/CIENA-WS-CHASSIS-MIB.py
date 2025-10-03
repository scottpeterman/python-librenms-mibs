# SNMP MIB module (CIENA-WS-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-WS-CHASSIS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:03 2025
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

(cienaWsConfig,) = mibBuilder.importSymbols(
    "CIENA-WS-MIB",
    "cienaWsConfig")

(EnabledDisabledEnum,
 LineModuleTypeBits,
 MacString,
 ModuleTypeBits,
 StringMaxl16,
 StringMaxl254,
 StringMaxl32,
 StringMaxl50,
 UpDownEnum,
 YesNoEnum) = mibBuilder.importSymbols(
    "CIENA-WS-TYPEDEFS-MIB",
    "EnabledDisabledEnum",
    "LineModuleTypeBits",
    "MacString",
    "ModuleTypeBits",
    "StringMaxl16",
    "StringMaxl254",
    "StringMaxl32",
    "StringMaxl50",
    "UpDownEnum",
    "YesNoEnum")

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


# MODULE-IDENTITY

cienaWsChassisMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6)
)
if mibBuilder.loadTexts:
    cienaWsChassisMIB.setRevisions(
        ("2017-07-07 00:00",
         "2017-03-02 00:00",
         "2016-12-12 00:00",
         "2016-06-14 00:00",
         "2015-11-29 00:00",
         "2015-06-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ChassisOperationState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uninstalled", 0),
          ("normal", 1),
          ("faulted", 2))
    )



class MacBlockSize(TextualConvention, Unsigned32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CienaWsChassisObjects_ObjectIdentity = ObjectIdentity
cienaWsChassisObjects = _CienaWsChassisObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 1)
)
_CienaWsChassisConformance_ObjectIdentity = ObjectIdentity
cienaWsChassisConformance = _CienaWsChassisConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 2)
)
_CienaWsChassisGroups_ObjectIdentity = ObjectIdentity
cienaWsChassisGroups = _CienaWsChassisGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 2, 1)
)
_CienaWsChassisCompliances_ObjectIdentity = ObjectIdentity
cienaWsChassisCompliances = _CienaWsChassisCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 2, 2)
)
_CwsChassisChassisidentificationTable_Object = MibTable
cwsChassisChassisidentificationTable = _CwsChassisChassisidentificationTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 3)
)
if mibBuilder.loadTexts:
    cwsChassisChassisidentificationTable.setStatus("current")
_CwsChassisChassisidentificationEntry_Object = MibTableRow
cwsChassisChassisidentificationEntry = _CwsChassisChassisidentificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 3, 1)
)
cwsChassisChassisidentificationEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisChassisidentificationTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisChassisidentificationEntry.setStatus("current")


class _CwsChassisChassisidentificationTableSnmpKey_Type(Integer32):
    """Custom type cwsChassisChassisidentificationTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisChassisidentificationTableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisChassisidentificationTableSnmpKey_Object = MibTableColumn
cwsChassisChassisidentificationTableSnmpKey = _CwsChassisChassisidentificationTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 3, 1, 1),
    _CwsChassisChassisidentificationTableSnmpKey_Type()
)
cwsChassisChassisidentificationTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisChassisidentificationTableSnmpKey.setStatus("current")
_CwsChassisChassisidentificationModel_Type = StringMaxl32
_CwsChassisChassisidentificationModel_Object = MibTableColumn
cwsChassisChassisidentificationModel = _CwsChassisChassisidentificationModel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 3, 1, 2),
    _CwsChassisChassisidentificationModel_Type()
)
cwsChassisChassisidentificationModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisChassisidentificationModel.setStatus("current")
_CwsChassisChassisidentificationDescription_Type = StringMaxl254
_CwsChassisChassisidentificationDescription_Object = MibTableColumn
cwsChassisChassisidentificationDescription = _CwsChassisChassisidentificationDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 3, 1, 3),
    _CwsChassisChassisidentificationDescription_Type()
)
cwsChassisChassisidentificationDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisChassisidentificationDescription.setStatus("current")


class _CwsChassisChassisidentificationType_Type(Integer32):
    """Custom type cwsChassisChassisidentificationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknownchassis", 0),
          ("waveserverchassis", 1))
    )


_CwsChassisChassisidentificationType_Type.__name__ = "Integer32"
_CwsChassisChassisidentificationType_Object = MibTableColumn
cwsChassisChassisidentificationType = _CwsChassisChassisidentificationType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 3, 1, 4),
    _CwsChassisChassisidentificationType_Type()
)
cwsChassisChassisidentificationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisChassisidentificationType.setStatus("current")
_CwsChassisChassiscapabilitiesTable_Object = MibTable
cwsChassisChassiscapabilitiesTable = _CwsChassisChassiscapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 4)
)
if mibBuilder.loadTexts:
    cwsChassisChassiscapabilitiesTable.setStatus("current")
_CwsChassisChassiscapabilitiesEntry_Object = MibTableRow
cwsChassisChassiscapabilitiesEntry = _CwsChassisChassiscapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 4, 1)
)
cwsChassisChassiscapabilitiesEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisChassiscapabilitiesTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisChassiscapabilitiesEntry.setStatus("current")


class _CwsChassisChassiscapabilitiesTableSnmpKey_Type(Integer32):
    """Custom type cwsChassisChassiscapabilitiesTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisChassiscapabilitiesTableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisChassiscapabilitiesTableSnmpKey_Object = MibTableColumn
cwsChassisChassiscapabilitiesTableSnmpKey = _CwsChassisChassiscapabilitiesTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 4, 1, 1),
    _CwsChassisChassiscapabilitiesTableSnmpKey_Type()
)
cwsChassisChassiscapabilitiesTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisChassiscapabilitiesTableSnmpKey.setStatus("current")
_CwsChassisChassiscapabilitiesNumOfSlots_Type = Unsigned32
_CwsChassisChassiscapabilitiesNumOfSlots_Object = MibTableColumn
cwsChassisChassiscapabilitiesNumOfSlots = _CwsChassisChassiscapabilitiesNumOfSlots_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 4, 1, 2),
    _CwsChassisChassiscapabilitiesNumOfSlots_Type()
)
cwsChassisChassiscapabilitiesNumOfSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisChassiscapabilitiesNumOfSlots.setStatus("current")
_CwsChassisControlTable_Object = MibTable
cwsChassisControlTable = _CwsChassisControlTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 5)
)
if mibBuilder.loadTexts:
    cwsChassisControlTable.setStatus("current")
_CwsChassisControlEntry_Object = MibTableRow
cwsChassisControlEntry = _CwsChassisControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 5, 1)
)
cwsChassisControlEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisControlTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisControlEntry.setStatus("current")


class _CwsChassisControlTableSnmpKey_Type(Integer32):
    """Custom type cwsChassisControlTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisControlTableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisControlTableSnmpKey_Object = MibTableColumn
cwsChassisControlTableSnmpKey = _CwsChassisControlTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 5, 1, 1),
    _CwsChassisControlTableSnmpKey_Type()
)
cwsChassisControlTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisControlTableSnmpKey.setStatus("current")
_CwsChassisControlCount_Type = Unsigned32
_CwsChassisControlCount_Object = MibTableColumn
cwsChassisControlCount = _CwsChassisControlCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 5, 1, 2),
    _CwsChassisControlCount_Type()
)
cwsChassisControlCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisControlCount.setStatus("current")
_CwsChassisControlType_Type = ModuleTypeBits
_CwsChassisControlType_Object = MibTableColumn
cwsChassisControlType = _CwsChassisControlType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 5, 1, 3),
    _CwsChassisControlType_Type()
)
cwsChassisControlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisControlType.setStatus("current")
_CwsChassisSwitchTable_Object = MibTable
cwsChassisSwitchTable = _CwsChassisSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 6)
)
if mibBuilder.loadTexts:
    cwsChassisSwitchTable.setStatus("current")
_CwsChassisSwitchEntry_Object = MibTableRow
cwsChassisSwitchEntry = _CwsChassisSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 6, 1)
)
cwsChassisSwitchEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisSwitchTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisSwitchEntry.setStatus("current")


class _CwsChassisSwitchTableSnmpKey_Type(Integer32):
    """Custom type cwsChassisSwitchTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisSwitchTableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisSwitchTableSnmpKey_Object = MibTableColumn
cwsChassisSwitchTableSnmpKey = _CwsChassisSwitchTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 6, 1, 1),
    _CwsChassisSwitchTableSnmpKey_Type()
)
cwsChassisSwitchTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisSwitchTableSnmpKey.setStatus("current")
_CwsChassisSwitchCount_Type = Unsigned32
_CwsChassisSwitchCount_Object = MibTableColumn
cwsChassisSwitchCount = _CwsChassisSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 6, 1, 2),
    _CwsChassisSwitchCount_Type()
)
cwsChassisSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisSwitchCount.setStatus("current")
_CwsChassisSwitchType_Type = ModuleTypeBits
_CwsChassisSwitchType_Object = MibTableColumn
cwsChassisSwitchType = _CwsChassisSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 6, 1, 3),
    _CwsChassisSwitchType_Type()
)
cwsChassisSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisSwitchType.setStatus("current")
_CwsChassisIntegratedTable_Object = MibTable
cwsChassisIntegratedTable = _CwsChassisIntegratedTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 7)
)
if mibBuilder.loadTexts:
    cwsChassisIntegratedTable.setStatus("current")
_CwsChassisIntegratedEntry_Object = MibTableRow
cwsChassisIntegratedEntry = _CwsChassisIntegratedEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 7, 1)
)
cwsChassisIntegratedEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisIntegratedTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisIntegratedEntry.setStatus("current")


class _CwsChassisIntegratedTableSnmpKey_Type(Integer32):
    """Custom type cwsChassisIntegratedTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisIntegratedTableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisIntegratedTableSnmpKey_Object = MibTableColumn
cwsChassisIntegratedTableSnmpKey = _CwsChassisIntegratedTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 7, 1, 1),
    _CwsChassisIntegratedTableSnmpKey_Type()
)
cwsChassisIntegratedTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisIntegratedTableSnmpKey.setStatus("current")
_CwsChassisIntegratedCount_Type = Unsigned32
_CwsChassisIntegratedCount_Object = MibTableColumn
cwsChassisIntegratedCount = _CwsChassisIntegratedCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 7, 1, 2),
    _CwsChassisIntegratedCount_Type()
)
cwsChassisIntegratedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisIntegratedCount.setStatus("current")
_CwsChassisIntegratedType_Type = LineModuleTypeBits
_CwsChassisIntegratedType_Object = MibTableColumn
cwsChassisIntegratedType = _CwsChassisIntegratedType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 7, 1, 3),
    _CwsChassisIntegratedType_Type()
)
cwsChassisIntegratedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisIntegratedType.setStatus("current")
_CwsChassisRemovableTable_Object = MibTable
cwsChassisRemovableTable = _CwsChassisRemovableTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 8)
)
if mibBuilder.loadTexts:
    cwsChassisRemovableTable.setStatus("current")
_CwsChassisRemovableEntry_Object = MibTableRow
cwsChassisRemovableEntry = _CwsChassisRemovableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 8, 1)
)
cwsChassisRemovableEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisRemovableTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisRemovableEntry.setStatus("current")


class _CwsChassisRemovableTableSnmpKey_Type(Integer32):
    """Custom type cwsChassisRemovableTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisRemovableTableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisRemovableTableSnmpKey_Object = MibTableColumn
cwsChassisRemovableTableSnmpKey = _CwsChassisRemovableTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 8, 1, 1),
    _CwsChassisRemovableTableSnmpKey_Type()
)
cwsChassisRemovableTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisRemovableTableSnmpKey.setStatus("current")
_CwsChassisRemovableCount_Type = Unsigned32
_CwsChassisRemovableCount_Object = MibTableColumn
cwsChassisRemovableCount = _CwsChassisRemovableCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 8, 1, 2),
    _CwsChassisRemovableCount_Type()
)
cwsChassisRemovableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisRemovableCount.setStatus("current")
_CwsChassisRemovableType_Type = LineModuleTypeBits
_CwsChassisRemovableType_Object = MibTableColumn
cwsChassisRemovableType = _CwsChassisRemovableType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 8, 1, 3),
    _CwsChassisRemovableType_Type()
)
cwsChassisRemovableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisRemovableType.setStatus("current")
_CwsChassisFanTable_Object = MibTable
cwsChassisFanTable = _CwsChassisFanTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 9)
)
if mibBuilder.loadTexts:
    cwsChassisFanTable.setStatus("current")
_CwsChassisFanEntry_Object = MibTableRow
cwsChassisFanEntry = _CwsChassisFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 9, 1)
)
cwsChassisFanEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisFanTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisFanEntry.setStatus("current")


class _CwsChassisFanTableSnmpKey_Type(Integer32):
    """Custom type cwsChassisFanTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisFanTableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisFanTableSnmpKey_Object = MibTableColumn
cwsChassisFanTableSnmpKey = _CwsChassisFanTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 9, 1, 1),
    _CwsChassisFanTableSnmpKey_Type()
)
cwsChassisFanTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisFanTableSnmpKey.setStatus("current")
_CwsChassisFanCount_Type = Unsigned32
_CwsChassisFanCount_Object = MibTableColumn
cwsChassisFanCount = _CwsChassisFanCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 9, 1, 2),
    _CwsChassisFanCount_Type()
)
cwsChassisFanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisFanCount.setStatus("current")
_CwsChassisFanType_Type = ModuleTypeBits
_CwsChassisFanType_Object = MibTableColumn
cwsChassisFanType = _CwsChassisFanType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 9, 1, 3),
    _CwsChassisFanType_Type()
)
cwsChassisFanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisFanType.setStatus("current")
_CwsChassisAirFilterTable_Object = MibTable
cwsChassisAirFilterTable = _CwsChassisAirFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 10)
)
if mibBuilder.loadTexts:
    cwsChassisAirFilterTable.setStatus("current")
_CwsChassisAirFilterEntry_Object = MibTableRow
cwsChassisAirFilterEntry = _CwsChassisAirFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 10, 1)
)
cwsChassisAirFilterEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisAirFilterTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisAirFilterEntry.setStatus("current")


class _CwsChassisAirFilterTableSnmpKey_Type(Integer32):
    """Custom type cwsChassisAirFilterTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisAirFilterTableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisAirFilterTableSnmpKey_Object = MibTableColumn
cwsChassisAirFilterTableSnmpKey = _CwsChassisAirFilterTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 10, 1, 1),
    _CwsChassisAirFilterTableSnmpKey_Type()
)
cwsChassisAirFilterTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisAirFilterTableSnmpKey.setStatus("current")
_CwsChassisAirFilterSupported_Type = YesNoEnum
_CwsChassisAirFilterSupported_Object = MibTableColumn
cwsChassisAirFilterSupported = _CwsChassisAirFilterSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 10, 1, 2),
    _CwsChassisAirFilterSupported_Type()
)
cwsChassisAirFilterSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisAirFilterSupported.setStatus("current")
_CwsChassisAirFilterType_Type = ModuleTypeBits
_CwsChassisAirFilterType_Object = MibTableColumn
cwsChassisAirFilterType = _CwsChassisAirFilterType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 10, 1, 3),
    _CwsChassisAirFilterType_Type()
)
cwsChassisAirFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisAirFilterType.setStatus("current")
_CwsChassisAirFilterActive_Type = YesNoEnum
_CwsChassisAirFilterActive_Object = MibTableColumn
cwsChassisAirFilterActive = _CwsChassisAirFilterActive_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 10, 1, 4),
    _CwsChassisAirFilterActive_Type()
)
cwsChassisAirFilterActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisAirFilterActive.setStatus("current")
_CwsChassisPowerTable_Object = MibTable
cwsChassisPowerTable = _CwsChassisPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 11)
)
if mibBuilder.loadTexts:
    cwsChassisPowerTable.setStatus("current")
_CwsChassisPowerEntry_Object = MibTableRow
cwsChassisPowerEntry = _CwsChassisPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 11, 1)
)
cwsChassisPowerEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisPowerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisPowerEntry.setStatus("current")


class _CwsChassisPowerTableSnmpKey_Type(Integer32):
    """Custom type cwsChassisPowerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisPowerTableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisPowerTableSnmpKey_Object = MibTableColumn
cwsChassisPowerTableSnmpKey = _CwsChassisPowerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 11, 1, 1),
    _CwsChassisPowerTableSnmpKey_Type()
)
cwsChassisPowerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisPowerTableSnmpKey.setStatus("current")
_CwsChassisPowerCount_Type = Unsigned32
_CwsChassisPowerCount_Object = MibTableColumn
cwsChassisPowerCount = _CwsChassisPowerCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 11, 1, 2),
    _CwsChassisPowerCount_Type()
)
cwsChassisPowerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisPowerCount.setStatus("current")
_CwsChassisPowerType_Type = ModuleTypeBits
_CwsChassisPowerType_Object = MibTableColumn
cwsChassisPowerType = _CwsChassisPowerType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 11, 1, 3),
    _CwsChassisPowerType_Type()
)
cwsChassisPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisPowerType.setStatus("current")
_CwsChassisPowerRedundant_Type = YesNoEnum
_CwsChassisPowerRedundant_Object = MibTableColumn
cwsChassisPowerRedundant = _CwsChassisPowerRedundant_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 11, 1, 4),
    _CwsChassisPowerRedundant_Type()
)
cwsChassisPowerRedundant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisPowerRedundant.setStatus("current")
_CwsChassisPowerDcSupport_Type = YesNoEnum
_CwsChassisPowerDcSupport_Object = MibTableColumn
cwsChassisPowerDcSupport = _CwsChassisPowerDcSupport_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 11, 1, 5),
    _CwsChassisPowerDcSupport_Type()
)
cwsChassisPowerDcSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisPowerDcSupport.setStatus("current")
_CwsChassisChassisTable_Object = MibTable
cwsChassisChassisTable = _CwsChassisChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 12)
)
if mibBuilder.loadTexts:
    cwsChassisChassisTable.setStatus("current")
_CwsChassisChassisEntry_Object = MibTableRow
cwsChassisChassisEntry = _CwsChassisChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 12, 1)
)
cwsChassisChassisEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisChassisTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisChassisEntry.setStatus("current")


class _CwsChassisChassisTableSnmpKey_Type(Integer32):
    """Custom type cwsChassisChassisTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisChassisTableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisChassisTableSnmpKey_Object = MibTableColumn
cwsChassisChassisTableSnmpKey = _CwsChassisChassisTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 12, 1, 1),
    _CwsChassisChassisTableSnmpKey_Type()
)
cwsChassisChassisTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisChassisTableSnmpKey.setStatus("current")
_CwsChassisChassisBase_Type = MacString
_CwsChassisChassisBase_Object = MibTableColumn
cwsChassisChassisBase = _CwsChassisChassisBase_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 12, 1, 2),
    _CwsChassisChassisBase_Type()
)
cwsChassisChassisBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisChassisBase.setStatus("current")
_CwsChassisChassisBlockSize_Type = MacBlockSize
_CwsChassisChassisBlockSize_Object = MibTableColumn
cwsChassisChassisBlockSize = _CwsChassisChassisBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 12, 1, 3),
    _CwsChassisChassisBlockSize_Type()
)
cwsChassisChassisBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisChassisBlockSize.setStatus("current")
_CwsChassisLocalManagementTable_Object = MibTable
cwsChassisLocalManagementTable = _CwsChassisLocalManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 13)
)
if mibBuilder.loadTexts:
    cwsChassisLocalManagementTable.setStatus("current")
_CwsChassisLocalManagementEntry_Object = MibTableRow
cwsChassisLocalManagementEntry = _CwsChassisLocalManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 13, 1)
)
cwsChassisLocalManagementEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisLocalManagementTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisLocalManagementEntry.setStatus("current")


class _CwsChassisLocalManagementTableSnmpKey_Type(Integer32):
    """Custom type cwsChassisLocalManagementTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisLocalManagementTableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisLocalManagementTableSnmpKey_Object = MibTableColumn
cwsChassisLocalManagementTableSnmpKey = _CwsChassisLocalManagementTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 13, 1, 1),
    _CwsChassisLocalManagementTableSnmpKey_Type()
)
cwsChassisLocalManagementTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisLocalManagementTableSnmpKey.setStatus("current")
_CwsChassisLocalManagementBase_Type = MacString
_CwsChassisLocalManagementBase_Object = MibTableColumn
cwsChassisLocalManagementBase = _CwsChassisLocalManagementBase_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 13, 1, 2),
    _CwsChassisLocalManagementBase_Type()
)
cwsChassisLocalManagementBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisLocalManagementBase.setStatus("current")
_CwsChassisLocalManagementBlockSize_Type = MacBlockSize
_CwsChassisLocalManagementBlockSize_Object = MibTableColumn
cwsChassisLocalManagementBlockSize = _CwsChassisLocalManagementBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 13, 1, 3),
    _CwsChassisLocalManagementBlockSize_Type()
)
cwsChassisLocalManagementBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisLocalManagementBlockSize.setStatus("current")
_CwsChassisRemoteManagementTable_Object = MibTable
cwsChassisRemoteManagementTable = _CwsChassisRemoteManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 14)
)
if mibBuilder.loadTexts:
    cwsChassisRemoteManagementTable.setStatus("current")
_CwsChassisRemoteManagementEntry_Object = MibTableRow
cwsChassisRemoteManagementEntry = _CwsChassisRemoteManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 14, 1)
)
cwsChassisRemoteManagementEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisRemoteManagementTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisRemoteManagementEntry.setStatus("current")


class _CwsChassisRemoteManagementTableSnmpKey_Type(Integer32):
    """Custom type cwsChassisRemoteManagementTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisRemoteManagementTableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisRemoteManagementTableSnmpKey_Object = MibTableColumn
cwsChassisRemoteManagementTableSnmpKey = _CwsChassisRemoteManagementTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 14, 1, 1),
    _CwsChassisRemoteManagementTableSnmpKey_Type()
)
cwsChassisRemoteManagementTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisRemoteManagementTableSnmpKey.setStatus("current")
_CwsChassisRemoteManagementBase_Type = MacString
_CwsChassisRemoteManagementBase_Object = MibTableColumn
cwsChassisRemoteManagementBase = _CwsChassisRemoteManagementBase_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 14, 1, 2),
    _CwsChassisRemoteManagementBase_Type()
)
cwsChassisRemoteManagementBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisRemoteManagementBase.setStatus("current")
_CwsChassisRemoteManagementBlockSize_Type = MacBlockSize
_CwsChassisRemoteManagementBlockSize_Object = MibTableColumn
cwsChassisRemoteManagementBlockSize = _CwsChassisRemoteManagementBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 14, 1, 3),
    _CwsChassisRemoteManagementBlockSize_Type()
)
cwsChassisRemoteManagementBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisRemoteManagementBlockSize.setStatus("current")
_CwsChassisDcnTable_Object = MibTable
cwsChassisDcnTable = _CwsChassisDcnTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 15)
)
if mibBuilder.loadTexts:
    cwsChassisDcnTable.setStatus("current")
_CwsChassisDcnEntry_Object = MibTableRow
cwsChassisDcnEntry = _CwsChassisDcnEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 15, 1)
)
cwsChassisDcnEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisDcnTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisDcnEntry.setStatus("current")


class _CwsChassisDcnTableSnmpKey_Type(Integer32):
    """Custom type cwsChassisDcnTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisDcnTableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisDcnTableSnmpKey_Object = MibTableColumn
cwsChassisDcnTableSnmpKey = _CwsChassisDcnTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 15, 1, 1),
    _CwsChassisDcnTableSnmpKey_Type()
)
cwsChassisDcnTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisDcnTableSnmpKey.setStatus("current")
_CwsChassisDcnBase_Type = MacString
_CwsChassisDcnBase_Object = MibTableColumn
cwsChassisDcnBase = _CwsChassisDcnBase_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 15, 1, 2),
    _CwsChassisDcnBase_Type()
)
cwsChassisDcnBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisDcnBase.setStatus("current")
_CwsChassisDcnBlockSize_Type = MacBlockSize
_CwsChassisDcnBlockSize_Object = MibTableColumn
cwsChassisDcnBlockSize = _CwsChassisDcnBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 15, 1, 3),
    _CwsChassisDcnBlockSize_Type()
)
cwsChassisDcnBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisDcnBlockSize.setStatus("current")
_CwsChassisIlan1Table_Object = MibTable
cwsChassisIlan1Table = _CwsChassisIlan1Table_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 16)
)
if mibBuilder.loadTexts:
    cwsChassisIlan1Table.setStatus("current")
_CwsChassisIlan1Entry_Object = MibTableRow
cwsChassisIlan1Entry = _CwsChassisIlan1Entry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 16, 1)
)
cwsChassisIlan1Entry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisIlan1TableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisIlan1Entry.setStatus("current")


class _CwsChassisIlan1TableSnmpKey_Type(Integer32):
    """Custom type cwsChassisIlan1TableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisIlan1TableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisIlan1TableSnmpKey_Object = MibTableColumn
cwsChassisIlan1TableSnmpKey = _CwsChassisIlan1TableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 16, 1, 1),
    _CwsChassisIlan1TableSnmpKey_Type()
)
cwsChassisIlan1TableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisIlan1TableSnmpKey.setStatus("current")
_CwsChassisIlan1Base_Type = MacString
_CwsChassisIlan1Base_Object = MibTableColumn
cwsChassisIlan1Base = _CwsChassisIlan1Base_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 16, 1, 2),
    _CwsChassisIlan1Base_Type()
)
cwsChassisIlan1Base.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisIlan1Base.setStatus("current")
_CwsChassisIlan1BlockSize_Type = MacBlockSize
_CwsChassisIlan1BlockSize_Object = MibTableColumn
cwsChassisIlan1BlockSize = _CwsChassisIlan1BlockSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 16, 1, 3),
    _CwsChassisIlan1BlockSize_Type()
)
cwsChassisIlan1BlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisIlan1BlockSize.setStatus("current")
_CwsChassisIlan2Table_Object = MibTable
cwsChassisIlan2Table = _CwsChassisIlan2Table_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 17)
)
if mibBuilder.loadTexts:
    cwsChassisIlan2Table.setStatus("current")
_CwsChassisIlan2Entry_Object = MibTableRow
cwsChassisIlan2Entry = _CwsChassisIlan2Entry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 17, 1)
)
cwsChassisIlan2Entry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisIlan2TableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisIlan2Entry.setStatus("current")


class _CwsChassisIlan2TableSnmpKey_Type(Integer32):
    """Custom type cwsChassisIlan2TableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisIlan2TableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisIlan2TableSnmpKey_Object = MibTableColumn
cwsChassisIlan2TableSnmpKey = _CwsChassisIlan2TableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 17, 1, 1),
    _CwsChassisIlan2TableSnmpKey_Type()
)
cwsChassisIlan2TableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisIlan2TableSnmpKey.setStatus("current")
_CwsChassisIlan2Base_Type = MacString
_CwsChassisIlan2Base_Object = MibTableColumn
cwsChassisIlan2Base = _CwsChassisIlan2Base_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 17, 1, 2),
    _CwsChassisIlan2Base_Type()
)
cwsChassisIlan2Base.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisIlan2Base.setStatus("current")
_CwsChassisIlan2BlockSize_Type = MacBlockSize
_CwsChassisIlan2BlockSize_Object = MibTableColumn
cwsChassisIlan2BlockSize = _CwsChassisIlan2BlockSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 17, 1, 3),
    _CwsChassisIlan2BlockSize_Type()
)
cwsChassisIlan2BlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisIlan2BlockSize.setStatus("current")
_CwsChassisPortsTable_Object = MibTable
cwsChassisPortsTable = _CwsChassisPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 18)
)
if mibBuilder.loadTexts:
    cwsChassisPortsTable.setStatus("current")
_CwsChassisPortsEntry_Object = MibTableRow
cwsChassisPortsEntry = _CwsChassisPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 18, 1)
)
cwsChassisPortsEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisPortsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisPortsEntry.setStatus("current")


class _CwsChassisPortsTableSnmpKey_Type(Integer32):
    """Custom type cwsChassisPortsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisPortsTableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisPortsTableSnmpKey_Object = MibTableColumn
cwsChassisPortsTableSnmpKey = _CwsChassisPortsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 18, 1, 1),
    _CwsChassisPortsTableSnmpKey_Type()
)
cwsChassisPortsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisPortsTableSnmpKey.setStatus("current")
_CwsChassisPortsBase_Type = MacString
_CwsChassisPortsBase_Object = MibTableColumn
cwsChassisPortsBase = _CwsChassisPortsBase_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 18, 1, 2),
    _CwsChassisPortsBase_Type()
)
cwsChassisPortsBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisPortsBase.setStatus("current")
_CwsChassisPortsBlockSize_Type = MacBlockSize
_CwsChassisPortsBlockSize_Object = MibTableColumn
cwsChassisPortsBlockSize = _CwsChassisPortsBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 18, 1, 3),
    _CwsChassisPortsBlockSize_Type()
)
cwsChassisPortsBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisPortsBlockSize.setStatus("current")
_CwsChassisReservedTable_Object = MibTable
cwsChassisReservedTable = _CwsChassisReservedTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 19)
)
if mibBuilder.loadTexts:
    cwsChassisReservedTable.setStatus("current")
_CwsChassisReservedEntry_Object = MibTableRow
cwsChassisReservedEntry = _CwsChassisReservedEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 19, 1)
)
cwsChassisReservedEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisReservedTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisReservedEntry.setStatus("current")


class _CwsChassisReservedTableSnmpKey_Type(Integer32):
    """Custom type cwsChassisReservedTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisReservedTableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisReservedTableSnmpKey_Object = MibTableColumn
cwsChassisReservedTableSnmpKey = _CwsChassisReservedTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 19, 1, 1),
    _CwsChassisReservedTableSnmpKey_Type()
)
cwsChassisReservedTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisReservedTableSnmpKey.setStatus("current")
_CwsChassisReservedBase_Type = MacString
_CwsChassisReservedBase_Object = MibTableColumn
cwsChassisReservedBase = _CwsChassisReservedBase_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 19, 1, 2),
    _CwsChassisReservedBase_Type()
)
cwsChassisReservedBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisReservedBase.setStatus("current")
_CwsChassisReservedBlockSize_Type = MacBlockSize
_CwsChassisReservedBlockSize_Object = MibTableColumn
cwsChassisReservedBlockSize = _CwsChassisReservedBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 19, 1, 3),
    _CwsChassisReservedBlockSize_Type()
)
cwsChassisReservedBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisReservedBlockSize.setStatus("current")
_CwsChassisPowerSupplyUnitsTable_Object = MibTable
cwsChassisPowerSupplyUnitsTable = _CwsChassisPowerSupplyUnitsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 20)
)
if mibBuilder.loadTexts:
    cwsChassisPowerSupplyUnitsTable.setStatus("current")
_CwsChassisPowerSupplyUnitsEntry_Object = MibTableRow
cwsChassisPowerSupplyUnitsEntry = _CwsChassisPowerSupplyUnitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 20, 1)
)
cwsChassisPowerSupplyUnitsEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisPowerSupplyUnitsPsuNumber"),
)
if mibBuilder.loadTexts:
    cwsChassisPowerSupplyUnitsEntry.setStatus("current")


class _CwsChassisPowerSupplyUnitsPsuNumber_Type(Integer32):
    """Custom type cwsChassisPowerSupplyUnitsPsuNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisPowerSupplyUnitsPsuNumber_Type.__name__ = "Integer32"
_CwsChassisPowerSupplyUnitsPsuNumber_Object = MibTableColumn
cwsChassisPowerSupplyUnitsPsuNumber = _CwsChassisPowerSupplyUnitsPsuNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 20, 1, 1),
    _CwsChassisPowerSupplyUnitsPsuNumber_Type()
)
cwsChassisPowerSupplyUnitsPsuNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisPowerSupplyUnitsPsuNumber.setStatus("current")
_CwsChassisPowerSupplyUnitsName_Type = StringMaxl16
_CwsChassisPowerSupplyUnitsName_Object = MibTableColumn
cwsChassisPowerSupplyUnitsName = _CwsChassisPowerSupplyUnitsName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 20, 1, 2),
    _CwsChassisPowerSupplyUnitsName_Type()
)
cwsChassisPowerSupplyUnitsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisPowerSupplyUnitsName.setStatus("current")
_CwsChassisPsuStateTable_Object = MibTable
cwsChassisPsuStateTable = _CwsChassisPsuStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 21)
)
if mibBuilder.loadTexts:
    cwsChassisPsuStateTable.setStatus("current")
_CwsChassisPsuStateEntry_Object = MibTableRow
cwsChassisPsuStateEntry = _CwsChassisPsuStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 21, 1)
)
cwsChassisPsuStateEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisPowerSupplyUnitsPsuNumber"),
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisPsuStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisPsuStateEntry.setStatus("current")


class _CwsChassisPsuStateTableSnmpKey_Type(Integer32):
    """Custom type cwsChassisPsuStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisPsuStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisPsuStateTableSnmpKey_Object = MibTableColumn
cwsChassisPsuStateTableSnmpKey = _CwsChassisPsuStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 21, 1, 1),
    _CwsChassisPsuStateTableSnmpKey_Type()
)
cwsChassisPsuStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisPsuStateTableSnmpKey.setStatus("current")
_CwsChassisPsuStateAdminState_Type = EnabledDisabledEnum
_CwsChassisPsuStateAdminState_Object = MibTableColumn
cwsChassisPsuStateAdminState = _CwsChassisPsuStateAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 21, 1, 2),
    _CwsChassisPsuStateAdminState_Type()
)
cwsChassisPsuStateAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsChassisPsuStateAdminState.setStatus("current")
_CwsChassisPsuStateOperationalState_Type = ChassisOperationState
_CwsChassisPsuStateOperationalState_Object = MibTableColumn
cwsChassisPsuStateOperationalState = _CwsChassisPsuStateOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 21, 1, 3),
    _CwsChassisPsuStateOperationalState_Type()
)
cwsChassisPsuStateOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisPsuStateOperationalState.setStatus("current")
_CwsChassisPsuPropertiesTable_Object = MibTable
cwsChassisPsuPropertiesTable = _CwsChassisPsuPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 22)
)
if mibBuilder.loadTexts:
    cwsChassisPsuPropertiesTable.setStatus("current")
_CwsChassisPsuPropertiesEntry_Object = MibTableRow
cwsChassisPsuPropertiesEntry = _CwsChassisPsuPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 22, 1)
)
cwsChassisPsuPropertiesEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisPowerSupplyUnitsPsuNumber"),
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisPsuPropertiesTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisPsuPropertiesEntry.setStatus("current")


class _CwsChassisPsuPropertiesTableSnmpKey_Type(Integer32):
    """Custom type cwsChassisPsuPropertiesTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisPsuPropertiesTableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisPsuPropertiesTableSnmpKey_Object = MibTableColumn
cwsChassisPsuPropertiesTableSnmpKey = _CwsChassisPsuPropertiesTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 22, 1, 1),
    _CwsChassisPsuPropertiesTableSnmpKey_Type()
)
cwsChassisPsuPropertiesTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisPsuPropertiesTableSnmpKey.setStatus("current")


class _CwsChassisPsuPropertiesType_Type(Integer32):
    """Custom type cwsChassisPsuPropertiesType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ac", 0),
          ("dc", 1),
          ("unequipped", 2))
    )


_CwsChassisPsuPropertiesType_Type.__name__ = "Integer32"
_CwsChassisPsuPropertiesType_Object = MibTableColumn
cwsChassisPsuPropertiesType = _CwsChassisPsuPropertiesType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 22, 1, 2),
    _CwsChassisPsuPropertiesType_Type()
)
cwsChassisPsuPropertiesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisPsuPropertiesType.setStatus("current")
_CwsChassisPsuDeviceIdTable_Object = MibTable
cwsChassisPsuDeviceIdTable = _CwsChassisPsuDeviceIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 23)
)
if mibBuilder.loadTexts:
    cwsChassisPsuDeviceIdTable.setStatus("current")
_CwsChassisPsuDeviceIdEntry_Object = MibTableRow
cwsChassisPsuDeviceIdEntry = _CwsChassisPsuDeviceIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 23, 1)
)
cwsChassisPsuDeviceIdEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisPowerSupplyUnitsPsuNumber"),
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisPsuDeviceIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisPsuDeviceIdEntry.setStatus("current")


class _CwsChassisPsuDeviceIdTableSnmpKey_Type(Integer32):
    """Custom type cwsChassisPsuDeviceIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisPsuDeviceIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisPsuDeviceIdTableSnmpKey_Object = MibTableColumn
cwsChassisPsuDeviceIdTableSnmpKey = _CwsChassisPsuDeviceIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 23, 1, 1),
    _CwsChassisPsuDeviceIdTableSnmpKey_Type()
)
cwsChassisPsuDeviceIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisPsuDeviceIdTableSnmpKey.setStatus("current")
_CwsChassisPsuDeviceIdModel_Type = StringMaxl50
_CwsChassisPsuDeviceIdModel_Object = MibTableColumn
cwsChassisPsuDeviceIdModel = _CwsChassisPsuDeviceIdModel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 23, 1, 2),
    _CwsChassisPsuDeviceIdModel_Type()
)
cwsChassisPsuDeviceIdModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisPsuDeviceIdModel.setStatus("current")
_CwsChassisPsuDeviceIdSerialNumber_Type = StringMaxl50
_CwsChassisPsuDeviceIdSerialNumber_Object = MibTableColumn
cwsChassisPsuDeviceIdSerialNumber = _CwsChassisPsuDeviceIdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 23, 1, 3),
    _CwsChassisPsuDeviceIdSerialNumber_Type()
)
cwsChassisPsuDeviceIdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisPsuDeviceIdSerialNumber.setStatus("current")
_CwsChassisPsuDeviceIdPartNumber_Type = StringMaxl50
_CwsChassisPsuDeviceIdPartNumber_Object = MibTableColumn
cwsChassisPsuDeviceIdPartNumber = _CwsChassisPsuDeviceIdPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 23, 1, 4),
    _CwsChassisPsuDeviceIdPartNumber_Type()
)
cwsChassisPsuDeviceIdPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisPsuDeviceIdPartNumber.setStatus("current")
_CwsChassisPsuDeviceIdRevision_Type = StringMaxl50
_CwsChassisPsuDeviceIdRevision_Object = MibTableColumn
cwsChassisPsuDeviceIdRevision = _CwsChassisPsuDeviceIdRevision_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 23, 1, 5),
    _CwsChassisPsuDeviceIdRevision_Type()
)
cwsChassisPsuDeviceIdRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisPsuDeviceIdRevision.setStatus("current")
_CwsChassisPsuDeviceIdManufactureDate_Type = StringMaxl50
_CwsChassisPsuDeviceIdManufactureDate_Object = MibTableColumn
cwsChassisPsuDeviceIdManufactureDate = _CwsChassisPsuDeviceIdManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 23, 1, 6),
    _CwsChassisPsuDeviceIdManufactureDate_Type()
)
cwsChassisPsuDeviceIdManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisPsuDeviceIdManufactureDate.setStatus("current")
_CwsChassisPsuDeviceIdManufactureLocation_Type = StringMaxl50
_CwsChassisPsuDeviceIdManufactureLocation_Object = MibTableColumn
cwsChassisPsuDeviceIdManufactureLocation = _CwsChassisPsuDeviceIdManufactureLocation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 23, 1, 7),
    _CwsChassisPsuDeviceIdManufactureLocation_Type()
)
cwsChassisPsuDeviceIdManufactureLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisPsuDeviceIdManufactureLocation.setStatus("current")
_CwsChassisCoolingFanUnitsTable_Object = MibTable
cwsChassisCoolingFanUnitsTable = _CwsChassisCoolingFanUnitsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 24)
)
if mibBuilder.loadTexts:
    cwsChassisCoolingFanUnitsTable.setStatus("current")
_CwsChassisCoolingFanUnitsEntry_Object = MibTableRow
cwsChassisCoolingFanUnitsEntry = _CwsChassisCoolingFanUnitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 24, 1)
)
cwsChassisCoolingFanUnitsEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisCoolingFanUnitsCfuNumber"),
)
if mibBuilder.loadTexts:
    cwsChassisCoolingFanUnitsEntry.setStatus("current")


class _CwsChassisCoolingFanUnitsCfuNumber_Type(Integer32):
    """Custom type cwsChassisCoolingFanUnitsCfuNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisCoolingFanUnitsCfuNumber_Type.__name__ = "Integer32"
_CwsChassisCoolingFanUnitsCfuNumber_Object = MibTableColumn
cwsChassisCoolingFanUnitsCfuNumber = _CwsChassisCoolingFanUnitsCfuNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 24, 1, 1),
    _CwsChassisCoolingFanUnitsCfuNumber_Type()
)
cwsChassisCoolingFanUnitsCfuNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisCoolingFanUnitsCfuNumber.setStatus("current")
_CwsChassisCoolingFanUnitsName_Type = StringMaxl16
_CwsChassisCoolingFanUnitsName_Object = MibTableColumn
cwsChassisCoolingFanUnitsName = _CwsChassisCoolingFanUnitsName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 24, 1, 2),
    _CwsChassisCoolingFanUnitsName_Type()
)
cwsChassisCoolingFanUnitsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisCoolingFanUnitsName.setStatus("current")
_CwsChassisFanStateTable_Object = MibTable
cwsChassisFanStateTable = _CwsChassisFanStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 25)
)
if mibBuilder.loadTexts:
    cwsChassisFanStateTable.setStatus("current")
_CwsChassisFanStateEntry_Object = MibTableRow
cwsChassisFanStateEntry = _CwsChassisFanStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 25, 1)
)
cwsChassisFanStateEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisCoolingFanUnitsCfuNumber"),
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisFanStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisFanStateEntry.setStatus("current")


class _CwsChassisFanStateTableSnmpKey_Type(Integer32):
    """Custom type cwsChassisFanStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisFanStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisFanStateTableSnmpKey_Object = MibTableColumn
cwsChassisFanStateTableSnmpKey = _CwsChassisFanStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 25, 1, 1),
    _CwsChassisFanStateTableSnmpKey_Type()
)
cwsChassisFanStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisFanStateTableSnmpKey.setStatus("current")
_CwsChassisFanStateAdminState_Type = EnabledDisabledEnum
_CwsChassisFanStateAdminState_Object = MibTableColumn
cwsChassisFanStateAdminState = _CwsChassisFanStateAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 25, 1, 2),
    _CwsChassisFanStateAdminState_Type()
)
cwsChassisFanStateAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsChassisFanStateAdminState.setStatus("current")
_CwsChassisFanStateOperationalState_Type = ChassisOperationState
_CwsChassisFanStateOperationalState_Object = MibTableColumn
cwsChassisFanStateOperationalState = _CwsChassisFanStateOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 25, 1, 3),
    _CwsChassisFanStateOperationalState_Type()
)
cwsChassisFanStateOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisFanStateOperationalState.setStatus("current")
_CwsChassisFanPropertiesTable_Object = MibTable
cwsChassisFanPropertiesTable = _CwsChassisFanPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 26)
)
if mibBuilder.loadTexts:
    cwsChassisFanPropertiesTable.setStatus("current")
_CwsChassisFanPropertiesEntry_Object = MibTableRow
cwsChassisFanPropertiesEntry = _CwsChassisFanPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 26, 1)
)
cwsChassisFanPropertiesEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisCoolingFanUnitsCfuNumber"),
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisFanPropertiesTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisFanPropertiesEntry.setStatus("current")


class _CwsChassisFanPropertiesTableSnmpKey_Type(Integer32):
    """Custom type cwsChassisFanPropertiesTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisFanPropertiesTableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisFanPropertiesTableSnmpKey_Object = MibTableColumn
cwsChassisFanPropertiesTableSnmpKey = _CwsChassisFanPropertiesTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 26, 1, 1),
    _CwsChassisFanPropertiesTableSnmpKey_Type()
)
cwsChassisFanPropertiesTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisFanPropertiesTableSnmpKey.setStatus("current")
_CwsChassisFanPropertiesAutomaticControl_Type = EnabledDisabledEnum
_CwsChassisFanPropertiesAutomaticControl_Object = MibTableColumn
cwsChassisFanPropertiesAutomaticControl = _CwsChassisFanPropertiesAutomaticControl_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 26, 1, 2),
    _CwsChassisFanPropertiesAutomaticControl_Type()
)
cwsChassisFanPropertiesAutomaticControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisFanPropertiesAutomaticControl.setStatus("current")
_CwsChassisFanPropertiesNumberOfTemperatureSensors_Type = Unsigned32
_CwsChassisFanPropertiesNumberOfTemperatureSensors_Object = MibTableColumn
cwsChassisFanPropertiesNumberOfTemperatureSensors = _CwsChassisFanPropertiesNumberOfTemperatureSensors_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 26, 1, 3),
    _CwsChassisFanPropertiesNumberOfTemperatureSensors_Type()
)
cwsChassisFanPropertiesNumberOfTemperatureSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisFanPropertiesNumberOfTemperatureSensors.setStatus("current")
_CwsChassisFanPropertiesNumberOfFans_Type = Unsigned32
_CwsChassisFanPropertiesNumberOfFans_Object = MibTableColumn
cwsChassisFanPropertiesNumberOfFans = _CwsChassisFanPropertiesNumberOfFans_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 26, 1, 4),
    _CwsChassisFanPropertiesNumberOfFans_Type()
)
cwsChassisFanPropertiesNumberOfFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisFanPropertiesNumberOfFans.setStatus("current")
_CwsChassisStatusTable_Object = MibTable
cwsChassisStatusTable = _CwsChassisStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 27)
)
if mibBuilder.loadTexts:
    cwsChassisStatusTable.setStatus("current")
_CwsChassisStatusEntry_Object = MibTableRow
cwsChassisStatusEntry = _CwsChassisStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 27, 1)
)
cwsChassisStatusEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisCoolingFanUnitsCfuNumber"),
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisStatusFanId"),
)
if mibBuilder.loadTexts:
    cwsChassisStatusEntry.setStatus("current")


class _CwsChassisStatusFanId_Type(Integer32):
    """Custom type cwsChassisStatusFanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisStatusFanId_Type.__name__ = "Integer32"
_CwsChassisStatusFanId_Object = MibTableColumn
cwsChassisStatusFanId = _CwsChassisStatusFanId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 27, 1, 1),
    _CwsChassisStatusFanId_Type()
)
cwsChassisStatusFanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisStatusFanId.setStatus("current")
_CwsChassisStatusCurrentRpm_Type = Unsigned32
_CwsChassisStatusCurrentRpm_Object = MibTableColumn
cwsChassisStatusCurrentRpm = _CwsChassisStatusCurrentRpm_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 27, 1, 2),
    _CwsChassisStatusCurrentRpm_Type()
)
cwsChassisStatusCurrentRpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisStatusCurrentRpm.setStatus("current")
_CwsChassisStatusAverageRpm_Type = Unsigned32
_CwsChassisStatusAverageRpm_Object = MibTableColumn
cwsChassisStatusAverageRpm = _CwsChassisStatusAverageRpm_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 27, 1, 3),
    _CwsChassisStatusAverageRpm_Type()
)
cwsChassisStatusAverageRpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisStatusAverageRpm.setStatus("current")
_CwsChassisStatusMinimumRpm_Type = Unsigned32
_CwsChassisStatusMinimumRpm_Object = MibTableColumn
cwsChassisStatusMinimumRpm = _CwsChassisStatusMinimumRpm_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 27, 1, 4),
    _CwsChassisStatusMinimumRpm_Type()
)
cwsChassisStatusMinimumRpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisStatusMinimumRpm.setStatus("current")
_CwsChassisStatusMaximumRpm_Type = Unsigned32
_CwsChassisStatusMaximumRpm_Object = MibTableColumn
cwsChassisStatusMaximumRpm = _CwsChassisStatusMaximumRpm_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 27, 1, 5),
    _CwsChassisStatusMaximumRpm_Type()
)
cwsChassisStatusMaximumRpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisStatusMaximumRpm.setStatus("current")
_CwsChassisFanDeviceIdTable_Object = MibTable
cwsChassisFanDeviceIdTable = _CwsChassisFanDeviceIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 28)
)
if mibBuilder.loadTexts:
    cwsChassisFanDeviceIdTable.setStatus("current")
_CwsChassisFanDeviceIdEntry_Object = MibTableRow
cwsChassisFanDeviceIdEntry = _CwsChassisFanDeviceIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 28, 1)
)
cwsChassisFanDeviceIdEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisCoolingFanUnitsCfuNumber"),
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisFanDeviceIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisFanDeviceIdEntry.setStatus("current")


class _CwsChassisFanDeviceIdTableSnmpKey_Type(Integer32):
    """Custom type cwsChassisFanDeviceIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisFanDeviceIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisFanDeviceIdTableSnmpKey_Object = MibTableColumn
cwsChassisFanDeviceIdTableSnmpKey = _CwsChassisFanDeviceIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 28, 1, 1),
    _CwsChassisFanDeviceIdTableSnmpKey_Type()
)
cwsChassisFanDeviceIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisFanDeviceIdTableSnmpKey.setStatus("current")
_CwsChassisFanDeviceIdModel_Type = StringMaxl50
_CwsChassisFanDeviceIdModel_Object = MibTableColumn
cwsChassisFanDeviceIdModel = _CwsChassisFanDeviceIdModel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 28, 1, 2),
    _CwsChassisFanDeviceIdModel_Type()
)
cwsChassisFanDeviceIdModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisFanDeviceIdModel.setStatus("current")
_CwsChassisFanDeviceIdSerialNumber_Type = StringMaxl50
_CwsChassisFanDeviceIdSerialNumber_Object = MibTableColumn
cwsChassisFanDeviceIdSerialNumber = _CwsChassisFanDeviceIdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 28, 1, 3),
    _CwsChassisFanDeviceIdSerialNumber_Type()
)
cwsChassisFanDeviceIdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisFanDeviceIdSerialNumber.setStatus("current")
_CwsChassisFanDeviceIdPartNumber_Type = StringMaxl50
_CwsChassisFanDeviceIdPartNumber_Object = MibTableColumn
cwsChassisFanDeviceIdPartNumber = _CwsChassisFanDeviceIdPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 28, 1, 4),
    _CwsChassisFanDeviceIdPartNumber_Type()
)
cwsChassisFanDeviceIdPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisFanDeviceIdPartNumber.setStatus("current")
_CwsChassisFanDeviceIdRevision_Type = StringMaxl50
_CwsChassisFanDeviceIdRevision_Object = MibTableColumn
cwsChassisFanDeviceIdRevision = _CwsChassisFanDeviceIdRevision_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 28, 1, 5),
    _CwsChassisFanDeviceIdRevision_Type()
)
cwsChassisFanDeviceIdRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisFanDeviceIdRevision.setStatus("current")
_CwsChassisFanDeviceIdManufactureDate_Type = StringMaxl50
_CwsChassisFanDeviceIdManufactureDate_Object = MibTableColumn
cwsChassisFanDeviceIdManufactureDate = _CwsChassisFanDeviceIdManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 28, 1, 6),
    _CwsChassisFanDeviceIdManufactureDate_Type()
)
cwsChassisFanDeviceIdManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisFanDeviceIdManufactureDate.setStatus("current")
_CwsChassisFanDeviceIdManufactureLocation_Type = StringMaxl50
_CwsChassisFanDeviceIdManufactureLocation_Object = MibTableColumn
cwsChassisFanDeviceIdManufactureLocation = _CwsChassisFanDeviceIdManufactureLocation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 28, 1, 7),
    _CwsChassisFanDeviceIdManufactureLocation_Type()
)
cwsChassisFanDeviceIdManufactureLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisFanDeviceIdManufactureLocation.setStatus("current")
_CwsChassisDeviceIdTable_Object = MibTable
cwsChassisDeviceIdTable = _CwsChassisDeviceIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 29)
)
if mibBuilder.loadTexts:
    cwsChassisDeviceIdTable.setStatus("current")
_CwsChassisDeviceIdEntry_Object = MibTableRow
cwsChassisDeviceIdEntry = _CwsChassisDeviceIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 29, 1)
)
cwsChassisDeviceIdEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisDeviceIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisDeviceIdEntry.setStatus("current")


class _CwsChassisDeviceIdTableSnmpKey_Type(Integer32):
    """Custom type cwsChassisDeviceIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisDeviceIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisDeviceIdTableSnmpKey_Object = MibTableColumn
cwsChassisDeviceIdTableSnmpKey = _CwsChassisDeviceIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 29, 1, 1),
    _CwsChassisDeviceIdTableSnmpKey_Type()
)
cwsChassisDeviceIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisDeviceIdTableSnmpKey.setStatus("current")
_CwsChassisDeviceIdModuleSerialNumber_Type = StringMaxl50
_CwsChassisDeviceIdModuleSerialNumber_Object = MibTableColumn
cwsChassisDeviceIdModuleSerialNumber = _CwsChassisDeviceIdModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 29, 1, 2),
    _CwsChassisDeviceIdModuleSerialNumber_Type()
)
cwsChassisDeviceIdModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisDeviceIdModuleSerialNumber.setStatus("current")
_CwsChassisDeviceIdModelPartNumber_Type = StringMaxl50
_CwsChassisDeviceIdModelPartNumber_Object = MibTableColumn
cwsChassisDeviceIdModelPartNumber = _CwsChassisDeviceIdModelPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 29, 1, 3),
    _CwsChassisDeviceIdModelPartNumber_Type()
)
cwsChassisDeviceIdModelPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisDeviceIdModelPartNumber.setStatus("current")
_CwsChassisDeviceIdModelRevision_Type = StringMaxl50
_CwsChassisDeviceIdModelRevision_Object = MibTableColumn
cwsChassisDeviceIdModelRevision = _CwsChassisDeviceIdModelRevision_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 29, 1, 4),
    _CwsChassisDeviceIdModelRevision_Type()
)
cwsChassisDeviceIdModelRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisDeviceIdModelRevision.setStatus("current")
_CwsChassisDeviceIdProductId_Type = StringMaxl50
_CwsChassisDeviceIdProductId_Object = MibTableColumn
cwsChassisDeviceIdProductId = _CwsChassisDeviceIdProductId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 29, 1, 5),
    _CwsChassisDeviceIdProductId_Type()
)
cwsChassisDeviceIdProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisDeviceIdProductId.setStatus("current")
_CwsChassisDeviceIdManufactureDate_Type = StringMaxl50
_CwsChassisDeviceIdManufactureDate_Object = MibTableColumn
cwsChassisDeviceIdManufactureDate = _CwsChassisDeviceIdManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 29, 1, 6),
    _CwsChassisDeviceIdManufactureDate_Type()
)
cwsChassisDeviceIdManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisDeviceIdManufactureDate.setStatus("current")
_CwsChassisDeviceIdManufactureLocation_Type = StringMaxl50
_CwsChassisDeviceIdManufactureLocation_Object = MibTableColumn
cwsChassisDeviceIdManufactureLocation = _CwsChassisDeviceIdManufactureLocation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 29, 1, 7),
    _CwsChassisDeviceIdManufactureLocation_Type()
)
cwsChassisDeviceIdManufactureLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisDeviceIdManufactureLocation.setStatus("current")
_CwsChassisDeviceIdBarCode_Type = StringMaxl50
_CwsChassisDeviceIdBarCode_Object = MibTableColumn
cwsChassisDeviceIdBarCode = _CwsChassisDeviceIdBarCode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 29, 1, 8),
    _CwsChassisDeviceIdBarCode_Type()
)
cwsChassisDeviceIdBarCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisDeviceIdBarCode.setStatus("current")
_CwsChassisDeviceIdBoardSerialNumber_Type = StringMaxl50
_CwsChassisDeviceIdBoardSerialNumber_Object = MibTableColumn
cwsChassisDeviceIdBoardSerialNumber = _CwsChassisDeviceIdBoardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 29, 1, 9),
    _CwsChassisDeviceIdBoardSerialNumber_Type()
)
cwsChassisDeviceIdBoardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisDeviceIdBoardSerialNumber.setStatus("current")
_CwsChassisDeviceIdBoardPartNumber_Type = StringMaxl50
_CwsChassisDeviceIdBoardPartNumber_Object = MibTableColumn
cwsChassisDeviceIdBoardPartNumber = _CwsChassisDeviceIdBoardPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 29, 1, 10),
    _CwsChassisDeviceIdBoardPartNumber_Type()
)
cwsChassisDeviceIdBoardPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisDeviceIdBoardPartNumber.setStatus("current")
_CwsChassisDeviceIdBoardRevision_Type = StringMaxl50
_CwsChassisDeviceIdBoardRevision_Object = MibTableColumn
cwsChassisDeviceIdBoardRevision = _CwsChassisDeviceIdBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 29, 1, 11),
    _CwsChassisDeviceIdBoardRevision_Type()
)
cwsChassisDeviceIdBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisDeviceIdBoardRevision.setStatus("current")
_CwsChassisDeviceIdEthernetBaseAddress_Type = StringMaxl50
_CwsChassisDeviceIdEthernetBaseAddress_Object = MibTableColumn
cwsChassisDeviceIdEthernetBaseAddress = _CwsChassisDeviceIdEthernetBaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 29, 1, 12),
    _CwsChassisDeviceIdEthernetBaseAddress_Type()
)
cwsChassisDeviceIdEthernetBaseAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisDeviceIdEthernetBaseAddress.setStatus("current")
_CwsChassisDeviceIdEthernetAddressBlockSize_Type = StringMaxl50
_CwsChassisDeviceIdEthernetAddressBlockSize_Object = MibTableColumn
cwsChassisDeviceIdEthernetAddressBlockSize = _CwsChassisDeviceIdEthernetAddressBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 29, 1, 13),
    _CwsChassisDeviceIdEthernetAddressBlockSize_Type()
)
cwsChassisDeviceIdEthernetAddressBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisDeviceIdEthernetAddressBlockSize.setStatus("current")
_CwsChassisDeviceIdSoftwareCompatibility_Type = StringMaxl50
_CwsChassisDeviceIdSoftwareCompatibility_Object = MibTableColumn
cwsChassisDeviceIdSoftwareCompatibility = _CwsChassisDeviceIdSoftwareCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 29, 1, 14),
    _CwsChassisDeviceIdSoftwareCompatibility_Type()
)
cwsChassisDeviceIdSoftwareCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisDeviceIdSoftwareCompatibility.setStatus("current")
_CwsChassisDeviceIdFunctionalTestCount_Type = StringMaxl50
_CwsChassisDeviceIdFunctionalTestCount_Object = MibTableColumn
cwsChassisDeviceIdFunctionalTestCount = _CwsChassisDeviceIdFunctionalTestCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 29, 1, 15),
    _CwsChassisDeviceIdFunctionalTestCount_Type()
)
cwsChassisDeviceIdFunctionalTestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisDeviceIdFunctionalTestCount.setStatus("current")
_CwsChassisDeviceIdFaultCard_Type = StringMaxl50
_CwsChassisDeviceIdFaultCard_Object = MibTableColumn
cwsChassisDeviceIdFaultCard = _CwsChassisDeviceIdFaultCard_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 29, 1, 16),
    _CwsChassisDeviceIdFaultCard_Type()
)
cwsChassisDeviceIdFaultCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisDeviceIdFaultCard.setStatus("current")
_CwsChassisDeviceIdPackageSerialNumber_Type = StringMaxl50
_CwsChassisDeviceIdPackageSerialNumber_Object = MibTableColumn
cwsChassisDeviceIdPackageSerialNumber = _CwsChassisDeviceIdPackageSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 29, 1, 17),
    _CwsChassisDeviceIdPackageSerialNumber_Type()
)
cwsChassisDeviceIdPackageSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisDeviceIdPackageSerialNumber.setStatus("current")
_CwsChassisDeviceIdPackagePartNumber_Type = StringMaxl50
_CwsChassisDeviceIdPackagePartNumber_Object = MibTableColumn
cwsChassisDeviceIdPackagePartNumber = _CwsChassisDeviceIdPackagePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 29, 1, 18),
    _CwsChassisDeviceIdPackagePartNumber_Type()
)
cwsChassisDeviceIdPackagePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisDeviceIdPackagePartNumber.setStatus("current")
_CwsChassisDeviceIdPackageRevision_Type = StringMaxl50
_CwsChassisDeviceIdPackageRevision_Object = MibTableColumn
cwsChassisDeviceIdPackageRevision = _CwsChassisDeviceIdPackageRevision_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 29, 1, 19),
    _CwsChassisDeviceIdPackageRevision_Type()
)
cwsChassisDeviceIdPackageRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisDeviceIdPackageRevision.setStatus("current")
_CwsChassisManagementPortTable_Object = MibTable
cwsChassisManagementPortTable = _CwsChassisManagementPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 30)
)
if mibBuilder.loadTexts:
    cwsChassisManagementPortTable.setStatus("current")
_CwsChassisManagementPortEntry_Object = MibTableRow
cwsChassisManagementPortEntry = _CwsChassisManagementPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 30, 1)
)
cwsChassisManagementPortEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisManagementPortIndex"),
)
if mibBuilder.loadTexts:
    cwsChassisManagementPortEntry.setStatus("current")


class _CwsChassisManagementPortIndex_Type(Integer32):
    """Custom type cwsChassisManagementPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisManagementPortIndex_Type.__name__ = "Integer32"
_CwsChassisManagementPortIndex_Object = MibTableColumn
cwsChassisManagementPortIndex = _CwsChassisManagementPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 30, 1, 1),
    _CwsChassisManagementPortIndex_Type()
)
cwsChassisManagementPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisManagementPortIndex.setStatus("current")
_CwsChassisIdTable_Object = MibTable
cwsChassisIdTable = _CwsChassisIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 31)
)
if mibBuilder.loadTexts:
    cwsChassisIdTable.setStatus("current")
_CwsChassisIdEntry_Object = MibTableRow
cwsChassisIdEntry = _CwsChassisIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 31, 1)
)
cwsChassisIdEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisManagementPortIndex"),
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisIdEntry.setStatus("current")


class _CwsChassisIdTableSnmpKey_Type(Integer32):
    """Custom type cwsChassisIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisIdTableSnmpKey_Object = MibTableColumn
cwsChassisIdTableSnmpKey = _CwsChassisIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 31, 1, 1),
    _CwsChassisIdTableSnmpKey_Type()
)
cwsChassisIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisIdTableSnmpKey.setStatus("current")
_CwsChassisIdName_Type = StringMaxl16
_CwsChassisIdName_Object = MibTableColumn
cwsChassisIdName = _CwsChassisIdName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 31, 1, 2),
    _CwsChassisIdName_Type()
)
cwsChassisIdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisIdName.setStatus("current")
_CwsChassisStateTable_Object = MibTable
cwsChassisStateTable = _CwsChassisStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 32)
)
if mibBuilder.loadTexts:
    cwsChassisStateTable.setStatus("current")
_CwsChassisStateEntry_Object = MibTableRow
cwsChassisStateEntry = _CwsChassisStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 32, 1)
)
cwsChassisStateEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisManagementPortIndex"),
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisStateEntry.setStatus("current")


class _CwsChassisStateTableSnmpKey_Type(Integer32):
    """Custom type cwsChassisStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisStateTableSnmpKey_Object = MibTableColumn
cwsChassisStateTableSnmpKey = _CwsChassisStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 32, 1, 1),
    _CwsChassisStateTableSnmpKey_Type()
)
cwsChassisStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisStateTableSnmpKey.setStatus("current")
_CwsChassisStateAdminState_Type = EnabledDisabledEnum
_CwsChassisStateAdminState_Object = MibTableColumn
cwsChassisStateAdminState = _CwsChassisStateAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 32, 1, 2),
    _CwsChassisStateAdminState_Type()
)
cwsChassisStateAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsChassisStateAdminState.setStatus("current")
_CwsChassisStateOperationalState_Type = UpDownEnum
_CwsChassisStateOperationalState_Object = MibTableColumn
cwsChassisStateOperationalState = _CwsChassisStateOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 32, 1, 3),
    _CwsChassisStateOperationalState_Type()
)
cwsChassisStateOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisStateOperationalState.setStatus("current")
_CwsChassisPropertiesTable_Object = MibTable
cwsChassisPropertiesTable = _CwsChassisPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 33)
)
if mibBuilder.loadTexts:
    cwsChassisPropertiesTable.setStatus("current")
_CwsChassisPropertiesEntry_Object = MibTableRow
cwsChassisPropertiesEntry = _CwsChassisPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 33, 1)
)
cwsChassisPropertiesEntry.setIndexNames(
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisManagementPortIndex"),
    (0, "CIENA-WS-CHASSIS-MIB", "cwsChassisPropertiesTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsChassisPropertiesEntry.setStatus("current")


class _CwsChassisPropertiesTableSnmpKey_Type(Integer32):
    """Custom type cwsChassisPropertiesTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsChassisPropertiesTableSnmpKey_Type.__name__ = "Integer32"
_CwsChassisPropertiesTableSnmpKey_Object = MibTableColumn
cwsChassisPropertiesTableSnmpKey = _CwsChassisPropertiesTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 33, 1, 1),
    _CwsChassisPropertiesTableSnmpKey_Type()
)
cwsChassisPropertiesTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsChassisPropertiesTableSnmpKey.setStatus("current")


class _CwsChassisPropertiesType_Type(Integer32):
    """Custom type cwsChassisPropertiesType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 0),
          ("serial", 1))
    )


_CwsChassisPropertiesType_Type.__name__ = "Integer32"
_CwsChassisPropertiesType_Object = MibTableColumn
cwsChassisPropertiesType = _CwsChassisPropertiesType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 33, 1, 2),
    _CwsChassisPropertiesType_Type()
)
cwsChassisPropertiesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisPropertiesType.setStatus("current")
_CwsChassisPropertiesMacAddress_Type = MacString
_CwsChassisPropertiesMacAddress_Object = MibTableColumn
cwsChassisPropertiesMacAddress = _CwsChassisPropertiesMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 33, 1, 3),
    _CwsChassisPropertiesMacAddress_Type()
)
cwsChassisPropertiesMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisPropertiesMacAddress.setStatus("current")
_CwsChassisPropertiesMaxFrameSize_Type = Unsigned32
_CwsChassisPropertiesMaxFrameSize_Object = MibTableColumn
cwsChassisPropertiesMaxFrameSize = _CwsChassisPropertiesMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 33, 1, 4),
    _CwsChassisPropertiesMaxFrameSize_Type()
)
cwsChassisPropertiesMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsChassisPropertiesMaxFrameSize.setStatus("current")

# Managed Objects groups

cienaWsChassisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 2, 1, 1)
)
cienaWsChassisGroup.setObjects(
      *(("CIENA-WS-CHASSIS-MIB", "cwsChassisChassisidentificationModel"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisChassisidentificationDescription"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisChassisidentificationType"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisChassiscapabilitiesNumOfSlots"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisControlCount"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisControlType"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisSwitchCount"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisSwitchType"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisIntegratedCount"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisIntegratedType"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisRemovableCount"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisRemovableType"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisFanCount"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisFanType"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisAirFilterSupported"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisAirFilterType"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisAirFilterActive"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisPowerCount"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisPowerType"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisPowerRedundant"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisPowerDcSupport"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisChassisBase"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisChassisBlockSize"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisLocalManagementBase"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisLocalManagementBlockSize"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisRemoteManagementBase"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisRemoteManagementBlockSize"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisDcnBase"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisDcnBlockSize"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisIlan1Base"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisIlan1BlockSize"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisIlan2Base"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisIlan2BlockSize"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisPortsBase"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisPortsBlockSize"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisReservedBase"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisReservedBlockSize"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisPowerSupplyUnitsName"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisPsuStateAdminState"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisPsuStateOperationalState"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisPsuPropertiesType"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisPsuDeviceIdModel"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisPsuDeviceIdSerialNumber"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisPsuDeviceIdPartNumber"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisPsuDeviceIdRevision"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisPsuDeviceIdManufactureDate"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisPsuDeviceIdManufactureLocation"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisCoolingFanUnitsName"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisFanStateAdminState"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisFanStateOperationalState"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisFanPropertiesAutomaticControl"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisFanPropertiesNumberOfTemperatureSensors"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisFanPropertiesNumberOfFans"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisStatusCurrentRpm"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisStatusAverageRpm"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisStatusMinimumRpm"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisStatusMaximumRpm"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisFanDeviceIdModel"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisFanDeviceIdSerialNumber"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisFanDeviceIdPartNumber"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisFanDeviceIdRevision"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisFanDeviceIdManufactureDate"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisFanDeviceIdManufactureLocation"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisDeviceIdModuleSerialNumber"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisDeviceIdModelPartNumber"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisDeviceIdModelRevision"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisDeviceIdProductId"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisDeviceIdManufactureDate"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisDeviceIdManufactureLocation"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisDeviceIdBarCode"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisDeviceIdBoardSerialNumber"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisDeviceIdBoardPartNumber"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisDeviceIdBoardRevision"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisDeviceIdEthernetBaseAddress"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisDeviceIdEthernetAddressBlockSize"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisDeviceIdSoftwareCompatibility"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisDeviceIdFunctionalTestCount"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisDeviceIdFaultCard"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisDeviceIdPackageSerialNumber"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisDeviceIdPackagePartNumber"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisDeviceIdPackageRevision"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisManagementPortIndex"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisIdName"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisStateAdminState"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisStateOperationalState"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisPropertiesType"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisPropertiesMacAddress"),
        ("CIENA-WS-CHASSIS-MIB", "cwsChassisPropertiesMaxFrameSize"))
)
if mibBuilder.loadTexts:
    cienaWsChassisGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cienaWsChassisCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 6, 2, 2, 1)
)
cienaWsChassisCompliance.setObjects(
    ("CIENA-WS-CHASSIS-MIB", "cienaWsChassisGroup")
)
if mibBuilder.loadTexts:
    cienaWsChassisCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-CHASSIS-MIB",
    **{"ChassisOperationState": ChassisOperationState,
       "MacBlockSize": MacBlockSize,
       "cienaWsChassisMIB": cienaWsChassisMIB,
       "cienaWsChassisObjects": cienaWsChassisObjects,
       "cienaWsChassisConformance": cienaWsChassisConformance,
       "cienaWsChassisGroups": cienaWsChassisGroups,
       "cienaWsChassisGroup": cienaWsChassisGroup,
       "cienaWsChassisCompliances": cienaWsChassisCompliances,
       "cienaWsChassisCompliance": cienaWsChassisCompliance,
       "cwsChassisChassisidentificationTable": cwsChassisChassisidentificationTable,
       "cwsChassisChassisidentificationEntry": cwsChassisChassisidentificationEntry,
       "cwsChassisChassisidentificationTableSnmpKey": cwsChassisChassisidentificationTableSnmpKey,
       "cwsChassisChassisidentificationModel": cwsChassisChassisidentificationModel,
       "cwsChassisChassisidentificationDescription": cwsChassisChassisidentificationDescription,
       "cwsChassisChassisidentificationType": cwsChassisChassisidentificationType,
       "cwsChassisChassiscapabilitiesTable": cwsChassisChassiscapabilitiesTable,
       "cwsChassisChassiscapabilitiesEntry": cwsChassisChassiscapabilitiesEntry,
       "cwsChassisChassiscapabilitiesTableSnmpKey": cwsChassisChassiscapabilitiesTableSnmpKey,
       "cwsChassisChassiscapabilitiesNumOfSlots": cwsChassisChassiscapabilitiesNumOfSlots,
       "cwsChassisControlTable": cwsChassisControlTable,
       "cwsChassisControlEntry": cwsChassisControlEntry,
       "cwsChassisControlTableSnmpKey": cwsChassisControlTableSnmpKey,
       "cwsChassisControlCount": cwsChassisControlCount,
       "cwsChassisControlType": cwsChassisControlType,
       "cwsChassisSwitchTable": cwsChassisSwitchTable,
       "cwsChassisSwitchEntry": cwsChassisSwitchEntry,
       "cwsChassisSwitchTableSnmpKey": cwsChassisSwitchTableSnmpKey,
       "cwsChassisSwitchCount": cwsChassisSwitchCount,
       "cwsChassisSwitchType": cwsChassisSwitchType,
       "cwsChassisIntegratedTable": cwsChassisIntegratedTable,
       "cwsChassisIntegratedEntry": cwsChassisIntegratedEntry,
       "cwsChassisIntegratedTableSnmpKey": cwsChassisIntegratedTableSnmpKey,
       "cwsChassisIntegratedCount": cwsChassisIntegratedCount,
       "cwsChassisIntegratedType": cwsChassisIntegratedType,
       "cwsChassisRemovableTable": cwsChassisRemovableTable,
       "cwsChassisRemovableEntry": cwsChassisRemovableEntry,
       "cwsChassisRemovableTableSnmpKey": cwsChassisRemovableTableSnmpKey,
       "cwsChassisRemovableCount": cwsChassisRemovableCount,
       "cwsChassisRemovableType": cwsChassisRemovableType,
       "cwsChassisFanTable": cwsChassisFanTable,
       "cwsChassisFanEntry": cwsChassisFanEntry,
       "cwsChassisFanTableSnmpKey": cwsChassisFanTableSnmpKey,
       "cwsChassisFanCount": cwsChassisFanCount,
       "cwsChassisFanType": cwsChassisFanType,
       "cwsChassisAirFilterTable": cwsChassisAirFilterTable,
       "cwsChassisAirFilterEntry": cwsChassisAirFilterEntry,
       "cwsChassisAirFilterTableSnmpKey": cwsChassisAirFilterTableSnmpKey,
       "cwsChassisAirFilterSupported": cwsChassisAirFilterSupported,
       "cwsChassisAirFilterType": cwsChassisAirFilterType,
       "cwsChassisAirFilterActive": cwsChassisAirFilterActive,
       "cwsChassisPowerTable": cwsChassisPowerTable,
       "cwsChassisPowerEntry": cwsChassisPowerEntry,
       "cwsChassisPowerTableSnmpKey": cwsChassisPowerTableSnmpKey,
       "cwsChassisPowerCount": cwsChassisPowerCount,
       "cwsChassisPowerType": cwsChassisPowerType,
       "cwsChassisPowerRedundant": cwsChassisPowerRedundant,
       "cwsChassisPowerDcSupport": cwsChassisPowerDcSupport,
       "cwsChassisChassisTable": cwsChassisChassisTable,
       "cwsChassisChassisEntry": cwsChassisChassisEntry,
       "cwsChassisChassisTableSnmpKey": cwsChassisChassisTableSnmpKey,
       "cwsChassisChassisBase": cwsChassisChassisBase,
       "cwsChassisChassisBlockSize": cwsChassisChassisBlockSize,
       "cwsChassisLocalManagementTable": cwsChassisLocalManagementTable,
       "cwsChassisLocalManagementEntry": cwsChassisLocalManagementEntry,
       "cwsChassisLocalManagementTableSnmpKey": cwsChassisLocalManagementTableSnmpKey,
       "cwsChassisLocalManagementBase": cwsChassisLocalManagementBase,
       "cwsChassisLocalManagementBlockSize": cwsChassisLocalManagementBlockSize,
       "cwsChassisRemoteManagementTable": cwsChassisRemoteManagementTable,
       "cwsChassisRemoteManagementEntry": cwsChassisRemoteManagementEntry,
       "cwsChassisRemoteManagementTableSnmpKey": cwsChassisRemoteManagementTableSnmpKey,
       "cwsChassisRemoteManagementBase": cwsChassisRemoteManagementBase,
       "cwsChassisRemoteManagementBlockSize": cwsChassisRemoteManagementBlockSize,
       "cwsChassisDcnTable": cwsChassisDcnTable,
       "cwsChassisDcnEntry": cwsChassisDcnEntry,
       "cwsChassisDcnTableSnmpKey": cwsChassisDcnTableSnmpKey,
       "cwsChassisDcnBase": cwsChassisDcnBase,
       "cwsChassisDcnBlockSize": cwsChassisDcnBlockSize,
       "cwsChassisIlan1Table": cwsChassisIlan1Table,
       "cwsChassisIlan1Entry": cwsChassisIlan1Entry,
       "cwsChassisIlan1TableSnmpKey": cwsChassisIlan1TableSnmpKey,
       "cwsChassisIlan1Base": cwsChassisIlan1Base,
       "cwsChassisIlan1BlockSize": cwsChassisIlan1BlockSize,
       "cwsChassisIlan2Table": cwsChassisIlan2Table,
       "cwsChassisIlan2Entry": cwsChassisIlan2Entry,
       "cwsChassisIlan2TableSnmpKey": cwsChassisIlan2TableSnmpKey,
       "cwsChassisIlan2Base": cwsChassisIlan2Base,
       "cwsChassisIlan2BlockSize": cwsChassisIlan2BlockSize,
       "cwsChassisPortsTable": cwsChassisPortsTable,
       "cwsChassisPortsEntry": cwsChassisPortsEntry,
       "cwsChassisPortsTableSnmpKey": cwsChassisPortsTableSnmpKey,
       "cwsChassisPortsBase": cwsChassisPortsBase,
       "cwsChassisPortsBlockSize": cwsChassisPortsBlockSize,
       "cwsChassisReservedTable": cwsChassisReservedTable,
       "cwsChassisReservedEntry": cwsChassisReservedEntry,
       "cwsChassisReservedTableSnmpKey": cwsChassisReservedTableSnmpKey,
       "cwsChassisReservedBase": cwsChassisReservedBase,
       "cwsChassisReservedBlockSize": cwsChassisReservedBlockSize,
       "cwsChassisPowerSupplyUnitsTable": cwsChassisPowerSupplyUnitsTable,
       "cwsChassisPowerSupplyUnitsEntry": cwsChassisPowerSupplyUnitsEntry,
       "cwsChassisPowerSupplyUnitsPsuNumber": cwsChassisPowerSupplyUnitsPsuNumber,
       "cwsChassisPowerSupplyUnitsName": cwsChassisPowerSupplyUnitsName,
       "cwsChassisPsuStateTable": cwsChassisPsuStateTable,
       "cwsChassisPsuStateEntry": cwsChassisPsuStateEntry,
       "cwsChassisPsuStateTableSnmpKey": cwsChassisPsuStateTableSnmpKey,
       "cwsChassisPsuStateAdminState": cwsChassisPsuStateAdminState,
       "cwsChassisPsuStateOperationalState": cwsChassisPsuStateOperationalState,
       "cwsChassisPsuPropertiesTable": cwsChassisPsuPropertiesTable,
       "cwsChassisPsuPropertiesEntry": cwsChassisPsuPropertiesEntry,
       "cwsChassisPsuPropertiesTableSnmpKey": cwsChassisPsuPropertiesTableSnmpKey,
       "cwsChassisPsuPropertiesType": cwsChassisPsuPropertiesType,
       "cwsChassisPsuDeviceIdTable": cwsChassisPsuDeviceIdTable,
       "cwsChassisPsuDeviceIdEntry": cwsChassisPsuDeviceIdEntry,
       "cwsChassisPsuDeviceIdTableSnmpKey": cwsChassisPsuDeviceIdTableSnmpKey,
       "cwsChassisPsuDeviceIdModel": cwsChassisPsuDeviceIdModel,
       "cwsChassisPsuDeviceIdSerialNumber": cwsChassisPsuDeviceIdSerialNumber,
       "cwsChassisPsuDeviceIdPartNumber": cwsChassisPsuDeviceIdPartNumber,
       "cwsChassisPsuDeviceIdRevision": cwsChassisPsuDeviceIdRevision,
       "cwsChassisPsuDeviceIdManufactureDate": cwsChassisPsuDeviceIdManufactureDate,
       "cwsChassisPsuDeviceIdManufactureLocation": cwsChassisPsuDeviceIdManufactureLocation,
       "cwsChassisCoolingFanUnitsTable": cwsChassisCoolingFanUnitsTable,
       "cwsChassisCoolingFanUnitsEntry": cwsChassisCoolingFanUnitsEntry,
       "cwsChassisCoolingFanUnitsCfuNumber": cwsChassisCoolingFanUnitsCfuNumber,
       "cwsChassisCoolingFanUnitsName": cwsChassisCoolingFanUnitsName,
       "cwsChassisFanStateTable": cwsChassisFanStateTable,
       "cwsChassisFanStateEntry": cwsChassisFanStateEntry,
       "cwsChassisFanStateTableSnmpKey": cwsChassisFanStateTableSnmpKey,
       "cwsChassisFanStateAdminState": cwsChassisFanStateAdminState,
       "cwsChassisFanStateOperationalState": cwsChassisFanStateOperationalState,
       "cwsChassisFanPropertiesTable": cwsChassisFanPropertiesTable,
       "cwsChassisFanPropertiesEntry": cwsChassisFanPropertiesEntry,
       "cwsChassisFanPropertiesTableSnmpKey": cwsChassisFanPropertiesTableSnmpKey,
       "cwsChassisFanPropertiesAutomaticControl": cwsChassisFanPropertiesAutomaticControl,
       "cwsChassisFanPropertiesNumberOfTemperatureSensors": cwsChassisFanPropertiesNumberOfTemperatureSensors,
       "cwsChassisFanPropertiesNumberOfFans": cwsChassisFanPropertiesNumberOfFans,
       "cwsChassisStatusTable": cwsChassisStatusTable,
       "cwsChassisStatusEntry": cwsChassisStatusEntry,
       "cwsChassisStatusFanId": cwsChassisStatusFanId,
       "cwsChassisStatusCurrentRpm": cwsChassisStatusCurrentRpm,
       "cwsChassisStatusAverageRpm": cwsChassisStatusAverageRpm,
       "cwsChassisStatusMinimumRpm": cwsChassisStatusMinimumRpm,
       "cwsChassisStatusMaximumRpm": cwsChassisStatusMaximumRpm,
       "cwsChassisFanDeviceIdTable": cwsChassisFanDeviceIdTable,
       "cwsChassisFanDeviceIdEntry": cwsChassisFanDeviceIdEntry,
       "cwsChassisFanDeviceIdTableSnmpKey": cwsChassisFanDeviceIdTableSnmpKey,
       "cwsChassisFanDeviceIdModel": cwsChassisFanDeviceIdModel,
       "cwsChassisFanDeviceIdSerialNumber": cwsChassisFanDeviceIdSerialNumber,
       "cwsChassisFanDeviceIdPartNumber": cwsChassisFanDeviceIdPartNumber,
       "cwsChassisFanDeviceIdRevision": cwsChassisFanDeviceIdRevision,
       "cwsChassisFanDeviceIdManufactureDate": cwsChassisFanDeviceIdManufactureDate,
       "cwsChassisFanDeviceIdManufactureLocation": cwsChassisFanDeviceIdManufactureLocation,
       "cwsChassisDeviceIdTable": cwsChassisDeviceIdTable,
       "cwsChassisDeviceIdEntry": cwsChassisDeviceIdEntry,
       "cwsChassisDeviceIdTableSnmpKey": cwsChassisDeviceIdTableSnmpKey,
       "cwsChassisDeviceIdModuleSerialNumber": cwsChassisDeviceIdModuleSerialNumber,
       "cwsChassisDeviceIdModelPartNumber": cwsChassisDeviceIdModelPartNumber,
       "cwsChassisDeviceIdModelRevision": cwsChassisDeviceIdModelRevision,
       "cwsChassisDeviceIdProductId": cwsChassisDeviceIdProductId,
       "cwsChassisDeviceIdManufactureDate": cwsChassisDeviceIdManufactureDate,
       "cwsChassisDeviceIdManufactureLocation": cwsChassisDeviceIdManufactureLocation,
       "cwsChassisDeviceIdBarCode": cwsChassisDeviceIdBarCode,
       "cwsChassisDeviceIdBoardSerialNumber": cwsChassisDeviceIdBoardSerialNumber,
       "cwsChassisDeviceIdBoardPartNumber": cwsChassisDeviceIdBoardPartNumber,
       "cwsChassisDeviceIdBoardRevision": cwsChassisDeviceIdBoardRevision,
       "cwsChassisDeviceIdEthernetBaseAddress": cwsChassisDeviceIdEthernetBaseAddress,
       "cwsChassisDeviceIdEthernetAddressBlockSize": cwsChassisDeviceIdEthernetAddressBlockSize,
       "cwsChassisDeviceIdSoftwareCompatibility": cwsChassisDeviceIdSoftwareCompatibility,
       "cwsChassisDeviceIdFunctionalTestCount": cwsChassisDeviceIdFunctionalTestCount,
       "cwsChassisDeviceIdFaultCard": cwsChassisDeviceIdFaultCard,
       "cwsChassisDeviceIdPackageSerialNumber": cwsChassisDeviceIdPackageSerialNumber,
       "cwsChassisDeviceIdPackagePartNumber": cwsChassisDeviceIdPackagePartNumber,
       "cwsChassisDeviceIdPackageRevision": cwsChassisDeviceIdPackageRevision,
       "cwsChassisManagementPortTable": cwsChassisManagementPortTable,
       "cwsChassisManagementPortEntry": cwsChassisManagementPortEntry,
       "cwsChassisManagementPortIndex": cwsChassisManagementPortIndex,
       "cwsChassisIdTable": cwsChassisIdTable,
       "cwsChassisIdEntry": cwsChassisIdEntry,
       "cwsChassisIdTableSnmpKey": cwsChassisIdTableSnmpKey,
       "cwsChassisIdName": cwsChassisIdName,
       "cwsChassisStateTable": cwsChassisStateTable,
       "cwsChassisStateEntry": cwsChassisStateEntry,
       "cwsChassisStateTableSnmpKey": cwsChassisStateTableSnmpKey,
       "cwsChassisStateAdminState": cwsChassisStateAdminState,
       "cwsChassisStateOperationalState": cwsChassisStateOperationalState,
       "cwsChassisPropertiesTable": cwsChassisPropertiesTable,
       "cwsChassisPropertiesEntry": cwsChassisPropertiesEntry,
       "cwsChassisPropertiesTableSnmpKey": cwsChassisPropertiesTableSnmpKey,
       "cwsChassisPropertiesType": cwsChassisPropertiesType,
       "cwsChassisPropertiesMacAddress": cwsChassisPropertiesMacAddress,
       "cwsChassisPropertiesMaxFrameSize": cwsChassisPropertiesMaxFrameSize}
)
