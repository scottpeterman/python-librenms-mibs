# SNMP MIB module (CIENA-WS-PTP-MODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-WS-PTP-MODEM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:13 2025
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

(cwsPtpDiagnosticsEntry,
 cwsPtpTransmitterEntry) = mibBuilder.importSymbols(
    "CIENA-WS-PTP-MIB",
    "cwsPtpDiagnosticsEntry",
    "cwsPtpTransmitterEntry")

(ChannelsNumber,
 Decimal1Dig,
 Decimal2Dig,
 EnabledDisabledEnum,
 LineSysEnum,
 ModemChannel,
 ModemFrequency,
 OnOffEnum,
 PtpId,
 RecoverLinkDispersionType,
 StringMaxl32,
 StringSci,
 TxPowerLvl,
 WlSpacing) = mibBuilder.importSymbols(
    "CIENA-WS-TYPEDEFS-MIB",
    "ChannelsNumber",
    "Decimal1Dig",
    "Decimal2Dig",
    "EnabledDisabledEnum",
    "LineSysEnum",
    "ModemChannel",
    "ModemFrequency",
    "OnOffEnum",
    "PtpId",
    "RecoverLinkDispersionType",
    "StringMaxl32",
    "StringSci",
    "TxPowerLvl",
    "WlSpacing")

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

cienaWsPtpModemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9)
)
if mibBuilder.loadTexts:
    cienaWsPtpModemMIB.setRevisions(
        ("2017-03-02 00:00",
         "2016-12-12 00:00",
         "2016-06-14 00:00",
         "2016-02-01 00:00",
         "2015-04-29 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaWsPtpModemObjects_ObjectIdentity = ObjectIdentity
cienaWsPtpModemObjects = _CienaWsPtpModemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 1)
)
_CienaWsPtpModemConformance_ObjectIdentity = ObjectIdentity
cienaWsPtpModemConformance = _CienaWsPtpModemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 2)
)
_CienaWsPtpModemGroups_ObjectIdentity = ObjectIdentity
cienaWsPtpModemGroups = _CienaWsPtpModemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 2, 1)
)
_CienaWsPtpModemCompliances_ObjectIdentity = ObjectIdentity
cienaWsPtpModemCompliances = _CienaWsPtpModemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 2, 2)
)
_CwsPtpAugPtpModemTransmitterTable_Object = MibTable
cwsPtpAugPtpModemTransmitterTable = _CwsPtpAugPtpModemTransmitterTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 3)
)
if mibBuilder.loadTexts:
    cwsPtpAugPtpModemTransmitterTable.setStatus("current")
_CwsPtpAugPtpModemTransmitterEntry_Object = MibTableRow
cwsPtpAugPtpModemTransmitterEntry = _CwsPtpAugPtpModemTransmitterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 3, 1)
)
if mibBuilder.loadTexts:
    cwsPtpAugPtpModemTransmitterEntry.setStatus("current")
_CwsPtpModemTransmitterLineSystemChannelNumber_Type = ModemChannel
_CwsPtpModemTransmitterLineSystemChannelNumber_Object = MibTableColumn
cwsPtpModemTransmitterLineSystemChannelNumber = _CwsPtpModemTransmitterLineSystemChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 3, 1, 1),
    _CwsPtpModemTransmitterLineSystemChannelNumber_Type()
)
cwsPtpModemTransmitterLineSystemChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemTransmitterLineSystemChannelNumber.setStatus("current")
_CwsPtpModemFrequencyTable_Object = MibTable
cwsPtpModemFrequencyTable = _CwsPtpModemFrequencyTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 4)
)
if mibBuilder.loadTexts:
    cwsPtpModemFrequencyTable.setStatus("current")
_CwsPtpModemFrequencyEntry_Object = MibTableRow
cwsPtpModemFrequencyEntry = _CwsPtpModemFrequencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 4, 1)
)
cwsPtpModemFrequencyEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemFrequencyTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemFrequencyEntry.setStatus("current")


class _CwsPtpModemFrequencyTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemFrequencyTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemFrequencyTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemFrequencyTableSnmpKey_Object = MibTableColumn
cwsPtpModemFrequencyTableSnmpKey = _CwsPtpModemFrequencyTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 4, 1, 1),
    _CwsPtpModemFrequencyTableSnmpKey_Type()
)
cwsPtpModemFrequencyTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemFrequencyTableSnmpKey.setStatus("current")
_CwsPtpModemFrequencyValue_Type = ModemFrequency
_CwsPtpModemFrequencyValue_Object = MibTableColumn
cwsPtpModemFrequencyValue = _CwsPtpModemFrequencyValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 4, 1, 2),
    _CwsPtpModemFrequencyValue_Type()
)
cwsPtpModemFrequencyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemFrequencyValue.setStatus("current")
_CwsPtpModemFrequencyMinValue_Type = Decimal1Dig
_CwsPtpModemFrequencyMinValue_Object = MibTableColumn
cwsPtpModemFrequencyMinValue = _CwsPtpModemFrequencyMinValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 4, 1, 3),
    _CwsPtpModemFrequencyMinValue_Type()
)
cwsPtpModemFrequencyMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemFrequencyMinValue.setStatus("current")
_CwsPtpModemFrequencyMaxValue_Type = Decimal1Dig
_CwsPtpModemFrequencyMaxValue_Object = MibTableColumn
cwsPtpModemFrequencyMaxValue = _CwsPtpModemFrequencyMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 4, 1, 4),
    _CwsPtpModemFrequencyMaxValue_Type()
)
cwsPtpModemFrequencyMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemFrequencyMaxValue.setStatus("current")
_CwsPtpModemFrequencyActual_Type = Decimal1Dig
_CwsPtpModemFrequencyActual_Object = MibTableColumn
cwsPtpModemFrequencyActual = _CwsPtpModemFrequencyActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 4, 1, 5),
    _CwsPtpModemFrequencyActual_Type()
)
cwsPtpModemFrequencyActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemFrequencyActual.setStatus("current")
_CwsPtpModemPowerTable_Object = MibTable
cwsPtpModemPowerTable = _CwsPtpModemPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 5)
)
if mibBuilder.loadTexts:
    cwsPtpModemPowerTable.setStatus("current")
_CwsPtpModemPowerEntry_Object = MibTableRow
cwsPtpModemPowerEntry = _CwsPtpModemPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 5, 1)
)
cwsPtpModemPowerEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemPowerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemPowerEntry.setStatus("current")


class _CwsPtpModemPowerTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemPowerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemPowerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemPowerTableSnmpKey_Object = MibTableColumn
cwsPtpModemPowerTableSnmpKey = _CwsPtpModemPowerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 5, 1, 1),
    _CwsPtpModemPowerTableSnmpKey_Type()
)
cwsPtpModemPowerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemPowerTableSnmpKey.setStatus("current")
_CwsPtpModemPowerValue_Type = TxPowerLvl
_CwsPtpModemPowerValue_Object = MibTableColumn
cwsPtpModemPowerValue = _CwsPtpModemPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 5, 1, 2),
    _CwsPtpModemPowerValue_Type()
)
cwsPtpModemPowerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemPowerValue.setStatus("current")
_CwsPtpModemPowerMinValue_Type = Decimal1Dig
_CwsPtpModemPowerMinValue_Object = MibTableColumn
cwsPtpModemPowerMinValue = _CwsPtpModemPowerMinValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 5, 1, 3),
    _CwsPtpModemPowerMinValue_Type()
)
cwsPtpModemPowerMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemPowerMinValue.setStatus("current")
_CwsPtpModemPowerMaxValue_Type = Decimal1Dig
_CwsPtpModemPowerMaxValue_Object = MibTableColumn
cwsPtpModemPowerMaxValue = _CwsPtpModemPowerMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 5, 1, 4),
    _CwsPtpModemPowerMaxValue_Type()
)
cwsPtpModemPowerMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemPowerMaxValue.setStatus("current")
_CwsPtpModemLineSystemTable_Object = MibTable
cwsPtpModemLineSystemTable = _CwsPtpModemLineSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 6)
)
if mibBuilder.loadTexts:
    cwsPtpModemLineSystemTable.setStatus("current")
_CwsPtpModemLineSystemEntry_Object = MibTableRow
cwsPtpModemLineSystemEntry = _CwsPtpModemLineSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 6, 1)
)
cwsPtpModemLineSystemEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemLineSystemTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemLineSystemEntry.setStatus("current")


class _CwsPtpModemLineSystemTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemLineSystemTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemLineSystemTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemLineSystemTableSnmpKey_Object = MibTableColumn
cwsPtpModemLineSystemTableSnmpKey = _CwsPtpModemLineSystemTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 6, 1, 1),
    _CwsPtpModemLineSystemTableSnmpKey_Type()
)
cwsPtpModemLineSystemTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemLineSystemTableSnmpKey.setStatus("current")
_CwsPtpModemLineSystemType_Type = LineSysEnum
_CwsPtpModemLineSystemType_Object = MibTableColumn
cwsPtpModemLineSystemType = _CwsPtpModemLineSystemType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 6, 1, 2),
    _CwsPtpModemLineSystemType_Type()
)
cwsPtpModemLineSystemType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemLineSystemType.setStatus("current")
_CwsPtpModemLineSystemWavelengthSpacing_Type = WlSpacing
_CwsPtpModemLineSystemWavelengthSpacing_Object = MibTableColumn
cwsPtpModemLineSystemWavelengthSpacing = _CwsPtpModemLineSystemWavelengthSpacing_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 6, 1, 3),
    _CwsPtpModemLineSystemWavelengthSpacing_Type()
)
cwsPtpModemLineSystemWavelengthSpacing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemLineSystemWavelengthSpacing.setStatus("current")
_CwsPtpModemCmdTable_Object = MibTable
cwsPtpModemCmdTable = _CwsPtpModemCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 7)
)
if mibBuilder.loadTexts:
    cwsPtpModemCmdTable.setStatus("current")
_CwsPtpModemCmdEntry_Object = MibTableRow
cwsPtpModemCmdEntry = _CwsPtpModemCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 7, 1)
)
cwsPtpModemCmdEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemCmdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemCmdEntry.setStatus("current")


class _CwsPtpModemCmdTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemCmdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemCmdTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemCmdTableSnmpKey_Object = MibTableColumn
cwsPtpModemCmdTableSnmpKey = _CwsPtpModemCmdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 7, 1, 1),
    _CwsPtpModemCmdTableSnmpKey_Type()
)
cwsPtpModemCmdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemCmdTableSnmpKey.setStatus("current")
_CwsPtpModemCmdSlot_Type = Unsigned32
_CwsPtpModemCmdSlot_Object = MibTableColumn
cwsPtpModemCmdSlot = _CwsPtpModemCmdSlot_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 7, 1, 2),
    _CwsPtpModemCmdSlot_Type()
)
cwsPtpModemCmdSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemCmdSlot.setStatus("current")
_CwsPtpModemCmdPortIn_Type = Unsigned32
_CwsPtpModemCmdPortIn_Object = MibTableColumn
cwsPtpModemCmdPortIn = _CwsPtpModemCmdPortIn_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 7, 1, 3),
    _CwsPtpModemCmdPortIn_Type()
)
cwsPtpModemCmdPortIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemCmdPortIn.setStatus("current")
_CwsPtpModemCmdPortOut_Type = Unsigned32
_CwsPtpModemCmdPortOut_Object = MibTableColumn
cwsPtpModemCmdPortOut = _CwsPtpModemCmdPortOut_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 7, 1, 4),
    _CwsPtpModemCmdPortOut_Type()
)
cwsPtpModemCmdPortOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemCmdPortOut.setStatus("current")
_CwsPtpModemModemTable_Object = MibTable
cwsPtpModemModemTable = _CwsPtpModemModemTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 8)
)
if mibBuilder.loadTexts:
    cwsPtpModemModemTable.setStatus("current")
_CwsPtpModemModemEntry_Object = MibTableRow
cwsPtpModemModemEntry = _CwsPtpModemModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 8, 1)
)
cwsPtpModemModemEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemModemEntry.setStatus("current")


class _CwsPtpModemModemTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemModemTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemModemTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemModemTableSnmpKey_Object = MibTableColumn
cwsPtpModemModemTableSnmpKey = _CwsPtpModemModemTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 8, 1, 1),
    _CwsPtpModemModemTableSnmpKey_Type()
)
cwsPtpModemModemTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemModemTableSnmpKey.setStatus("current")
_CwsPtpModemModemChannelContentionDetectionAvoidance_Type = OnOffEnum
_CwsPtpModemModemChannelContentionDetectionAvoidance_Object = MibTableColumn
cwsPtpModemModemChannelContentionDetectionAvoidance = _CwsPtpModemModemChannelContentionDetectionAvoidance_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 8, 1, 2),
    _CwsPtpModemModemChannelContentionDetectionAvoidance_Type()
)
cwsPtpModemModemChannelContentionDetectionAvoidance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemModemChannelContentionDetectionAvoidance.setStatus("current")


