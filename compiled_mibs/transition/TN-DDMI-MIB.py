# SNMP MIB module (TN-DDMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-DDMI-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:50 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(TNDisplayString,
 TNInterfaceIndex,
 TNSfpTransceiver) = mibBuilder.importSymbols(
    "TN-TC",
    "TNDisplayString",
    "TNInterfaceIndex",
    "TNSfpTransceiver")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnDdmiMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152)
)
if mibBuilder.loadTexts:
    tnDdmiMib.setRevisions(
        ("2014-10-10 00:00",
         "2015-06-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnDdmiMibObjects_ObjectIdentity = ObjectIdentity
tnDdmiMibObjects = _TnDdmiMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1)
)
_TnDdmiConfig_ObjectIdentity = ObjectIdentity
tnDdmiConfig = _TnDdmiConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 2)
)
_TnDdmiConfigGlobals_ObjectIdentity = ObjectIdentity
tnDdmiConfigGlobals = _TnDdmiConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 2, 1)
)
_TnDdmiConfigGlobalsMode_Type = TruthValue
_TnDdmiConfigGlobalsMode_Object = MibScalar
tnDdmiConfigGlobalsMode = _TnDdmiConfigGlobalsMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 2, 1, 1),
    _TnDdmiConfigGlobalsMode_Type()
)
tnDdmiConfigGlobalsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDdmiConfigGlobalsMode.setStatus("current")
_TnDdmiStatus_ObjectIdentity = ObjectIdentity
tnDdmiStatus = _TnDdmiStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3)
)
_TnDdmiStatusInterfaceTable_Object = MibTable
tnDdmiStatusInterfaceTable = _TnDdmiStatusInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceTable.setStatus("current")
_TnDdmiStatusInterfaceEntry_Object = MibTableRow
tnDdmiStatusInterfaceEntry = _TnDdmiStatusInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1)
)
tnDdmiStatusInterfaceEntry.setIndexNames(
    (0, "TN-DDMI-MIB", "tnDdmiStatusInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceEntry.setStatus("current")
_TnDdmiStatusInterfaceIfIndex_Type = TNInterfaceIndex
_TnDdmiStatusInterfaceIfIndex_Object = MibTableColumn
tnDdmiStatusInterfaceIfIndex = _TnDdmiStatusInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1),
    _TnDdmiStatusInterfaceIfIndex_Type()
)
tnDdmiStatusInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceIfIndex.setStatus("current")
_TnDdmiStatusInterfaceA0Supported_Type = TruthValue
_TnDdmiStatusInterfaceA0Supported_Object = MibTableColumn
tnDdmiStatusInterfaceA0Supported = _TnDdmiStatusInterfaceA0Supported_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 2),
    _TnDdmiStatusInterfaceA0Supported_Type()
)
tnDdmiStatusInterfaceA0Supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA0Supported.setStatus("current")
_TnDdmiStatusInterfaceA0SfpDetected_Type = TruthValue
_TnDdmiStatusInterfaceA0SfpDetected_Object = MibTableColumn
tnDdmiStatusInterfaceA0SfpDetected = _TnDdmiStatusInterfaceA0SfpDetected_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 3),
    _TnDdmiStatusInterfaceA0SfpDetected_Type()
)
tnDdmiStatusInterfaceA0SfpDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA0SfpDetected.setStatus("current")


class _TnDdmiStatusInterfaceA0Vendor_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA0Vendor based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA0Vendor_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA0Vendor_Object = MibTableColumn
tnDdmiStatusInterfaceA0Vendor = _TnDdmiStatusInterfaceA0Vendor_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 4),
    _TnDdmiStatusInterfaceA0Vendor_Type()
)
tnDdmiStatusInterfaceA0Vendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA0Vendor.setStatus("current")


class _TnDdmiStatusInterfaceA0PartNumber_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA0PartNumber based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA0PartNumber_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA0PartNumber_Object = MibTableColumn
tnDdmiStatusInterfaceA0PartNumber = _TnDdmiStatusInterfaceA0PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 5),
    _TnDdmiStatusInterfaceA0PartNumber_Type()
)
tnDdmiStatusInterfaceA0PartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA0PartNumber.setStatus("current")


