# SNMP MIB module (CIENA-WS-PTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-WS-PTP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:12 2025
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

(ChannelsNumber,
 Decimal1Dig,
 Decimal2Dig,
 Decimal2DigSmall,
 EnabledDisabledEnum,
 EnabledDisabledNaEnum,
 NameString,
 PtpId,
 StringMaxl15,
 StringMaxl32,
 TraceMismatchFailMode,
 TraceMismatchMode,
 TraceTxOperMode,
 XcvrId,
 XcvrType) = mibBuilder.importSymbols(
    "CIENA-WS-TYPEDEFS-MIB",
    "ChannelsNumber",
    "Decimal1Dig",
    "Decimal2Dig",
    "Decimal2DigSmall",
    "EnabledDisabledEnum",
    "EnabledDisabledNaEnum",
    "NameString",
    "PtpId",
    "StringMaxl15",
    "StringMaxl32",
    "TraceMismatchFailMode",
    "TraceMismatchMode",
    "TraceTxOperMode",
    "XcvrId",
    "XcvrType")

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


# MODULE-IDENTITY

cienaWsPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8)
)
if mibBuilder.loadTexts:
    cienaWsPtpMIB.setRevisions(
        ("2017-08-07 00:00",
         "2017-03-02 00:00",
         "2016-12-12 00:00",
         "2016-06-14 00:00",
         "2016-02-01 00:00",
         "2015-04-29 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PtpOpEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1),
          ("tuning", 2),
          ("fault", 3),
          ("unknown", 4))
    )



# MIB Managed Objects in the order of their OIDs

_CienaWsPtpObjects_ObjectIdentity = ObjectIdentity
cienaWsPtpObjects = _CienaWsPtpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 1)
)
_CienaWsPtpConformance_ObjectIdentity = ObjectIdentity
cienaWsPtpConformance = _CienaWsPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 2)
)
_CienaWsPtpGroups_ObjectIdentity = ObjectIdentity
cienaWsPtpGroups = _CienaWsPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 2, 1)
)
_CienaWsPtpCompliances_ObjectIdentity = ObjectIdentity
cienaWsPtpCompliances = _CienaWsPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 2, 2)
)
_CwsPtpPtpsTable_Object = MibTable
cwsPtpPtpsTable = _CwsPtpPtpsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 3)
)
if mibBuilder.loadTexts:
    cwsPtpPtpsTable.setStatus("current")
_CwsPtpPtpsEntry_Object = MibTableRow
cwsPtpPtpsEntry = _CwsPtpPtpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 3, 1)
)
cwsPtpPtpsEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpsPtpIndex"),
)
if mibBuilder.loadTexts:
    cwsPtpPtpsEntry.setStatus("current")


class _CwsPtpPtpsPtpIndex_Type(Integer32):
    """Custom type cwsPtpPtpsPtpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpPtpsPtpIndex_Type.__name__ = "Integer32"
_CwsPtpPtpsPtpIndex_Object = MibTableColumn
cwsPtpPtpsPtpIndex = _CwsPtpPtpsPtpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 3, 1, 1),
    _CwsPtpPtpsPtpIndex_Type()
)
cwsPtpPtpsPtpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpPtpsPtpIndex.setStatus("current")
_CwsPtpPtpIdTable_Object = MibTable
cwsPtpPtpIdTable = _CwsPtpPtpIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 4)
)
if mibBuilder.loadTexts:
    cwsPtpPtpIdTable.setStatus("current")
_CwsPtpPtpIdEntry_Object = MibTableRow
cwsPtpPtpIdEntry = _CwsPtpPtpIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 4, 1)
)
cwsPtpPtpIdEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpPtpIdEntry.setStatus("current")


class _CwsPtpPtpIdTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpPtpIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpPtpIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpPtpIdTableSnmpKey_Object = MibTableColumn
cwsPtpPtpIdTableSnmpKey = _CwsPtpPtpIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 4, 1, 1),
    _CwsPtpPtpIdTableSnmpKey_Type()
)
cwsPtpPtpIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpPtpIdTableSnmpKey.setStatus("current")
_CwsPtpPtpIdName_Type = NameString
_CwsPtpPtpIdName_Object = MibTableColumn
cwsPtpPtpIdName = _CwsPtpPtpIdName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 4, 1, 2),
    _CwsPtpPtpIdName_Type()
)
cwsPtpPtpIdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpPtpIdName.setStatus("current")
_CwsPtpPtpStateTable_Object = MibTable
cwsPtpPtpStateTable = _CwsPtpPtpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 5)
)
if mibBuilder.loadTexts:
    cwsPtpPtpStateTable.setStatus("current")
_CwsPtpPtpStateEntry_Object = MibTableRow
cwsPtpPtpStateEntry = _CwsPtpPtpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 5, 1)
)
cwsPtpPtpStateEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpPtpStateEntry.setStatus("current")


class _CwsPtpPtpStateTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpPtpStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpPtpStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpPtpStateTableSnmpKey_Object = MibTableColumn
cwsPtpPtpStateTableSnmpKey = _CwsPtpPtpStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 5, 1, 1),
    _CwsPtpPtpStateTableSnmpKey_Type()
)
cwsPtpPtpStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpPtpStateTableSnmpKey.setStatus("current")
_CwsPtpPtpStateAdminState_Type = EnabledDisabledEnum
_CwsPtpPtpStateAdminState_Object = MibTableColumn
cwsPtpPtpStateAdminState = _CwsPtpPtpStateAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 5, 1, 2),
    _CwsPtpPtpStateAdminState_Type()
)
cwsPtpPtpStateAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpPtpStateAdminState.setStatus("current")
_CwsPtpPtpStateOperationalState_Type = PtpOpEnum
_CwsPtpPtpStateOperationalState_Object = MibTableColumn
cwsPtpPtpStateOperationalState = _CwsPtpPtpStateOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 5, 1, 3),
    _CwsPtpPtpStateOperationalState_Type()
)
cwsPtpPtpStateOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpPtpStateOperationalState.setStatus("current")
_CwsPtpPtpStateSpliManagement_Type = EnabledDisabledEnum
_CwsPtpPtpStateSpliManagement_Object = MibTableColumn
cwsPtpPtpStateSpliManagement = _CwsPtpPtpStateSpliManagement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 5, 1, 4),
    _CwsPtpPtpStateSpliManagement_Type()
)
cwsPtpPtpStateSpliManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpPtpStateSpliManagement.setStatus("current")
_CwsPtpPtpPropertiesTable_Object = MibTable
cwsPtpPtpPropertiesTable = _CwsPtpPtpPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 6)
)
if mibBuilder.loadTexts:
    cwsPtpPtpPropertiesTable.setStatus("current")
_CwsPtpPtpPropertiesEntry_Object = MibTableRow
cwsPtpPtpPropertiesEntry = _CwsPtpPtpPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 6, 1)
)
cwsPtpPtpPropertiesEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpPropertiesTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpPtpPropertiesEntry.setStatus("current")


class _CwsPtpPtpPropertiesTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpPtpPropertiesTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpPtpPropertiesTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpPtpPropertiesTableSnmpKey_Object = MibTableColumn
cwsPtpPtpPropertiesTableSnmpKey = _CwsPtpPtpPropertiesTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 6, 1, 1),
    _CwsPtpPtpPropertiesTableSnmpKey_Type()
)
cwsPtpPtpPropertiesTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpPtpPropertiesTableSnmpKey.setStatus("current")
_CwsPtpPtpPropertiesXcvrType_Type = XcvrType
_CwsPtpPtpPropertiesXcvrType_Object = MibTableColumn
cwsPtpPtpPropertiesXcvrType = _CwsPtpPtpPropertiesXcvrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 6, 1, 2),
    _CwsPtpPtpPropertiesXcvrType_Type()
)
cwsPtpPtpPropertiesXcvrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpPtpPropertiesXcvrType.setStatus("current")
_CwsPtpPtpPropertiesParentIndex_Type = XcvrId
_CwsPtpPtpPropertiesParentIndex_Object = MibTableColumn
cwsPtpPtpPropertiesParentIndex = _CwsPtpPtpPropertiesParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 6, 1, 3),
    _CwsPtpPtpPropertiesParentIndex_Type()
)
cwsPtpPtpPropertiesParentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpPtpPropertiesParentIndex.setStatus("current")


class _CwsPtpPtpPropertiesRate_Type(Integer32):
    """Custom type cwsPtpPtpPropertiesRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("linerate10dot3125gbps", 1),
          ("linerate41dot25gbps", 2),
          ("linerate103dot125gpbs", 3),
          ("linerate2xotu4", 4),
          ("linerate1xotu4", 5),
          ("linerate1dot5xotu4", 6))
    )


