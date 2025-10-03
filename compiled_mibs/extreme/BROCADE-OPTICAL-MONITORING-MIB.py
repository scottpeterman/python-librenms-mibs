# SNMP MIB module (BROCADE-OPTICAL-MONITORING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\extreme\BROCADE-OPTICAL-MONITORING-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:43:15 2025
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

(bcsiModules,) = mibBuilder.importSymbols(
    "Brocade-REG-MIB",
    "bcsiModules")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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


# MODULE-IDENTITY

brocadeOpticalMonitoringMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8)
)
if mibBuilder.loadTexts:
    brocadeOpticalMonitoringMIB.setRevisions(
        ("2019-09-23 00:00",
         "2018-05-29 12:00",
         "2016-11-23 00:00",
         "2016-09-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BcsiOptMonNotifications_ObjectIdentity = ObjectIdentity
bcsiOptMonNotifications = _BcsiOptMonNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 0)
)
_BcsiOptMonObjects_ObjectIdentity = ObjectIdentity
bcsiOptMonObjects = _BcsiOptMonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1)
)
_BcsiOptMonLaneTable_Object = MibTable
bcsiOptMonLaneTable = _BcsiOptMonLaneTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    bcsiOptMonLaneTable.setStatus("current")
_BcsiOptMonLaneEntry_Object = MibTableRow
bcsiOptMonLaneEntry = _BcsiOptMonLaneEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 1, 1)
)
bcsiOptMonLaneEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "BROCADE-OPTICAL-MONITORING-MIB", "bcsiOptMonLaneNum"),
)
if mibBuilder.loadTexts:
    bcsiOptMonLaneEntry.setStatus("current")
_BcsiOptMonLaneNum_Type = Unsigned32
_BcsiOptMonLaneNum_Object = MibTableColumn
bcsiOptMonLaneNum = _BcsiOptMonLaneNum_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 1, 1, 1),
    _BcsiOptMonLaneNum_Type()
)
bcsiOptMonLaneNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsiOptMonLaneNum.setStatus("current")


class _BcsiOptMonLaneTemperature_Type(SnmpAdminString):
    """Custom type bcsiOptMonLaneTemperature based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BcsiOptMonLaneTemperature_Type.__name__ = "SnmpAdminString"
_BcsiOptMonLaneTemperature_Object = MibTableColumn
bcsiOptMonLaneTemperature = _BcsiOptMonLaneTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 1, 1, 2),
    _BcsiOptMonLaneTemperature_Type()
)
bcsiOptMonLaneTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiOptMonLaneTemperature.setStatus("current")


class _BcsiOptMonLaneTxPowerStatus_Type(Integer32):
    """Custom type bcsiOptMonLaneTxPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("notApplicable", 2),
          ("highAlarm", 3),
          ("highWarn", 4),
          ("normal", 5),
          ("lowWarn", 6),
          ("lowAlarm", 7))
    )


_BcsiOptMonLaneTxPowerStatus_Type.__name__ = "Integer32"
_BcsiOptMonLaneTxPowerStatus_Object = MibTableColumn
bcsiOptMonLaneTxPowerStatus = _BcsiOptMonLaneTxPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 1, 1, 3),
    _BcsiOptMonLaneTxPowerStatus_Type()
)
bcsiOptMonLaneTxPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiOptMonLaneTxPowerStatus.setStatus("current")


class _BcsiOptMonLaneTxPower_Type(SnmpAdminString):
    """Custom type bcsiOptMonLaneTxPower based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BcsiOptMonLaneTxPower_Type.__name__ = "SnmpAdminString"
_BcsiOptMonLaneTxPower_Object = MibTableColumn
bcsiOptMonLaneTxPower = _BcsiOptMonLaneTxPower_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 1, 1, 4),
    _BcsiOptMonLaneTxPower_Type()
)
bcsiOptMonLaneTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiOptMonLaneTxPower.setStatus("current")
_BcsiOptMonLaneTxPowerVal_Type = Unsigned32
_BcsiOptMonLaneTxPowerVal_Object = MibTableColumn
bcsiOptMonLaneTxPowerVal = _BcsiOptMonLaneTxPowerVal_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 1, 1, 5),
    _BcsiOptMonLaneTxPowerVal_Type()
)
bcsiOptMonLaneTxPowerVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiOptMonLaneTxPowerVal.setStatus("current")
if mibBuilder.loadTexts:
    bcsiOptMonLaneTxPowerVal.setUnits("microWatt")


class _BcsiOptMonLaneRxPowerStatus_Type(Integer32):
    """Custom type bcsiOptMonLaneRxPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("notApplicable", 2),
          ("highAlarm", 3),
          ("highWarn", 4),
          ("normal", 5),
          ("lowWarn", 6),
          ("lowAlarm", 7))
    )