class _TnDdmiStatusInterfaceA0SerialNumber_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA0SerialNumber based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA0SerialNumber_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA0SerialNumber_Object = MibTableColumn
tnDdmiStatusInterfaceA0SerialNumber = _TnDdmiStatusInterfaceA0SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 6),
    _TnDdmiStatusInterfaceA0SerialNumber_Type()
)
tnDdmiStatusInterfaceA0SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA0SerialNumber.setStatus("current")


class _TnDdmiStatusInterfaceA0Revision_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA0Revision based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA0Revision_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA0Revision_Object = MibTableColumn
tnDdmiStatusInterfaceA0Revision = _TnDdmiStatusInterfaceA0Revision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 7),
    _TnDdmiStatusInterfaceA0Revision_Type()
)
tnDdmiStatusInterfaceA0Revision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA0Revision.setStatus("current")


class _TnDdmiStatusInterfaceA0DateCode_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA0DateCode based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA0DateCode_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA0DateCode_Object = MibTableColumn
tnDdmiStatusInterfaceA0DateCode = _TnDdmiStatusInterfaceA0DateCode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 8),
    _TnDdmiStatusInterfaceA0DateCode_Type()
)
tnDdmiStatusInterfaceA0DateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA0DateCode.setStatus("current")
_TnDdmiStatusInterfaceA0SfpType_Type = TNSfpTransceiver
_TnDdmiStatusInterfaceA0SfpType_Object = MibTableColumn
tnDdmiStatusInterfaceA0SfpType = _TnDdmiStatusInterfaceA0SfpType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 9),
    _TnDdmiStatusInterfaceA0SfpType_Type()
)
tnDdmiStatusInterfaceA0SfpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA0SfpType.setStatus("current")
_TnDdmiStatusInterfaceA2Supported_Type = TruthValue
_TnDdmiStatusInterfaceA2Supported_Object = MibTableColumn
tnDdmiStatusInterfaceA2Supported = _TnDdmiStatusInterfaceA2Supported_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1002),
    _TnDdmiStatusInterfaceA2Supported_Type()
)
tnDdmiStatusInterfaceA2Supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2Supported.setStatus("current")


class _TnDdmiStatusInterfaceA2CurrentTemperature_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA2CurrentTemperature based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA2CurrentTemperature_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA2CurrentTemperature_Object = MibTableColumn
tnDdmiStatusInterfaceA2CurrentTemperature = _TnDdmiStatusInterfaceA2CurrentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1003),
    _TnDdmiStatusInterfaceA2CurrentTemperature_Type()
)
tnDdmiStatusInterfaceA2CurrentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2CurrentTemperature.setStatus("current")


class _TnDdmiStatusInterfaceA2TemperatureHighAlarmThreshold_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA2TemperatureHighAlarmThreshold based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA2TemperatureHighAlarmThreshold_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA2TemperatureHighAlarmThreshold_Object = MibTableColumn
tnDdmiStatusInterfaceA2TemperatureHighAlarmThreshold = _TnDdmiStatusInterfaceA2TemperatureHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1004),
    _TnDdmiStatusInterfaceA2TemperatureHighAlarmThreshold_Type()
)
tnDdmiStatusInterfaceA2TemperatureHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2TemperatureHighAlarmThreshold.setStatus("current")


class _TnDdmiStatusInterfaceA2TemperatureLowAlarmThreshold_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA2TemperatureLowAlarmThreshold based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA2TemperatureLowAlarmThreshold_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA2TemperatureLowAlarmThreshold_Object = MibTableColumn
tnDdmiStatusInterfaceA2TemperatureLowAlarmThreshold = _TnDdmiStatusInterfaceA2TemperatureLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1005),
    _TnDdmiStatusInterfaceA2TemperatureLowAlarmThreshold_Type()
)
tnDdmiStatusInterfaceA2TemperatureLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2TemperatureLowAlarmThreshold.setStatus("current")


class _TnDdmiStatusInterfaceA2TemperatureHighWarnThreshold_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA2TemperatureHighWarnThreshold based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA2TemperatureHighWarnThreshold_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA2TemperatureHighWarnThreshold_Object = MibTableColumn
tnDdmiStatusInterfaceA2TemperatureHighWarnThreshold = _TnDdmiStatusInterfaceA2TemperatureHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1006),
    _TnDdmiStatusInterfaceA2TemperatureHighWarnThreshold_Type()
)
tnDdmiStatusInterfaceA2TemperatureHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2TemperatureHighWarnThreshold.setStatus("current")


