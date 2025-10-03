# SNMP MIB module (CIENA-WS-XCVR-MODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-WS-XCVR-MODEM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:18 2025
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

(Decimal2Dig,
 EnabledDisabledEnum,
 XcvrId,
 YesNoEnum) = mibBuilder.importSymbols(
    "CIENA-WS-TYPEDEFS-MIB",
    "Decimal2Dig",
    "EnabledDisabledEnum",
    "XcvrId",
    "YesNoEnum")

(cwsXcvrVendorDiagnosticMonitoringEntry,) = mibBuilder.importSymbols(
    "CIENA-WS-XCVR-MIB",
    "cwsXcvrVendorDiagnosticMonitoringEntry")

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

cienaWsXcvrModemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16)
)
if mibBuilder.loadTexts:
    cienaWsXcvrModemMIB.setRevisions(
        ("2017-03-02 00:00",
         "2016-12-12 00:00",
         "2016-06-14 00:00",
         "2016-03-03 00:00",
         "2015-02-25 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaWsXcvrModemObjects_ObjectIdentity = ObjectIdentity
cienaWsXcvrModemObjects = _CienaWsXcvrModemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 1)
)
_CienaWsXcvrModemConformance_ObjectIdentity = ObjectIdentity
cienaWsXcvrModemConformance = _CienaWsXcvrModemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 2)
)
_CienaWsXcvrModemGroups_ObjectIdentity = ObjectIdentity
cienaWsXcvrModemGroups = _CienaWsXcvrModemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 2, 1)
)
_CienaWsXcvrModemCompliances_ObjectIdentity = ObjectIdentity
cienaWsXcvrModemCompliances = _CienaWsXcvrModemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 2, 2)
)
_CwsXcvrAugXcvrModemVendorDiagnosticMonitoringTable_Object = MibTable
cwsXcvrAugXcvrModemVendorDiagnosticMonitoringTable = _CwsXcvrAugXcvrModemVendorDiagnosticMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 3)
)
if mibBuilder.loadTexts:
    cwsXcvrAugXcvrModemVendorDiagnosticMonitoringTable.setStatus("current")
_CwsXcvrAugXcvrModemVendorDiagnosticMonitoringEntry_Object = MibTableRow
cwsXcvrAugXcvrModemVendorDiagnosticMonitoringEntry = _CwsXcvrAugXcvrModemVendorDiagnosticMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 3, 1)
)
if mibBuilder.loadTexts:
    cwsXcvrAugXcvrModemVendorDiagnosticMonitoringEntry.setStatus("current")
_CwsXcvrModemVendorDiagnosticMonitoringDiagnosticSupport_Type = YesNoEnum
_CwsXcvrModemVendorDiagnosticMonitoringDiagnosticSupport_Object = MibTableColumn
cwsXcvrModemVendorDiagnosticMonitoringDiagnosticSupport = _CwsXcvrModemVendorDiagnosticMonitoringDiagnosticSupport_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 3, 1, 1),
    _CwsXcvrModemVendorDiagnosticMonitoringDiagnosticSupport_Type()
)
cwsXcvrModemVendorDiagnosticMonitoringDiagnosticSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemVendorDiagnosticMonitoringDiagnosticSupport.setStatus("current")
_CwsXcvrModemVendorDiagnosticMonitoringDispersionMeasurement_Type = YesNoEnum
_CwsXcvrModemVendorDiagnosticMonitoringDispersionMeasurement_Object = MibTableColumn
cwsXcvrModemVendorDiagnosticMonitoringDispersionMeasurement = _CwsXcvrModemVendorDiagnosticMonitoringDispersionMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 3, 1, 2),
    _CwsXcvrModemVendorDiagnosticMonitoringDispersionMeasurement_Type()
)
cwsXcvrModemVendorDiagnosticMonitoringDispersionMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemVendorDiagnosticMonitoringDispersionMeasurement.setStatus("current")
_CwsXcvrModemTransmitterTechnologyTable_Object = MibTable
cwsXcvrModemTransmitterTechnologyTable = _CwsXcvrModemTransmitterTechnologyTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 4)
)
if mibBuilder.loadTexts:
    cwsXcvrModemTransmitterTechnologyTable.setStatus("current")
_CwsXcvrModemTransmitterTechnologyEntry_Object = MibTableRow
cwsXcvrModemTransmitterTechnologyEntry = _CwsXcvrModemTransmitterTechnologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 4, 1)
)
cwsXcvrModemTransmitterTechnologyEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemTransmitterTechnologyTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrModemTransmitterTechnologyEntry.setStatus("current")