_BcsiOptMonLaneRxPowerStatus_Type.__name__ = "Integer32"
_BcsiOptMonLaneRxPowerStatus_Object = MibTableColumn
bcsiOptMonLaneRxPowerStatus = _BcsiOptMonLaneRxPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 1, 1, 6),
    _BcsiOptMonLaneRxPowerStatus_Type()
)
bcsiOptMonLaneRxPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiOptMonLaneRxPowerStatus.setStatus("current")


class _BcsiOptMonLaneRxPower_Type(SnmpAdminString):
    """Custom type bcsiOptMonLaneRxPower based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BcsiOptMonLaneRxPower_Type.__name__ = "SnmpAdminString"
_BcsiOptMonLaneRxPower_Object = MibTableColumn
bcsiOptMonLaneRxPower = _BcsiOptMonLaneRxPower_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 1, 1, 7),
    _BcsiOptMonLaneRxPower_Type()
)
bcsiOptMonLaneRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiOptMonLaneRxPower.setStatus("current")
_BcsiOptMonLaneRxPowerVal_Type = Unsigned32
_BcsiOptMonLaneRxPowerVal_Object = MibTableColumn
bcsiOptMonLaneRxPowerVal = _BcsiOptMonLaneRxPowerVal_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 1, 1, 8),
    _BcsiOptMonLaneRxPowerVal_Type()
)
bcsiOptMonLaneRxPowerVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiOptMonLaneRxPowerVal.setStatus("current")
if mibBuilder.loadTexts:
    bcsiOptMonLaneRxPowerVal.setUnits("microWatt")


class _BcsiOptMonLaneTxBiasCurrent_Type(SnmpAdminString):
    """Custom type bcsiOptMonLaneTxBiasCurrent based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BcsiOptMonLaneTxBiasCurrent_Type.__name__ = "SnmpAdminString"
_BcsiOptMonLaneTxBiasCurrent_Object = MibTableColumn
bcsiOptMonLaneTxBiasCurrent = _BcsiOptMonLaneTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 1, 1, 9),
    _BcsiOptMonLaneTxBiasCurrent_Type()
)
bcsiOptMonLaneTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiOptMonLaneTxBiasCurrent.setStatus("current")
_BcsiOptMonInfoTable_Object = MibTable
bcsiOptMonInfoTable = _BcsiOptMonInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 2)
)
if mibBuilder.loadTexts:
    bcsiOptMonInfoTable.setStatus("current")
_BcsiOptMonInfoEntry_Object = MibTableRow
bcsiOptMonInfoEntry = _BcsiOptMonInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 2, 1)
)
bcsiOptMonInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    bcsiOptMonInfoEntry.setStatus("current")


class _BcsiOptMonTemperature_Type(DisplayString):
    """Custom type bcsiOptMonTemperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BcsiOptMonTemperature_Type.__name__ = "DisplayString"
_BcsiOptMonTemperature_Object = MibTableColumn
bcsiOptMonTemperature = _BcsiOptMonTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 2, 1, 1),
    _BcsiOptMonTemperature_Type()
)
bcsiOptMonTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiOptMonTemperature.setStatus("current")


class _BcsiOptMonTxPowerStatus_Type(Integer32):
    """Custom type bcsiOptMonTxPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("notApplicable", 2),
          ("highAlarm", 3),
          ("highWarn", 4),
          ("normal", 5),
          ("lowWarn", 6),
          ("lowAlarm", 7))
    )


_BcsiOptMonTxPowerStatus_Type.__name__ = "Integer32"
_BcsiOptMonTxPowerStatus_Object = MibTableColumn
bcsiOptMonTxPowerStatus = _BcsiOptMonTxPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 2, 1, 2),
    _BcsiOptMonTxPowerStatus_Type()
)
bcsiOptMonTxPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiOptMonTxPowerStatus.setStatus("current")