_CwsPtpPtpPropertiesRate_Type.__name__ = "Integer32"
_CwsPtpPtpPropertiesRate_Object = MibTableColumn
cwsPtpPtpPropertiesRate = _CwsPtpPtpPropertiesRate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 6, 1, 4),
    _CwsPtpPtpPropertiesRate_Type()
)
cwsPtpPtpPropertiesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpPtpPropertiesRate.setStatus("current")
_CwsPtpTransmitterTable_Object = MibTable
cwsPtpTransmitterTable = _CwsPtpTransmitterTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 7)
)
if mibBuilder.loadTexts:
    cwsPtpTransmitterTable.setStatus("current")
_CwsPtpTransmitterEntry_Object = MibTableRow
cwsPtpTransmitterEntry = _CwsPtpTransmitterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 7, 1)
)
cwsPtpTransmitterEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpTransmitterTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpTransmitterEntry.setStatus("current")


class _CwsPtpTransmitterTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpTransmitterTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpTransmitterTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpTransmitterTableSnmpKey_Object = MibTableColumn
cwsPtpTransmitterTableSnmpKey = _CwsPtpTransmitterTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 7, 1, 1),
    _CwsPtpTransmitterTableSnmpKey_Type()
)
cwsPtpTransmitterTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpTransmitterTableSnmpKey.setStatus("current")
_CwsPtpTransmitterState_Type = EnabledDisabledNaEnum
_CwsPtpTransmitterState_Object = MibTableColumn
cwsPtpTransmitterState = _CwsPtpTransmitterState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 7, 1, 2),
    _CwsPtpTransmitterState_Type()
)
cwsPtpTransmitterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpTransmitterState.setStatus("current")
_CwsPtpWavelengthTable_Object = MibTable
cwsPtpWavelengthTable = _CwsPtpWavelengthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 8)
)
if mibBuilder.loadTexts:
    cwsPtpWavelengthTable.setStatus("current")
_CwsPtpWavelengthEntry_Object = MibTableRow
cwsPtpWavelengthEntry = _CwsPtpWavelengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 8, 1)
)
cwsPtpWavelengthEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpWavelengthTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpWavelengthEntry.setStatus("current")


class _CwsPtpWavelengthTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpWavelengthTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpWavelengthTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpWavelengthTableSnmpKey_Object = MibTableColumn
cwsPtpWavelengthTableSnmpKey = _CwsPtpWavelengthTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 8, 1, 1),
    _CwsPtpWavelengthTableSnmpKey_Type()
)
cwsPtpWavelengthTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpWavelengthTableSnmpKey.setStatus("current")
_CwsPtpWavelengthValue_Type = Decimal2Dig
_CwsPtpWavelengthValue_Object = MibTableColumn
cwsPtpWavelengthValue = _CwsPtpWavelengthValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 8, 1, 2),
    _CwsPtpWavelengthValue_Type()
)
cwsPtpWavelengthValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpWavelengthValue.setStatus("current")
_CwsPtpWavelengthMinValue_Type = Decimal2DigSmall
_CwsPtpWavelengthMinValue_Object = MibTableColumn
cwsPtpWavelengthMinValue = _CwsPtpWavelengthMinValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 8, 1, 3),
    _CwsPtpWavelengthMinValue_Type()
)
cwsPtpWavelengthMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpWavelengthMinValue.setStatus("current")
_CwsPtpWavelengthMaxValue_Type = Decimal2DigSmall
_CwsPtpWavelengthMaxValue_Object = MibTableColumn
cwsPtpWavelengthMaxValue = _CwsPtpWavelengthMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 8, 1, 4),
    _CwsPtpWavelengthMaxValue_Type()
)
cwsPtpWavelengthMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpWavelengthMaxValue.setStatus("current")
_CwsPtpWavelengthActual_Type = Decimal2Dig
_CwsPtpWavelengthActual_Object = MibTableColumn
cwsPtpWavelengthActual = _CwsPtpWavelengthActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 8, 1, 5),
    _CwsPtpWavelengthActual_Type()
)
cwsPtpWavelengthActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpWavelengthActual.setStatus("current")
_CwsPtpChannelsTable_Object = MibTable
cwsPtpChannelsTable = _CwsPtpChannelsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 9)
)
if mibBuilder.loadTexts:
    cwsPtpChannelsTable.setStatus("current")
_CwsPtpChannelsEntry_Object = MibTableRow
cwsPtpChannelsEntry = _CwsPtpChannelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 9, 1)
)
cwsPtpChannelsEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpChannelsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpChannelsEntry.setStatus("current")


class _CwsPtpChannelsTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpChannelsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpChannelsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpChannelsTableSnmpKey_Object = MibTableColumn
cwsPtpChannelsTableSnmpKey = _CwsPtpChannelsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 9, 1, 1),
    _CwsPtpChannelsTableSnmpKey_Type()
)
cwsPtpChannelsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpChannelsTableSnmpKey.setStatus("current")
_CwsPtpChannelsNumberOfChannels_Type = ChannelsNumber
_CwsPtpChannelsNumberOfChannels_Object = MibTableColumn
cwsPtpChannelsNumberOfChannels = _CwsPtpChannelsNumberOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 9, 1, 2),
    _CwsPtpChannelsNumberOfChannels_Type()
)
cwsPtpChannelsNumberOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpChannelsNumberOfChannels.setStatus("current")
_CwsPtpChannelTable_Object = MibTable
cwsPtpChannelTable = _CwsPtpChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 10)
)
if mibBuilder.loadTexts:
    cwsPtpChannelTable.setStatus("current")
_CwsPtpChannelEntry_Object = MibTableRow
cwsPtpChannelEntry = _CwsPtpChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 10, 1)
)
cwsPtpChannelEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpChannelChannelNumber"),
)
if mibBuilder.loadTexts:
    cwsPtpChannelEntry.setStatus("current")