class _CwsPtpModemModemPerformanceOptimizationMode_Type(Integer32):
    """Custom type cwsPtpModemModemPerformanceOptimizationMode based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("reach", 0),
          ("latency", 1),
          ("fasttracking", 2),
          ("improvedtracking", 3),
          ("mode5", 4),
          ("mode6", 5),
          ("mode7", 6),
          ("mode8", 7),
          ("mode9", 8),
          ("mode10", 9),
          ("mode11", 10),
          ("mode12", 11),
          ("mode13", 12),
          ("mode14", 13))
    )


_CwsPtpModemModemPerformanceOptimizationMode_Type.__name__ = "Integer32"
_CwsPtpModemModemPerformanceOptimizationMode_Object = MibTableColumn
cwsPtpModemModemPerformanceOptimizationMode = _CwsPtpModemModemPerformanceOptimizationMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 8, 1, 3),
    _CwsPtpModemModemPerformanceOptimizationMode_Type()
)
cwsPtpModemModemPerformanceOptimizationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemModemPerformanceOptimizationMode.setStatus("current")


class _CwsPtpModemModemCarrierCenteringMode_Type(Integer32):
    """Custom type cwsPtpModemModemCarrierCenteringMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mode1", 0),
          ("mode2", 1),
          ("mode3", 3))
    )


_CwsPtpModemModemCarrierCenteringMode_Type.__name__ = "Integer32"
_CwsPtpModemModemCarrierCenteringMode_Object = MibTableColumn
cwsPtpModemModemCarrierCenteringMode = _CwsPtpModemModemCarrierCenteringMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 8, 1, 4),
    _CwsPtpModemModemCarrierCenteringMode_Type()
)
cwsPtpModemModemCarrierCenteringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemModemCarrierCenteringMode.setStatus("current")


class _CwsPtpModemModemInterleaverMode_Type(Integer32):
    """Custom type cwsPtpModemModemInterleaverMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("standard", 1),
          ("enhanced", 2),
          ("auto", 3))
    )


_CwsPtpModemModemInterleaverMode_Type.__name__ = "Integer32"
_CwsPtpModemModemInterleaverMode_Object = MibTableColumn
cwsPtpModemModemInterleaverMode = _CwsPtpModemModemInterleaverMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 8, 1, 5),
    _CwsPtpModemModemInterleaverMode_Type()
)
cwsPtpModemModemInterleaverMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemModemInterleaverMode.setStatus("current")
_CwsPtpModemModemRotation_Type = OnOffEnum
_CwsPtpModemModemRotation_Object = MibTableColumn
cwsPtpModemModemRotation = _CwsPtpModemModemRotation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 8, 1, 6),
    _CwsPtpModemModemRotation_Type()
)
cwsPtpModemModemRotation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemModemRotation.setStatus("current")


class _CwsPtpModemModemSpectralOccupancyMode_Type(Integer32):
    """Custom type cwsPtpModemModemSpectralOccupancyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("narrow", 0),
          ("wide", 1))
    )


_CwsPtpModemModemSpectralOccupancyMode_Type.__name__ = "Integer32"
_CwsPtpModemModemSpectralOccupancyMode_Object = MibTableColumn
cwsPtpModemModemSpectralOccupancyMode = _CwsPtpModemModemSpectralOccupancyMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 8, 1, 7),
    _CwsPtpModemModemSpectralOccupancyMode_Type()
)
cwsPtpModemModemSpectralOccupancyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemModemSpectralOccupancyMode.setStatus("current")
_CwsPtpModemModemTxPowerReductionState_Type = EnabledDisabledEnum
_CwsPtpModemModemTxPowerReductionState_Object = MibTableColumn
cwsPtpModemModemTxPowerReductionState = _CwsPtpModemModemTxPowerReductionState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 8, 1, 8),
    _CwsPtpModemModemTxPowerReductionState_Type()
)
cwsPtpModemModemTxPowerReductionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemModemTxPowerReductionState.setStatus("current")


class _CwsPtpModemModemTxReductionMode_Type(Integer32):
    """Custom type cwsPtpModemModemTxReductionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("positive", 0),
          ("negative", 1),
          ("auto", 2))
    )


_CwsPtpModemModemTxReductionMode_Type.__name__ = "Integer32"
_CwsPtpModemModemTxReductionMode_Object = MibTableColumn
cwsPtpModemModemTxReductionMode = _CwsPtpModemModemTxReductionMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 8, 1, 9),
    _CwsPtpModemModemTxReductionMode_Type()
)
cwsPtpModemModemTxReductionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemModemTxReductionMode.setStatus("current")


class _CwsPtpModemModemTxTuningMode_Type(Integer32):
    """Custom type cwsPtpModemModemTxTuningMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("performanceoptimized", 0),
          ("accelerated", 1))
    )


_CwsPtpModemModemTxTuningMode_Type.__name__ = "Integer32"
_CwsPtpModemModemTxTuningMode_Object = MibTableColumn
cwsPtpModemModemTxTuningMode = _CwsPtpModemModemTxTuningMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 8, 1, 10),
    _CwsPtpModemModemTxTuningMode_Type()
)
cwsPtpModemModemTxTuningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemModemTxTuningMode.setStatus("current")


class _CwsPtpModemModemDifferentialEncoding_Type(Integer32):
    """Custom type cwsPtpModemModemDifferentialEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("hard", 1),
          ("soft", 2),
          ("xd", 3))
    )


_CwsPtpModemModemDifferentialEncoding_Type.__name__ = "Integer32"
_CwsPtpModemModemDifferentialEncoding_Object = MibTableColumn
cwsPtpModemModemDifferentialEncoding = _CwsPtpModemModemDifferentialEncoding_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 8, 1, 11),
    _CwsPtpModemModemDifferentialEncoding_Type()
)
cwsPtpModemModemDifferentialEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemModemDifferentialEncoding.setStatus("current")


class _CwsPtpModemModemTxCompensationDispersionMode_Type(Integer32):
    """Custom type cwsPtpModemModemTxCompensationDispersionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manual", 0),
          ("automatic", 1),
          ("custom1", 2),
          ("off", 3))
    )


_CwsPtpModemModemTxCompensationDispersionMode_Type.__name__ = "Integer32"
_CwsPtpModemModemTxCompensationDispersionMode_Object = MibTableColumn
cwsPtpModemModemTxCompensationDispersionMode = _CwsPtpModemModemTxCompensationDispersionMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 8, 1, 12),
    _CwsPtpModemModemTxCompensationDispersionMode_Type()
)
cwsPtpModemModemTxCompensationDispersionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemModemTxCompensationDispersionMode.setStatus("current")
_CwsPtpModemModemTxCompensationDispersionValue_Type = Decimal1Dig
_CwsPtpModemModemTxCompensationDispersionValue_Object = MibTableColumn
cwsPtpModemModemTxCompensationDispersionValue = _CwsPtpModemModemTxCompensationDispersionValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 8, 1, 13),
    _CwsPtpModemModemTxCompensationDispersionValue_Type()
)
cwsPtpModemModemTxCompensationDispersionValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemModemTxCompensationDispersionValue.setStatus("current")
_CwsPtpModemModemFastReceiverRecoveryState_Type = EnabledDisabledEnum
_CwsPtpModemModemFastReceiverRecoveryState_Object = MibTableColumn
cwsPtpModemModemFastReceiverRecoveryState = _CwsPtpModemModemFastReceiverRecoveryState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 8, 1, 14),
    _CwsPtpModemModemFastReceiverRecoveryState_Type()
)
cwsPtpModemModemFastReceiverRecoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemModemFastReceiverRecoveryState.setStatus("obsolete")
_CwsPtpModemModemLaserCenteringRange_Type = Decimal1Dig
_CwsPtpModemModemLaserCenteringRange_Object = MibTableColumn
cwsPtpModemModemLaserCenteringRange = _CwsPtpModemModemLaserCenteringRange_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 8, 1, 15),
    _CwsPtpModemModemLaserCenteringRange_Type()
)
cwsPtpModemModemLaserCenteringRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemModemLaserCenteringRange.setStatus("current")
_CwsPtpModemPerformanceStatisticsTable_Object = MibTable
cwsPtpModemPerformanceStatisticsTable = _CwsPtpModemPerformanceStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 9)
)
if mibBuilder.loadTexts:
    cwsPtpModemPerformanceStatisticsTable.setStatus("current")
_CwsPtpModemPerformanceStatisticsEntry_Object = MibTableRow
cwsPtpModemPerformanceStatisticsEntry = _CwsPtpModemPerformanceStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 9, 1)
)
cwsPtpModemPerformanceStatisticsEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemPerformanceStatisticsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemPerformanceStatisticsEntry.setStatus("current")


class _CwsPtpModemPerformanceStatisticsTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemPerformanceStatisticsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemPerformanceStatisticsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemPerformanceStatisticsTableSnmpKey_Object = MibTableColumn
cwsPtpModemPerformanceStatisticsTableSnmpKey = _CwsPtpModemPerformanceStatisticsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 9, 1, 1),
    _CwsPtpModemPerformanceStatisticsTableSnmpKey_Type()
)
cwsPtpModemPerformanceStatisticsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemPerformanceStatisticsTableSnmpKey.setStatus("current")
_CwsPtpModemPerformanceStatisticsSecondsSinceLastClear_Type = Unsigned32
_CwsPtpModemPerformanceStatisticsSecondsSinceLastClear_Object = MibTableColumn
cwsPtpModemPerformanceStatisticsSecondsSinceLastClear = _CwsPtpModemPerformanceStatisticsSecondsSinceLastClear_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 9, 1, 2),
    _CwsPtpModemPerformanceStatisticsSecondsSinceLastClear_Type()
)
cwsPtpModemPerformanceStatisticsSecondsSinceLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemPerformanceStatisticsSecondsSinceLastClear.setStatus("current")
_CwsPtpModemPerformanceStatisticsFecUncorrectedBlockCount_Type = Unsigned32
_CwsPtpModemPerformanceStatisticsFecUncorrectedBlockCount_Object = MibTableColumn
cwsPtpModemPerformanceStatisticsFecUncorrectedBlockCount = _CwsPtpModemPerformanceStatisticsFecUncorrectedBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 9, 1, 3),
    _CwsPtpModemPerformanceStatisticsFecUncorrectedBlockCount_Type()
)
cwsPtpModemPerformanceStatisticsFecUncorrectedBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemPerformanceStatisticsFecUncorrectedBlockCount.setStatus("current")
_CwsPtpModemPerformanceStatisticsHighCorrectionCountSeconds_Type = Unsigned32
_CwsPtpModemPerformanceStatisticsHighCorrectionCountSeconds_Object = MibTableColumn
cwsPtpModemPerformanceStatisticsHighCorrectionCountSeconds = _CwsPtpModemPerformanceStatisticsHighCorrectionCountSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 9, 1, 4),
    _CwsPtpModemPerformanceStatisticsHighCorrectionCountSeconds_Type()
)
cwsPtpModemPerformanceStatisticsHighCorrectionCountSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemPerformanceStatisticsHighCorrectionCountSeconds.setStatus("current")
_CwsPtpModemPreFecBerTable_Object = MibTable
cwsPtpModemPreFecBerTable = _CwsPtpModemPreFecBerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 10)
)
if mibBuilder.loadTexts:
    cwsPtpModemPreFecBerTable.setStatus("current")
_CwsPtpModemPreFecBerEntry_Object = MibTableRow
cwsPtpModemPreFecBerEntry = _CwsPtpModemPreFecBerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 10, 1)
)
cwsPtpModemPreFecBerEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemPreFecBerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemPreFecBerEntry.setStatus("current")


class _CwsPtpModemPreFecBerTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemPreFecBerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemPreFecBerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemPreFecBerTableSnmpKey_Object = MibTableColumn
cwsPtpModemPreFecBerTableSnmpKey = _CwsPtpModemPreFecBerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 10, 1, 1),
    _CwsPtpModemPreFecBerTableSnmpKey_Type()
)
cwsPtpModemPreFecBerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemPreFecBerTableSnmpKey.setStatus("current")
_CwsPtpModemPreFecBerActual_Type = StringSci
_CwsPtpModemPreFecBerActual_Object = MibTableColumn
cwsPtpModemPreFecBerActual = _CwsPtpModemPreFecBerActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 10, 1, 2),
    _CwsPtpModemPreFecBerActual_Type()
)
cwsPtpModemPreFecBerActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemPreFecBerActual.setStatus("current")
_CwsPtpModemPreFecBerMax_Type = StringSci
_CwsPtpModemPreFecBerMax_Object = MibTableColumn
cwsPtpModemPreFecBerMax = _CwsPtpModemPreFecBerMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 10, 1, 3),
    _CwsPtpModemPreFecBerMax_Type()
)
cwsPtpModemPreFecBerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemPreFecBerMax.setStatus("current")
_CwsPtpModemPreFecBerMin_Type = StringSci
_CwsPtpModemPreFecBerMin_Object = MibTableColumn
cwsPtpModemPreFecBerMin = _CwsPtpModemPreFecBerMin_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 10, 1, 4),
    _CwsPtpModemPreFecBerMin_Type()
)
cwsPtpModemPreFecBerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemPreFecBerMin.setStatus("obsolete")
_CwsPtpModemPreFecBerAverage_Type = StringSci
_CwsPtpModemPreFecBerAverage_Object = MibTableColumn
cwsPtpModemPreFecBerAverage = _CwsPtpModemPreFecBerAverage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 10, 1, 5),
    _CwsPtpModemPreFecBerAverage_Type()
)
cwsPtpModemPreFecBerAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemPreFecBerAverage.setStatus("obsolete")
_CwsPtpModemPostFecBerTable_Object = MibTable
cwsPtpModemPostFecBerTable = _CwsPtpModemPostFecBerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 11)
)
if mibBuilder.loadTexts:
    cwsPtpModemPostFecBerTable.setStatus("current")