class _BcsiOptMonTxPower_Type(DisplayString):
    """Custom type bcsiOptMonTxPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BcsiOptMonTxPower_Type.__name__ = "DisplayString"
_BcsiOptMonTxPower_Object = MibTableColumn
bcsiOptMonTxPower = _BcsiOptMonTxPower_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 2, 1, 3),
    _BcsiOptMonTxPower_Type()
)
bcsiOptMonTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiOptMonTxPower.setStatus("current")
_BcsiOptMonTxPowerVal_Type = Unsigned32
_BcsiOptMonTxPowerVal_Object = MibTableColumn
bcsiOptMonTxPowerVal = _BcsiOptMonTxPowerVal_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 2, 1, 4),
    _BcsiOptMonTxPowerVal_Type()
)
bcsiOptMonTxPowerVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiOptMonTxPowerVal.setStatus("current")
if mibBuilder.loadTexts:
    bcsiOptMonTxPowerVal.setUnits("microWatt")


class _BcsiOptMonRxPowerStatus_Type(Integer32):
    """Custom type bcsiOptMonRxPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("notApplicable", 2),
          ("highAlarm", 3),
          ("highWarn", 4),
          ("normal", 5),
          ("lowWarn", 6),
          ("lowAlarm", 7))
    )


_BcsiOptMonRxPowerStatus_Type.__name__ = "Integer32"
_BcsiOptMonRxPowerStatus_Object = MibTableColumn
bcsiOptMonRxPowerStatus = _BcsiOptMonRxPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 2, 1, 5),
    _BcsiOptMonRxPowerStatus_Type()
)
bcsiOptMonRxPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiOptMonRxPowerStatus.setStatus("current")


class _BcsiOptMonRxPower_Type(DisplayString):
    """Custom type bcsiOptMonRxPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BcsiOptMonRxPower_Type.__name__ = "DisplayString"
_BcsiOptMonRxPower_Object = MibTableColumn
bcsiOptMonRxPower = _BcsiOptMonRxPower_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 2, 1, 6),
    _BcsiOptMonRxPower_Type()
)
bcsiOptMonRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiOptMonRxPower.setStatus("current")
_BcsiOptMonRxPowerVal_Type = Unsigned32
_BcsiOptMonRxPowerVal_Object = MibTableColumn
bcsiOptMonRxPowerVal = _BcsiOptMonRxPowerVal_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 2, 1, 7),
    _BcsiOptMonRxPowerVal_Type()
)
bcsiOptMonRxPowerVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiOptMonRxPowerVal.setStatus("current")
if mibBuilder.loadTexts:
    bcsiOptMonRxPowerVal.setUnits("microWatt")


class _BcsiOptMonTxBiasCurrent_Type(DisplayString):
    """Custom type bcsiOptMonTxBiasCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BcsiOptMonTxBiasCurrent_Type.__name__ = "DisplayString"
_BcsiOptMonTxBiasCurrent_Object = MibTableColumn
bcsiOptMonTxBiasCurrent = _BcsiOptMonTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 2, 1, 8),
    _BcsiOptMonTxBiasCurrent_Type()
)
bcsiOptMonTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiOptMonTxBiasCurrent.setStatus("current")
_BcsiIfMediaInfoTable_Object = MibTable
bcsiIfMediaInfoTable = _BcsiIfMediaInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 3)
)
if mibBuilder.loadTexts:
    bcsiIfMediaInfoTable.setStatus("current")
_BcsiIfMediaInfoEntry_Object = MibTableRow
bcsiIfMediaInfoEntry = _BcsiIfMediaInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 3, 1)
)
bcsiIfMediaInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    bcsiIfMediaInfoEntry.setStatus("current")


class _BcsiIfMediaType_Type(DisplayString):
    """Custom type bcsiIfMediaType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BcsiIfMediaType_Type.__name__ = "DisplayString"
_BcsiIfMediaType_Object = MibTableColumn
bcsiIfMediaType = _BcsiIfMediaType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 3, 1, 1),
    _BcsiIfMediaType_Type()
)
bcsiIfMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiIfMediaType.setStatus("current")


class _BcsiIfMediaVendorName_Type(DisplayString):
    """Custom type bcsiIfMediaVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BcsiIfMediaVendorName_Type.__name__ = "DisplayString"
_BcsiIfMediaVendorName_Object = MibTableColumn
bcsiIfMediaVendorName = _BcsiIfMediaVendorName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 3, 1, 2),
    _BcsiIfMediaVendorName_Type()
)
bcsiIfMediaVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiIfMediaVendorName.setStatus("current")