class _CwsPtpChannelChannelNumber_Type(Integer32):
    """Custom type cwsPtpChannelChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpChannelChannelNumber_Type.__name__ = "Integer32"
_CwsPtpChannelChannelNumber_Object = MibTableColumn
cwsPtpChannelChannelNumber = _CwsPtpChannelChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 10, 1, 1),
    _CwsPtpChannelChannelNumber_Type()
)
cwsPtpChannelChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpChannelChannelNumber.setStatus("current")
_CwsPtpRxPowerTable_Object = MibTable
cwsPtpRxPowerTable = _CwsPtpRxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 11)
)
if mibBuilder.loadTexts:
    cwsPtpRxPowerTable.setStatus("current")
_CwsPtpRxPowerEntry_Object = MibTableRow
cwsPtpRxPowerEntry = _CwsPtpRxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 11, 1)
)
cwsPtpRxPowerEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpChannelChannelNumber"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpRxPowerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpRxPowerEntry.setStatus("current")


class _CwsPtpRxPowerTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpRxPowerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpRxPowerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpRxPowerTableSnmpKey_Object = MibTableColumn
cwsPtpRxPowerTableSnmpKey = _CwsPtpRxPowerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 11, 1, 1),
    _CwsPtpRxPowerTableSnmpKey_Type()
)
cwsPtpRxPowerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpRxPowerTableSnmpKey.setStatus("current")
_CwsXcvrRxPowerActual_Type = Decimal1Dig
_CwsXcvrRxPowerActual_Object = MibTableColumn
cwsXcvrRxPowerActual = _CwsXcvrRxPowerActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 11, 1, 2),
    _CwsXcvrRxPowerActual_Type()
)
cwsXcvrRxPowerActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrRxPowerActual.setStatus("current")
_CwsXcvrRxPowerMaximum_Type = Decimal1Dig
_CwsXcvrRxPowerMaximum_Object = MibTableColumn
cwsXcvrRxPowerMaximum = _CwsXcvrRxPowerMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 11, 1, 3),
    _CwsXcvrRxPowerMaximum_Type()
)
cwsXcvrRxPowerMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrRxPowerMaximum.setStatus("current")
_CwsXcvrRxPowerMinimum_Type = Decimal1Dig
_CwsXcvrRxPowerMinimum_Object = MibTableColumn
cwsXcvrRxPowerMinimum = _CwsXcvrRxPowerMinimum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 11, 1, 4),
    _CwsXcvrRxPowerMinimum_Type()
)
cwsXcvrRxPowerMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrRxPowerMinimum.setStatus("current")
_CwsXcvrRxPowerMaximumRecordedTime_Type = StringMaxl32
_CwsXcvrRxPowerMaximumRecordedTime_Object = MibTableColumn
cwsXcvrRxPowerMaximumRecordedTime = _CwsXcvrRxPowerMaximumRecordedTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 11, 1, 5),
    _CwsXcvrRxPowerMaximumRecordedTime_Type()
)
cwsXcvrRxPowerMaximumRecordedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrRxPowerMaximumRecordedTime.setStatus("current")
_CwsXcvrRxPowerMinimumRecordedTime_Type = StringMaxl32
_CwsXcvrRxPowerMinimumRecordedTime_Object = MibTableColumn
cwsXcvrRxPowerMinimumRecordedTime = _CwsXcvrRxPowerMinimumRecordedTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 11, 1, 6),
    _CwsXcvrRxPowerMinimumRecordedTime_Type()
)
cwsXcvrRxPowerMinimumRecordedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrRxPowerMinimumRecordedTime.setStatus("current")
_CwsPtpRxStatusTable_Object = MibTable
cwsPtpRxStatusTable = _CwsPtpRxStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 12)
)
if mibBuilder.loadTexts:
    cwsPtpRxStatusTable.setStatus("current")
_CwsPtpRxStatusEntry_Object = MibTableRow
cwsPtpRxStatusEntry = _CwsPtpRxStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 12, 1)
)
cwsPtpRxStatusEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpChannelChannelNumber"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpRxStatusTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpRxStatusEntry.setStatus("current")


class _CwsPtpRxStatusTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpRxStatusTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpRxStatusTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpRxStatusTableSnmpKey_Object = MibTableColumn
cwsPtpRxStatusTableSnmpKey = _CwsPtpRxStatusTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 12, 1, 1),
    _CwsPtpRxStatusTableSnmpKey_Type()
)
cwsPtpRxStatusTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpRxStatusTableSnmpKey.setStatus("current")
_CwsXcvrRxStatusHighAlarmStatus_Type = TruthValue
_CwsXcvrRxStatusHighAlarmStatus_Object = MibTableColumn
cwsXcvrRxStatusHighAlarmStatus = _CwsXcvrRxStatusHighAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 12, 1, 2),
    _CwsXcvrRxStatusHighAlarmStatus_Type()
)
cwsXcvrRxStatusHighAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrRxStatusHighAlarmStatus.setStatus("current")
_CwsXcvrRxStatusLowAlarmStatus_Type = TruthValue
_CwsXcvrRxStatusLowAlarmStatus_Object = MibTableColumn
cwsXcvrRxStatusLowAlarmStatus = _CwsXcvrRxStatusLowAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 12, 1, 3),
    _CwsXcvrRxStatusLowAlarmStatus_Type()
)
cwsXcvrRxStatusLowAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrRxStatusLowAlarmStatus.setStatus("current")
_CwsXcvrRxStatusHighWarningStatus_Type = TruthValue
_CwsXcvrRxStatusHighWarningStatus_Object = MibTableColumn
cwsXcvrRxStatusHighWarningStatus = _CwsXcvrRxStatusHighWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 12, 1, 4),
    _CwsXcvrRxStatusHighWarningStatus_Type()
)
cwsXcvrRxStatusHighWarningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrRxStatusHighWarningStatus.setStatus("current")
_CwsXcvrRxStatusLowWarningStatus_Type = TruthValue
_CwsXcvrRxStatusLowWarningStatus_Object = MibTableColumn
cwsXcvrRxStatusLowWarningStatus = _CwsXcvrRxStatusLowWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 12, 1, 5),
    _CwsXcvrRxStatusLowWarningStatus_Type()
)
cwsXcvrRxStatusLowWarningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrRxStatusLowWarningStatus.setStatus("current")
_CwsPtpRxStatusLossOfSignal_Type = TruthValue
_CwsPtpRxStatusLossOfSignal_Object = MibTableColumn
cwsPtpRxStatusLossOfSignal = _CwsPtpRxStatusLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 12, 1, 6),
    _CwsPtpRxStatusLossOfSignal_Type()
)
cwsPtpRxStatusLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpRxStatusLossOfSignal.setStatus("current")
_CwsPtpRxStatusLossOfLock_Type = TruthValue
_CwsPtpRxStatusLossOfLock_Object = MibTableColumn
cwsPtpRxStatusLossOfLock = _CwsPtpRxStatusLossOfLock_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 12, 1, 7),
    _CwsPtpRxStatusLossOfLock_Type()
)
cwsPtpRxStatusLossOfLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpRxStatusLossOfLock.setStatus("current")
_CwsPtpTxPowerTable_Object = MibTable
cwsPtpTxPowerTable = _CwsPtpTxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 13)
)
if mibBuilder.loadTexts:
    cwsPtpTxPowerTable.setStatus("current")
_CwsPtpTxPowerEntry_Object = MibTableRow
cwsPtpTxPowerEntry = _CwsPtpTxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 13, 1)
)
cwsPtpTxPowerEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpChannelChannelNumber"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpTxPowerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpTxPowerEntry.setStatus("current")


class _CwsPtpTxPowerTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpTxPowerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpTxPowerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpTxPowerTableSnmpKey_Object = MibTableColumn
cwsPtpTxPowerTableSnmpKey = _CwsPtpTxPowerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 13, 1, 1),
    _CwsPtpTxPowerTableSnmpKey_Type()
)
cwsPtpTxPowerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpTxPowerTableSnmpKey.setStatus("current")
_CwsXcvrTxPowerActual_Type = Decimal1Dig
_CwsXcvrTxPowerActual_Object = MibTableColumn
cwsXcvrTxPowerActual = _CwsXcvrTxPowerActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 13, 1, 2),
    _CwsXcvrTxPowerActual_Type()
)
cwsXcvrTxPowerActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTxPowerActual.setStatus("current")
_CwsXcvrTxPowerMaximum_Type = Decimal1Dig
_CwsXcvrTxPowerMaximum_Object = MibTableColumn
cwsXcvrTxPowerMaximum = _CwsXcvrTxPowerMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 13, 1, 3),
    _CwsXcvrTxPowerMaximum_Type()
)
cwsXcvrTxPowerMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTxPowerMaximum.setStatus("current")
_CwsXcvrTxPowerMinimum_Type = Decimal1Dig
_CwsXcvrTxPowerMinimum_Object = MibTableColumn
cwsXcvrTxPowerMinimum = _CwsXcvrTxPowerMinimum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 13, 1, 4),
    _CwsXcvrTxPowerMinimum_Type()
)
cwsXcvrTxPowerMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTxPowerMinimum.setStatus("current")
_CwsXcvrTxPowerMaximumRecordedTime_Type = StringMaxl32
_CwsXcvrTxPowerMaximumRecordedTime_Object = MibTableColumn
cwsXcvrTxPowerMaximumRecordedTime = _CwsXcvrTxPowerMaximumRecordedTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 13, 1, 5),
    _CwsXcvrTxPowerMaximumRecordedTime_Type()
)
cwsXcvrTxPowerMaximumRecordedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTxPowerMaximumRecordedTime.setStatus("current")
_CwsXcvrTxPowerMinimumRecordedTime_Type = StringMaxl32
_CwsXcvrTxPowerMinimumRecordedTime_Object = MibTableColumn
cwsXcvrTxPowerMinimumRecordedTime = _CwsXcvrTxPowerMinimumRecordedTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 13, 1, 6),
    _CwsXcvrTxPowerMinimumRecordedTime_Type()
)
cwsXcvrTxPowerMinimumRecordedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTxPowerMinimumRecordedTime.setStatus("current")
_CwsPtpTxStatusTable_Object = MibTable
cwsPtpTxStatusTable = _CwsPtpTxStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 14)
)
if mibBuilder.loadTexts:
    cwsPtpTxStatusTable.setStatus("current")
_CwsPtpTxStatusEntry_Object = MibTableRow
cwsPtpTxStatusEntry = _CwsPtpTxStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 14, 1)
)
cwsPtpTxStatusEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpChannelChannelNumber"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpTxStatusTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpTxStatusEntry.setStatus("current")


class _CwsPtpTxStatusTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpTxStatusTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpTxStatusTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpTxStatusTableSnmpKey_Object = MibTableColumn
cwsPtpTxStatusTableSnmpKey = _CwsPtpTxStatusTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 14, 1, 1),
    _CwsPtpTxStatusTableSnmpKey_Type()
)
cwsPtpTxStatusTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpTxStatusTableSnmpKey.setStatus("current")
_CwsXcvrTxStatusHighAlarmStatus_Type = TruthValue
_CwsXcvrTxStatusHighAlarmStatus_Object = MibTableColumn
cwsXcvrTxStatusHighAlarmStatus = _CwsXcvrTxStatusHighAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 14, 1, 2),
    _CwsXcvrTxStatusHighAlarmStatus_Type()
)
cwsXcvrTxStatusHighAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTxStatusHighAlarmStatus.setStatus("current")
_CwsXcvrTxStatusLowAlarmStatus_Type = TruthValue
_CwsXcvrTxStatusLowAlarmStatus_Object = MibTableColumn
cwsXcvrTxStatusLowAlarmStatus = _CwsXcvrTxStatusLowAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 14, 1, 3),
    _CwsXcvrTxStatusLowAlarmStatus_Type()
)
cwsXcvrTxStatusLowAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTxStatusLowAlarmStatus.setStatus("current")
_CwsXcvrTxStatusHighWarningStatus_Type = TruthValue
_CwsXcvrTxStatusHighWarningStatus_Object = MibTableColumn
cwsXcvrTxStatusHighWarningStatus = _CwsXcvrTxStatusHighWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 14, 1, 4),
    _CwsXcvrTxStatusHighWarningStatus_Type()
)
cwsXcvrTxStatusHighWarningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTxStatusHighWarningStatus.setStatus("current")
_CwsXcvrTxStatusLowWarningStatus_Type = TruthValue
_CwsXcvrTxStatusLowWarningStatus_Object = MibTableColumn
cwsXcvrTxStatusLowWarningStatus = _CwsXcvrTxStatusLowWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 14, 1, 5),
    _CwsXcvrTxStatusLowWarningStatus_Type()
)
cwsXcvrTxStatusLowWarningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrTxStatusLowWarningStatus.setStatus("current")
_CwsPtpDiagnosticsTable_Object = MibTable
cwsPtpDiagnosticsTable = _CwsPtpDiagnosticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 15)
)
if mibBuilder.loadTexts:
    cwsPtpDiagnosticsTable.setStatus("current")
_CwsPtpDiagnosticsEntry_Object = MibTableRow
cwsPtpDiagnosticsEntry = _CwsPtpDiagnosticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 15, 1)
)
cwsPtpDiagnosticsEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpDiagnosticsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpDiagnosticsEntry.setStatus("current")


class _CwsPtpDiagnosticsTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpDiagnosticsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpDiagnosticsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpDiagnosticsTableSnmpKey_Object = MibTableColumn
cwsPtpDiagnosticsTableSnmpKey = _CwsPtpDiagnosticsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 15, 1, 1),
    _CwsPtpDiagnosticsTableSnmpKey_Type()
)
cwsPtpDiagnosticsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpDiagnosticsTableSnmpKey.setStatus("current")
_CwsPtpDiagnosticsNumberOfChannels_Type = ChannelsNumber
_CwsPtpDiagnosticsNumberOfChannels_Object = MibTableColumn
cwsPtpDiagnosticsNumberOfChannels = _CwsPtpDiagnosticsNumberOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 15, 1, 2),
    _CwsPtpDiagnosticsNumberOfChannels_Type()
)
cwsPtpDiagnosticsNumberOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpDiagnosticsNumberOfChannels.setStatus("current")
_CwsPtpDiagnosticsNumberOfEthernet_Type = Unsigned32
_CwsPtpDiagnosticsNumberOfEthernet_Object = MibTableColumn
cwsPtpDiagnosticsNumberOfEthernet = _CwsPtpDiagnosticsNumberOfEthernet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 15, 1, 3),
    _CwsPtpDiagnosticsNumberOfEthernet_Type()
)
cwsPtpDiagnosticsNumberOfEthernet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpDiagnosticsNumberOfEthernet.setStatus("current")
_CwsPtpPtpOpticalDiagnosticsTable_Object = MibTable
cwsPtpPtpOpticalDiagnosticsTable = _CwsPtpPtpOpticalDiagnosticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 16)
)
if mibBuilder.loadTexts:
    cwsPtpPtpOpticalDiagnosticsTable.setStatus("current")
_CwsPtpPtpOpticalDiagnosticsEntry_Object = MibTableRow
cwsPtpPtpOpticalDiagnosticsEntry = _CwsPtpPtpOpticalDiagnosticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 16, 1)
)
cwsPtpPtpOpticalDiagnosticsEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpOpticalDiagnosticsChannelNumber"),
)
if mibBuilder.loadTexts:
    cwsPtpPtpOpticalDiagnosticsEntry.setStatus("current")


class _CwsPtpPtpOpticalDiagnosticsChannelNumber_Type(Integer32):
    """Custom type cwsPtpPtpOpticalDiagnosticsChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpPtpOpticalDiagnosticsChannelNumber_Type.__name__ = "Integer32"