_CwsPtpModemPostFecBerEntry_Object = MibTableRow
cwsPtpModemPostFecBerEntry = _CwsPtpModemPostFecBerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 11, 1)
)
cwsPtpModemPostFecBerEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemPostFecBerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemPostFecBerEntry.setStatus("current")


class _CwsPtpModemPostFecBerTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemPostFecBerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemPostFecBerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemPostFecBerTableSnmpKey_Object = MibTableColumn
cwsPtpModemPostFecBerTableSnmpKey = _CwsPtpModemPostFecBerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 11, 1, 1),
    _CwsPtpModemPostFecBerTableSnmpKey_Type()
)
cwsPtpModemPostFecBerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemPostFecBerTableSnmpKey.setStatus("current")
_CwsPtpModemPostFecBerActual_Type = StringSci
_CwsPtpModemPostFecBerActual_Object = MibTableColumn
cwsPtpModemPostFecBerActual = _CwsPtpModemPostFecBerActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 11, 1, 2),
    _CwsPtpModemPostFecBerActual_Type()
)
cwsPtpModemPostFecBerActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemPostFecBerActual.setStatus("current")
_CwsPtpModemPostFecBerMax_Type = StringSci
_CwsPtpModemPostFecBerMax_Object = MibTableColumn
cwsPtpModemPostFecBerMax = _CwsPtpModemPostFecBerMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 11, 1, 3),
    _CwsPtpModemPostFecBerMax_Type()
)
cwsPtpModemPostFecBerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemPostFecBerMax.setStatus("obsolete")
_CwsPtpModemPostFecBerMin_Type = StringSci
_CwsPtpModemPostFecBerMin_Object = MibTableColumn
cwsPtpModemPostFecBerMin = _CwsPtpModemPostFecBerMin_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 11, 1, 4),
    _CwsPtpModemPostFecBerMin_Type()
)
cwsPtpModemPostFecBerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemPostFecBerMin.setStatus("obsolete")
_CwsPtpModemPostFecBerAverage_Type = StringSci
_CwsPtpModemPostFecBerAverage_Object = MibTableColumn
cwsPtpModemPostFecBerAverage = _CwsPtpModemPostFecBerAverage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 11, 1, 5),
    _CwsPtpModemPostFecBerAverage_Type()
)
cwsPtpModemPostFecBerAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemPostFecBerAverage.setStatus("obsolete")
_CwsPtpModemQFactorTable_Object = MibTable
cwsPtpModemQFactorTable = _CwsPtpModemQFactorTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 12)
)
if mibBuilder.loadTexts:
    cwsPtpModemQFactorTable.setStatus("current")
_CwsPtpModemQFactorEntry_Object = MibTableRow
cwsPtpModemQFactorEntry = _CwsPtpModemQFactorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 12, 1)
)
cwsPtpModemQFactorEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemQFactorTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemQFactorEntry.setStatus("current")


class _CwsPtpModemQFactorTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemQFactorTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemQFactorTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemQFactorTableSnmpKey_Object = MibTableColumn
cwsPtpModemQFactorTableSnmpKey = _CwsPtpModemQFactorTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 12, 1, 1),
    _CwsPtpModemQFactorTableSnmpKey_Type()
)
cwsPtpModemQFactorTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemQFactorTableSnmpKey.setStatus("current")
_CwsPtpModemQFactorActual_Type = Decimal2Dig
_CwsPtpModemQFactorActual_Object = MibTableColumn
cwsPtpModemQFactorActual = _CwsPtpModemQFactorActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 12, 1, 2),
    _CwsPtpModemQFactorActual_Type()
)
cwsPtpModemQFactorActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemQFactorActual.setStatus("current")
_CwsPtpModemQFactorMax_Type = Decimal2Dig
_CwsPtpModemQFactorMax_Object = MibTableColumn
cwsPtpModemQFactorMax = _CwsPtpModemQFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 12, 1, 3),
    _CwsPtpModemQFactorMax_Type()
)
cwsPtpModemQFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemQFactorMax.setStatus("current")
_CwsPtpModemQFactorMin_Type = Decimal2Dig
_CwsPtpModemQFactorMin_Object = MibTableColumn
cwsPtpModemQFactorMin = _CwsPtpModemQFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 12, 1, 4),
    _CwsPtpModemQFactorMin_Type()
)
cwsPtpModemQFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemQFactorMin.setStatus("current")
_CwsPtpModemQFactorAverage_Type = Decimal2Dig
_CwsPtpModemQFactorAverage_Object = MibTableColumn
cwsPtpModemQFactorAverage = _CwsPtpModemQFactorAverage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 12, 1, 5),
    _CwsPtpModemQFactorAverage_Type()
)
cwsPtpModemQFactorAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemQFactorAverage.setStatus("obsolete")
_CwsPtpModemFecFrameErrorCountTable_Object = MibTable
cwsPtpModemFecFrameErrorCountTable = _CwsPtpModemFecFrameErrorCountTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 13)
)
if mibBuilder.loadTexts:
    cwsPtpModemFecFrameErrorCountTable.setStatus("current")
_CwsPtpModemFecFrameErrorCountEntry_Object = MibTableRow
cwsPtpModemFecFrameErrorCountEntry = _CwsPtpModemFecFrameErrorCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 13, 1)
)
cwsPtpModemFecFrameErrorCountEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemFecFrameErrorCountTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemFecFrameErrorCountEntry.setStatus("current")


class _CwsPtpModemFecFrameErrorCountTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemFecFrameErrorCountTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemFecFrameErrorCountTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemFecFrameErrorCountTableSnmpKey_Object = MibTableColumn
cwsPtpModemFecFrameErrorCountTableSnmpKey = _CwsPtpModemFecFrameErrorCountTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 13, 1, 1),
    _CwsPtpModemFecFrameErrorCountTableSnmpKey_Type()
)
cwsPtpModemFecFrameErrorCountTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemFecFrameErrorCountTableSnmpKey.setStatus("current")
_CwsPtpModemFecFrameErrorCountValue_Type = Unsigned32
_CwsPtpModemFecFrameErrorCountValue_Object = MibTableColumn
cwsPtpModemFecFrameErrorCountValue = _CwsPtpModemFecFrameErrorCountValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 13, 1, 2),
    _CwsPtpModemFecFrameErrorCountValue_Type()
)
cwsPtpModemFecFrameErrorCountValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemFecFrameErrorCountValue.setStatus("current")
_CwsPtpModemFecFrameErrorCountSeconds_Type = Unsigned32
_CwsPtpModemFecFrameErrorCountSeconds_Object = MibTableColumn
cwsPtpModemFecFrameErrorCountSeconds = _CwsPtpModemFecFrameErrorCountSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 13, 1, 3),
    _CwsPtpModemFecFrameErrorCountSeconds_Type()
)
cwsPtpModemFecFrameErrorCountSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemFecFrameErrorCountSeconds.setStatus("current")
_CwsPtpModemModemprefecsignalfailalarmTable_Object = MibTable
cwsPtpModemModemprefecsignalfailalarmTable = _CwsPtpModemModemprefecsignalfailalarmTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 14)
)
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignalfailalarmTable.setStatus("current")
_CwsPtpModemModemprefecsignalfailalarmEntry_Object = MibTableRow
cwsPtpModemModemprefecsignalfailalarmEntry = _CwsPtpModemModemprefecsignalfailalarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 14, 1)
)
cwsPtpModemModemprefecsignalfailalarmEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemprefecsignalfailalarmTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignalfailalarmEntry.setStatus("current")


class _CwsPtpModemModemprefecsignalfailalarmTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemModemprefecsignalfailalarmTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemModemprefecsignalfailalarmTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemModemprefecsignalfailalarmTableSnmpKey_Object = MibTableColumn
cwsPtpModemModemprefecsignalfailalarmTableSnmpKey = _CwsPtpModemModemprefecsignalfailalarmTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 14, 1, 1),
    _CwsPtpModemModemprefecsignalfailalarmTableSnmpKey_Type()
)
cwsPtpModemModemprefecsignalfailalarmTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignalfailalarmTableSnmpKey.setStatus("current")
_CwsPtpModemModemprefecsignalfailalarmActive_Type = TruthValue
_CwsPtpModemModemprefecsignalfailalarmActive_Object = MibTableColumn
cwsPtpModemModemprefecsignalfailalarmActive = _CwsPtpModemModemprefecsignalfailalarmActive_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 14, 1, 2),
    _CwsPtpModemModemprefecsignalfailalarmActive_Type()
)
cwsPtpModemModemprefecsignalfailalarmActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignalfailalarmActive.setStatus("current")
_CwsPtpModemModemprefecsignalfailalarmthresholdTable_Object = MibTable
cwsPtpModemModemprefecsignalfailalarmthresholdTable = _CwsPtpModemModemprefecsignalfailalarmthresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 15)
)
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignalfailalarmthresholdTable.setStatus("current")
_CwsPtpModemModemprefecsignalfailalarmthresholdEntry_Object = MibTableRow
cwsPtpModemModemprefecsignalfailalarmthresholdEntry = _CwsPtpModemModemprefecsignalfailalarmthresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 15, 1)
)
cwsPtpModemModemprefecsignalfailalarmthresholdEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemprefecsignalfailalarmthresholdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignalfailalarmthresholdEntry.setStatus("current")


class _CwsPtpModemModemprefecsignalfailalarmthresholdTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemModemprefecsignalfailalarmthresholdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemModemprefecsignalfailalarmthresholdTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemModemprefecsignalfailalarmthresholdTableSnmpKey_Object = MibTableColumn
cwsPtpModemModemprefecsignalfailalarmthresholdTableSnmpKey = _CwsPtpModemModemprefecsignalfailalarmthresholdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 15, 1, 1),
    _CwsPtpModemModemprefecsignalfailalarmthresholdTableSnmpKey_Type()
)
cwsPtpModemModemprefecsignalfailalarmthresholdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignalfailalarmthresholdTableSnmpKey.setStatus("current")
_CwsPtpModemModemprefecsignalfailalarmthresholdDbq_Type = Decimal2Dig
_CwsPtpModemModemprefecsignalfailalarmthresholdDbq_Object = MibTableColumn
cwsPtpModemModemprefecsignalfailalarmthresholdDbq = _CwsPtpModemModemprefecsignalfailalarmthresholdDbq_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 15, 1, 2),
    _CwsPtpModemModemprefecsignalfailalarmthresholdDbq_Type()
)
cwsPtpModemModemprefecsignalfailalarmthresholdDbq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignalfailalarmthresholdDbq.setStatus("current")
_CwsPtpModemModemprefecsignaldegradealarmTable_Object = MibTable
cwsPtpModemModemprefecsignaldegradealarmTable = _CwsPtpModemModemprefecsignaldegradealarmTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 16)
)
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignaldegradealarmTable.setStatus("current")
_CwsPtpModemModemprefecsignaldegradealarmEntry_Object = MibTableRow
cwsPtpModemModemprefecsignaldegradealarmEntry = _CwsPtpModemModemprefecsignaldegradealarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 16, 1)
)
cwsPtpModemModemprefecsignaldegradealarmEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemprefecsignaldegradealarmTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignaldegradealarmEntry.setStatus("current")


class _CwsPtpModemModemprefecsignaldegradealarmTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemModemprefecsignaldegradealarmTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemModemprefecsignaldegradealarmTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemModemprefecsignaldegradealarmTableSnmpKey_Object = MibTableColumn
cwsPtpModemModemprefecsignaldegradealarmTableSnmpKey = _CwsPtpModemModemprefecsignaldegradealarmTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 16, 1, 1),
    _CwsPtpModemModemprefecsignaldegradealarmTableSnmpKey_Type()
)
cwsPtpModemModemprefecsignaldegradealarmTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignaldegradealarmTableSnmpKey.setStatus("current")
_CwsPtpModemModemprefecsignaldegradealarmActive_Type = TruthValue
_CwsPtpModemModemprefecsignaldegradealarmActive_Object = MibTableColumn
cwsPtpModemModemprefecsignaldegradealarmActive = _CwsPtpModemModemprefecsignaldegradealarmActive_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 16, 1, 2),
    _CwsPtpModemModemprefecsignaldegradealarmActive_Type()
)
cwsPtpModemModemprefecsignaldegradealarmActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignaldegradealarmActive.setStatus("current")
_CwsPtpModemModemprefecsignaldegradealarmthresholdTable_Object = MibTable
cwsPtpModemModemprefecsignaldegradealarmthresholdTable = _CwsPtpModemModemprefecsignaldegradealarmthresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 17)
)
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignaldegradealarmthresholdTable.setStatus("current")
_CwsPtpModemModemprefecsignaldegradealarmthresholdEntry_Object = MibTableRow
cwsPtpModemModemprefecsignaldegradealarmthresholdEntry = _CwsPtpModemModemprefecsignaldegradealarmthresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 17, 1)
)
cwsPtpModemModemprefecsignaldegradealarmthresholdEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemprefecsignaldegradealarmthresholdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignaldegradealarmthresholdEntry.setStatus("current")