class _BcsiIfMediaVersion_Type(DisplayString):
    """Custom type bcsiIfMediaVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BcsiIfMediaVersion_Type.__name__ = "DisplayString"
_BcsiIfMediaVersion_Object = MibTableColumn
bcsiIfMediaVersion = _BcsiIfMediaVersion_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 3, 1, 3),
    _BcsiIfMediaVersion_Type()
)
bcsiIfMediaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiIfMediaVersion.setStatus("current")


class _BcsiIfMediaPartNumber_Type(DisplayString):
    """Custom type bcsiIfMediaPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BcsiIfMediaPartNumber_Type.__name__ = "DisplayString"
_BcsiIfMediaPartNumber_Object = MibTableColumn
bcsiIfMediaPartNumber = _BcsiIfMediaPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 3, 1, 4),
    _BcsiIfMediaPartNumber_Type()
)
bcsiIfMediaPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiIfMediaPartNumber.setStatus("current")


class _BcsiIfMediaSerialNumber_Type(DisplayString):
    """Custom type bcsiIfMediaSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BcsiIfMediaSerialNumber_Type.__name__ = "DisplayString"
_BcsiIfMediaSerialNumber_Object = MibTableColumn
bcsiIfMediaSerialNumber = _BcsiIfMediaSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 1, 3, 1, 5),
    _BcsiIfMediaSerialNumber_Type()
)
bcsiIfMediaSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiIfMediaSerialNumber.setStatus("current")
_BcsiOptMonConformance_ObjectIdentity = ObjectIdentity
bcsiOptMonConformance = _BcsiOptMonConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 2)
)
_BcsiOptMonCompliances_ObjectIdentity = ObjectIdentity
bcsiOptMonCompliances = _BcsiOptMonCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 2, 1)
)
_BcsiOptMonGroups_ObjectIdentity = ObjectIdentity
bcsiOptMonGroups = _BcsiOptMonGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 2, 2)
)

# Managed Objects groups

bcsiOptMonLaneMonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 2, 2, 1)
)
bcsiOptMonLaneMonGroup.setObjects(
      *(("BROCADE-OPTICAL-MONITORING-MIB", "bcsiOptMonLaneNum"),
        ("BROCADE-OPTICAL-MONITORING-MIB", "bcsiOptMonLaneTemperature"),
        ("BROCADE-OPTICAL-MONITORING-MIB", "bcsiOptMonLaneTxPowerStatus"),
        ("BROCADE-OPTICAL-MONITORING-MIB", "bcsiOptMonLaneTxPower"),
        ("BROCADE-OPTICAL-MONITORING-MIB", "bcsiOptMonLaneTxPowerVal"),
        ("BROCADE-OPTICAL-MONITORING-MIB", "bcsiOptMonLaneRxPowerStatus"),
        ("BROCADE-OPTICAL-MONITORING-MIB", "bcsiOptMonLaneRxPower"),
        ("BROCADE-OPTICAL-MONITORING-MIB", "bcsiOptMonLaneRxPowerVal"),
        ("BROCADE-OPTICAL-MONITORING-MIB", "bcsiOptMonLaneTxBiasCurrent"))
)
if mibBuilder.loadTexts:
    bcsiOptMonLaneMonGroup.setStatus("current")

bcsiOptMonInfoMonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 2, 2, 2)
)
bcsiOptMonInfoMonGroup.setObjects(
      *(("BROCADE-OPTICAL-MONITORING-MIB", "bcsiOptMonTemperature"),
        ("BROCADE-OPTICAL-MONITORING-MIB", "bcsiOptMonTxPowerStatus"),
        ("BROCADE-OPTICAL-MONITORING-MIB", "bcsiOptMonTxPower"),
        ("BROCADE-OPTICAL-MONITORING-MIB", "bcsiOptMonTxPowerVal"),
        ("BROCADE-OPTICAL-MONITORING-MIB", "bcsiOptMonRxPowerStatus"),
        ("BROCADE-OPTICAL-MONITORING-MIB", "bcsiOptMonRxPower"),
        ("BROCADE-OPTICAL-MONITORING-MIB", "bcsiOptMonRxPowerVal"),
        ("BROCADE-OPTICAL-MONITORING-MIB", "bcsiOptMonTxBiasCurrent"))
)
if mibBuilder.loadTexts:
    bcsiOptMonInfoMonGroup.setStatus("current")

bcsiIfMediaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 2, 2, 3)
)
bcsiIfMediaGroup.setObjects(
      *(("BROCADE-OPTICAL-MONITORING-MIB", "bcsiIfMediaType"),
        ("BROCADE-OPTICAL-MONITORING-MIB", "bcsiIfMediaVendorName"),
        ("BROCADE-OPTICAL-MONITORING-MIB", "bcsiIfMediaVersion"),
        ("BROCADE-OPTICAL-MONITORING-MIB", "bcsiIfMediaPartNumber"),
        ("BROCADE-OPTICAL-MONITORING-MIB", "bcsiIfMediaSerialNumber"))
)
if mibBuilder.loadTexts:
    bcsiIfMediaGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bcsiOptMonCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 8, 2, 1, 1)
)
bcsiOptMonCompliance.setObjects(
      *(("BROCADE-OPTICAL-MONITORING-MIB", "bcsiOptMonLaneMonGroup"),
        ("BROCADE-OPTICAL-MONITORING-MIB", "bcsiOptMonInfoMonGroup"),
        ("BROCADE-OPTICAL-MONITORING-MIB", "bcsiIfMediaGroup"))
)
if mibBuilder.loadTexts:
    bcsiOptMonCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROCADE-OPTICAL-MONITORING-MIB",
    **{"brocadeOpticalMonitoringMIB": brocadeOpticalMonitoringMIB,
       "bcsiOptMonNotifications": bcsiOptMonNotifications,
       "bcsiOptMonObjects": bcsiOptMonObjects,
       "bcsiOptMonLaneTable": bcsiOptMonLaneTable,
       "bcsiOptMonLaneEntry": bcsiOptMonLaneEntry,
       "bcsiOptMonLaneNum": bcsiOptMonLaneNum,
       "bcsiOptMonLaneTemperature": bcsiOptMonLaneTemperature,
       "bcsiOptMonLaneTxPowerStatus": bcsiOptMonLaneTxPowerStatus,
       "bcsiOptMonLaneTxPower": bcsiOptMonLaneTxPower,
       "bcsiOptMonLaneTxPowerVal": bcsiOptMonLaneTxPowerVal,
       "bcsiOptMonLaneRxPowerStatus": bcsiOptMonLaneRxPowerStatus,
       "bcsiOptMonLaneRxPower": bcsiOptMonLaneRxPower,
       "bcsiOptMonLaneRxPowerVal": bcsiOptMonLaneRxPowerVal,
       "bcsiOptMonLaneTxBiasCurrent": bcsiOptMonLaneTxBiasCurrent,
       "bcsiOptMonInfoTable": bcsiOptMonInfoTable,
       "bcsiOptMonInfoEntry": bcsiOptMonInfoEntry,
       "bcsiOptMonTemperature": bcsiOptMonTemperature,
       "bcsiOptMonTxPowerStatus": bcsiOptMonTxPowerStatus,
       "bcsiOptMonTxPower": bcsiOptMonTxPower,
       "bcsiOptMonTxPowerVal": bcsiOptMonTxPowerVal,
       "bcsiOptMonRxPowerStatus": bcsiOptMonRxPowerStatus,
       "bcsiOptMonRxPower": bcsiOptMonRxPower,
       "bcsiOptMonRxPowerVal": bcsiOptMonRxPowerVal,
       "bcsiOptMonTxBiasCurrent": bcsiOptMonTxBiasCurrent,
       "bcsiIfMediaInfoTable": bcsiIfMediaInfoTable,
       "bcsiIfMediaInfoEntry": bcsiIfMediaInfoEntry,
       "bcsiIfMediaType": bcsiIfMediaType,
       "bcsiIfMediaVendorName": bcsiIfMediaVendorName,
       "bcsiIfMediaVersion": bcsiIfMediaVersion,
       "bcsiIfMediaPartNumber": bcsiIfMediaPartNumber,
       "bcsiIfMediaSerialNumber": bcsiIfMediaSerialNumber,
       "bcsiOptMonConformance": bcsiOptMonConformance,
       "bcsiOptMonCompliances": bcsiOptMonCompliances,
       "bcsiOptMonCompliance": bcsiOptMonCompliance,
       "bcsiOptMonGroups": bcsiOptMonGroups,
       "bcsiOptMonLaneMonGroup": bcsiOptMonLaneMonGroup,
       "bcsiOptMonInfoMonGroup": bcsiOptMonInfoMonGroup,
       "bcsiIfMediaGroup": bcsiIfMediaGroup}
)