_CwsPtpPtpOpticalDiagnosticsChannelNumber_Object = MibTableColumn
cwsPtpPtpOpticalDiagnosticsChannelNumber = _CwsPtpPtpOpticalDiagnosticsChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 16, 1, 1),
    _CwsPtpPtpOpticalDiagnosticsChannelNumber_Type()
)
cwsPtpPtpOpticalDiagnosticsChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpPtpOpticalDiagnosticsChannelNumber.setStatus("current")
_CwsPtpPtpRxOpticalDiagnosticsTable_Object = MibTable
cwsPtpPtpRxOpticalDiagnosticsTable = _CwsPtpPtpRxOpticalDiagnosticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 17)
)
if mibBuilder.loadTexts:
    cwsPtpPtpRxOpticalDiagnosticsTable.setStatus("current")
_CwsPtpPtpRxOpticalDiagnosticsEntry_Object = MibTableRow
cwsPtpPtpRxOpticalDiagnosticsEntry = _CwsPtpPtpRxOpticalDiagnosticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 17, 1)
)
cwsPtpPtpRxOpticalDiagnosticsEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpOpticalDiagnosticsChannelNumber"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpRxOpticalDiagnosticsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpPtpRxOpticalDiagnosticsEntry.setStatus("current")


class _CwsPtpPtpRxOpticalDiagnosticsTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpPtpRxOpticalDiagnosticsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpPtpRxOpticalDiagnosticsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpPtpRxOpticalDiagnosticsTableSnmpKey_Object = MibTableColumn
cwsPtpPtpRxOpticalDiagnosticsTableSnmpKey = _CwsPtpPtpRxOpticalDiagnosticsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 17, 1, 1),
    _CwsPtpPtpRxOpticalDiagnosticsTableSnmpKey_Type()
)
cwsPtpPtpRxOpticalDiagnosticsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpPtpRxOpticalDiagnosticsTableSnmpKey.setStatus("current")
_CwsPtpPtpRxOpticalDiagnosticsLossOfSignal_Type = TruthValue
_CwsPtpPtpRxOpticalDiagnosticsLossOfSignal_Object = MibTableColumn
cwsPtpPtpRxOpticalDiagnosticsLossOfSignal = _CwsPtpPtpRxOpticalDiagnosticsLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 17, 1, 2),
    _CwsPtpPtpRxOpticalDiagnosticsLossOfSignal_Type()
)
cwsPtpPtpRxOpticalDiagnosticsLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpPtpRxOpticalDiagnosticsLossOfSignal.setStatus("current")
_CwsPtpPtpRxOpticalDiagnosticsLossOfLock_Type = TruthValue
_CwsPtpPtpRxOpticalDiagnosticsLossOfLock_Object = MibTableColumn
cwsPtpPtpRxOpticalDiagnosticsLossOfLock = _CwsPtpPtpRxOpticalDiagnosticsLossOfLock_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 17, 1, 3),
    _CwsPtpPtpRxOpticalDiagnosticsLossOfLock_Type()
)
cwsPtpPtpRxOpticalDiagnosticsLossOfLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpPtpRxOpticalDiagnosticsLossOfLock.setStatus("current")
_CwsPtpPtpTxOpticalDiagnosticsTable_Object = MibTable
cwsPtpPtpTxOpticalDiagnosticsTable = _CwsPtpPtpTxOpticalDiagnosticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 18)
)
if mibBuilder.loadTexts:
    cwsPtpPtpTxOpticalDiagnosticsTable.setStatus("current")
_CwsPtpPtpTxOpticalDiagnosticsEntry_Object = MibTableRow
cwsPtpPtpTxOpticalDiagnosticsEntry = _CwsPtpPtpTxOpticalDiagnosticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 18, 1)
)
cwsPtpPtpTxOpticalDiagnosticsEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpOpticalDiagnosticsChannelNumber"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpTxOpticalDiagnosticsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpPtpTxOpticalDiagnosticsEntry.setStatus("current")