class _CwsPtpModemModemprefecsignaldegradealarmthresholdTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemModemprefecsignaldegradealarmthresholdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemModemprefecsignaldegradealarmthresholdTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemModemprefecsignaldegradealarmthresholdTableSnmpKey_Object = MibTableColumn
cwsPtpModemModemprefecsignaldegradealarmthresholdTableSnmpKey = _CwsPtpModemModemprefecsignaldegradealarmthresholdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 17, 1, 1),
    _CwsPtpModemModemprefecsignaldegradealarmthresholdTableSnmpKey_Type()
)
cwsPtpModemModemprefecsignaldegradealarmthresholdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignaldegradealarmthresholdTableSnmpKey.setStatus("current")
_CwsPtpModemModemprefecsignaldegradealarmthresholdDbq_Type = Decimal2Dig
_CwsPtpModemModemprefecsignaldegradealarmthresholdDbq_Object = MibTableColumn
cwsPtpModemModemprefecsignaldegradealarmthresholdDbq = _CwsPtpModemModemprefecsignaldegradealarmthresholdDbq_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 17, 1, 2),
    _CwsPtpModemModemprefecsignaldegradealarmthresholdDbq_Type()
)
cwsPtpModemModemprefecsignaldegradealarmthresholdDbq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignaldegradealarmthresholdDbq.setStatus("current")
_CwsPtpModemPreFecSignalFailTable_Object = MibTable
cwsPtpModemPreFecSignalFailTable = _CwsPtpModemPreFecSignalFailTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 18)
)
if mibBuilder.loadTexts:
    cwsPtpModemPreFecSignalFailTable.setStatus("obsolete")
_CwsPtpModemPreFecSignalFailEntry_Object = MibTableRow
cwsPtpModemPreFecSignalFailEntry = _CwsPtpModemPreFecSignalFailEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 18, 1)
)
cwsPtpModemPreFecSignalFailEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemPreFecSignalFailTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemPreFecSignalFailEntry.setStatus("obsolete")


class _CwsPtpModemPreFecSignalFailTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemPreFecSignalFailTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemPreFecSignalFailTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemPreFecSignalFailTableSnmpKey_Object = MibTableColumn
cwsPtpModemPreFecSignalFailTableSnmpKey = _CwsPtpModemPreFecSignalFailTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 18, 1, 1),
    _CwsPtpModemPreFecSignalFailTableSnmpKey_Type()
)
cwsPtpModemPreFecSignalFailTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemPreFecSignalFailTableSnmpKey.setStatus("current")
_CwsPtpModemPreFecSignalFailFailStatus_Type = TruthValue
_CwsPtpModemPreFecSignalFailFailStatus_Object = MibTableColumn
cwsPtpModemPreFecSignalFailFailStatus = _CwsPtpModemPreFecSignalFailFailStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 18, 1, 2),
    _CwsPtpModemPreFecSignalFailFailStatus_Type()
)
cwsPtpModemPreFecSignalFailFailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemPreFecSignalFailFailStatus.setStatus("obsolete")
_CwsPtpModemModemprefecsignalfailthresholdTable_Object = MibTable
cwsPtpModemModemprefecsignalfailthresholdTable = _CwsPtpModemModemprefecsignalfailthresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 19)
)
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignalfailthresholdTable.setStatus("obsolete")
_CwsPtpModemModemprefecsignalfailthresholdEntry_Object = MibTableRow
cwsPtpModemModemprefecsignalfailthresholdEntry = _CwsPtpModemModemprefecsignalfailthresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 19, 1)
)
cwsPtpModemModemprefecsignalfailthresholdEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemprefecsignalfailthresholdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignalfailthresholdEntry.setStatus("obsolete")


class _CwsPtpModemModemprefecsignalfailthresholdTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemModemprefecsignalfailthresholdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemModemprefecsignalfailthresholdTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemModemprefecsignalfailthresholdTableSnmpKey_Object = MibTableColumn
cwsPtpModemModemprefecsignalfailthresholdTableSnmpKey = _CwsPtpModemModemprefecsignalfailthresholdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 19, 1, 1),
    _CwsPtpModemModemprefecsignalfailthresholdTableSnmpKey_Type()
)
cwsPtpModemModemprefecsignalfailthresholdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignalfailthresholdTableSnmpKey.setStatus("current")
_CwsPtpModemModemprefecsignalfailthresholdDbq_Type = Decimal2Dig
_CwsPtpModemModemprefecsignalfailthresholdDbq_Object = MibTableColumn
cwsPtpModemModemprefecsignalfailthresholdDbq = _CwsPtpModemModemprefecsignalfailthresholdDbq_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 19, 1, 2),
    _CwsPtpModemModemprefecsignalfailthresholdDbq_Type()
)
cwsPtpModemModemprefecsignalfailthresholdDbq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignalfailthresholdDbq.setStatus("obsolete")
_CwsPtpModemModemprefecsignalfailthresholdBer_Type = StringSci
_CwsPtpModemModemprefecsignalfailthresholdBer_Object = MibTableColumn
cwsPtpModemModemprefecsignalfailthresholdBer = _CwsPtpModemModemprefecsignalfailthresholdBer_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 19, 1, 3),
    _CwsPtpModemModemprefecsignalfailthresholdBer_Type()
)
cwsPtpModemModemprefecsignalfailthresholdBer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignalfailthresholdBer.setStatus("obsolete")
_CwsPtpModemPreFecSignalDegradeTable_Object = MibTable
cwsPtpModemPreFecSignalDegradeTable = _CwsPtpModemPreFecSignalDegradeTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 20)
)
if mibBuilder.loadTexts:
    cwsPtpModemPreFecSignalDegradeTable.setStatus("obsolete")
_CwsPtpModemPreFecSignalDegradeEntry_Object = MibTableRow
cwsPtpModemPreFecSignalDegradeEntry = _CwsPtpModemPreFecSignalDegradeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 20, 1)
)
cwsPtpModemPreFecSignalDegradeEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemPreFecSignalDegradeTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemPreFecSignalDegradeEntry.setStatus("obsolete")


class _CwsPtpModemPreFecSignalDegradeTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemPreFecSignalDegradeTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemPreFecSignalDegradeTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemPreFecSignalDegradeTableSnmpKey_Object = MibTableColumn
cwsPtpModemPreFecSignalDegradeTableSnmpKey = _CwsPtpModemPreFecSignalDegradeTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 20, 1, 1),
    _CwsPtpModemPreFecSignalDegradeTableSnmpKey_Type()
)
cwsPtpModemPreFecSignalDegradeTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemPreFecSignalDegradeTableSnmpKey.setStatus("current")
_CwsPtpModemPreFecSignalDegradeDegradeStatus_Type = TruthValue
_CwsPtpModemPreFecSignalDegradeDegradeStatus_Object = MibTableColumn
cwsPtpModemPreFecSignalDegradeDegradeStatus = _CwsPtpModemPreFecSignalDegradeDegradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 20, 1, 2),
    _CwsPtpModemPreFecSignalDegradeDegradeStatus_Type()
)
cwsPtpModemPreFecSignalDegradeDegradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemPreFecSignalDegradeDegradeStatus.setStatus("obsolete")
_CwsPtpModemModemprefecsignaldegradethresholdTable_Object = MibTable
cwsPtpModemModemprefecsignaldegradethresholdTable = _CwsPtpModemModemprefecsignaldegradethresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 21)
)
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignaldegradethresholdTable.setStatus("obsolete")
_CwsPtpModemModemprefecsignaldegradethresholdEntry_Object = MibTableRow
cwsPtpModemModemprefecsignaldegradethresholdEntry = _CwsPtpModemModemprefecsignaldegradethresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 21, 1)
)
cwsPtpModemModemprefecsignaldegradethresholdEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemprefecsignaldegradethresholdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignaldegradethresholdEntry.setStatus("obsolete")


class _CwsPtpModemModemprefecsignaldegradethresholdTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemModemprefecsignaldegradethresholdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemModemprefecsignaldegradethresholdTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemModemprefecsignaldegradethresholdTableSnmpKey_Object = MibTableColumn
cwsPtpModemModemprefecsignaldegradethresholdTableSnmpKey = _CwsPtpModemModemprefecsignaldegradethresholdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 21, 1, 1),
    _CwsPtpModemModemprefecsignaldegradethresholdTableSnmpKey_Type()
)
cwsPtpModemModemprefecsignaldegradethresholdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignaldegradethresholdTableSnmpKey.setStatus("current")
_CwsPtpModemModemprefecsignaldegradethresholdDbq_Type = Decimal2Dig
_CwsPtpModemModemprefecsignaldegradethresholdDbq_Object = MibTableColumn
cwsPtpModemModemprefecsignaldegradethresholdDbq = _CwsPtpModemModemprefecsignaldegradethresholdDbq_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 21, 1, 2),
    _CwsPtpModemModemprefecsignaldegradethresholdDbq_Type()
)
cwsPtpModemModemprefecsignaldegradethresholdDbq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignaldegradethresholdDbq.setStatus("obsolete")
_CwsPtpModemModemprefecsignaldegradethresholdBer_Type = StringSci
_CwsPtpModemModemprefecsignaldegradethresholdBer_Object = MibTableColumn
cwsPtpModemModemprefecsignaldegradethresholdBer = _CwsPtpModemModemprefecsignaldegradethresholdBer_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 21, 1, 3),
    _CwsPtpModemModemprefecsignaldegradethresholdBer_Type()
)
cwsPtpModemModemprefecsignaldegradethresholdBer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemModemprefecsignaldegradethresholdBer.setStatus("obsolete")
_CwsPtpModemRxlinkdispersionTable_Object = MibTable
cwsPtpModemRxlinkdispersionTable = _CwsPtpModemRxlinkdispersionTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 22)
)
if mibBuilder.loadTexts:
    cwsPtpModemRxlinkdispersionTable.setStatus("current")
_CwsPtpModemRxlinkdispersionEntry_Object = MibTableRow
cwsPtpModemRxlinkdispersionEntry = _CwsPtpModemRxlinkdispersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 22, 1)
)
cwsPtpModemRxlinkdispersionEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemRxlinkdispersionTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemRxlinkdispersionEntry.setStatus("current")


class _CwsPtpModemRxlinkdispersionTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemRxlinkdispersionTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemRxlinkdispersionTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemRxlinkdispersionTableSnmpKey_Object = MibTableColumn
cwsPtpModemRxlinkdispersionTableSnmpKey = _CwsPtpModemRxlinkdispersionTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 22, 1, 1),
    _CwsPtpModemRxlinkdispersionTableSnmpKey_Type()
)
cwsPtpModemRxlinkdispersionTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemRxlinkdispersionTableSnmpKey.setStatus("current")
_CwsPtpModemRxlinkdispersionTotal_Type = Integer32
_CwsPtpModemRxlinkdispersionTotal_Object = MibTableColumn
cwsPtpModemRxlinkdispersionTotal = _CwsPtpModemRxlinkdispersionTotal_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 22, 1, 2),
    _CwsPtpModemRxlinkdispersionTotal_Type()
)
cwsPtpModemRxlinkdispersionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemRxlinkdispersionTotal.setStatus("current")
_CwsPtpModemRxlinkdispersionCompensation_Type = Integer32
_CwsPtpModemRxlinkdispersionCompensation_Object = MibTableColumn
cwsPtpModemRxlinkdispersionCompensation = _CwsPtpModemRxlinkdispersionCompensation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 22, 1, 3),
    _CwsPtpModemRxlinkdispersionCompensation_Type()
)
cwsPtpModemRxlinkdispersionCompensation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemRxlinkdispersionCompensation.setStatus("current")
_CwsPtpModemTxlinkdispersionTable_Object = MibTable
cwsPtpModemTxlinkdispersionTable = _CwsPtpModemTxlinkdispersionTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 23)
)
if mibBuilder.loadTexts:
    cwsPtpModemTxlinkdispersionTable.setStatus("current")
_CwsPtpModemTxlinkdispersionEntry_Object = MibTableRow
cwsPtpModemTxlinkdispersionEntry = _CwsPtpModemTxlinkdispersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 23, 1)
)
cwsPtpModemTxlinkdispersionEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemTxlinkdispersionTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemTxlinkdispersionEntry.setStatus("current")


class _CwsPtpModemTxlinkdispersionTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemTxlinkdispersionTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemTxlinkdispersionTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemTxlinkdispersionTableSnmpKey_Object = MibTableColumn
cwsPtpModemTxlinkdispersionTableSnmpKey = _CwsPtpModemTxlinkdispersionTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 23, 1, 1),
    _CwsPtpModemTxlinkdispersionTableSnmpKey_Type()
)
cwsPtpModemTxlinkdispersionTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemTxlinkdispersionTableSnmpKey.setStatus("current")
_CwsPtpModemTxlinkdispersionTotal_Type = Integer32
_CwsPtpModemTxlinkdispersionTotal_Object = MibTableColumn
cwsPtpModemTxlinkdispersionTotal = _CwsPtpModemTxlinkdispersionTotal_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 23, 1, 2),
    _CwsPtpModemTxlinkdispersionTotal_Type()
)
cwsPtpModemTxlinkdispersionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemTxlinkdispersionTotal.setStatus("current")
_CwsPtpModemTxlinkdispersionActual_Type = Integer32
_CwsPtpModemTxlinkdispersionActual_Object = MibTableColumn
cwsPtpModemTxlinkdispersionActual = _CwsPtpModemTxlinkdispersionActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 23, 1, 3),
    _CwsPtpModemTxlinkdispersionActual_Type()
)
cwsPtpModemTxlinkdispersionActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemTxlinkdispersionActual.setStatus("current")
_CwsPtpModemDifferentialGroupDelayTable_Object = MibTable
cwsPtpModemDifferentialGroupDelayTable = _CwsPtpModemDifferentialGroupDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 24)
)
if mibBuilder.loadTexts:
    cwsPtpModemDifferentialGroupDelayTable.setStatus("current")