class _TnDdmiStatusInterfaceA2TemperatureLowWarnThreshold_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA2TemperatureLowWarnThreshold based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA2TemperatureLowWarnThreshold_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA2TemperatureLowWarnThreshold_Object = MibTableColumn
tnDdmiStatusInterfaceA2TemperatureLowWarnThreshold = _TnDdmiStatusInterfaceA2TemperatureLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1007),
    _TnDdmiStatusInterfaceA2TemperatureLowWarnThreshold_Type()
)
tnDdmiStatusInterfaceA2TemperatureLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2TemperatureLowWarnThreshold.setStatus("current")


class _TnDdmiStatusInterfaceA2CurrentVoltage_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA2CurrentVoltage based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA2CurrentVoltage_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA2CurrentVoltage_Object = MibTableColumn
tnDdmiStatusInterfaceA2CurrentVoltage = _TnDdmiStatusInterfaceA2CurrentVoltage_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1008),
    _TnDdmiStatusInterfaceA2CurrentVoltage_Type()
)
tnDdmiStatusInterfaceA2CurrentVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2CurrentVoltage.setStatus("current")


class _TnDdmiStatusInterfaceA2VoltageHighAlarmThreshold_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA2VoltageHighAlarmThreshold based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA2VoltageHighAlarmThreshold_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA2VoltageHighAlarmThreshold_Object = MibTableColumn
tnDdmiStatusInterfaceA2VoltageHighAlarmThreshold = _TnDdmiStatusInterfaceA2VoltageHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1009),
    _TnDdmiStatusInterfaceA2VoltageHighAlarmThreshold_Type()
)
tnDdmiStatusInterfaceA2VoltageHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2VoltageHighAlarmThreshold.setStatus("current")


class _TnDdmiStatusInterfaceA2VoltageLowAlarmThreshold_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA2VoltageLowAlarmThreshold based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA2VoltageLowAlarmThreshold_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA2VoltageLowAlarmThreshold_Object = MibTableColumn
tnDdmiStatusInterfaceA2VoltageLowAlarmThreshold = _TnDdmiStatusInterfaceA2VoltageLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1010),
    _TnDdmiStatusInterfaceA2VoltageLowAlarmThreshold_Type()
)
tnDdmiStatusInterfaceA2VoltageLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2VoltageLowAlarmThreshold.setStatus("current")


class _TnDdmiStatusInterfaceA2VoltageHighWarnThreshold_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA2VoltageHighWarnThreshold based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA2VoltageHighWarnThreshold_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA2VoltageHighWarnThreshold_Object = MibTableColumn
tnDdmiStatusInterfaceA2VoltageHighWarnThreshold = _TnDdmiStatusInterfaceA2VoltageHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1011),
    _TnDdmiStatusInterfaceA2VoltageHighWarnThreshold_Type()
)
tnDdmiStatusInterfaceA2VoltageHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2VoltageHighWarnThreshold.setStatus("current")


class _TnDdmiStatusInterfaceA2VoltageLowWarnThreshold_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA2VoltageLowWarnThreshold based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA2VoltageLowWarnThreshold_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA2VoltageLowWarnThreshold_Object = MibTableColumn
tnDdmiStatusInterfaceA2VoltageLowWarnThreshold = _TnDdmiStatusInterfaceA2VoltageLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1012),
    _TnDdmiStatusInterfaceA2VoltageLowWarnThreshold_Type()
)
tnDdmiStatusInterfaceA2VoltageLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2VoltageLowWarnThreshold.setStatus("current")


class _TnDdmiStatusInterfaceA2CurrentTxBias_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA2CurrentTxBias based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA2CurrentTxBias_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA2CurrentTxBias_Object = MibTableColumn
tnDdmiStatusInterfaceA2CurrentTxBias = _TnDdmiStatusInterfaceA2CurrentTxBias_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1013),
    _TnDdmiStatusInterfaceA2CurrentTxBias_Type()
)
tnDdmiStatusInterfaceA2CurrentTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2CurrentTxBias.setStatus("current")