class _CwsPtpPtpTxOpticalDiagnosticsTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpPtpTxOpticalDiagnosticsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpPtpTxOpticalDiagnosticsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpPtpTxOpticalDiagnosticsTableSnmpKey_Object = MibTableColumn
cwsPtpPtpTxOpticalDiagnosticsTableSnmpKey = _CwsPtpPtpTxOpticalDiagnosticsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 18, 1, 1),
    _CwsPtpPtpTxOpticalDiagnosticsTableSnmpKey_Type()
)
cwsPtpPtpTxOpticalDiagnosticsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpPtpTxOpticalDiagnosticsTableSnmpKey.setStatus("current")
_CwsPtpPtpTxOpticalDiagnosticsLossOfSignal_Type = TruthValue
_CwsPtpPtpTxOpticalDiagnosticsLossOfSignal_Object = MibTableColumn
cwsPtpPtpTxOpticalDiagnosticsLossOfSignal = _CwsPtpPtpTxOpticalDiagnosticsLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 18, 1, 2),
    _CwsPtpPtpTxOpticalDiagnosticsLossOfSignal_Type()
)
cwsPtpPtpTxOpticalDiagnosticsLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpPtpTxOpticalDiagnosticsLossOfSignal.setStatus("current")
_CwsPtpPtpTxOpticalDiagnosticsLossOfLock_Type = TruthValue
_CwsPtpPtpTxOpticalDiagnosticsLossOfLock_Object = MibTableColumn
cwsPtpPtpTxOpticalDiagnosticsLossOfLock = _CwsPtpPtpTxOpticalDiagnosticsLossOfLock_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 18, 1, 3),
    _CwsPtpPtpTxOpticalDiagnosticsLossOfLock_Type()
)
cwsPtpPtpTxOpticalDiagnosticsLossOfLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpPtpTxOpticalDiagnosticsLossOfLock.setStatus("current")
_CwsPtpPtpEthernetDiagnosticsTable_Object = MibTable
cwsPtpPtpEthernetDiagnosticsTable = _CwsPtpPtpEthernetDiagnosticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 19)
)
if mibBuilder.loadTexts:
    cwsPtpPtpEthernetDiagnosticsTable.setStatus("current")
_CwsPtpPtpEthernetDiagnosticsEntry_Object = MibTableRow
cwsPtpPtpEthernetDiagnosticsEntry = _CwsPtpPtpEthernetDiagnosticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 19, 1)
)
cwsPtpPtpEthernetDiagnosticsEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpEthernetDiagnosticsEthernetId"),
)
if mibBuilder.loadTexts:
    cwsPtpPtpEthernetDiagnosticsEntry.setStatus("current")