_CwsPtpModemDifferentialGroupDelayEntry_Object = MibTableRow
cwsPtpModemDifferentialGroupDelayEntry = _CwsPtpModemDifferentialGroupDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 24, 1)
)
cwsPtpModemDifferentialGroupDelayEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemDifferentialGroupDelayTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemDifferentialGroupDelayEntry.setStatus("current")


class _CwsPtpModemDifferentialGroupDelayTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemDifferentialGroupDelayTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemDifferentialGroupDelayTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemDifferentialGroupDelayTableSnmpKey_Object = MibTableColumn
cwsPtpModemDifferentialGroupDelayTableSnmpKey = _CwsPtpModemDifferentialGroupDelayTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 24, 1, 1),
    _CwsPtpModemDifferentialGroupDelayTableSnmpKey_Type()
)
cwsPtpModemDifferentialGroupDelayTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemDifferentialGroupDelayTableSnmpKey.setStatus("current")
_CwsPtpModemDifferentialGroupDelayMeanSupported_Type = Integer32
_CwsPtpModemDifferentialGroupDelayMeanSupported_Object = MibTableColumn
cwsPtpModemDifferentialGroupDelayMeanSupported = _CwsPtpModemDifferentialGroupDelayMeanSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 24, 1, 2),
    _CwsPtpModemDifferentialGroupDelayMeanSupported_Type()
)
cwsPtpModemDifferentialGroupDelayMeanSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemDifferentialGroupDelayMeanSupported.setStatus("current")
_CwsPtpModemDifferentialGroupDelayEstimatedInstance_Type = Integer32
_CwsPtpModemDifferentialGroupDelayEstimatedInstance_Object = MibTableColumn
cwsPtpModemDifferentialGroupDelayEstimatedInstance = _CwsPtpModemDifferentialGroupDelayEstimatedInstance_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 24, 1, 3),
    _CwsPtpModemDifferentialGroupDelayEstimatedInstance_Type()
)
cwsPtpModemDifferentialGroupDelayEstimatedInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemDifferentialGroupDelayEstimatedInstance.setStatus("current")
_CwsPtpModemFastRxRecoveryTable_Object = MibTable
cwsPtpModemFastRxRecoveryTable = _CwsPtpModemFastRxRecoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 25)
)
if mibBuilder.loadTexts:
    cwsPtpModemFastRxRecoveryTable.setStatus("current")
_CwsPtpModemFastRxRecoveryEntry_Object = MibTableRow
cwsPtpModemFastRxRecoveryEntry = _CwsPtpModemFastRxRecoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 25, 1)
)
cwsPtpModemFastRxRecoveryEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemFastRxRecoveryTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemFastRxRecoveryEntry.setStatus("current")


class _CwsPtpModemFastRxRecoveryTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemFastRxRecoveryTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemFastRxRecoveryTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemFastRxRecoveryTableSnmpKey_Object = MibTableColumn
cwsPtpModemFastRxRecoveryTableSnmpKey = _CwsPtpModemFastRxRecoveryTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 25, 1, 1),
    _CwsPtpModemFastRxRecoveryTableSnmpKey_Type()
)
cwsPtpModemFastRxRecoveryTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemFastRxRecoveryTableSnmpKey.setStatus("current")
_CwsPtpModemFastRxRecoveryState_Type = EnabledDisabledEnum
_CwsPtpModemFastRxRecoveryState_Object = MibTableColumn
cwsPtpModemFastRxRecoveryState = _CwsPtpModemFastRxRecoveryState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 25, 1, 2),
    _CwsPtpModemFastRxRecoveryState_Type()
)
cwsPtpModemFastRxRecoveryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemFastRxRecoveryState.setStatus("current")


class _CwsPtpModemFastRxRecoveryNetworkConfiguration_Type(Integer32):
    """Custom type cwsPtpModemFastRxRecoveryNetworkConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("matched", 0),
          ("diverse", 1))
    )


_CwsPtpModemFastRxRecoveryNetworkConfiguration_Type.__name__ = "Integer32"
_CwsPtpModemFastRxRecoveryNetworkConfiguration_Object = MibTableColumn
cwsPtpModemFastRxRecoveryNetworkConfiguration = _CwsPtpModemFastRxRecoveryNetworkConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 25, 1, 3),
    _CwsPtpModemFastRxRecoveryNetworkConfiguration_Type()
)
cwsPtpModemFastRxRecoveryNetworkConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemFastRxRecoveryNetworkConfiguration.setStatus("current")
_CwsPtpModemFastRxRecoveryPath1Dispersion_Type = RecoverLinkDispersionType
_CwsPtpModemFastRxRecoveryPath1Dispersion_Object = MibTableColumn
cwsPtpModemFastRxRecoveryPath1Dispersion = _CwsPtpModemFastRxRecoveryPath1Dispersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 25, 1, 4),
    _CwsPtpModemFastRxRecoveryPath1Dispersion_Type()
)
cwsPtpModemFastRxRecoveryPath1Dispersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemFastRxRecoveryPath1Dispersion.setStatus("current")
_CwsPtpModemFastRxRecoveryPath2Dispersion_Type = RecoverLinkDispersionType
_CwsPtpModemFastRxRecoveryPath2Dispersion_Object = MibTableColumn
cwsPtpModemFastRxRecoveryPath2Dispersion = _CwsPtpModemFastRxRecoveryPath2Dispersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 25, 1, 5),
    _CwsPtpModemFastRxRecoveryPath2Dispersion_Type()
)
cwsPtpModemFastRxRecoveryPath2Dispersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPtpModemFastRxRecoveryPath2Dispersion.setStatus("current")
_CwsPtpModemColourlessRxChannelPowerTable_Object = MibTable
cwsPtpModemColourlessRxChannelPowerTable = _CwsPtpModemColourlessRxChannelPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 26)
)
if mibBuilder.loadTexts:
    cwsPtpModemColourlessRxChannelPowerTable.setStatus("current")
_CwsPtpModemColourlessRxChannelPowerEntry_Object = MibTableRow
cwsPtpModemColourlessRxChannelPowerEntry = _CwsPtpModemColourlessRxChannelPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 26, 1)
)
cwsPtpModemColourlessRxChannelPowerEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpChannelChannelNumber"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemColourlessRxChannelPowerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemColourlessRxChannelPowerEntry.setStatus("current")


class _CwsPtpModemColourlessRxChannelPowerTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemColourlessRxChannelPowerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemColourlessRxChannelPowerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemColourlessRxChannelPowerTableSnmpKey_Object = MibTableColumn
cwsPtpModemColourlessRxChannelPowerTableSnmpKey = _CwsPtpModemColourlessRxChannelPowerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 26, 1, 1),
    _CwsPtpModemColourlessRxChannelPowerTableSnmpKey_Type()
)
cwsPtpModemColourlessRxChannelPowerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemColourlessRxChannelPowerTableSnmpKey.setStatus("current")
_CwsXcvrColourlessRxChannelPowerActual_Type = Decimal1Dig
_CwsXcvrColourlessRxChannelPowerActual_Object = MibTableColumn
cwsXcvrColourlessRxChannelPowerActual = _CwsXcvrColourlessRxChannelPowerActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 26, 1, 2),
    _CwsXcvrColourlessRxChannelPowerActual_Type()
)
cwsXcvrColourlessRxChannelPowerActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrColourlessRxChannelPowerActual.setStatus("current")
_CwsXcvrColourlessRxChannelPowerMaximum_Type = Decimal1Dig
_CwsXcvrColourlessRxChannelPowerMaximum_Object = MibTableColumn
cwsXcvrColourlessRxChannelPowerMaximum = _CwsXcvrColourlessRxChannelPowerMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 26, 1, 3),
    _CwsXcvrColourlessRxChannelPowerMaximum_Type()
)
cwsXcvrColourlessRxChannelPowerMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrColourlessRxChannelPowerMaximum.setStatus("current")
_CwsXcvrColourlessRxChannelPowerMinimum_Type = Decimal1Dig
_CwsXcvrColourlessRxChannelPowerMinimum_Object = MibTableColumn
cwsXcvrColourlessRxChannelPowerMinimum = _CwsXcvrColourlessRxChannelPowerMinimum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 26, 1, 4),
    _CwsXcvrColourlessRxChannelPowerMinimum_Type()
)
cwsXcvrColourlessRxChannelPowerMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrColourlessRxChannelPowerMinimum.setStatus("current")
_CwsXcvrColourlessRxChannelPowerMaximumRecordedTime_Type = StringMaxl32
_CwsXcvrColourlessRxChannelPowerMaximumRecordedTime_Object = MibTableColumn
cwsXcvrColourlessRxChannelPowerMaximumRecordedTime = _CwsXcvrColourlessRxChannelPowerMaximumRecordedTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 26, 1, 5),
    _CwsXcvrColourlessRxChannelPowerMaximumRecordedTime_Type()
)
cwsXcvrColourlessRxChannelPowerMaximumRecordedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrColourlessRxChannelPowerMaximumRecordedTime.setStatus("current")
_CwsXcvrColourlessRxChannelPowerMinimumRecordedTime_Type = StringMaxl32
_CwsXcvrColourlessRxChannelPowerMinimumRecordedTime_Object = MibTableColumn
cwsXcvrColourlessRxChannelPowerMinimumRecordedTime = _CwsXcvrColourlessRxChannelPowerMinimumRecordedTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 26, 1, 6),
    _CwsXcvrColourlessRxChannelPowerMinimumRecordedTime_Type()
)
cwsXcvrColourlessRxChannelPowerMinimumRecordedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrColourlessRxChannelPowerMinimumRecordedTime.setStatus("current")
_CwsPtpModemColourlessRxChannelStatusTable_Object = MibTable
cwsPtpModemColourlessRxChannelStatusTable = _CwsPtpModemColourlessRxChannelStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 27)
)
if mibBuilder.loadTexts:
    cwsPtpModemColourlessRxChannelStatusTable.setStatus("current")
_CwsPtpModemColourlessRxChannelStatusEntry_Object = MibTableRow
cwsPtpModemColourlessRxChannelStatusEntry = _CwsPtpModemColourlessRxChannelStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 27, 1)
)
cwsPtpModemColourlessRxChannelStatusEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpChannelChannelNumber"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemColourlessRxChannelStatusTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemColourlessRxChannelStatusEntry.setStatus("current")


class _CwsPtpModemColourlessRxChannelStatusTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemColourlessRxChannelStatusTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemColourlessRxChannelStatusTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemColourlessRxChannelStatusTableSnmpKey_Object = MibTableColumn
cwsPtpModemColourlessRxChannelStatusTableSnmpKey = _CwsPtpModemColourlessRxChannelStatusTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 27, 1, 1),
    _CwsPtpModemColourlessRxChannelStatusTableSnmpKey_Type()
)
cwsPtpModemColourlessRxChannelStatusTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemColourlessRxChannelStatusTableSnmpKey.setStatus("current")
_CwsPtpModemColourlessRxChannelStatusLossOfSignal_Type = TruthValue
_CwsPtpModemColourlessRxChannelStatusLossOfSignal_Object = MibTableColumn
cwsPtpModemColourlessRxChannelStatusLossOfSignal = _CwsPtpModemColourlessRxChannelStatusLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 27, 1, 2),
    _CwsPtpModemColourlessRxChannelStatusLossOfSignal_Type()
)
cwsPtpModemColourlessRxChannelStatusLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemColourlessRxChannelStatusLossOfSignal.setStatus("current")
_CwsPtpModemColourlessRxChannelStatusHighAlarmStatus_Type = TruthValue
_CwsPtpModemColourlessRxChannelStatusHighAlarmStatus_Object = MibTableColumn
cwsPtpModemColourlessRxChannelStatusHighAlarmStatus = _CwsPtpModemColourlessRxChannelStatusHighAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 27, 1, 3),
    _CwsPtpModemColourlessRxChannelStatusHighAlarmStatus_Type()
)
cwsPtpModemColourlessRxChannelStatusHighAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemColourlessRxChannelStatusHighAlarmStatus.setStatus("current")
_CwsPtpModemColourlessRxChannelStatusLowAlarmStatus_Type = TruthValue
_CwsPtpModemColourlessRxChannelStatusLowAlarmStatus_Object = MibTableColumn
cwsPtpModemColourlessRxChannelStatusLowAlarmStatus = _CwsPtpModemColourlessRxChannelStatusLowAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 27, 1, 4),
    _CwsPtpModemColourlessRxChannelStatusLowAlarmStatus_Type()
)
cwsPtpModemColourlessRxChannelStatusLowAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemColourlessRxChannelStatusLowAlarmStatus.setStatus("current")
_CwsPtpModemColourlessTxChannelPowerTable_Object = MibTable
cwsPtpModemColourlessTxChannelPowerTable = _CwsPtpModemColourlessTxChannelPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 28)
)
if mibBuilder.loadTexts:
    cwsPtpModemColourlessTxChannelPowerTable.setStatus("current")
_CwsPtpModemColourlessTxChannelPowerEntry_Object = MibTableRow
cwsPtpModemColourlessTxChannelPowerEntry = _CwsPtpModemColourlessTxChannelPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 28, 1)
)
cwsPtpModemColourlessTxChannelPowerEntry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpChannelChannelNumber"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemColourlessTxChannelPowerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemColourlessTxChannelPowerEntry.setStatus("current")


class _CwsPtpModemColourlessTxChannelPowerTableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemColourlessTxChannelPowerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemColourlessTxChannelPowerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemColourlessTxChannelPowerTableSnmpKey_Object = MibTableColumn
cwsPtpModemColourlessTxChannelPowerTableSnmpKey = _CwsPtpModemColourlessTxChannelPowerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 28, 1, 1),
    _CwsPtpModemColourlessTxChannelPowerTableSnmpKey_Type()
)
cwsPtpModemColourlessTxChannelPowerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemColourlessTxChannelPowerTableSnmpKey.setStatus("current")
_CwsXcvrColourlessTxChannelPowerActual_Type = Decimal1Dig
_CwsXcvrColourlessTxChannelPowerActual_Object = MibTableColumn
cwsXcvrColourlessTxChannelPowerActual = _CwsXcvrColourlessTxChannelPowerActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 28, 1, 2),
    _CwsXcvrColourlessTxChannelPowerActual_Type()
)
cwsXcvrColourlessTxChannelPowerActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrColourlessTxChannelPowerActual.setStatus("current")
_CwsXcvrColourlessTxChannelPowerMaximum_Type = Decimal1Dig
_CwsXcvrColourlessTxChannelPowerMaximum_Object = MibTableColumn
cwsXcvrColourlessTxChannelPowerMaximum = _CwsXcvrColourlessTxChannelPowerMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 28, 1, 3),
    _CwsXcvrColourlessTxChannelPowerMaximum_Type()
)
cwsXcvrColourlessTxChannelPowerMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrColourlessTxChannelPowerMaximum.setStatus("current")
_CwsXcvrColourlessTxChannelPowerMinimum_Type = Decimal1Dig
_CwsXcvrColourlessTxChannelPowerMinimum_Object = MibTableColumn
cwsXcvrColourlessTxChannelPowerMinimum = _CwsXcvrColourlessTxChannelPowerMinimum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 28, 1, 4),
    _CwsXcvrColourlessTxChannelPowerMinimum_Type()
)
cwsXcvrColourlessTxChannelPowerMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrColourlessTxChannelPowerMinimum.setStatus("current")
_CwsXcvrColourlessTxChannelPowerMaximumRecordedTime_Type = StringMaxl32
_CwsXcvrColourlessTxChannelPowerMaximumRecordedTime_Object = MibTableColumn
cwsXcvrColourlessTxChannelPowerMaximumRecordedTime = _CwsXcvrColourlessTxChannelPowerMaximumRecordedTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 28, 1, 5),
    _CwsXcvrColourlessTxChannelPowerMaximumRecordedTime_Type()
)
cwsXcvrColourlessTxChannelPowerMaximumRecordedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrColourlessTxChannelPowerMaximumRecordedTime.setStatus("current")
_CwsXcvrColourlessTxChannelPowerMinimumRecordedTime_Type = StringMaxl32
_CwsXcvrColourlessTxChannelPowerMinimumRecordedTime_Object = MibTableColumn
cwsXcvrColourlessTxChannelPowerMinimumRecordedTime = _CwsXcvrColourlessTxChannelPowerMinimumRecordedTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 28, 1, 6),
    _CwsXcvrColourlessTxChannelPowerMinimumRecordedTime_Type()
)
cwsXcvrColourlessTxChannelPowerMinimumRecordedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrColourlessTxChannelPowerMinimumRecordedTime.setStatus("current")
_CwsPtpAugPtpModemDiagnosticsTable_Object = MibTable
cwsPtpAugPtpModemDiagnosticsTable = _CwsPtpAugPtpModemDiagnosticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 29)
)
if mibBuilder.loadTexts:
    cwsPtpAugPtpModemDiagnosticsTable.setStatus("current")
_CwsPtpAugPtpModemDiagnosticsEntry_Object = MibTableRow
cwsPtpAugPtpModemDiagnosticsEntry = _CwsPtpAugPtpModemDiagnosticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 29, 1)
)
if mibBuilder.loadTexts:
    cwsPtpAugPtpModemDiagnosticsEntry.setStatus("current")
_CwsPtpModemDiagnosticsNumberOfOdu_Type = Unsigned32
_CwsPtpModemDiagnosticsNumberOfOdu_Object = MibTableColumn
cwsPtpModemDiagnosticsNumberOfOdu = _CwsPtpModemDiagnosticsNumberOfOdu_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 29, 1, 1),
    _CwsPtpModemDiagnosticsNumberOfOdu_Type()
)
cwsPtpModemDiagnosticsNumberOfOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemDiagnosticsNumberOfOdu.setStatus("current")
_CwsPtpModemOtu4Table_Object = MibTable
cwsPtpModemOtu4Table = _CwsPtpModemOtu4Table_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 30)
)
if mibBuilder.loadTexts:
    cwsPtpModemOtu4Table.setStatus("current")
_CwsPtpModemOtu4Entry_Object = MibTableRow
cwsPtpModemOtu4Entry = _CwsPtpModemOtu4Entry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 30, 1)
)
cwsPtpModemOtu4Entry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemOtu4TableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPtpModemOtu4Entry.setStatus("current")


class _CwsPtpModemOtu4TableSnmpKey_Type(Integer32):
    """Custom type cwsPtpModemOtu4TableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemOtu4TableSnmpKey_Type.__name__ = "Integer32"