class _TnDdmiStatusInterfaceA2TxBiasHighAlarmThreshold_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA2TxBiasHighAlarmThreshold based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA2TxBiasHighAlarmThreshold_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA2TxBiasHighAlarmThreshold_Object = MibTableColumn
tnDdmiStatusInterfaceA2TxBiasHighAlarmThreshold = _TnDdmiStatusInterfaceA2TxBiasHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1014),
    _TnDdmiStatusInterfaceA2TxBiasHighAlarmThreshold_Type()
)
tnDdmiStatusInterfaceA2TxBiasHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2TxBiasHighAlarmThreshold.setStatus("current")


class _TnDdmiStatusInterfaceA2TxBiasLowAlarmThreshold_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA2TxBiasLowAlarmThreshold based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA2TxBiasLowAlarmThreshold_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA2TxBiasLowAlarmThreshold_Object = MibTableColumn
tnDdmiStatusInterfaceA2TxBiasLowAlarmThreshold = _TnDdmiStatusInterfaceA2TxBiasLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1015),
    _TnDdmiStatusInterfaceA2TxBiasLowAlarmThreshold_Type()
)
tnDdmiStatusInterfaceA2TxBiasLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2TxBiasLowAlarmThreshold.setStatus("current")


class _TnDdmiStatusInterfaceA2TxBiasHighWarnThreshold_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA2TxBiasHighWarnThreshold based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA2TxBiasHighWarnThreshold_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA2TxBiasHighWarnThreshold_Object = MibTableColumn
tnDdmiStatusInterfaceA2TxBiasHighWarnThreshold = _TnDdmiStatusInterfaceA2TxBiasHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1016),
    _TnDdmiStatusInterfaceA2TxBiasHighWarnThreshold_Type()
)
tnDdmiStatusInterfaceA2TxBiasHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2TxBiasHighWarnThreshold.setStatus("current")


class _TnDdmiStatusInterfaceA2TxBiasLowWarnThreshold_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA2TxBiasLowWarnThreshold based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA2TxBiasLowWarnThreshold_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA2TxBiasLowWarnThreshold_Object = MibTableColumn
tnDdmiStatusInterfaceA2TxBiasLowWarnThreshold = _TnDdmiStatusInterfaceA2TxBiasLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1017),
    _TnDdmiStatusInterfaceA2TxBiasLowWarnThreshold_Type()
)
tnDdmiStatusInterfaceA2TxBiasLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2TxBiasLowWarnThreshold.setStatus("current")


class _TnDdmiStatusInterfaceA2CurrentTxPower_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA2CurrentTxPower based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA2CurrentTxPower_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA2CurrentTxPower_Object = MibTableColumn
tnDdmiStatusInterfaceA2CurrentTxPower = _TnDdmiStatusInterfaceA2CurrentTxPower_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1018),
    _TnDdmiStatusInterfaceA2CurrentTxPower_Type()
)
tnDdmiStatusInterfaceA2CurrentTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2CurrentTxPower.setStatus("current")


class _TnDdmiStatusInterfaceA2TxPowerHighAlarmThreshold_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA2TxPowerHighAlarmThreshold based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA2TxPowerHighAlarmThreshold_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA2TxPowerHighAlarmThreshold_Object = MibTableColumn
tnDdmiStatusInterfaceA2TxPowerHighAlarmThreshold = _TnDdmiStatusInterfaceA2TxPowerHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1019),
    _TnDdmiStatusInterfaceA2TxPowerHighAlarmThreshold_Type()
)
tnDdmiStatusInterfaceA2TxPowerHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2TxPowerHighAlarmThreshold.setStatus("current")


class _TnDdmiStatusInterfaceA2TxPowerLowAlarmThreshold_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA2TxPowerLowAlarmThreshold based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA2TxPowerLowAlarmThreshold_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA2TxPowerLowAlarmThreshold_Object = MibTableColumn
tnDdmiStatusInterfaceA2TxPowerLowAlarmThreshold = _TnDdmiStatusInterfaceA2TxPowerLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1020),
    _TnDdmiStatusInterfaceA2TxPowerLowAlarmThreshold_Type()
)
tnDdmiStatusInterfaceA2TxPowerLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2TxPowerLowAlarmThreshold.setStatus("current")


class _TnDdmiStatusInterfaceA2TxPowerHighWarnThreshold_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA2TxPowerHighWarnThreshold based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA2TxPowerHighWarnThreshold_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA2TxPowerHighWarnThreshold_Object = MibTableColumn
tnDdmiStatusInterfaceA2TxPowerHighWarnThreshold = _TnDdmiStatusInterfaceA2TxPowerHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1021),
    _TnDdmiStatusInterfaceA2TxPowerHighWarnThreshold_Type()
)
tnDdmiStatusInterfaceA2TxPowerHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2TxPowerHighWarnThreshold.setStatus("current")