class _CwsPtpPtpEthernetDiagnosticsEthernetId_Type(Integer32):
    """Custom type cwsPtpPtpEthernetDiagnosticsEthernetId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpPtpEthernetDiagnosticsEthernetId_Type.__name__ = "Integer32"
_CwsPtpPtpEthernetDiagnosticsEthernetId_Object = MibTableColumn
cwsPtpPtpEthernetDiagnosticsEthernetId = _CwsPtpPtpEthernetDiagnosticsEthernetId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 19, 1, 1),
    _CwsPtpPtpEthernetDiagnosticsEthernetId_Type()
)
cwsPtpPtpEthernetDiagnosticsEthernetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpPtpEthernetDiagnosticsEthernetId.setStatus("current")
_CwsPtpPmaTable_Object = MibTable
cwsPtpPmaTable = _CwsPtpPmaTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 20)
)
if mibBuilder.loadTexts:
    cwsPtpPmaTable.setStatus("current")
_CwsPtpPmaEntry_Object = MibTableRow
cwsPtpPmaEntry = _CwsPtpPmaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 20, 1)
)
cwsPtpPmaEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpEthernetDiagnosticsEthernetId"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPmaTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpPmaEntry.setStatus("current")


class _CwsPtpPmaTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpPmaTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpPmaTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpPmaTableSnmpKey_Object = MibTableColumn
cwsPtpPmaTableSnmpKey = _CwsPtpPmaTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 20, 1, 1),
    _CwsPtpPmaTableSnmpKey_Type()
)
cwsPtpPmaTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpPmaTableSnmpKey.setStatus("current")
_CwsPtpPmaSerdesOutOfLock_Type = TruthValue
_CwsPtpPmaSerdesOutOfLock_Object = MibTableColumn
cwsPtpPmaSerdesOutOfLock = _CwsPtpPmaSerdesOutOfLock_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 20, 1, 2),
    _CwsPtpPmaSerdesOutOfLock_Type()
)
cwsPtpPmaSerdesOutOfLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpPmaSerdesOutOfLock.setStatus("current")
_CwsPtpFecTable_Object = MibTable
cwsPtpFecTable = _CwsPtpFecTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 21)
)
if mibBuilder.loadTexts:
    cwsPtpFecTable.setStatus("current")
_CwsPtpFecEntry_Object = MibTableRow
cwsPtpFecEntry = _CwsPtpFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 21, 1)
)
cwsPtpFecEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpEthernetDiagnosticsEthernetId"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpFecTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpFecEntry.setStatus("current")


class _CwsPtpFecTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpFecTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpFecTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpFecTableSnmpKey_Object = MibTableColumn
cwsPtpFecTableSnmpKey = _CwsPtpFecTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 21, 1, 1),
    _CwsPtpFecTableSnmpKey_Type()
)
cwsPtpFecTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpFecTableSnmpKey.setStatus("current")
_CwsPtpFecLossOfAlignmentMarkerLock_Type = TruthValue
_CwsPtpFecLossOfAlignmentMarkerLock_Object = MibTableColumn
cwsPtpFecLossOfAlignmentMarkerLock = _CwsPtpFecLossOfAlignmentMarkerLock_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 21, 1, 2),
    _CwsPtpFecLossOfAlignmentMarkerLock_Type()
)
cwsPtpFecLossOfAlignmentMarkerLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpFecLossOfAlignmentMarkerLock.setStatus("current")
_CwsPtpPcsTable_Object = MibTable
cwsPtpPcsTable = _CwsPtpPcsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 22)
)
if mibBuilder.loadTexts:
    cwsPtpPcsTable.setStatus("current")
_CwsPtpPcsEntry_Object = MibTableRow
cwsPtpPcsEntry = _CwsPtpPcsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 22, 1)
)
cwsPtpPcsEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpEthernetDiagnosticsEthernetId"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPcsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpPcsEntry.setStatus("current")


class _CwsPtpPcsTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpPcsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpPcsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpPcsTableSnmpKey_Object = MibTableColumn
cwsPtpPcsTableSnmpKey = _CwsPtpPcsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 22, 1, 1),
    _CwsPtpPcsTableSnmpKey_Type()
)
cwsPtpPcsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpPcsTableSnmpKey.setStatus("current")
_CwsPtpPcsLossOfAlignmentMarker_Type = TruthValue
_CwsPtpPcsLossOfAlignmentMarker_Object = MibTableColumn
cwsPtpPcsLossOfAlignmentMarker = _CwsPtpPcsLossOfAlignmentMarker_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 22, 1, 2),
    _CwsPtpPcsLossOfAlignmentMarker_Type()
)
cwsPtpPcsLossOfAlignmentMarker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpPcsLossOfAlignmentMarker.setStatus("current")
_CwsPtpPcsLossOfBlockLock_Type = TruthValue
_CwsPtpPcsLossOfBlockLock_Object = MibTableColumn
cwsPtpPcsLossOfBlockLock = _CwsPtpPcsLossOfBlockLock_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 22, 1, 3),
    _CwsPtpPcsLossOfBlockLock_Type()
)
cwsPtpPcsLossOfBlockLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpPcsLossOfBlockLock.setStatus("current")
_CwsPtpPcsHighBitErrorRate_Type = TruthValue
_CwsPtpPcsHighBitErrorRate_Object = MibTableColumn
cwsPtpPcsHighBitErrorRate = _CwsPtpPcsHighBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 22, 1, 4),
    _CwsPtpPcsHighBitErrorRate_Type()
)
cwsPtpPcsHighBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpPcsHighBitErrorRate.setStatus("current")
_CwsPtpRsTable_Object = MibTable
cwsPtpRsTable = _CwsPtpRsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 23)
)
if mibBuilder.loadTexts:
    cwsPtpRsTable.setStatus("current")
_CwsPtpRsEntry_Object = MibTableRow
cwsPtpRsEntry = _CwsPtpRsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 23, 1)
)
cwsPtpRsEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpEthernetDiagnosticsEthernetId"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpRsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpRsEntry.setStatus("current")


class _CwsPtpRsTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpRsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpRsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpRsTableSnmpKey_Object = MibTableColumn
cwsPtpRsTableSnmpKey = _CwsPtpRsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 23, 1, 1),
    _CwsPtpRsTableSnmpKey_Type()
)
cwsPtpRsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpRsTableSnmpKey.setStatus("current")
_CwsPtpRsLinkDown_Type = TruthValue
_CwsPtpRsLinkDown_Object = MibTableColumn
cwsPtpRsLinkDown = _CwsPtpRsLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 23, 1, 2),
    _CwsPtpRsLinkDown_Type()
)
cwsPtpRsLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpRsLinkDown.setStatus("current")
_CwsPtpRsLocalFault_Type = TruthValue
_CwsPtpRsLocalFault_Object = MibTableColumn
cwsPtpRsLocalFault = _CwsPtpRsLocalFault_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 23, 1, 3),
    _CwsPtpRsLocalFault_Type()
)
cwsPtpRsLocalFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpRsLocalFault.setStatus("current")
_CwsPtpRsRemoteFault_Type = TruthValue
_CwsPtpRsRemoteFault_Object = MibTableColumn
cwsPtpRsRemoteFault = _CwsPtpRsRemoteFault_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 23, 1, 4),
    _CwsPtpRsRemoteFault_Type()
)
cwsPtpRsRemoteFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpRsRemoteFault.setStatus("current")
_CwsPtpTraceTable_Object = MibTable
cwsPtpTraceTable = _CwsPtpTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 24)
)
if mibBuilder.loadTexts:
    cwsPtpTraceTable.setStatus("current")
_CwsPtpTraceEntry_Object = MibTableRow
cwsPtpTraceEntry = _CwsPtpTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 24, 1)
)
cwsPtpTraceEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MIB", "cwsPtpTraceTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpTraceEntry.setStatus("current")


class _CwsPtpTraceTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpTraceTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpTraceTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpTraceTableSnmpKey_Object = MibTableColumn
cwsPtpTraceTableSnmpKey = _CwsPtpTraceTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 24, 1, 1),
    _CwsPtpTraceTableSnmpKey_Type()
)
cwsPtpTraceTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpTraceTableSnmpKey.setStatus("current")
_CwsPtpTraceMismatchMode_Type = TraceMismatchMode
_CwsPtpTraceMismatchMode_Object = MibTableColumn
cwsPtpTraceMismatchMode = _CwsPtpTraceMismatchMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 24, 1, 2),
    _CwsPtpTraceMismatchMode_Type()
)
cwsPtpTraceMismatchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpTraceMismatchMode.setStatus("current")
_CwsPtpTraceMismatchFailMode_Type = TraceMismatchFailMode
_CwsPtpTraceMismatchFailMode_Object = MibTableColumn
cwsPtpTraceMismatchFailMode = _CwsPtpTraceMismatchFailMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 24, 1, 3),
    _CwsPtpTraceMismatchFailMode_Type()
)
cwsPtpTraceMismatchFailMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpTraceMismatchFailMode.setStatus("current")
_CwsPtpTraceTxSapi_Type = StringMaxl15
_CwsPtpTraceTxSapi_Object = MibTableColumn
cwsPtpTraceTxSapi = _CwsPtpTraceTxSapi_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 24, 1, 4),
    _CwsPtpTraceTxSapi_Type()
)
cwsPtpTraceTxSapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpTraceTxSapi.setStatus("current")
_CwsPtpTraceTxDapi_Type = StringMaxl15
_CwsPtpTraceTxDapi_Object = MibTableColumn
cwsPtpTraceTxDapi = _CwsPtpTraceTxDapi_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 24, 1, 5),
    _CwsPtpTraceTxDapi_Type()
)
cwsPtpTraceTxDapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpTraceTxDapi.setStatus("current")
_CwsPtpTraceTxOper_Type = StringMaxl32
_CwsPtpTraceTxOper_Object = MibTableColumn
cwsPtpTraceTxOper = _CwsPtpTraceTxOper_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 24, 1, 6),
    _CwsPtpTraceTxOper_Type()
)
cwsPtpTraceTxOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpTraceTxOper.setStatus("current")
_CwsPtpTraceTxOperActual_Type = StringMaxl32
_CwsPtpTraceTxOperActual_Object = MibTableColumn
cwsPtpTraceTxOperActual = _CwsPtpTraceTxOperActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 24, 1, 7),
    _CwsPtpTraceTxOperActual_Type()
)
cwsPtpTraceTxOperActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpTraceTxOperActual.setStatus("current")
_CwsPtpTraceTxOperMode_Type = TraceTxOperMode
_CwsPtpTraceTxOperMode_Object = MibTableColumn
cwsPtpTraceTxOperMode = _CwsPtpTraceTxOperMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 24, 1, 8),
    _CwsPtpTraceTxOperMode_Type()
)
cwsPtpTraceTxOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpTraceTxOperMode.setStatus("current")
_CwsPtpTraceRxSapi_Type = StringMaxl15
_CwsPtpTraceRxSapi_Object = MibTableColumn
cwsPtpTraceRxSapi = _CwsPtpTraceRxSapi_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 24, 1, 9),
    _CwsPtpTraceRxSapi_Type()
)
cwsPtpTraceRxSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpTraceRxSapi.setStatus("current")
_CwsPtpTraceRxDapi_Type = StringMaxl15
_CwsPtpTraceRxDapi_Object = MibTableColumn
cwsPtpTraceRxDapi = _CwsPtpTraceRxDapi_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 24, 1, 10),
    _CwsPtpTraceRxDapi_Type()
)
cwsPtpTraceRxDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpTraceRxDapi.setStatus("current")
_CwsPtpTraceRxOper_Type = StringMaxl32
_CwsPtpTraceRxOper_Object = MibTableColumn
cwsPtpTraceRxOper = _CwsPtpTraceRxOper_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 24, 1, 11),
    _CwsPtpTraceRxOper_Type()
)
cwsPtpTraceRxOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpTraceRxOper.setStatus("current")
_CwsPtpTraceExpSapi_Type = StringMaxl15
_CwsPtpTraceExpSapi_Object = MibTableColumn
cwsPtpTraceExpSapi = _CwsPtpTraceExpSapi_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 24, 1, 12),
    _CwsPtpTraceExpSapi_Type()
)
cwsPtpTraceExpSapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpTraceExpSapi.setStatus("current")
_CwsPtpTraceExpDapi_Type = StringMaxl15
_CwsPtpTraceExpDapi_Object = MibTableColumn
cwsPtpTraceExpDapi = _CwsPtpTraceExpDapi_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 24, 1, 13),
    _CwsPtpTraceExpDapi_Type()
)
cwsPtpTraceExpDapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpTraceExpDapi.setStatus("current")
_CwsPtpTraceExpOper_Type = StringMaxl32
_CwsPtpTraceExpOper_Object = MibTableColumn
cwsPtpTraceExpOper = _CwsPtpTraceExpOper_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 24, 1, 14),
    _CwsPtpTraceExpOper_Type()
)
cwsPtpTraceExpOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpTraceExpOper.setStatus("current")

# Managed Objects groups

cienaWsPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 2, 1, 1)
)
cienaWsPtpGroup.setObjects(
      *(("CIENA-WS-PTP-MIB", "cwsPtpPtpsPtpIndex"),
        ("CIENA-WS-PTP-MIB", "cwsPtpPtpIdName"),
        ("CIENA-WS-PTP-MIB", "cwsPtpPtpStateAdminState"),
        ("CIENA-WS-PTP-MIB", "cwsPtpPtpStateOperationalState"),
        ("CIENA-WS-PTP-MIB", "cwsPtpPtpStateSpliManagement"),
        ("CIENA-WS-PTP-MIB", "cwsPtpPtpPropertiesXcvrType"),
        ("CIENA-WS-PTP-MIB", "cwsPtpPtpPropertiesParentIndex"),
        ("CIENA-WS-PTP-MIB", "cwsPtpPtpPropertiesRate"),
        ("CIENA-WS-PTP-MIB", "cwsPtpTransmitterState"),
        ("CIENA-WS-PTP-MIB", "cwsPtpWavelengthValue"),
        ("CIENA-WS-PTP-MIB", "cwsPtpWavelengthMinValue"),
        ("CIENA-WS-PTP-MIB", "cwsPtpWavelengthMaxValue"),
        ("CIENA-WS-PTP-MIB", "cwsPtpWavelengthActual"),
        ("CIENA-WS-PTP-MIB", "cwsPtpChannelsNumberOfChannels"),
        ("CIENA-WS-PTP-MIB", "cwsPtpChannelChannelNumber"),
        ("CIENA-WS-PTP-MIB", "cwsXcvrRxPowerActual"),
        ("CIENA-WS-PTP-MIB", "cwsXcvrRxPowerMaximum"),
        ("CIENA-WS-PTP-MIB", "cwsXcvrRxPowerMinimum"),
        ("CIENA-WS-PTP-MIB", "cwsXcvrRxPowerMaximumRecordedTime"),
        ("CIENA-WS-PTP-MIB", "cwsXcvrRxPowerMinimumRecordedTime"),
        ("CIENA-WS-PTP-MIB", "cwsXcvrRxStatusHighAlarmStatus"),
        ("CIENA-WS-PTP-MIB", "cwsXcvrRxStatusLowAlarmStatus"),
        ("CIENA-WS-PTP-MIB", "cwsXcvrRxStatusHighWarningStatus"),
        ("CIENA-WS-PTP-MIB", "cwsXcvrRxStatusLowWarningStatus"),
        ("CIENA-WS-PTP-MIB", "cwsPtpRxStatusLossOfSignal"),
        ("CIENA-WS-PTP-MIB", "cwsPtpRxStatusLossOfLock"),
        ("CIENA-WS-PTP-MIB", "cwsXcvrTxPowerActual"),
        ("CIENA-WS-PTP-MIB", "cwsXcvrTxPowerMaximum"),
        ("CIENA-WS-PTP-MIB", "cwsXcvrTxPowerMinimum"),
        ("CIENA-WS-PTP-MIB", "cwsXcvrTxPowerMaximumRecordedTime"),
        ("CIENA-WS-PTP-MIB", "cwsXcvrTxPowerMinimumRecordedTime"),
        ("CIENA-WS-PTP-MIB", "cwsXcvrTxStatusHighAlarmStatus"),
        ("CIENA-WS-PTP-MIB", "cwsXcvrTxStatusLowAlarmStatus"),
        ("CIENA-WS-PTP-MIB", "cwsXcvrTxStatusHighWarningStatus"),
        ("CIENA-WS-PTP-MIB", "cwsXcvrTxStatusLowWarningStatus"),
        ("CIENA-WS-PTP-MIB", "cwsPtpDiagnosticsNumberOfChannels"),
        ("CIENA-WS-PTP-MIB", "cwsPtpDiagnosticsNumberOfEthernet"),
        ("CIENA-WS-PTP-MIB", "cwsPtpPtpOpticalDiagnosticsChannelNumber"),
        ("CIENA-WS-PTP-MIB", "cwsPtpPtpRxOpticalDiagnosticsLossOfSignal"),
        ("CIENA-WS-PTP-MIB", "cwsPtpPtpRxOpticalDiagnosticsLossOfLock"),
        ("CIENA-WS-PTP-MIB", "cwsPtpPtpTxOpticalDiagnosticsLossOfSignal"),
        ("CIENA-WS-PTP-MIB", "cwsPtpPtpTxOpticalDiagnosticsLossOfLock"),
        ("CIENA-WS-PTP-MIB", "cwsPtpPtpEthernetDiagnosticsEthernetId"),
        ("CIENA-WS-PTP-MIB", "cwsPtpPmaSerdesOutOfLock"),
        ("CIENA-WS-PTP-MIB", "cwsPtpFecLossOfAlignmentMarkerLock"),
        ("CIENA-WS-PTP-MIB", "cwsPtpPcsLossOfAlignmentMarker"),
        ("CIENA-WS-PTP-MIB", "cwsPtpPcsLossOfBlockLock"),
        ("CIENA-WS-PTP-MIB", "cwsPtpPcsHighBitErrorRate"),
        ("CIENA-WS-PTP-MIB", "cwsPtpRsLinkDown"),
        ("CIENA-WS-PTP-MIB", "cwsPtpRsLocalFault"),
        ("CIENA-WS-PTP-MIB", "cwsPtpRsRemoteFault"),
        ("CIENA-WS-PTP-MIB", "cwsPtpTraceMismatchMode"),
        ("CIENA-WS-PTP-MIB", "cwsPtpTraceMismatchFailMode"),
        ("CIENA-WS-PTP-MIB", "cwsPtpTraceTxSapi"),
        ("CIENA-WS-PTP-MIB", "cwsPtpTraceTxDapi"),
        ("CIENA-WS-PTP-MIB", "cwsPtpTraceTxOper"),
        ("CIENA-WS-PTP-MIB", "cwsPtpTraceTxOperActual"),
        ("CIENA-WS-PTP-MIB", "cwsPtpTraceTxOperMode"),
        ("CIENA-WS-PTP-MIB", "cwsPtpTraceRxSapi"),
        ("CIENA-WS-PTP-MIB", "cwsPtpTraceRxDapi"),
        ("CIENA-WS-PTP-MIB", "cwsPtpTraceRxOper"),
        ("CIENA-WS-PTP-MIB", "cwsPtpTraceExpSapi"),
        ("CIENA-WS-PTP-MIB", "cwsPtpTraceExpDapi"),
        ("CIENA-WS-PTP-MIB", "cwsPtpTraceExpOper"))
)
if mibBuilder.loadTexts:
    cienaWsPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cienaWsPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 8, 2, 2, 1)
)
cienaWsPtpCompliance.setObjects(
    ("CIENA-WS-PTP-MIB", "cienaWsPtpGroup")
)
if mibBuilder.loadTexts:
    cienaWsPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-PTP-MIB",
    **{"PtpOpEnum": PtpOpEnum,
       "cienaWsPtpMIB": cienaWsPtpMIB,
       "cienaWsPtpObjects": cienaWsPtpObjects,
       "cienaWsPtpConformance": cienaWsPtpConformance,
       "cienaWsPtpGroups": cienaWsPtpGroups,
       "cienaWsPtpGroup": cienaWsPtpGroup,
       "cienaWsPtpCompliances": cienaWsPtpCompliances,
       "cienaWsPtpCompliance": cienaWsPtpCompliance,
       "cwsPtpPtpsTable": cwsPtpPtpsTable,
       "cwsPtpPtpsEntry": cwsPtpPtpsEntry,
       "cwsPtpPtpsPtpIndex": cwsPtpPtpsPtpIndex,
       "cwsPtpPtpIdTable": cwsPtpPtpIdTable,
       "cwsPtpPtpIdEntry": cwsPtpPtpIdEntry,
       "cwsPtpPtpIdTableSnmpKey": cwsPtpPtpIdTableSnmpKey,
       "cwsPtpPtpIdName": cwsPtpPtpIdName,
       "cwsPtpPtpStateTable": cwsPtpPtpStateTable,
       "cwsPtpPtpStateEntry": cwsPtpPtpStateEntry,
       "cwsPtpPtpStateTableSnmpKey": cwsPtpPtpStateTableSnmpKey,
       "cwsPtpPtpStateAdminState": cwsPtpPtpStateAdminState,
       "cwsPtpPtpStateOperationalState": cwsPtpPtpStateOperationalState,
       "cwsPtpPtpStateSpliManagement": cwsPtpPtpStateSpliManagement,
       "cwsPtpPtpPropertiesTable": cwsPtpPtpPropertiesTable,
       "cwsPtpPtpPropertiesEntry": cwsPtpPtpPropertiesEntry,
       "cwsPtpPtpPropertiesTableSnmpKey": cwsPtpPtpPropertiesTableSnmpKey,
       "cwsPtpPtpPropertiesXcvrType": cwsPtpPtpPropertiesXcvrType,
       "cwsPtpPtpPropertiesParentIndex": cwsPtpPtpPropertiesParentIndex,
       "cwsPtpPtpPropertiesRate": cwsPtpPtpPropertiesRate,
       "cwsPtpTransmitterTable": cwsPtpTransmitterTable,
       "cwsPtpTransmitterEntry": cwsPtpTransmitterEntry,
       "cwsPtpTransmitterTableSnmpKey": cwsPtpTransmitterTableSnmpKey,
       "cwsPtpTransmitterState": cwsPtpTransmitterState,
       "cwsPtpWavelengthTable": cwsPtpWavelengthTable,
       "cwsPtpWavelengthEntry": cwsPtpWavelengthEntry,
       "cwsPtpWavelengthTableSnmpKey": cwsPtpWavelengthTableSnmpKey,
       "cwsPtpWavelengthValue": cwsPtpWavelengthValue,
       "cwsPtpWavelengthMinValue": cwsPtpWavelengthMinValue,
       "cwsPtpWavelengthMaxValue": cwsPtpWavelengthMaxValue,
       "cwsPtpWavelengthActual": cwsPtpWavelengthActual,
       "cwsPtpChannelsTable": cwsPtpChannelsTable,
       "cwsPtpChannelsEntry": cwsPtpChannelsEntry,
       "cwsPtpChannelsTableSnmpKey": cwsPtpChannelsTableSnmpKey,
       "cwsPtpChannelsNumberOfChannels": cwsPtpChannelsNumberOfChannels,
       "cwsPtpChannelTable": cwsPtpChannelTable,
       "cwsPtpChannelEntry": cwsPtpChannelEntry,
       "cwsPtpChannelChannelNumber": cwsPtpChannelChannelNumber,
       "cwsPtpRxPowerTable": cwsPtpRxPowerTable,
       "cwsPtpRxPowerEntry": cwsPtpRxPowerEntry,
       "cwsPtpRxPowerTableSnmpKey": cwsPtpRxPowerTableSnmpKey,
       "cwsXcvrRxPowerActual": cwsXcvrRxPowerActual,
       "cwsXcvrRxPowerMaximum": cwsXcvrRxPowerMaximum,
       "cwsXcvrRxPowerMinimum": cwsXcvrRxPowerMinimum,
       "cwsXcvrRxPowerMaximumRecordedTime": cwsXcvrRxPowerMaximumRecordedTime,
       "cwsXcvrRxPowerMinimumRecordedTime": cwsXcvrRxPowerMinimumRecordedTime,
       "cwsPtpRxStatusTable": cwsPtpRxStatusTable,
       "cwsPtpRxStatusEntry": cwsPtpRxStatusEntry,
       "cwsPtpRxStatusTableSnmpKey": cwsPtpRxStatusTableSnmpKey,
       "cwsXcvrRxStatusHighAlarmStatus": cwsXcvrRxStatusHighAlarmStatus,
       "cwsXcvrRxStatusLowAlarmStatus": cwsXcvrRxStatusLowAlarmStatus,
       "cwsXcvrRxStatusHighWarningStatus": cwsXcvrRxStatusHighWarningStatus,
       "cwsXcvrRxStatusLowWarningStatus": cwsXcvrRxStatusLowWarningStatus,
       "cwsPtpRxStatusLossOfSignal": cwsPtpRxStatusLossOfSignal,
       "cwsPtpRxStatusLossOfLock": cwsPtpRxStatusLossOfLock,
       "cwsPtpTxPowerTable": cwsPtpTxPowerTable,
       "cwsPtpTxPowerEntry": cwsPtpTxPowerEntry,
       "cwsPtpTxPowerTableSnmpKey": cwsPtpTxPowerTableSnmpKey,
       "cwsXcvrTxPowerActual": cwsXcvrTxPowerActual,
       "cwsXcvrTxPowerMaximum": cwsXcvrTxPowerMaximum,
       "cwsXcvrTxPowerMinimum": cwsXcvrTxPowerMinimum,
       "cwsXcvrTxPowerMaximumRecordedTime": cwsXcvrTxPowerMaximumRecordedTime,
       "cwsXcvrTxPowerMinimumRecordedTime": cwsXcvrTxPowerMinimumRecordedTime,
       "cwsPtpTxStatusTable": cwsPtpTxStatusTable,
       "cwsPtpTxStatusEntry": cwsPtpTxStatusEntry,
       "cwsPtpTxStatusTableSnmpKey": cwsPtpTxStatusTableSnmpKey,
       "cwsXcvrTxStatusHighAlarmStatus": cwsXcvrTxStatusHighAlarmStatus,
       "cwsXcvrTxStatusLowAlarmStatus": cwsXcvrTxStatusLowAlarmStatus,
       "cwsXcvrTxStatusHighWarningStatus": cwsXcvrTxStatusHighWarningStatus,
       "cwsXcvrTxStatusLowWarningStatus": cwsXcvrTxStatusLowWarningStatus,
       "cwsPtpDiagnosticsTable": cwsPtpDiagnosticsTable,
       "cwsPtpDiagnosticsEntry": cwsPtpDiagnosticsEntry,
       "cwsPtpDiagnosticsTableSnmpKey": cwsPtpDiagnosticsTableSnmpKey,
       "cwsPtpDiagnosticsNumberOfChannels": cwsPtpDiagnosticsNumberOfChannels,
       "cwsPtpDiagnosticsNumberOfEthernet": cwsPtpDiagnosticsNumberOfEthernet,
       "cwsPtpPtpOpticalDiagnosticsTable": cwsPtpPtpOpticalDiagnosticsTable,
       "cwsPtpPtpOpticalDiagnosticsEntry": cwsPtpPtpOpticalDiagnosticsEntry,
       "cwsPtpPtpOpticalDiagnosticsChannelNumber": cwsPtpPtpOpticalDiagnosticsChannelNumber,
       "cwsPtpPtpRxOpticalDiagnosticsTable": cwsPtpPtpRxOpticalDiagnosticsTable,
       "cwsPtpPtpRxOpticalDiagnosticsEntry": cwsPtpPtpRxOpticalDiagnosticsEntry,
       "cwsPtpPtpRxOpticalDiagnosticsTableSnmpKey": cwsPtpPtpRxOpticalDiagnosticsTableSnmpKey,
       "cwsPtpPtpRxOpticalDiagnosticsLossOfSignal": cwsPtpPtpRxOpticalDiagnosticsLossOfSignal,
       "cwsPtpPtpRxOpticalDiagnosticsLossOfLock": cwsPtpPtpRxOpticalDiagnosticsLossOfLock,
       "cwsPtpPtpTxOpticalDiagnosticsTable": cwsPtpPtpTxOpticalDiagnosticsTable,
       "cwsPtpPtpTxOpticalDiagnosticsEntry": cwsPtpPtpTxOpticalDiagnosticsEntry,
       "cwsPtpPtpTxOpticalDiagnosticsTableSnmpKey": cwsPtpPtpTxOpticalDiagnosticsTableSnmpKey,
       "cwsPtpPtpTxOpticalDiagnosticsLossOfSignal": cwsPtpPtpTxOpticalDiagnosticsLossOfSignal,
       "cwsPtpPtpTxOpticalDiagnosticsLossOfLock": cwsPtpPtpTxOpticalDiagnosticsLossOfLock,
       "cwsPtpPtpEthernetDiagnosticsTable": cwsPtpPtpEthernetDiagnosticsTable,
       "cwsPtpPtpEthernetDiagnosticsEntry": cwsPtpPtpEthernetDiagnosticsEntry,
       "cwsPtpPtpEthernetDiagnosticsEthernetId": cwsPtpPtpEthernetDiagnosticsEthernetId,
       "cwsPtpPmaTable": cwsPtpPmaTable,
       "cwsPtpPmaEntry": cwsPtpPmaEntry,
       "cwsPtpPmaTableSnmpKey": cwsPtpPmaTableSnmpKey,
       "cwsPtpPmaSerdesOutOfLock": cwsPtpPmaSerdesOutOfLock,
       "cwsPtpFecTable": cwsPtpFecTable,
       "cwsPtpFecEntry": cwsPtpFecEntry,
       "cwsPtpFecTableSnmpKey": cwsPtpFecTableSnmpKey,
       "cwsPtpFecLossOfAlignmentMarkerLock": cwsPtpFecLossOfAlignmentMarkerLock,
       "cwsPtpPcsTable": cwsPtpPcsTable,
       "cwsPtpPcsEntry": cwsPtpPcsEntry,
       "cwsPtpPcsTableSnmpKey": cwsPtpPcsTableSnmpKey,
       "cwsPtpPcsLossOfAlignmentMarker": cwsPtpPcsLossOfAlignmentMarker,
       "cwsPtpPcsLossOfBlockLock": cwsPtpPcsLossOfBlockLock,
       "cwsPtpPcsHighBitErrorRate": cwsPtpPcsHighBitErrorRate,
       "cwsPtpRsTable": cwsPtpRsTable,
       "cwsPtpRsEntry": cwsPtpRsEntry,
       "cwsPtpRsTableSnmpKey": cwsPtpRsTableSnmpKey,
       "cwsPtpRsLinkDown": cwsPtpRsLinkDown,
       "cwsPtpRsLocalFault": cwsPtpRsLocalFault,
       "cwsPtpRsRemoteFault": cwsPtpRsRemoteFault,
       "cwsPtpTraceTable": cwsPtpTraceTable,
       "cwsPtpTraceEntry": cwsPtpTraceEntry,
       "cwsPtpTraceTableSnmpKey": cwsPtpTraceTableSnmpKey,
       "cwsPtpTraceMismatchMode": cwsPtpTraceMismatchMode,
       "cwsPtpTraceMismatchFailMode": cwsPtpTraceMismatchFailMode,
       "cwsPtpTraceTxSapi": cwsPtpTraceTxSapi,
       "cwsPtpTraceTxDapi": cwsPtpTraceTxDapi,
       "cwsPtpTraceTxOper": cwsPtpTraceTxOper,
       "cwsPtpTraceTxOperActual": cwsPtpTraceTxOperActual,
       "cwsPtpTraceTxOperMode": cwsPtpTraceTxOperMode,
       "cwsPtpTraceRxSapi": cwsPtpTraceRxSapi,
       "cwsPtpTraceRxDapi": cwsPtpTraceRxDapi,
       "cwsPtpTraceRxOper": cwsPtpTraceRxOper,
       "cwsPtpTraceExpSapi": cwsPtpTraceExpSapi,
       "cwsPtpTraceExpDapi": cwsPtpTraceExpDapi,
       "cwsPtpTraceExpOper": cwsPtpTraceExpOper}
)