_CwsPtpModemOtu4TableSnmpKey_Object = MibTableColumn
cwsPtpModemOtu4TableSnmpKey = _CwsPtpModemOtu4TableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 30, 1, 1),
    _CwsPtpModemOtu4TableSnmpKey_Type()
)
cwsPtpModemOtu4TableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemOtu4TableSnmpKey.setStatus("current")
_CwsPtpModemOtu4LossOfClock_Type = TruthValue
_CwsPtpModemOtu4LossOfClock_Object = MibTableColumn
cwsPtpModemOtu4LossOfClock = _CwsPtpModemOtu4LossOfClock_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 30, 1, 2),
    _CwsPtpModemOtu4LossOfClock_Type()
)
cwsPtpModemOtu4LossOfClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemOtu4LossOfClock.setStatus("current")
_CwsPtpModemOtu4FrequencyOutOfRange_Type = TruthValue
_CwsPtpModemOtu4FrequencyOutOfRange_Object = MibTableColumn
cwsPtpModemOtu4FrequencyOutOfRange = _CwsPtpModemOtu4FrequencyOutOfRange_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 30, 1, 3),
    _CwsPtpModemOtu4FrequencyOutOfRange_Type()
)
cwsPtpModemOtu4FrequencyOutOfRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemOtu4FrequencyOutOfRange.setStatus("current")
_CwsPtpModemOtu4LossOfFrame_Type = TruthValue
_CwsPtpModemOtu4LossOfFrame_Object = MibTableColumn
cwsPtpModemOtu4LossOfFrame = _CwsPtpModemOtu4LossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 30, 1, 4),
    _CwsPtpModemOtu4LossOfFrame_Type()
)
cwsPtpModemOtu4LossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemOtu4LossOfFrame.setStatus("current")
_CwsPtpModemOtu4LossOfMultiFrame_Type = TruthValue
_CwsPtpModemOtu4LossOfMultiFrame_Object = MibTableColumn
cwsPtpModemOtu4LossOfMultiFrame = _CwsPtpModemOtu4LossOfMultiFrame_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 30, 1, 5),
    _CwsPtpModemOtu4LossOfMultiFrame_Type()
)
cwsPtpModemOtu4LossOfMultiFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemOtu4LossOfMultiFrame.setStatus("current")
_CwsPtpModemOtu4BackwardDefectIndication_Type = TruthValue
_CwsPtpModemOtu4BackwardDefectIndication_Object = MibTableColumn
cwsPtpModemOtu4BackwardDefectIndication = _CwsPtpModemOtu4BackwardDefectIndication_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 30, 1, 6),
    _CwsPtpModemOtu4BackwardDefectIndication_Type()
)
cwsPtpModemOtu4BackwardDefectIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemOtu4BackwardDefectIndication.setStatus("current")
_CwsPtpModemOtu4TrailTraceIdMismatch_Type = TruthValue
_CwsPtpModemOtu4TrailTraceIdMismatch_Object = MibTableColumn
cwsPtpModemOtu4TrailTraceIdMismatch = _CwsPtpModemOtu4TrailTraceIdMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 30, 1, 7),
    _CwsPtpModemOtu4TrailTraceIdMismatch_Type()
)
cwsPtpModemOtu4TrailTraceIdMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemOtu4TrailTraceIdMismatch.setStatus("current")
_CwsPtpModemOdu4Table_Object = MibTable
cwsPtpModemOdu4Table = _CwsPtpModemOdu4Table_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 31)
)
if mibBuilder.loadTexts:
    cwsPtpModemOdu4Table.setStatus("current")
_CwsPtpModemOdu4Entry_Object = MibTableRow
cwsPtpModemOdu4Entry = _CwsPtpModemOdu4Entry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 31, 1)
)
cwsPtpModemOdu4Entry.setIndexNames(
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpPtpsPtpIndex"),
    (0, "CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemOdu4OduId"),
)
if mibBuilder.loadTexts:
    cwsPtpModemOdu4Entry.setStatus("current")