class _TnDdmiStatusInterfaceA2TxPowerLowWarnThreshold_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA2TxPowerLowWarnThreshold based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA2TxPowerLowWarnThreshold_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA2TxPowerLowWarnThreshold_Object = MibTableColumn
tnDdmiStatusInterfaceA2TxPowerLowWarnThreshold = _TnDdmiStatusInterfaceA2TxPowerLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1022),
    _TnDdmiStatusInterfaceA2TxPowerLowWarnThreshold_Type()
)
tnDdmiStatusInterfaceA2TxPowerLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2TxPowerLowWarnThreshold.setStatus("current")


class _TnDdmiStatusInterfaceA2CurrentRxPower_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA2CurrentRxPower based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA2CurrentRxPower_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA2CurrentRxPower_Object = MibTableColumn
tnDdmiStatusInterfaceA2CurrentRxPower = _TnDdmiStatusInterfaceA2CurrentRxPower_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1023),
    _TnDdmiStatusInterfaceA2CurrentRxPower_Type()
)
tnDdmiStatusInterfaceA2CurrentRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2CurrentRxPower.setStatus("current")


class _TnDdmiStatusInterfaceA2RxPowerHighAlarmThreshold_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA2RxPowerHighAlarmThreshold based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA2RxPowerHighAlarmThreshold_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA2RxPowerHighAlarmThreshold_Object = MibTableColumn
tnDdmiStatusInterfaceA2RxPowerHighAlarmThreshold = _TnDdmiStatusInterfaceA2RxPowerHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1024),
    _TnDdmiStatusInterfaceA2RxPowerHighAlarmThreshold_Type()
)
tnDdmiStatusInterfaceA2RxPowerHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2RxPowerHighAlarmThreshold.setStatus("current")


class _TnDdmiStatusInterfaceA2RxPowerLowAlarmThreshold_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA2RxPowerLowAlarmThreshold based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA2RxPowerLowAlarmThreshold_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA2RxPowerLowAlarmThreshold_Object = MibTableColumn
tnDdmiStatusInterfaceA2RxPowerLowAlarmThreshold = _TnDdmiStatusInterfaceA2RxPowerLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1025),
    _TnDdmiStatusInterfaceA2RxPowerLowAlarmThreshold_Type()
)
tnDdmiStatusInterfaceA2RxPowerLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2RxPowerLowAlarmThreshold.setStatus("current")


class _TnDdmiStatusInterfaceA2RxPowerHighWarnThreshold_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA2RxPowerHighWarnThreshold based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA2RxPowerHighWarnThreshold_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA2RxPowerHighWarnThreshold_Object = MibTableColumn
tnDdmiStatusInterfaceA2RxPowerHighWarnThreshold = _TnDdmiStatusInterfaceA2RxPowerHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1026),
    _TnDdmiStatusInterfaceA2RxPowerHighWarnThreshold_Type()
)
tnDdmiStatusInterfaceA2RxPowerHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2RxPowerHighWarnThreshold.setStatus("current")