class _CwsXcvrModemTransmitterTechnologyTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrModemTransmitterTechnologyTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrModemTransmitterTechnologyTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrModemTransmitterTechnologyTableSnmpKey_Object = MibTableColumn
cwsXcvrModemTransmitterTechnologyTableSnmpKey = _CwsXcvrModemTransmitterTechnologyTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 4, 1, 1),
    _CwsXcvrModemTransmitterTechnologyTableSnmpKey_Type()
)
cwsXcvrModemTransmitterTechnologyTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrModemTransmitterTechnologyTableSnmpKey.setStatus("current")


class _CwsXcvrModemTransmitterTechnologyWavelengthControl_Type(Integer32):
    """Custom type cwsXcvrModemTransmitterTechnologyWavelengthControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("active", 1))
    )


_CwsXcvrModemTransmitterTechnologyWavelengthControl_Type.__name__ = "Integer32"
_CwsXcvrModemTransmitterTechnologyWavelengthControl_Object = MibTableColumn
cwsXcvrModemTransmitterTechnologyWavelengthControl = _CwsXcvrModemTransmitterTechnologyWavelengthControl_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 4, 1, 2),
    _CwsXcvrModemTransmitterTechnologyWavelengthControl_Type()
)
cwsXcvrModemTransmitterTechnologyWavelengthControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemTransmitterTechnologyWavelengthControl.setStatus("current")
_CwsXcvrModemTransmitterTechnologyTunable_Type = YesNoEnum
_CwsXcvrModemTransmitterTechnologyTunable_Object = MibTableColumn
cwsXcvrModemTransmitterTechnologyTunable = _CwsXcvrModemTransmitterTechnologyTunable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 4, 1, 3),
    _CwsXcvrModemTransmitterTechnologyTunable_Type()
)
cwsXcvrModemTransmitterTechnologyTunable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemTransmitterTechnologyTunable.setStatus("current")
_CwsXcvrModemTransmitterTechnologyWavelengthMin_Type = Decimal2Dig
_CwsXcvrModemTransmitterTechnologyWavelengthMin_Object = MibTableColumn
cwsXcvrModemTransmitterTechnologyWavelengthMin = _CwsXcvrModemTransmitterTechnologyWavelengthMin_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 4, 1, 4),
    _CwsXcvrModemTransmitterTechnologyWavelengthMin_Type()
)
cwsXcvrModemTransmitterTechnologyWavelengthMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemTransmitterTechnologyWavelengthMin.setStatus("current")
_CwsXcvrModemTransmitterTechnologyWavelengthMax_Type = Decimal2Dig
_CwsXcvrModemTransmitterTechnologyWavelengthMax_Object = MibTableColumn
cwsXcvrModemTransmitterTechnologyWavelengthMax = _CwsXcvrModemTransmitterTechnologyWavelengthMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 4, 1, 5),
    _CwsXcvrModemTransmitterTechnologyWavelengthMax_Type()
)
cwsXcvrModemTransmitterTechnologyWavelengthMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemTransmitterTechnologyWavelengthMax.setStatus("current")
_CwsXcvrModemTransmitterTechnologyWavelengthTolerance_Type = Unsigned32
_CwsXcvrModemTransmitterTechnologyWavelengthTolerance_Object = MibTableColumn
cwsXcvrModemTransmitterTechnologyWavelengthTolerance = _CwsXcvrModemTransmitterTechnologyWavelengthTolerance_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 4, 1, 6),
    _CwsXcvrModemTransmitterTechnologyWavelengthTolerance_Type()
)
cwsXcvrModemTransmitterTechnologyWavelengthTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemTransmitterTechnologyWavelengthTolerance.setStatus("current")
_CwsXcvrModemTransmitterTechnologyFrequencyMin_Type = Unsigned32
_CwsXcvrModemTransmitterTechnologyFrequencyMin_Object = MibTableColumn
cwsXcvrModemTransmitterTechnologyFrequencyMin = _CwsXcvrModemTransmitterTechnologyFrequencyMin_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 4, 1, 7),
    _CwsXcvrModemTransmitterTechnologyFrequencyMin_Type()
)
cwsXcvrModemTransmitterTechnologyFrequencyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemTransmitterTechnologyFrequencyMin.setStatus("current")
_CwsXcvrModemTransmitterTechnologyFrequencyMax_Type = Unsigned32
_CwsXcvrModemTransmitterTechnologyFrequencyMax_Object = MibTableColumn
cwsXcvrModemTransmitterTechnologyFrequencyMax = _CwsXcvrModemTransmitterTechnologyFrequencyMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 4, 1, 8),
    _CwsXcvrModemTransmitterTechnologyFrequencyMax_Type()
)
cwsXcvrModemTransmitterTechnologyFrequencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemTransmitterTechnologyFrequencyMax.setStatus("current")
_CwsXcvrModemTransmitterTechnologyTxDispersionMin_Type = Unsigned32
_CwsXcvrModemTransmitterTechnologyTxDispersionMin_Object = MibTableColumn
cwsXcvrModemTransmitterTechnologyTxDispersionMin = _CwsXcvrModemTransmitterTechnologyTxDispersionMin_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 4, 1, 9),
    _CwsXcvrModemTransmitterTechnologyTxDispersionMin_Type()
)
cwsXcvrModemTransmitterTechnologyTxDispersionMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemTransmitterTechnologyTxDispersionMin.setStatus("current")
_CwsXcvrModemTransmitterTechnologyTxDispersionMax_Type = Unsigned32
_CwsXcvrModemTransmitterTechnologyTxDispersionMax_Object = MibTableColumn
cwsXcvrModemTransmitterTechnologyTxDispersionMax = _CwsXcvrModemTransmitterTechnologyTxDispersionMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 4, 1, 10),
    _CwsXcvrModemTransmitterTechnologyTxDispersionMax_Type()
)
cwsXcvrModemTransmitterTechnologyTxDispersionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemTransmitterTechnologyTxDispersionMax.setStatus("current")
_CwsXcvrModemTransmitterTechnologyEdfa_Type = YesNoEnum
_CwsXcvrModemTransmitterTechnologyEdfa_Object = MibTableColumn
cwsXcvrModemTransmitterTechnologyEdfa = _CwsXcvrModemTransmitterTechnologyEdfa_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 4, 1, 11),
    _CwsXcvrModemTransmitterTechnologyEdfa_Type()
)
cwsXcvrModemTransmitterTechnologyEdfa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemTransmitterTechnologyEdfa.setStatus("current")
_CwsXcvrModemModulationSupportTable_Object = MibTable
cwsXcvrModemModulationSupportTable = _CwsXcvrModemModulationSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 5)
)
if mibBuilder.loadTexts:
    cwsXcvrModemModulationSupportTable.setStatus("current")
_CwsXcvrModemModulationSupportEntry_Object = MibTableRow
cwsXcvrModemModulationSupportEntry = _CwsXcvrModemModulationSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 5, 1)
)
cwsXcvrModemModulationSupportEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemModulationSupportTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrModemModulationSupportEntry.setStatus("current")


class _CwsXcvrModemModulationSupportTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrModemModulationSupportTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrModemModulationSupportTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrModemModulationSupportTableSnmpKey_Object = MibTableColumn
cwsXcvrModemModulationSupportTableSnmpKey = _CwsXcvrModemModulationSupportTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 5, 1, 1),
    _CwsXcvrModemModulationSupportTableSnmpKey_Type()
)
cwsXcvrModemModulationSupportTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrModemModulationSupportTableSnmpKey.setStatus("current")
_CwsXcvrModemModulationSupportModulation16qam_Type = YesNoEnum
_CwsXcvrModemModulationSupportModulation16qam_Object = MibTableColumn
cwsXcvrModemModulationSupportModulation16qam = _CwsXcvrModemModulationSupportModulation16qam_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 5, 1, 2),
    _CwsXcvrModemModulationSupportModulation16qam_Type()
)
cwsXcvrModemModulationSupportModulation16qam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemModulationSupportModulation16qam.setStatus("current")
_CwsXcvrModemModulationSupportModulationQpsk_Type = YesNoEnum
_CwsXcvrModemModulationSupportModulationQpsk_Object = MibTableColumn
cwsXcvrModemModulationSupportModulationQpsk = _CwsXcvrModemModulationSupportModulationQpsk_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 5, 1, 3),
    _CwsXcvrModemModulationSupportModulationQpsk_Type()
)
cwsXcvrModemModulationSupportModulationQpsk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemModulationSupportModulationQpsk.setStatus("current")
_CwsXcvrModemModulationSupportModulationBpsk_Type = YesNoEnum
_CwsXcvrModemModulationSupportModulationBpsk_Object = MibTableColumn
cwsXcvrModemModulationSupportModulationBpsk = _CwsXcvrModemModulationSupportModulationBpsk_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 5, 1, 4),
    _CwsXcvrModemModulationSupportModulationBpsk_Type()
)
cwsXcvrModemModulationSupportModulationBpsk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemModulationSupportModulationBpsk.setStatus("current")
_CwsXcvrModemModulationSupportModulation8qam_Type = YesNoEnum
_CwsXcvrModemModulationSupportModulation8qam_Object = MibTableColumn
cwsXcvrModemModulationSupportModulation8qam = _CwsXcvrModemModulationSupportModulation8qam_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 5, 1, 5),
    _CwsXcvrModemModulationSupportModulation8qam_Type()
)
cwsXcvrModemModulationSupportModulation8qam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemModulationSupportModulation8qam.setStatus("current")
_CwsXcvrModemTransportProtocolsTable_Object = MibTable
cwsXcvrModemTransportProtocolsTable = _CwsXcvrModemTransportProtocolsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 6)
)
if mibBuilder.loadTexts:
    cwsXcvrModemTransportProtocolsTable.setStatus("current")
_CwsXcvrModemTransportProtocolsEntry_Object = MibTableRow
cwsXcvrModemTransportProtocolsEntry = _CwsXcvrModemTransportProtocolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 6, 1)
)
cwsXcvrModemTransportProtocolsEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemTransportProtocolsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrModemTransportProtocolsEntry.setStatus("current")


class _CwsXcvrModemTransportProtocolsTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrModemTransportProtocolsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrModemTransportProtocolsTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrModemTransportProtocolsTableSnmpKey_Object = MibTableColumn
cwsXcvrModemTransportProtocolsTableSnmpKey = _CwsXcvrModemTransportProtocolsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 6, 1, 1),
    _CwsXcvrModemTransportProtocolsTableSnmpKey_Type()
)
cwsXcvrModemTransportProtocolsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrModemTransportProtocolsTableSnmpKey.setStatus("current")
_CwsXcvrModemTransportProtocolsOtnBookended_Type = YesNoEnum
_CwsXcvrModemTransportProtocolsOtnBookended_Object = MibTableColumn
cwsXcvrModemTransportProtocolsOtnBookended = _CwsXcvrModemTransportProtocolsOtnBookended_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 6, 1, 2),
    _CwsXcvrModemTransportProtocolsOtnBookended_Type()
)
cwsXcvrModemTransportProtocolsOtnBookended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemTransportProtocolsOtnBookended.setStatus("current")
_CwsXcvrModemTransportProtocolsOtnInterworking_Type = YesNoEnum
_CwsXcvrModemTransportProtocolsOtnInterworking_Object = MibTableColumn
cwsXcvrModemTransportProtocolsOtnInterworking = _CwsXcvrModemTransportProtocolsOtnInterworking_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 6, 1, 3),
    _CwsXcvrModemTransportProtocolsOtnInterworking_Type()
)
cwsXcvrModemTransportProtocolsOtnInterworking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemTransportProtocolsOtnInterworking.setStatus("current")
_CwsXcvrModemTransportProtocolsEthernet_Type = YesNoEnum
_CwsXcvrModemTransportProtocolsEthernet_Object = MibTableColumn
cwsXcvrModemTransportProtocolsEthernet = _CwsXcvrModemTransportProtocolsEthernet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 6, 1, 4),
    _CwsXcvrModemTransportProtocolsEthernet_Type()
)
cwsXcvrModemTransportProtocolsEthernet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemTransportProtocolsEthernet.setStatus("current")
_CwsXcvrModemLineSystemSupportTable_Object = MibTable
cwsXcvrModemLineSystemSupportTable = _CwsXcvrModemLineSystemSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 7)
)
if mibBuilder.loadTexts:
    cwsXcvrModemLineSystemSupportTable.setStatus("current")
_CwsXcvrModemLineSystemSupportEntry_Object = MibTableRow
cwsXcvrModemLineSystemSupportEntry = _CwsXcvrModemLineSystemSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 7, 1)
)
cwsXcvrModemLineSystemSupportEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemLineSystemSupportTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrModemLineSystemSupportEntry.setStatus("current")


class _CwsXcvrModemLineSystemSupportTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrModemLineSystemSupportTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrModemLineSystemSupportTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrModemLineSystemSupportTableSnmpKey_Object = MibTableColumn
cwsXcvrModemLineSystemSupportTableSnmpKey = _CwsXcvrModemLineSystemSupportTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 7, 1, 1),
    _CwsXcvrModemLineSystemSupportTableSnmpKey_Type()
)
cwsXcvrModemLineSystemSupportTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrModemLineSystemSupportTableSnmpKey.setStatus("current")
_CwsXcvrModemLineSystemSupportColoured_Type = YesNoEnum
_CwsXcvrModemLineSystemSupportColoured_Object = MibTableColumn
cwsXcvrModemLineSystemSupportColoured = _CwsXcvrModemLineSystemSupportColoured_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 7, 1, 2),
    _CwsXcvrModemLineSystemSupportColoured_Type()
)
cwsXcvrModemLineSystemSupportColoured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemLineSystemSupportColoured.setStatus("current")
_CwsXcvrModemLineSystemSupportColourless_Type = YesNoEnum
_CwsXcvrModemLineSystemSupportColourless_Object = MibTableColumn
cwsXcvrModemLineSystemSupportColourless = _CwsXcvrModemLineSystemSupportColourless_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 7, 1, 3),
    _CwsXcvrModemLineSystemSupportColourless_Type()
)
cwsXcvrModemLineSystemSupportColourless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemLineSystemSupportColourless.setStatus("current")
_CwsXcvrModemLineSystemSupportContentionless_Type = YesNoEnum
_CwsXcvrModemLineSystemSupportContentionless_Object = MibTableColumn
cwsXcvrModemLineSystemSupportContentionless = _CwsXcvrModemLineSystemSupportContentionless_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 7, 1, 4),
    _CwsXcvrModemLineSystemSupportContentionless_Type()
)
cwsXcvrModemLineSystemSupportContentionless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemLineSystemSupportContentionless.setStatus("current")
_CwsXcvrModemLineSystemSupportCoherentSelectColoured_Type = YesNoEnum
_CwsXcvrModemLineSystemSupportCoherentSelectColoured_Object = MibTableColumn
cwsXcvrModemLineSystemSupportCoherentSelectColoured = _CwsXcvrModemLineSystemSupportCoherentSelectColoured_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 7, 1, 5),
    _CwsXcvrModemLineSystemSupportCoherentSelectColoured_Type()
)
cwsXcvrModemLineSystemSupportCoherentSelectColoured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemLineSystemSupportCoherentSelectColoured.setStatus("current")
_CwsXcvrModemLineSystemSupportCoherentSelectColourless_Type = YesNoEnum
_CwsXcvrModemLineSystemSupportCoherentSelectColourless_Object = MibTableColumn
cwsXcvrModemLineSystemSupportCoherentSelectColourless = _CwsXcvrModemLineSystemSupportCoherentSelectColourless_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 7, 1, 6),
    _CwsXcvrModemLineSystemSupportCoherentSelectColourless_Type()
)
cwsXcvrModemLineSystemSupportCoherentSelectColourless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemLineSystemSupportCoherentSelectColourless.setStatus("current")
_CwsXcvrModemLineSystemSupportThirdParty_Type = YesNoEnum
_CwsXcvrModemLineSystemSupportThirdParty_Object = MibTableColumn
cwsXcvrModemLineSystemSupportThirdParty = _CwsXcvrModemLineSystemSupportThirdParty_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 7, 1, 7),
    _CwsXcvrModemLineSystemSupportThirdParty_Type()
)
cwsXcvrModemLineSystemSupportThirdParty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemLineSystemSupportThirdParty.setStatus("current")
_CwsXcvrModemEquipmentStatusTable_Object = MibTable
cwsXcvrModemEquipmentStatusTable = _CwsXcvrModemEquipmentStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 8)
)
if mibBuilder.loadTexts:
    cwsXcvrModemEquipmentStatusTable.setStatus("current")
_CwsXcvrModemEquipmentStatusEntry_Object = MibTableRow
cwsXcvrModemEquipmentStatusEntry = _CwsXcvrModemEquipmentStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 8, 1)
)
cwsXcvrModemEquipmentStatusEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemEquipmentStatusTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrModemEquipmentStatusEntry.setStatus("current")


class _CwsXcvrModemEquipmentStatusTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrModemEquipmentStatusTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrModemEquipmentStatusTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrModemEquipmentStatusTableSnmpKey_Object = MibTableColumn
cwsXcvrModemEquipmentStatusTableSnmpKey = _CwsXcvrModemEquipmentStatusTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 8, 1, 1),
    _CwsXcvrModemEquipmentStatusTableSnmpKey_Type()
)
cwsXcvrModemEquipmentStatusTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrModemEquipmentStatusTableSnmpKey.setStatus("current")
_CwsXcvrModemEquipmentStatusTransmitterState_Type = EnabledDisabledEnum
_CwsXcvrModemEquipmentStatusTransmitterState_Object = MibTableColumn
cwsXcvrModemEquipmentStatusTransmitterState = _CwsXcvrModemEquipmentStatusTransmitterState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 8, 1, 2),
    _CwsXcvrModemEquipmentStatusTransmitterState_Type()
)
cwsXcvrModemEquipmentStatusTransmitterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemEquipmentStatusTransmitterState.setStatus("current")
_CwsXcvrModemEquipmentStatusEquipmentOutOfSpec_Type = YesNoEnum
_CwsXcvrModemEquipmentStatusEquipmentOutOfSpec_Object = MibTableColumn
cwsXcvrModemEquipmentStatusEquipmentOutOfSpec = _CwsXcvrModemEquipmentStatusEquipmentOutOfSpec_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 8, 1, 3),
    _CwsXcvrModemEquipmentStatusEquipmentOutOfSpec_Type()
)
cwsXcvrModemEquipmentStatusEquipmentOutOfSpec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemEquipmentStatusEquipmentOutOfSpec.setStatus("current")
_CwsXcvrModemEquipmentStatusEquipmentFailure_Type = YesNoEnum
_CwsXcvrModemEquipmentStatusEquipmentFailure_Object = MibTableColumn
cwsXcvrModemEquipmentStatusEquipmentFailure = _CwsXcvrModemEquipmentStatusEquipmentFailure_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 8, 1, 4),
    _CwsXcvrModemEquipmentStatusEquipmentFailure_Type()
)
cwsXcvrModemEquipmentStatusEquipmentFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemEquipmentStatusEquipmentFailure.setStatus("current")
_CwsXcvrModemEquipmentStatusDataLinkSuspect_Type = YesNoEnum
_CwsXcvrModemEquipmentStatusDataLinkSuspect_Object = MibTableColumn
cwsXcvrModemEquipmentStatusDataLinkSuspect = _CwsXcvrModemEquipmentStatusDataLinkSuspect_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 8, 1, 5),
    _CwsXcvrModemEquipmentStatusDataLinkSuspect_Type()
)
cwsXcvrModemEquipmentStatusDataLinkSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemEquipmentStatusDataLinkSuspect.setStatus("current")
_CwsXcvrModemEquipmentStatusCommsLinkSuspect_Type = YesNoEnum
_CwsXcvrModemEquipmentStatusCommsLinkSuspect_Object = MibTableColumn
cwsXcvrModemEquipmentStatusCommsLinkSuspect = _CwsXcvrModemEquipmentStatusCommsLinkSuspect_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 8, 1, 6),
    _CwsXcvrModemEquipmentStatusCommsLinkSuspect_Type()
)
cwsXcvrModemEquipmentStatusCommsLinkSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemEquipmentStatusCommsLinkSuspect.setStatus("current")
_CwsXcvrModemEquipmentStatusClockSuspect_Type = YesNoEnum
_CwsXcvrModemEquipmentStatusClockSuspect_Object = MibTableColumn
cwsXcvrModemEquipmentStatusClockSuspect = _CwsXcvrModemEquipmentStatusClockSuspect_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 8, 1, 7),
    _CwsXcvrModemEquipmentStatusClockSuspect_Type()
)
cwsXcvrModemEquipmentStatusClockSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemEquipmentStatusClockSuspect.setStatus("current")
_CwsXcvrModemEquipmentStatusLossOfSynchronizationTick_Type = YesNoEnum
_CwsXcvrModemEquipmentStatusLossOfSynchronizationTick_Object = MibTableColumn
cwsXcvrModemEquipmentStatusLossOfSynchronizationTick = _CwsXcvrModemEquipmentStatusLossOfSynchronizationTick_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 8, 1, 8),
    _CwsXcvrModemEquipmentStatusLossOfSynchronizationTick_Type()
)
cwsXcvrModemEquipmentStatusLossOfSynchronizationTick.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrModemEquipmentStatusLossOfSynchronizationTick.setStatus("current")
cwsXcvrVendorDiagnosticMonitoringEntry.registerAugmentions(
    ("CIENA-WS-XCVR-MODEM-MIB",
     "cwsXcvrAugXcvrModemVendorDiagnosticMonitoringEntry")
)
cwsXcvrAugXcvrModemVendorDiagnosticMonitoringEntry.setIndexNames(*cwsXcvrVendorDiagnosticMonitoringEntry.getIndexNames())

# Managed Objects groups

cienaWsXcvrModemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 2, 1, 1)
)
cienaWsXcvrModemGroup.setObjects(
      *(("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemVendorDiagnosticMonitoringDiagnosticSupport"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemVendorDiagnosticMonitoringDispersionMeasurement"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemTransmitterTechnologyWavelengthControl"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemTransmitterTechnologyTunable"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemTransmitterTechnologyWavelengthMin"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemTransmitterTechnologyWavelengthMax"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemTransmitterTechnologyWavelengthTolerance"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemTransmitterTechnologyFrequencyMin"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemTransmitterTechnologyFrequencyMax"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemTransmitterTechnologyTxDispersionMin"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemTransmitterTechnologyTxDispersionMax"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemTransmitterTechnologyEdfa"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemModulationSupportModulation16qam"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemModulationSupportModulationQpsk"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemModulationSupportModulationBpsk"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemModulationSupportModulation8qam"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemTransportProtocolsOtnBookended"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemTransportProtocolsOtnInterworking"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemTransportProtocolsEthernet"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemLineSystemSupportColoured"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemLineSystemSupportColourless"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemLineSystemSupportContentionless"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemLineSystemSupportCoherentSelectColoured"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemLineSystemSupportCoherentSelectColourless"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemLineSystemSupportThirdParty"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemEquipmentStatusTransmitterState"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemEquipmentStatusEquipmentOutOfSpec"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemEquipmentStatusEquipmentFailure"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemEquipmentStatusDataLinkSuspect"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemEquipmentStatusCommsLinkSuspect"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemEquipmentStatusClockSuspect"),
        ("CIENA-WS-XCVR-MODEM-MIB", "cwsXcvrModemEquipmentStatusLossOfSynchronizationTick"))
)
if mibBuilder.loadTexts:
    cienaWsXcvrModemGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cienaWsXcvrModemCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 16, 2, 2, 1)
)
cienaWsXcvrModemCompliance.setObjects(
    ("CIENA-WS-XCVR-MODEM-MIB", "cienaWsXcvrModemGroup")
)
if mibBuilder.loadTexts:
    cienaWsXcvrModemCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-XCVR-MODEM-MIB",
    **{"cienaWsXcvrModemMIB": cienaWsXcvrModemMIB,
       "cienaWsXcvrModemObjects": cienaWsXcvrModemObjects,
       "cienaWsXcvrModemConformance": cienaWsXcvrModemConformance,
       "cienaWsXcvrModemGroups": cienaWsXcvrModemGroups,
       "cienaWsXcvrModemGroup": cienaWsXcvrModemGroup,
       "cienaWsXcvrModemCompliances": cienaWsXcvrModemCompliances,
       "cienaWsXcvrModemCompliance": cienaWsXcvrModemCompliance,
       "cwsXcvrAugXcvrModemVendorDiagnosticMonitoringTable": cwsXcvrAugXcvrModemVendorDiagnosticMonitoringTable,
       "cwsXcvrAugXcvrModemVendorDiagnosticMonitoringEntry": cwsXcvrAugXcvrModemVendorDiagnosticMonitoringEntry,
       "cwsXcvrModemVendorDiagnosticMonitoringDiagnosticSupport": cwsXcvrModemVendorDiagnosticMonitoringDiagnosticSupport,
       "cwsXcvrModemVendorDiagnosticMonitoringDispersionMeasurement": cwsXcvrModemVendorDiagnosticMonitoringDispersionMeasurement,
       "cwsXcvrModemTransmitterTechnologyTable": cwsXcvrModemTransmitterTechnologyTable,
       "cwsXcvrModemTransmitterTechnologyEntry": cwsXcvrModemTransmitterTechnologyEntry,
       "cwsXcvrModemTransmitterTechnologyTableSnmpKey": cwsXcvrModemTransmitterTechnologyTableSnmpKey,
       "cwsXcvrModemTransmitterTechnologyWavelengthControl": cwsXcvrModemTransmitterTechnologyWavelengthControl,
       "cwsXcvrModemTransmitterTechnologyTunable": cwsXcvrModemTransmitterTechnologyTunable,
       "cwsXcvrModemTransmitterTechnologyWavelengthMin": cwsXcvrModemTransmitterTechnologyWavelengthMin,
       "cwsXcvrModemTransmitterTechnologyWavelengthMax": cwsXcvrModemTransmitterTechnologyWavelengthMax,
       "cwsXcvrModemTransmitterTechnologyWavelengthTolerance": cwsXcvrModemTransmitterTechnologyWavelengthTolerance,
       "cwsXcvrModemTransmitterTechnologyFrequencyMin": cwsXcvrModemTransmitterTechnologyFrequencyMin,
       "cwsXcvrModemTransmitterTechnologyFrequencyMax": cwsXcvrModemTransmitterTechnologyFrequencyMax,
       "cwsXcvrModemTransmitterTechnologyTxDispersionMin": cwsXcvrModemTransmitterTechnologyTxDispersionMin,
       "cwsXcvrModemTransmitterTechnologyTxDispersionMax": cwsXcvrModemTransmitterTechnologyTxDispersionMax,
       "cwsXcvrModemTransmitterTechnologyEdfa": cwsXcvrModemTransmitterTechnologyEdfa,
       "cwsXcvrModemModulationSupportTable": cwsXcvrModemModulationSupportTable,
       "cwsXcvrModemModulationSupportEntry": cwsXcvrModemModulationSupportEntry,
       "cwsXcvrModemModulationSupportTableSnmpKey": cwsXcvrModemModulationSupportTableSnmpKey,
       "cwsXcvrModemModulationSupportModulation16qam": cwsXcvrModemModulationSupportModulation16qam,
       "cwsXcvrModemModulationSupportModulationQpsk": cwsXcvrModemModulationSupportModulationQpsk,
       "cwsXcvrModemModulationSupportModulationBpsk": cwsXcvrModemModulationSupportModulationBpsk,
       "cwsXcvrModemModulationSupportModulation8qam": cwsXcvrModemModulationSupportModulation8qam,
       "cwsXcvrModemTransportProtocolsTable": cwsXcvrModemTransportProtocolsTable,
       "cwsXcvrModemTransportProtocolsEntry": cwsXcvrModemTransportProtocolsEntry,
       "cwsXcvrModemTransportProtocolsTableSnmpKey": cwsXcvrModemTransportProtocolsTableSnmpKey,
       "cwsXcvrModemTransportProtocolsOtnBookended": cwsXcvrModemTransportProtocolsOtnBookended,
       "cwsXcvrModemTransportProtocolsOtnInterworking": cwsXcvrModemTransportProtocolsOtnInterworking,
       "cwsXcvrModemTransportProtocolsEthernet": cwsXcvrModemTransportProtocolsEthernet,
       "cwsXcvrModemLineSystemSupportTable": cwsXcvrModemLineSystemSupportTable,
       "cwsXcvrModemLineSystemSupportEntry": cwsXcvrModemLineSystemSupportEntry,
       "cwsXcvrModemLineSystemSupportTableSnmpKey": cwsXcvrModemLineSystemSupportTableSnmpKey,
       "cwsXcvrModemLineSystemSupportColoured": cwsXcvrModemLineSystemSupportColoured,
       "cwsXcvrModemLineSystemSupportColourless": cwsXcvrModemLineSystemSupportColourless,
       "cwsXcvrModemLineSystemSupportContentionless": cwsXcvrModemLineSystemSupportContentionless,
       "cwsXcvrModemLineSystemSupportCoherentSelectColoured": cwsXcvrModemLineSystemSupportCoherentSelectColoured,
       "cwsXcvrModemLineSystemSupportCoherentSelectColourless": cwsXcvrModemLineSystemSupportCoherentSelectColourless,
       "cwsXcvrModemLineSystemSupportThirdParty": cwsXcvrModemLineSystemSupportThirdParty,
       "cwsXcvrModemEquipmentStatusTable": cwsXcvrModemEquipmentStatusTable,
       "cwsXcvrModemEquipmentStatusEntry": cwsXcvrModemEquipmentStatusEntry,
       "cwsXcvrModemEquipmentStatusTableSnmpKey": cwsXcvrModemEquipmentStatusTableSnmpKey,
       "cwsXcvrModemEquipmentStatusTransmitterState": cwsXcvrModemEquipmentStatusTransmitterState,
       "cwsXcvrModemEquipmentStatusEquipmentOutOfSpec": cwsXcvrModemEquipmentStatusEquipmentOutOfSpec,
       "cwsXcvrModemEquipmentStatusEquipmentFailure": cwsXcvrModemEquipmentStatusEquipmentFailure,
       "cwsXcvrModemEquipmentStatusDataLinkSuspect": cwsXcvrModemEquipmentStatusDataLinkSuspect,
       "cwsXcvrModemEquipmentStatusCommsLinkSuspect": cwsXcvrModemEquipmentStatusCommsLinkSuspect,
       "cwsXcvrModemEquipmentStatusClockSuspect": cwsXcvrModemEquipmentStatusClockSuspect,
       "cwsXcvrModemEquipmentStatusLossOfSynchronizationTick": cwsXcvrModemEquipmentStatusLossOfSynchronizationTick}
)