class _CwsPtpModemOdu4OduId_Type(Integer32):
    """Custom type cwsPtpModemOdu4OduId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPtpModemOdu4OduId_Type.__name__ = "Integer32"
_CwsPtpModemOdu4OduId_Object = MibTableColumn
cwsPtpModemOdu4OduId = _CwsPtpModemOdu4OduId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 31, 1, 1),
    _CwsPtpModemOdu4OduId_Type()
)
cwsPtpModemOdu4OduId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPtpModemOdu4OduId.setStatus("current")
_CwsPtpModemOdu4OpenConnectionIndication_Type = TruthValue
_CwsPtpModemOdu4OpenConnectionIndication_Object = MibTableColumn
cwsPtpModemOdu4OpenConnectionIndication = _CwsPtpModemOdu4OpenConnectionIndication_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 31, 1, 2),
    _CwsPtpModemOdu4OpenConnectionIndication_Type()
)
cwsPtpModemOdu4OpenConnectionIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemOdu4OpenConnectionIndication.setStatus("current")
_CwsPtpModemOdu4AlarmIndicationSignal_Type = TruthValue
_CwsPtpModemOdu4AlarmIndicationSignal_Object = MibTableColumn
cwsPtpModemOdu4AlarmIndicationSignal = _CwsPtpModemOdu4AlarmIndicationSignal_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 31, 1, 3),
    _CwsPtpModemOdu4AlarmIndicationSignal_Type()
)
cwsPtpModemOdu4AlarmIndicationSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemOdu4AlarmIndicationSignal.setStatus("current")
_CwsPtpModemOdu4Locked_Type = TruthValue
_CwsPtpModemOdu4Locked_Object = MibTableColumn
cwsPtpModemOdu4Locked = _CwsPtpModemOdu4Locked_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 31, 1, 4),
    _CwsPtpModemOdu4Locked_Type()
)
cwsPtpModemOdu4Locked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemOdu4Locked.setStatus("current")
_CwsPtpModemOdu4SignalFail_Type = TruthValue
_CwsPtpModemOdu4SignalFail_Object = MibTableColumn
cwsPtpModemOdu4SignalFail = _CwsPtpModemOdu4SignalFail_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 31, 1, 5),
    _CwsPtpModemOdu4SignalFail_Type()
)
cwsPtpModemOdu4SignalFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemOdu4SignalFail.setStatus("current")
_CwsPtpModemOdu4SignalDegrade_Type = TruthValue
_CwsPtpModemOdu4SignalDegrade_Object = MibTableColumn
cwsPtpModemOdu4SignalDegrade = _CwsPtpModemOdu4SignalDegrade_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 31, 1, 6),
    _CwsPtpModemOdu4SignalDegrade_Type()
)
cwsPtpModemOdu4SignalDegrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemOdu4SignalDegrade.setStatus("current")
_CwsPtpModemOdu4TrailTraceIdMismatch_Type = TruthValue
_CwsPtpModemOdu4TrailTraceIdMismatch_Object = MibTableColumn
cwsPtpModemOdu4TrailTraceIdMismatch = _CwsPtpModemOdu4TrailTraceIdMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 31, 1, 7),
    _CwsPtpModemOdu4TrailTraceIdMismatch_Type()
)
cwsPtpModemOdu4TrailTraceIdMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemOdu4TrailTraceIdMismatch.setStatus("current")
_CwsPtpModemOdu4BackwardDefectIndication_Type = TruthValue
_CwsPtpModemOdu4BackwardDefectIndication_Object = MibTableColumn
cwsPtpModemOdu4BackwardDefectIndication = _CwsPtpModemOdu4BackwardDefectIndication_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 31, 1, 8),
    _CwsPtpModemOdu4BackwardDefectIndication_Type()
)
cwsPtpModemOdu4BackwardDefectIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemOdu4BackwardDefectIndication.setStatus("current")
_CwsPtpModemOdu4PayloadLabelMismatch_Type = TruthValue
_CwsPtpModemOdu4PayloadLabelMismatch_Object = MibTableColumn
cwsPtpModemOdu4PayloadLabelMismatch = _CwsPtpModemOdu4PayloadLabelMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 31, 1, 9),
    _CwsPtpModemOdu4PayloadLabelMismatch_Type()
)
cwsPtpModemOdu4PayloadLabelMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemOdu4PayloadLabelMismatch.setStatus("current")
_CwsPtpModemOdu4ClientSignalFailure_Type = TruthValue
_CwsPtpModemOdu4ClientSignalFailure_Object = MibTableColumn
cwsPtpModemOdu4ClientSignalFailure = _CwsPtpModemOdu4ClientSignalFailure_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 31, 1, 10),
    _CwsPtpModemOdu4ClientSignalFailure_Type()
)
cwsPtpModemOdu4ClientSignalFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpModemOdu4ClientSignalFailure.setStatus("current")
cwsPtpTransmitterEntry.registerAugmentions(
    ("CIENA-WS-PTP-MODEM-MIB",
     "cwsPtpAugPtpModemTransmitterEntry")
)
cwsPtpAugPtpModemTransmitterEntry.setIndexNames(*cwsPtpTransmitterEntry.getIndexNames())
cwsPtpDiagnosticsEntry.registerAugmentions(
    ("CIENA-WS-PTP-MODEM-MIB",
     "cwsPtpAugPtpModemDiagnosticsEntry")
)
cwsPtpAugPtpModemDiagnosticsEntry.setIndexNames(*cwsPtpDiagnosticsEntry.getIndexNames())

# Managed Objects groups

cienaWsPtpModemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 2, 1, 1)
)
cienaWsPtpModemGroup.setObjects(
      *(("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemTransmitterLineSystemChannelNumber"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemFrequencyValue"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemFrequencyMinValue"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemFrequencyMaxValue"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemFrequencyActual"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemPowerValue"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemPowerMinValue"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemPowerMaxValue"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemLineSystemType"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemLineSystemWavelengthSpacing"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemCmdSlot"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemCmdPortIn"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemCmdPortOut"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemChannelContentionDetectionAvoidance"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemPerformanceOptimizationMode"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemCarrierCenteringMode"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemInterleaverMode"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemRotation"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemSpectralOccupancyMode"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemTxPowerReductionState"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemTxReductionMode"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemTxTuningMode"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemDifferentialEncoding"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemTxCompensationDispersionMode"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemTxCompensationDispersionValue"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemFastReceiverRecoveryState"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemLaserCenteringRange"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemPerformanceStatisticsSecondsSinceLastClear"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemPerformanceStatisticsFecUncorrectedBlockCount"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemPerformanceStatisticsHighCorrectionCountSeconds"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemPreFecBerActual"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemPreFecBerMax"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemPreFecBerMin"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemPreFecBerAverage"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemPostFecBerActual"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemPostFecBerMax"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemPostFecBerMin"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemPostFecBerAverage"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemQFactorActual"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemQFactorMax"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemQFactorMin"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemQFactorAverage"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemFecFrameErrorCountValue"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemFecFrameErrorCountSeconds"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemprefecsignalfailalarmActive"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemprefecsignalfailalarmthresholdDbq"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemprefecsignaldegradealarmActive"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemprefecsignaldegradealarmthresholdDbq"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemPreFecSignalFailFailStatus"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemprefecsignalfailthresholdDbq"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemprefecsignalfailthresholdBer"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemPreFecSignalDegradeDegradeStatus"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemprefecsignaldegradethresholdDbq"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemModemprefecsignaldegradethresholdBer"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemRxlinkdispersionTotal"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemRxlinkdispersionCompensation"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemTxlinkdispersionTotal"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemTxlinkdispersionActual"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemDifferentialGroupDelayMeanSupported"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemDifferentialGroupDelayEstimatedInstance"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemFastRxRecoveryState"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemFastRxRecoveryNetworkConfiguration"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemFastRxRecoveryPath1Dispersion"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemFastRxRecoveryPath2Dispersion"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsXcvrColourlessRxChannelPowerActual"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsXcvrColourlessRxChannelPowerMaximum"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsXcvrColourlessRxChannelPowerMinimum"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsXcvrColourlessRxChannelPowerMaximumRecordedTime"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsXcvrColourlessRxChannelPowerMinimumRecordedTime"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemColourlessRxChannelStatusLossOfSignal"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemColourlessRxChannelStatusHighAlarmStatus"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemColourlessRxChannelStatusLowAlarmStatus"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsXcvrColourlessTxChannelPowerActual"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsXcvrColourlessTxChannelPowerMaximum"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsXcvrColourlessTxChannelPowerMinimum"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsXcvrColourlessTxChannelPowerMaximumRecordedTime"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsXcvrColourlessTxChannelPowerMinimumRecordedTime"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemDiagnosticsNumberOfOdu"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemOtu4LossOfClock"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemOtu4FrequencyOutOfRange"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemOtu4LossOfFrame"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemOtu4LossOfMultiFrame"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemOtu4BackwardDefectIndication"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemOtu4TrailTraceIdMismatch"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemOdu4OpenConnectionIndication"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemOdu4AlarmIndicationSignal"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemOdu4Locked"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemOdu4SignalFail"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemOdu4SignalDegrade"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemOdu4TrailTraceIdMismatch"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemOdu4BackwardDefectIndication"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemOdu4PayloadLabelMismatch"),
        ("CIENA-WS-PTP-MODEM-MIB", "cwsPtpModemOdu4ClientSignalFailure"))
)
if mibBuilder.loadTexts:
    cienaWsPtpModemGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cienaWsPtpModemCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 9, 2, 2, 1)
)
cienaWsPtpModemCompliance.setObjects(
    ("CIENA-WS-PTP-MODEM-MIB", "cienaWsPtpModemGroup")
)
if mibBuilder.loadTexts:
    cienaWsPtpModemCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-PTP-MODEM-MIB",
    **{"cienaWsPtpModemMIB": cienaWsPtpModemMIB,
       "cienaWsPtpModemObjects": cienaWsPtpModemObjects,
       "cienaWsPtpModemConformance": cienaWsPtpModemConformance,
       "cienaWsPtpModemGroups": cienaWsPtpModemGroups,
       "cienaWsPtpModemGroup": cienaWsPtpModemGroup,
       "cienaWsPtpModemCompliances": cienaWsPtpModemCompliances,
       "cienaWsPtpModemCompliance": cienaWsPtpModemCompliance,
       "cwsPtpAugPtpModemTransmitterTable": cwsPtpAugPtpModemTransmitterTable,
       "cwsPtpAugPtpModemTransmitterEntry": cwsPtpAugPtpModemTransmitterEntry,
       "cwsPtpModemTransmitterLineSystemChannelNumber": cwsPtpModemTransmitterLineSystemChannelNumber,
       "cwsPtpModemFrequencyTable": cwsPtpModemFrequencyTable,
       "cwsPtpModemFrequencyEntry": cwsPtpModemFrequencyEntry,
       "cwsPtpModemFrequencyTableSnmpKey": cwsPtpModemFrequencyTableSnmpKey,
       "cwsPtpModemFrequencyValue": cwsPtpModemFrequencyValue,
       "cwsPtpModemFrequencyMinValue": cwsPtpModemFrequencyMinValue,
       "cwsPtpModemFrequencyMaxValue": cwsPtpModemFrequencyMaxValue,
       "cwsPtpModemFrequencyActual": cwsPtpModemFrequencyActual,
       "cwsPtpModemPowerTable": cwsPtpModemPowerTable,
       "cwsPtpModemPowerEntry": cwsPtpModemPowerEntry,
       "cwsPtpModemPowerTableSnmpKey": cwsPtpModemPowerTableSnmpKey,
       "cwsPtpModemPowerValue": cwsPtpModemPowerValue,
       "cwsPtpModemPowerMinValue": cwsPtpModemPowerMinValue,
       "cwsPtpModemPowerMaxValue": cwsPtpModemPowerMaxValue,
       "cwsPtpModemLineSystemTable": cwsPtpModemLineSystemTable,
       "cwsPtpModemLineSystemEntry": cwsPtpModemLineSystemEntry,
       "cwsPtpModemLineSystemTableSnmpKey": cwsPtpModemLineSystemTableSnmpKey,
       "cwsPtpModemLineSystemType": cwsPtpModemLineSystemType,
       "cwsPtpModemLineSystemWavelengthSpacing": cwsPtpModemLineSystemWavelengthSpacing,
       "cwsPtpModemCmdTable": cwsPtpModemCmdTable,
       "cwsPtpModemCmdEntry": cwsPtpModemCmdEntry,
       "cwsPtpModemCmdTableSnmpKey": cwsPtpModemCmdTableSnmpKey,
       "cwsPtpModemCmdSlot": cwsPtpModemCmdSlot,
       "cwsPtpModemCmdPortIn": cwsPtpModemCmdPortIn,
       "cwsPtpModemCmdPortOut": cwsPtpModemCmdPortOut,
       "cwsPtpModemModemTable": cwsPtpModemModemTable,
       "cwsPtpModemModemEntry": cwsPtpModemModemEntry,
       "cwsPtpModemModemTableSnmpKey": cwsPtpModemModemTableSnmpKey,
       "cwsPtpModemModemChannelContentionDetectionAvoidance": cwsPtpModemModemChannelContentionDetectionAvoidance,
       "cwsPtpModemModemPerformanceOptimizationMode": cwsPtpModemModemPerformanceOptimizationMode,
       "cwsPtpModemModemCarrierCenteringMode": cwsPtpModemModemCarrierCenteringMode,
       "cwsPtpModemModemInterleaverMode": cwsPtpModemModemInterleaverMode,
       "cwsPtpModemModemRotation": cwsPtpModemModemRotation,
       "cwsPtpModemModemSpectralOccupancyMode": cwsPtpModemModemSpectralOccupancyMode,
       "cwsPtpModemModemTxPowerReductionState": cwsPtpModemModemTxPowerReductionState,
       "cwsPtpModemModemTxReductionMode": cwsPtpModemModemTxReductionMode,
       "cwsPtpModemModemTxTuningMode": cwsPtpModemModemTxTuningMode,
       "cwsPtpModemModemDifferentialEncoding": cwsPtpModemModemDifferentialEncoding,
       "cwsPtpModemModemTxCompensationDispersionMode": cwsPtpModemModemTxCompensationDispersionMode,
       "cwsPtpModemModemTxCompensationDispersionValue": cwsPtpModemModemTxCompensationDispersionValue,
       "cwsPtpModemModemFastReceiverRecoveryState": cwsPtpModemModemFastReceiverRecoveryState,
       "cwsPtpModemModemLaserCenteringRange": cwsPtpModemModemLaserCenteringRange,
       "cwsPtpModemPerformanceStatisticsTable": cwsPtpModemPerformanceStatisticsTable,
       "cwsPtpModemPerformanceStatisticsEntry": cwsPtpModemPerformanceStatisticsEntry,
       "cwsPtpModemPerformanceStatisticsTableSnmpKey": cwsPtpModemPerformanceStatisticsTableSnmpKey,
       "cwsPtpModemPerformanceStatisticsSecondsSinceLastClear": cwsPtpModemPerformanceStatisticsSecondsSinceLastClear,
       "cwsPtpModemPerformanceStatisticsFecUncorrectedBlockCount": cwsPtpModemPerformanceStatisticsFecUncorrectedBlockCount,
       "cwsPtpModemPerformanceStatisticsHighCorrectionCountSeconds": cwsPtpModemPerformanceStatisticsHighCorrectionCountSeconds,
       "cwsPtpModemPreFecBerTable": cwsPtpModemPreFecBerTable,
       "cwsPtpModemPreFecBerEntry": cwsPtpModemPreFecBerEntry,
       "cwsPtpModemPreFecBerTableSnmpKey": cwsPtpModemPreFecBerTableSnmpKey,
       "cwsPtpModemPreFecBerActual": cwsPtpModemPreFecBerActual,
       "cwsPtpModemPreFecBerMax": cwsPtpModemPreFecBerMax,
       "cwsPtpModemPreFecBerMin": cwsPtpModemPreFecBerMin,
       "cwsPtpModemPreFecBerAverage": cwsPtpModemPreFecBerAverage,
       "cwsPtpModemPostFecBerTable": cwsPtpModemPostFecBerTable,
       "cwsPtpModemPostFecBerEntry": cwsPtpModemPostFecBerEntry,
       "cwsPtpModemPostFecBerTableSnmpKey": cwsPtpModemPostFecBerTableSnmpKey,
       "cwsPtpModemPostFecBerActual": cwsPtpModemPostFecBerActual,
       "cwsPtpModemPostFecBerMax": cwsPtpModemPostFecBerMax,
       "cwsPtpModemPostFecBerMin": cwsPtpModemPostFecBerMin,
       "cwsPtpModemPostFecBerAverage": cwsPtpModemPostFecBerAverage,
       "cwsPtpModemQFactorTable": cwsPtpModemQFactorTable,
       "cwsPtpModemQFactorEntry": cwsPtpModemQFactorEntry,
       "cwsPtpModemQFactorTableSnmpKey": cwsPtpModemQFactorTableSnmpKey,
       "cwsPtpModemQFactorActual": cwsPtpModemQFactorActual,
       "cwsPtpModemQFactorMax": cwsPtpModemQFactorMax,
       "cwsPtpModemQFactorMin": cwsPtpModemQFactorMin,
       "cwsPtpModemQFactorAverage": cwsPtpModemQFactorAverage,
       "cwsPtpModemFecFrameErrorCountTable": cwsPtpModemFecFrameErrorCountTable,
       "cwsPtpModemFecFrameErrorCountEntry": cwsPtpModemFecFrameErrorCountEntry,
       "cwsPtpModemFecFrameErrorCountTableSnmpKey": cwsPtpModemFecFrameErrorCountTableSnmpKey,
       "cwsPtpModemFecFrameErrorCountValue": cwsPtpModemFecFrameErrorCountValue,
       "cwsPtpModemFecFrameErrorCountSeconds": cwsPtpModemFecFrameErrorCountSeconds,
       "cwsPtpModemModemprefecsignalfailalarmTable": cwsPtpModemModemprefecsignalfailalarmTable,
       "cwsPtpModemModemprefecsignalfailalarmEntry": cwsPtpModemModemprefecsignalfailalarmEntry,
       "cwsPtpModemModemprefecsignalfailalarmTableSnmpKey": cwsPtpModemModemprefecsignalfailalarmTableSnmpKey,
       "cwsPtpModemModemprefecsignalfailalarmActive": cwsPtpModemModemprefecsignalfailalarmActive,
       "cwsPtpModemModemprefecsignalfailalarmthresholdTable": cwsPtpModemModemprefecsignalfailalarmthresholdTable,
       "cwsPtpModemModemprefecsignalfailalarmthresholdEntry": cwsPtpModemModemprefecsignalfailalarmthresholdEntry,
       "cwsPtpModemModemprefecsignalfailalarmthresholdTableSnmpKey": cwsPtpModemModemprefecsignalfailalarmthresholdTableSnmpKey,
       "cwsPtpModemModemprefecsignalfailalarmthresholdDbq": cwsPtpModemModemprefecsignalfailalarmthresholdDbq,
       "cwsPtpModemModemprefecsignaldegradealarmTable": cwsPtpModemModemprefecsignaldegradealarmTable,
       "cwsPtpModemModemprefecsignaldegradealarmEntry": cwsPtpModemModemprefecsignaldegradealarmEntry,
       "cwsPtpModemModemprefecsignaldegradealarmTableSnmpKey": cwsPtpModemModemprefecsignaldegradealarmTableSnmpKey,
       "cwsPtpModemModemprefecsignaldegradealarmActive": cwsPtpModemModemprefecsignaldegradealarmActive,
       "cwsPtpModemModemprefecsignaldegradealarmthresholdTable": cwsPtpModemModemprefecsignaldegradealarmthresholdTable,
       "cwsPtpModemModemprefecsignaldegradealarmthresholdEntry": cwsPtpModemModemprefecsignaldegradealarmthresholdEntry,
       "cwsPtpModemModemprefecsignaldegradealarmthresholdTableSnmpKey": cwsPtpModemModemprefecsignaldegradealarmthresholdTableSnmpKey,
       "cwsPtpModemModemprefecsignaldegradealarmthresholdDbq": cwsPtpModemModemprefecsignaldegradealarmthresholdDbq,
       "cwsPtpModemPreFecSignalFailTable": cwsPtpModemPreFecSignalFailTable,
       "cwsPtpModemPreFecSignalFailEntry": cwsPtpModemPreFecSignalFailEntry,
       "cwsPtpModemPreFecSignalFailTableSnmpKey": cwsPtpModemPreFecSignalFailTableSnmpKey,
       "cwsPtpModemPreFecSignalFailFailStatus": cwsPtpModemPreFecSignalFailFailStatus,
       "cwsPtpModemModemprefecsignalfailthresholdTable": cwsPtpModemModemprefecsignalfailthresholdTable,
       "cwsPtpModemModemprefecsignalfailthresholdEntry": cwsPtpModemModemprefecsignalfailthresholdEntry,
       "cwsPtpModemModemprefecsignalfailthresholdTableSnmpKey": cwsPtpModemModemprefecsignalfailthresholdTableSnmpKey,
       "cwsPtpModemModemprefecsignalfailthresholdDbq": cwsPtpModemModemprefecsignalfailthresholdDbq,
       "cwsPtpModemModemprefecsignalfailthresholdBer": cwsPtpModemModemprefecsignalfailthresholdBer,
       "cwsPtpModemPreFecSignalDegradeTable": cwsPtpModemPreFecSignalDegradeTable,
       "cwsPtpModemPreFecSignalDegradeEntry": cwsPtpModemPreFecSignalDegradeEntry,
       "cwsPtpModemPreFecSignalDegradeTableSnmpKey": cwsPtpModemPreFecSignalDegradeTableSnmpKey,
       "cwsPtpModemPreFecSignalDegradeDegradeStatus": cwsPtpModemPreFecSignalDegradeDegradeStatus,
       "cwsPtpModemModemprefecsignaldegradethresholdTable": cwsPtpModemModemprefecsignaldegradethresholdTable,
       "cwsPtpModemModemprefecsignaldegradethresholdEntry": cwsPtpModemModemprefecsignaldegradethresholdEntry,
       "cwsPtpModemModemprefecsignaldegradethresholdTableSnmpKey": cwsPtpModemModemprefecsignaldegradethresholdTableSnmpKey,
       "cwsPtpModemModemprefecsignaldegradethresholdDbq": cwsPtpModemModemprefecsignaldegradethresholdDbq,
       "cwsPtpModemModemprefecsignaldegradethresholdBer": cwsPtpModemModemprefecsignaldegradethresholdBer,
       "cwsPtpModemRxlinkdispersionTable": cwsPtpModemRxlinkdispersionTable,
       "cwsPtpModemRxlinkdispersionEntry": cwsPtpModemRxlinkdispersionEntry,
       "cwsPtpModemRxlinkdispersionTableSnmpKey": cwsPtpModemRxlinkdispersionTableSnmpKey,
       "cwsPtpModemRxlinkdispersionTotal": cwsPtpModemRxlinkdispersionTotal,
       "cwsPtpModemRxlinkdispersionCompensation": cwsPtpModemRxlinkdispersionCompensation,
       "cwsPtpModemTxlinkdispersionTable": cwsPtpModemTxlinkdispersionTable,
       "cwsPtpModemTxlinkdispersionEntry": cwsPtpModemTxlinkdispersionEntry,
       "cwsPtpModemTxlinkdispersionTableSnmpKey": cwsPtpModemTxlinkdispersionTableSnmpKey,
       "cwsPtpModemTxlinkdispersionTotal": cwsPtpModemTxlinkdispersionTotal,
       "cwsPtpModemTxlinkdispersionActual": cwsPtpModemTxlinkdispersionActual,
       "cwsPtpModemDifferentialGroupDelayTable": cwsPtpModemDifferentialGroupDelayTable,
       "cwsPtpModemDifferentialGroupDelayEntry": cwsPtpModemDifferentialGroupDelayEntry,
       "cwsPtpModemDifferentialGroupDelayTableSnmpKey": cwsPtpModemDifferentialGroupDelayTableSnmpKey,
       "cwsPtpModemDifferentialGroupDelayMeanSupported": cwsPtpModemDifferentialGroupDelayMeanSupported,
       "cwsPtpModemDifferentialGroupDelayEstimatedInstance": cwsPtpModemDifferentialGroupDelayEstimatedInstance,
       "cwsPtpModemFastRxRecoveryTable": cwsPtpModemFastRxRecoveryTable,
       "cwsPtpModemFastRxRecoveryEntry": cwsPtpModemFastRxRecoveryEntry,
       "cwsPtpModemFastRxRecoveryTableSnmpKey": cwsPtpModemFastRxRecoveryTableSnmpKey,
       "cwsPtpModemFastRxRecoveryState": cwsPtpModemFastRxRecoveryState,
       "cwsPtpModemFastRxRecoveryNetworkConfiguration": cwsPtpModemFastRxRecoveryNetworkConfiguration,
       "cwsPtpModemFastRxRecoveryPath1Dispersion": cwsPtpModemFastRxRecoveryPath1Dispersion,
       "cwsPtpModemFastRxRecoveryPath2Dispersion": cwsPtpModemFastRxRecoveryPath2Dispersion,
       "cwsPtpModemColourlessRxChannelPowerTable": cwsPtpModemColourlessRxChannelPowerTable,
       "cwsPtpModemColourlessRxChannelPowerEntry": cwsPtpModemColourlessRxChannelPowerEntry,
       "cwsPtpModemColourlessRxChannelPowerTableSnmpKey": cwsPtpModemColourlessRxChannelPowerTableSnmpKey,
       "cwsXcvrColourlessRxChannelPowerActual": cwsXcvrColourlessRxChannelPowerActual,
       "cwsXcvrColourlessRxChannelPowerMaximum": cwsXcvrColourlessRxChannelPowerMaximum,
       "cwsXcvrColourlessRxChannelPowerMinimum": cwsXcvrColourlessRxChannelPowerMinimum,
       "cwsXcvrColourlessRxChannelPowerMaximumRecordedTime": cwsXcvrColourlessRxChannelPowerMaximumRecordedTime,
       "cwsXcvrColourlessRxChannelPowerMinimumRecordedTime": cwsXcvrColourlessRxChannelPowerMinimumRecordedTime,
       "cwsPtpModemColourlessRxChannelStatusTable": cwsPtpModemColourlessRxChannelStatusTable,
       "cwsPtpModemColourlessRxChannelStatusEntry": cwsPtpModemColourlessRxChannelStatusEntry,
       "cwsPtpModemColourlessRxChannelStatusTableSnmpKey": cwsPtpModemColourlessRxChannelStatusTableSnmpKey,
       "cwsPtpModemColourlessRxChannelStatusLossOfSignal": cwsPtpModemColourlessRxChannelStatusLossOfSignal,
       "cwsPtpModemColourlessRxChannelStatusHighAlarmStatus": cwsPtpModemColourlessRxChannelStatusHighAlarmStatus,
       "cwsPtpModemColourlessRxChannelStatusLowAlarmStatus": cwsPtpModemColourlessRxChannelStatusLowAlarmStatus,
       "cwsPtpModemColourlessTxChannelPowerTable": cwsPtpModemColourlessTxChannelPowerTable,
       "cwsPtpModemColourlessTxChannelPowerEntry": cwsPtpModemColourlessTxChannelPowerEntry,
       "cwsPtpModemColourlessTxChannelPowerTableSnmpKey": cwsPtpModemColourlessTxChannelPowerTableSnmpKey,
       "cwsXcvrColourlessTxChannelPowerActual": cwsXcvrColourlessTxChannelPowerActual,
       "cwsXcvrColourlessTxChannelPowerMaximum": cwsXcvrColourlessTxChannelPowerMaximum,
       "cwsXcvrColourlessTxChannelPowerMinimum": cwsXcvrColourlessTxChannelPowerMinimum,
       "cwsXcvrColourlessTxChannelPowerMaximumRecordedTime": cwsXcvrColourlessTxChannelPowerMaximumRecordedTime,
       "cwsXcvrColourlessTxChannelPowerMinimumRecordedTime": cwsXcvrColourlessTxChannelPowerMinimumRecordedTime,
       "cwsPtpAugPtpModemDiagnosticsTable": cwsPtpAugPtpModemDiagnosticsTable,
       "cwsPtpAugPtpModemDiagnosticsEntry": cwsPtpAugPtpModemDiagnosticsEntry,
       "cwsPtpModemDiagnosticsNumberOfOdu": cwsPtpModemDiagnosticsNumberOfOdu,
       "cwsPtpModemOtu4Table": cwsPtpModemOtu4Table,
       "cwsPtpModemOtu4Entry": cwsPtpModemOtu4Entry,
       "cwsPtpModemOtu4TableSnmpKey": cwsPtpModemOtu4TableSnmpKey,
       "cwsPtpModemOtu4LossOfClock": cwsPtpModemOtu4LossOfClock,
       "cwsPtpModemOtu4FrequencyOutOfRange": cwsPtpModemOtu4FrequencyOutOfRange,
       "cwsPtpModemOtu4LossOfFrame": cwsPtpModemOtu4LossOfFrame,
       "cwsPtpModemOtu4LossOfMultiFrame": cwsPtpModemOtu4LossOfMultiFrame,
       "cwsPtpModemOtu4BackwardDefectIndication": cwsPtpModemOtu4BackwardDefectIndication,
       "cwsPtpModemOtu4TrailTraceIdMismatch": cwsPtpModemOtu4TrailTraceIdMismatch,
       "cwsPtpModemOdu4Table": cwsPtpModemOdu4Table,
       "cwsPtpModemOdu4Entry": cwsPtpModemOdu4Entry,
       "cwsPtpModemOdu4OduId": cwsPtpModemOdu4OduId,
       "cwsPtpModemOdu4OpenConnectionIndication": cwsPtpModemOdu4OpenConnectionIndication,
       "cwsPtpModemOdu4AlarmIndicationSignal": cwsPtpModemOdu4AlarmIndicationSignal,
       "cwsPtpModemOdu4Locked": cwsPtpModemOdu4Locked,
       "cwsPtpModemOdu4SignalFail": cwsPtpModemOdu4SignalFail,
       "cwsPtpModemOdu4SignalDegrade": cwsPtpModemOdu4SignalDegrade,
       "cwsPtpModemOdu4TrailTraceIdMismatch": cwsPtpModemOdu4TrailTraceIdMismatch,
       "cwsPtpModemOdu4BackwardDefectIndication": cwsPtpModemOdu4BackwardDefectIndication,
       "cwsPtpModemOdu4PayloadLabelMismatch": cwsPtpModemOdu4PayloadLabelMismatch,
       "cwsPtpModemOdu4ClientSignalFailure": cwsPtpModemOdu4ClientSignalFailure}
)