class _TnDdmiStatusInterfaceA2RxPowerLowWarnThreshold_Type(TNDisplayString):
    """Custom type tnDdmiStatusInterfaceA2RxPowerLowWarnThreshold based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDdmiStatusInterfaceA2RxPowerLowWarnThreshold_Type.__name__ = "TNDisplayString"
_TnDdmiStatusInterfaceA2RxPowerLowWarnThreshold_Object = MibTableColumn
tnDdmiStatusInterfaceA2RxPowerLowWarnThreshold = _TnDdmiStatusInterfaceA2RxPowerLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 1, 3, 2, 1, 1027),
    _TnDdmiStatusInterfaceA2RxPowerLowWarnThreshold_Type()
)
tnDdmiStatusInterfaceA2RxPowerLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceA2RxPowerLowWarnThreshold.setStatus("current")
_TnDdmiMibConformance_ObjectIdentity = ObjectIdentity
tnDdmiMibConformance = _TnDdmiMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 2)
)
_TnDdmiMibCompliances_ObjectIdentity = ObjectIdentity
tnDdmiMibCompliances = _TnDdmiMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 2, 1)
)
_TnDdmiMibGroups_ObjectIdentity = ObjectIdentity
tnDdmiMibGroups = _TnDdmiMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 2, 2)
)

# Managed Objects groups

tnDdmiConfigGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 2, 2, 1)
)
tnDdmiConfigGlobalsInfoGroup.setObjects(
    ("TN-DDMI-MIB", "tnDdmiConfigGlobalsMode")
)
if mibBuilder.loadTexts:
    tnDdmiConfigGlobalsInfoGroup.setStatus("current")

tnDdmiStatusInterfaceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 2, 2, 2)
)
tnDdmiStatusInterfaceTableInfoGroup.setObjects(
      *(("TN-DDMI-MIB", "tnDdmiStatusInterfaceA0Supported"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA0SfpDetected"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA0Vendor"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA0PartNumber"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA0SerialNumber"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA0Revision"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA0DateCode"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA0SfpType"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2Supported"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2CurrentTemperature"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2TemperatureHighAlarmThreshold"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2TemperatureLowAlarmThreshold"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2TemperatureHighWarnThreshold"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2TemperatureLowWarnThreshold"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2CurrentVoltage"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2VoltageHighAlarmThreshold"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2VoltageLowAlarmThreshold"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2VoltageHighWarnThreshold"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2VoltageLowWarnThreshold"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2CurrentTxBias"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2TxBiasHighAlarmThreshold"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2TxBiasLowAlarmThreshold"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2TxBiasHighWarnThreshold"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2TxBiasLowWarnThreshold"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2CurrentTxPower"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2TxPowerHighAlarmThreshold"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2TxPowerLowAlarmThreshold"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2TxPowerHighWarnThreshold"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2TxPowerLowWarnThreshold"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2CurrentRxPower"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2RxPowerHighAlarmThreshold"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2RxPowerLowAlarmThreshold"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2RxPowerHighWarnThreshold"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceA2RxPowerLowWarnThreshold"))
)
if mibBuilder.loadTexts:
    tnDdmiStatusInterfaceTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnDdmiMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 152, 2, 1, 1)
)
tnDdmiMibCompliance.setObjects(
      *(("TN-DDMI-MIB", "tnDdmiConfigGlobalsInfoGroup"),
        ("TN-DDMI-MIB", "tnDdmiStatusInterfaceTableInfoGroup"))
)
if mibBuilder.loadTexts:
    tnDdmiMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-DDMI-MIB",
    **{"tnDdmiMib": tnDdmiMib,
       "tnDdmiMibObjects": tnDdmiMibObjects,
       "tnDdmiConfig": tnDdmiConfig,
       "tnDdmiConfigGlobals": tnDdmiConfigGlobals,
       "tnDdmiConfigGlobalsMode": tnDdmiConfigGlobalsMode,
       "tnDdmiStatus": tnDdmiStatus,
       "tnDdmiStatusInterfaceTable": tnDdmiStatusInterfaceTable,
       "tnDdmiStatusInterfaceEntry": tnDdmiStatusInterfaceEntry,
       "tnDdmiStatusInterfaceIfIndex": tnDdmiStatusInterfaceIfIndex,
       "tnDdmiStatusInterfaceA0Supported": tnDdmiStatusInterfaceA0Supported,
       "tnDdmiStatusInterfaceA0SfpDetected": tnDdmiStatusInterfaceA0SfpDetected,
       "tnDdmiStatusInterfaceA0Vendor": tnDdmiStatusInterfaceA0Vendor,
       "tnDdmiStatusInterfaceA0PartNumber": tnDdmiStatusInterfaceA0PartNumber,
       "tnDdmiStatusInterfaceA0SerialNumber": tnDdmiStatusInterfaceA0SerialNumber,
       "tnDdmiStatusInterfaceA0Revision": tnDdmiStatusInterfaceA0Revision,
       "tnDdmiStatusInterfaceA0DateCode": tnDdmiStatusInterfaceA0DateCode,
       "tnDdmiStatusInterfaceA0SfpType": tnDdmiStatusInterfaceA0SfpType,
       "tnDdmiStatusInterfaceA2Supported": tnDdmiStatusInterfaceA2Supported,
       "tnDdmiStatusInterfaceA2CurrentTemperature": tnDdmiStatusInterfaceA2CurrentTemperature,
       "tnDdmiStatusInterfaceA2TemperatureHighAlarmThreshold": tnDdmiStatusInterfaceA2TemperatureHighAlarmThreshold,
       "tnDdmiStatusInterfaceA2TemperatureLowAlarmThreshold": tnDdmiStatusInterfaceA2TemperatureLowAlarmThreshold,
       "tnDdmiStatusInterfaceA2TemperatureHighWarnThreshold": tnDdmiStatusInterfaceA2TemperatureHighWarnThreshold,
       "tnDdmiStatusInterfaceA2TemperatureLowWarnThreshold": tnDdmiStatusInterfaceA2TemperatureLowWarnThreshold,
       "tnDdmiStatusInterfaceA2CurrentVoltage": tnDdmiStatusInterfaceA2CurrentVoltage,
       "tnDdmiStatusInterfaceA2VoltageHighAlarmThreshold": tnDdmiStatusInterfaceA2VoltageHighAlarmThreshold,
       "tnDdmiStatusInterfaceA2VoltageLowAlarmThreshold": tnDdmiStatusInterfaceA2VoltageLowAlarmThreshold,
       "tnDdmiStatusInterfaceA2VoltageHighWarnThreshold": tnDdmiStatusInterfaceA2VoltageHighWarnThreshold,
       "tnDdmiStatusInterfaceA2VoltageLowWarnThreshold": tnDdmiStatusInterfaceA2VoltageLowWarnThreshold,
       "tnDdmiStatusInterfaceA2CurrentTxBias": tnDdmiStatusInterfaceA2CurrentTxBias,
       "tnDdmiStatusInterfaceA2TxBiasHighAlarmThreshold": tnDdmiStatusInterfaceA2TxBiasHighAlarmThreshold,
       "tnDdmiStatusInterfaceA2TxBiasLowAlarmThreshold": tnDdmiStatusInterfaceA2TxBiasLowAlarmThreshold,
       "tnDdmiStatusInterfaceA2TxBiasHighWarnThreshold": tnDdmiStatusInterfaceA2TxBiasHighWarnThreshold,
       "tnDdmiStatusInterfaceA2TxBiasLowWarnThreshold": tnDdmiStatusInterfaceA2TxBiasLowWarnThreshold,
       "tnDdmiStatusInterfaceA2CurrentTxPower": tnDdmiStatusInterfaceA2CurrentTxPower,
       "tnDdmiStatusInterfaceA2TxPowerHighAlarmThreshold": tnDdmiStatusInterfaceA2TxPowerHighAlarmThreshold,
       "tnDdmiStatusInterfaceA2TxPowerLowAlarmThreshold": tnDdmiStatusInterfaceA2TxPowerLowAlarmThreshold,
       "tnDdmiStatusInterfaceA2TxPowerHighWarnThreshold": tnDdmiStatusInterfaceA2TxPowerHighWarnThreshold,
       "tnDdmiStatusInterfaceA2TxPowerLowWarnThreshold": tnDdmiStatusInterfaceA2TxPowerLowWarnThreshold,
       "tnDdmiStatusInterfaceA2CurrentRxPower": tnDdmiStatusInterfaceA2CurrentRxPower,
       "tnDdmiStatusInterfaceA2RxPowerHighAlarmThreshold": tnDdmiStatusInterfaceA2RxPowerHighAlarmThreshold,
       "tnDdmiStatusInterfaceA2RxPowerLowAlarmThreshold": tnDdmiStatusInterfaceA2RxPowerLowAlarmThreshold,
       "tnDdmiStatusInterfaceA2RxPowerHighWarnThreshold": tnDdmiStatusInterfaceA2RxPowerHighWarnThreshold,
       "tnDdmiStatusInterfaceA2RxPowerLowWarnThreshold": tnDdmiStatusInterfaceA2RxPowerLowWarnThreshold,
       "tnDdmiMibConformance": tnDdmiMibConformance,
       "tnDdmiMibCompliances": tnDdmiMibCompliances,
       "tnDdmiMibCompliance": tnDdmiMibCompliance,
       "tnDdmiMibGroups": tnDdmiMibGroups,
       "tnDdmiConfigGlobalsInfoGroup": tnDdmiConfigGlobalsInfoGroup,
       "tnDdmiStatusInterfaceTableInfoGroup": tnDdmiStatusInterfaceTableInfoGroup}
)
