# SNMP MIB module (CIENA-WS-XCVR-PLUGGABLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-WS-XCVR-PLUGGABLE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:19 2025
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
 Decimal2Dig,
 StringMaxl16,
 StringMaxl32,
 XcvrId,
 XcvrSerdesRxAmplitude,
 XcvrSerdesRxEmphasis,
 XcvrSerdesTxEq) = mibBuilder.importSymbols(
    "CIENA-WS-TYPEDEFS-MIB",
    "ChannelsNumber",
    "Decimal2Dig",
    "StringMaxl16",
    "StringMaxl32",
    "XcvrId",
    "XcvrSerdesRxAmplitude",
    "XcvrSerdesRxEmphasis",
    "XcvrSerdesTxEq")

(cwsXcvrChannelDiagnosticsEntry,
 cwsXcvrDeviceIdEntry,
 cwsXcvrVendorDiagnosticMonitoringEntry,
 cwsXcvrVendorIdEntry,
 cwsXcvrVendorTransmitterEntry) = mibBuilder.importSymbols(
    "CIENA-WS-XCVR-MIB",
    "cwsXcvrChannelDiagnosticsEntry",
    "cwsXcvrDeviceIdEntry",
    "cwsXcvrVendorDiagnosticMonitoringEntry",
    "cwsXcvrVendorIdEntry",
    "cwsXcvrVendorTransmitterEntry")

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

cienaWsXcvrPluggableMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17)
)
if mibBuilder.loadTexts:
    cienaWsXcvrPluggableMIB.setRevisions(
        ("2017-07-24 00:00",
         "2017-03-02 00:00",
         "2016-12-12 00:00",
         "2016-06-14 00:00",
         "2015-02-25 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaWsXcvrPluggableObjects_ObjectIdentity = ObjectIdentity
cienaWsXcvrPluggableObjects = _CienaWsXcvrPluggableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 1)
)
_CienaWsXcvrPluggableConformance_ObjectIdentity = ObjectIdentity
cienaWsXcvrPluggableConformance = _CienaWsXcvrPluggableConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 2)
)
_CienaWsXcvrPluggableGroups_ObjectIdentity = ObjectIdentity
cienaWsXcvrPluggableGroups = _CienaWsXcvrPluggableGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 2, 1)
)
_CienaWsXcvrPluggableCompliances_ObjectIdentity = ObjectIdentity
cienaWsXcvrPluggableCompliances = _CienaWsXcvrPluggableCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 2, 2)
)
_CwsXcvrAugXcvrPluggableVendorIdTable_Object = MibTable
cwsXcvrAugXcvrPluggableVendorIdTable = _CwsXcvrAugXcvrPluggableVendorIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 3)
)
if mibBuilder.loadTexts:
    cwsXcvrAugXcvrPluggableVendorIdTable.setStatus("current")
_CwsXcvrAugXcvrPluggableVendorIdEntry_Object = MibTableRow
cwsXcvrAugXcvrPluggableVendorIdEntry = _CwsXcvrAugXcvrPluggableVendorIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 3, 1)
)
if mibBuilder.loadTexts:
    cwsXcvrAugXcvrPluggableVendorIdEntry.setStatus("current")


class _CwsXcvrPluggableVendorIdRevisionCompliance_Type(Integer32):
    """Custom type cwsXcvrPluggableVendorIdRevisionCompliance based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("notspecified", 0),
          ("rv47", 1),
          ("rv472h", 2),
          ("rv13", 3),
          ("rv14", 4),
          ("rv15", 5),
          ("rv20", 6),
          ("rv20and26and27", 7))
    )


_CwsXcvrPluggableVendorIdRevisionCompliance_Type.__name__ = "Integer32"
_CwsXcvrPluggableVendorIdRevisionCompliance_Object = MibTableColumn
cwsXcvrPluggableVendorIdRevisionCompliance = _CwsXcvrPluggableVendorIdRevisionCompliance_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 3, 1, 1),
    _CwsXcvrPluggableVendorIdRevisionCompliance_Type()
)
cwsXcvrPluggableVendorIdRevisionCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableVendorIdRevisionCompliance.setStatus("current")
_CwsXcvrPluggableVendorOuiTable_Object = MibTable
cwsXcvrPluggableVendorOuiTable = _CwsXcvrPluggableVendorOuiTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 4)
)
if mibBuilder.loadTexts:
    cwsXcvrPluggableVendorOuiTable.setStatus("current")
_CwsXcvrPluggableVendorOuiEntry_Object = MibTableRow
cwsXcvrPluggableVendorOuiEntry = _CwsXcvrPluggableVendorOuiEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 4, 1)
)
cwsXcvrPluggableVendorOuiEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrVendorIdTableSnmpKey"),
    (0, "CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableVendorOuiTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrPluggableVendorOuiEntry.setStatus("current")


class _CwsXcvrPluggableVendorOuiTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrPluggableVendorOuiTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrPluggableVendorOuiTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrPluggableVendorOuiTableSnmpKey_Object = MibTableColumn
cwsXcvrPluggableVendorOuiTableSnmpKey = _CwsXcvrPluggableVendorOuiTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 4, 1, 1),
    _CwsXcvrPluggableVendorOuiTableSnmpKey_Type()
)
cwsXcvrPluggableVendorOuiTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrPluggableVendorOuiTableSnmpKey.setStatus("current")
_CwsXcvrPluggableVendorOui_Type = Unsigned32
_CwsXcvrPluggableVendorOui_Object = MibTableColumn
cwsXcvrPluggableVendorOui = _CwsXcvrPluggableVendorOui_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 4, 1, 2),
    _CwsXcvrPluggableVendorOui_Type()
)
cwsXcvrPluggableVendorOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableVendorOui.setStatus("current")
_CwsXcvrAugXcvrPluggableDeviceIdTable_Object = MibTable
cwsXcvrAugXcvrPluggableDeviceIdTable = _CwsXcvrAugXcvrPluggableDeviceIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 5)
)
if mibBuilder.loadTexts:
    cwsXcvrAugXcvrPluggableDeviceIdTable.setStatus("current")
_CwsXcvrAugXcvrPluggableDeviceIdEntry_Object = MibTableRow
cwsXcvrAugXcvrPluggableDeviceIdEntry = _CwsXcvrAugXcvrPluggableDeviceIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 5, 1)
)
if mibBuilder.loadTexts:
    cwsXcvrAugXcvrPluggableDeviceIdEntry.setStatus("current")


class _CwsXcvrPluggableDeviceIdIdentifier_Type(Integer32):
    """Custom type cwsXcvrPluggableDeviceIdIdentifier based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              256)
        )
    )
    namedValues = NamedValues(
        *(("unknownorunspecified", 0),
          ("gbic", 1),
          ("moduleconnectorsolderedtomotherboard", 2),
          ("fpsfpplussfp", 3),
          ("xbi300pin", 4),
          ("xenpak", 5),
          ("xfp", 6),
          ("xff", 7),
          ("xfpe", 8),
          ("xpak", 9),
          ("x2", 10),
          ("wdmsfporsf", 11),
          ("qsfp", 12),
          ("qsfpplus", 13),
          ("cxp", 14),
          ("shieldedminimultilanehd4x", 15),
          ("qsfp28", 17),
          ("cxp2", 18),
          ("cdfpstyle1or2", 19),
          ("shieldedminimultilanehd4xfanout", 20),
          ("shieldedminimultilanehd8xfanout", 21),
          ("cdfpstyle3", 22),
          ("wavelogic3extreme", 256))
    )


_CwsXcvrPluggableDeviceIdIdentifier_Type.__name__ = "Integer32"
_CwsXcvrPluggableDeviceIdIdentifier_Object = MibTableColumn
cwsXcvrPluggableDeviceIdIdentifier = _CwsXcvrPluggableDeviceIdIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 5, 1, 1),
    _CwsXcvrPluggableDeviceIdIdentifier_Type()
)
cwsXcvrPluggableDeviceIdIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableDeviceIdIdentifier.setStatus("current")
_CwsXcvrPluggableDeviceIdIdentifierRaw_Type = StringMaxl32
_CwsXcvrPluggableDeviceIdIdentifierRaw_Object = MibTableColumn
cwsXcvrPluggableDeviceIdIdentifierRaw = _CwsXcvrPluggableDeviceIdIdentifierRaw_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 5, 1, 2),
    _CwsXcvrPluggableDeviceIdIdentifierRaw_Type()
)
cwsXcvrPluggableDeviceIdIdentifierRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableDeviceIdIdentifierRaw.setStatus("current")
_CwsXcvrPluggableDeviceIdExtendedIdentifierRaw_Type = StringMaxl32
_CwsXcvrPluggableDeviceIdExtendedIdentifierRaw_Object = MibTableColumn
cwsXcvrPluggableDeviceIdExtendedIdentifierRaw = _CwsXcvrPluggableDeviceIdExtendedIdentifierRaw_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 5, 1, 3),
    _CwsXcvrPluggableDeviceIdExtendedIdentifierRaw_Type()
)
cwsXcvrPluggableDeviceIdExtendedIdentifierRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableDeviceIdExtendedIdentifierRaw.setStatus("current")


class _CwsXcvrPluggableDeviceIdPowerConsumption_Type(Integer32):
    """Custom type cwsXcvrPluggableDeviceIdPowerConsumption based on Integer32"""
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
        *(("class1module15wmax", 0),
          ("class2module20wmax", 1),
          ("class3module25wmax", 2),
          ("class4module35wmax", 3))
    )


_CwsXcvrPluggableDeviceIdPowerConsumption_Type.__name__ = "Integer32"
_CwsXcvrPluggableDeviceIdPowerConsumption_Object = MibTableColumn
cwsXcvrPluggableDeviceIdPowerConsumption = _CwsXcvrPluggableDeviceIdPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 5, 1, 4),
    _CwsXcvrPluggableDeviceIdPowerConsumption_Type()
)
cwsXcvrPluggableDeviceIdPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableDeviceIdPowerConsumption.setStatus("current")
_CwsXcvrPluggableDeviceIdClei_Type = StringMaxl16
_CwsXcvrPluggableDeviceIdClei_Object = MibTableColumn
cwsXcvrPluggableDeviceIdClei = _CwsXcvrPluggableDeviceIdClei_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 5, 1, 5),
    _CwsXcvrPluggableDeviceIdClei_Type()
)
cwsXcvrPluggableDeviceIdClei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableDeviceIdClei.setStatus("current")
_CwsXcvrPluggableDeviceIdConnectorTypeRaw_Type = StringMaxl32
_CwsXcvrPluggableDeviceIdConnectorTypeRaw_Object = MibTableColumn
cwsXcvrPluggableDeviceIdConnectorTypeRaw = _CwsXcvrPluggableDeviceIdConnectorTypeRaw_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 5, 1, 6),
    _CwsXcvrPluggableDeviceIdConnectorTypeRaw_Type()
)
cwsXcvrPluggableDeviceIdConnectorTypeRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableDeviceIdConnectorTypeRaw.setStatus("current")
_CwsXcvrAugXcvrPluggableVendorTransmitterTable_Object = MibTable
cwsXcvrAugXcvrPluggableVendorTransmitterTable = _CwsXcvrAugXcvrPluggableVendorTransmitterTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 6)
)
if mibBuilder.loadTexts:
    cwsXcvrAugXcvrPluggableVendorTransmitterTable.setStatus("current")
_CwsXcvrAugXcvrPluggableVendorTransmitterEntry_Object = MibTableRow
cwsXcvrAugXcvrPluggableVendorTransmitterEntry = _CwsXcvrAugXcvrPluggableVendorTransmitterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 6, 1)
)
if mibBuilder.loadTexts:
    cwsXcvrAugXcvrPluggableVendorTransmitterEntry.setStatus("current")
_CwsXcvrPluggableVendorTransmitterWavelength_Type = Decimal2Dig
_CwsXcvrPluggableVendorTransmitterWavelength_Object = MibTableColumn
cwsXcvrPluggableVendorTransmitterWavelength = _CwsXcvrPluggableVendorTransmitterWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 6, 1, 1),
    _CwsXcvrPluggableVendorTransmitterWavelength_Type()
)
cwsXcvrPluggableVendorTransmitterWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableVendorTransmitterWavelength.setStatus("current")
_CwsXcvrPluggableVendorTransmitterWavelengthRaw_Type = StringMaxl32
_CwsXcvrPluggableVendorTransmitterWavelengthRaw_Object = MibTableColumn
cwsXcvrPluggableVendorTransmitterWavelengthRaw = _CwsXcvrPluggableVendorTransmitterWavelengthRaw_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 6, 1, 2),
    _CwsXcvrPluggableVendorTransmitterWavelengthRaw_Type()
)
cwsXcvrPluggableVendorTransmitterWavelengthRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableVendorTransmitterWavelengthRaw.setStatus("current")


class _CwsXcvrPluggableVendorTransmitterEncodingDescription_Type(Integer32):
    """Custom type cwsXcvrPluggableVendorTransmitterEncodingDescription based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 0),
          ("encoding8b10b", 1),
          ("encoding4b5b", 2),
          ("nrz", 3),
          ("sonetscrambled", 4),
          ("encoding64b66b", 5),
          ("manchester", 6),
          ("encoding256b257b", 7))
    )


_CwsXcvrPluggableVendorTransmitterEncodingDescription_Type.__name__ = "Integer32"
_CwsXcvrPluggableVendorTransmitterEncodingDescription_Object = MibTableColumn
cwsXcvrPluggableVendorTransmitterEncodingDescription = _CwsXcvrPluggableVendorTransmitterEncodingDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 6, 1, 3),
    _CwsXcvrPluggableVendorTransmitterEncodingDescription_Type()
)
cwsXcvrPluggableVendorTransmitterEncodingDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableVendorTransmitterEncodingDescription.setStatus("current")
_CwsXcvrPluggableVendorTransmitterEncodingRaw_Type = StringMaxl32
_CwsXcvrPluggableVendorTransmitterEncodingRaw_Object = MibTableColumn
cwsXcvrPluggableVendorTransmitterEncodingRaw = _CwsXcvrPluggableVendorTransmitterEncodingRaw_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 6, 1, 4),
    _CwsXcvrPluggableVendorTransmitterEncodingRaw_Type()
)
cwsXcvrPluggableVendorTransmitterEncodingRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableVendorTransmitterEncodingRaw.setStatus("current")
_CwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringTable_Object = MibTable
cwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringTable = _CwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 7)
)
if mibBuilder.loadTexts:
    cwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringTable.setStatus("current")
_CwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringEntry_Object = MibTableRow
cwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringEntry = _CwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 7, 1)
)
if mibBuilder.loadTexts:
    cwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringEntry.setStatus("current")
_CwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringTypeRaw_Type = StringMaxl32
_CwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringTypeRaw_Object = MibTableColumn
cwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringTypeRaw = _CwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringTypeRaw_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 7, 1, 1),
    _CwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringTypeRaw_Type()
)
cwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringTypeRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringTypeRaw.setStatus("current")
_CwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringImplemented_Type = TruthValue
_CwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringImplemented_Object = MibTableColumn
cwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringImplemented = _CwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringImplemented_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 7, 1, 2),
    _CwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringImplemented_Type()
)
cwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringImplemented.setStatus("current")
_CwsXcvrPluggableTransceiverCodeTable_Object = MibTable
cwsXcvrPluggableTransceiverCodeTable = _CwsXcvrPluggableTransceiverCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 8)
)
if mibBuilder.loadTexts:
    cwsXcvrPluggableTransceiverCodeTable.setStatus("current")
_CwsXcvrPluggableTransceiverCodeEntry_Object = MibTableRow
cwsXcvrPluggableTransceiverCodeEntry = _CwsXcvrPluggableTransceiverCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 8, 1)
)
cwsXcvrPluggableTransceiverCodeEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableTransceiverCodeTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrPluggableTransceiverCodeEntry.setStatus("current")


class _CwsXcvrPluggableTransceiverCodeTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrPluggableTransceiverCodeTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrPluggableTransceiverCodeTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrPluggableTransceiverCodeTableSnmpKey_Object = MibTableColumn
cwsXcvrPluggableTransceiverCodeTableSnmpKey = _CwsXcvrPluggableTransceiverCodeTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 8, 1, 1),
    _CwsXcvrPluggableTransceiverCodeTableSnmpKey_Type()
)
cwsXcvrPluggableTransceiverCodeTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrPluggableTransceiverCodeTableSnmpKey.setStatus("current")


class _CwsXcvrPluggableTransceiverCodeSpecificationCompliance_Type(Bits):
    """Custom type cwsXcvrPluggableTransceiverCodeSpecificationCompliance based on Bits"""
    namedValues = NamedValues(
        *(("speccompliance40gactivecablexlppi", 0),
          ("speccompliance40gbaselr4", 1),
          ("speccompliance40gbasesr4", 2),
          ("speccompliance40gbasecr4", 3),
          ("speccompliance10gbasesr", 4),
          ("speccompliance10gbaselr", 5),
          ("speccompliance10gbaselrm", 6),
          ("extendedspeccompliance100gactiveopticalcable", 8),
          ("extendedspeccompliance100gbasesr4", 9),
          ("extendedspeccompliance100gbaselr4", 10),
          ("extendedspeccompliance100gbaseer4", 11),
          ("extendedspeccompliance100gbasesr10", 12),
          ("extendedspeccompliance100gcwdm4msawithfec", 13),
          ("extendedspeccompliance100gpsm4parallelsmf", 14),
          ("extendedspeccompliance100gactivecoppercable", 15),
          ("extendedspeccompliance100gcwdmmsawithoutfec", 16),
          ("extendedspeccompliance100gbasecr4", 18),
          ("extendedspeccompliance40gbaseer4", 23),
          ("extendedspeccompliance4x10gbasesr", 24),
          ("extendedspeccompliance40gpsm4parallelsmf", 25),
          ("extendedspeccomplianceg9591p1i12d1", 26),
          ("extendedspeccomplianceg9591p1s12d2", 27),
          ("extendedspeccomplianceg9591p1l12d2", 28),
          ("extspeccode10gbasetwithsfi", 29),
          ("unknown", 30))
    )

_CwsXcvrPluggableTransceiverCodeSpecificationCompliance_Type.__name__ = "Bits"
_CwsXcvrPluggableTransceiverCodeSpecificationCompliance_Object = MibTableColumn
cwsXcvrPluggableTransceiverCodeSpecificationCompliance = _CwsXcvrPluggableTransceiverCodeSpecificationCompliance_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 8, 1, 2),
    _CwsXcvrPluggableTransceiverCodeSpecificationCompliance_Type()
)
cwsXcvrPluggableTransceiverCodeSpecificationCompliance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsXcvrPluggableTransceiverCodeSpecificationCompliance.setStatus("current")
_CwsXcvrPluggableTransceiverCodeTransceiverCodeRaw_Type = StringMaxl32
_CwsXcvrPluggableTransceiverCodeTransceiverCodeRaw_Object = MibTableColumn
cwsXcvrPluggableTransceiverCodeTransceiverCodeRaw = _CwsXcvrPluggableTransceiverCodeTransceiverCodeRaw_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 8, 1, 3),
    _CwsXcvrPluggableTransceiverCodeTransceiverCodeRaw_Type()
)
cwsXcvrPluggableTransceiverCodeTransceiverCodeRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableTransceiverCodeTransceiverCodeRaw.setStatus("current")
_CwsXcvrPluggableDeviceTechnologyTable_Object = MibTable
cwsXcvrPluggableDeviceTechnologyTable = _CwsXcvrPluggableDeviceTechnologyTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 9)
)
if mibBuilder.loadTexts:
    cwsXcvrPluggableDeviceTechnologyTable.setStatus("current")
_CwsXcvrPluggableDeviceTechnologyEntry_Object = MibTableRow
cwsXcvrPluggableDeviceTechnologyEntry = _CwsXcvrPluggableDeviceTechnologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 9, 1)
)
cwsXcvrPluggableDeviceTechnologyEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableDeviceTechnologyTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrPluggableDeviceTechnologyEntry.setStatus("current")


class _CwsXcvrPluggableDeviceTechnologyTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrPluggableDeviceTechnologyTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrPluggableDeviceTechnologyTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrPluggableDeviceTechnologyTableSnmpKey_Object = MibTableColumn
cwsXcvrPluggableDeviceTechnologyTableSnmpKey = _CwsXcvrPluggableDeviceTechnologyTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 9, 1, 1),
    _CwsXcvrPluggableDeviceTechnologyTableSnmpKey_Type()
)
cwsXcvrPluggableDeviceTechnologyTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrPluggableDeviceTechnologyTableSnmpKey.setStatus("current")
_CwsXcvrPluggableDeviceTechnologyDeviceTechnologyRaw_Type = StringMaxl32
_CwsXcvrPluggableDeviceTechnologyDeviceTechnologyRaw_Object = MibTableColumn
cwsXcvrPluggableDeviceTechnologyDeviceTechnologyRaw = _CwsXcvrPluggableDeviceTechnologyDeviceTechnologyRaw_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 9, 1, 2),
    _CwsXcvrPluggableDeviceTechnologyDeviceTechnologyRaw_Type()
)
cwsXcvrPluggableDeviceTechnologyDeviceTechnologyRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableDeviceTechnologyDeviceTechnologyRaw.setStatus("current")
_CwsXcvrPluggableDeviceTechnologyTransmitterTunable_Type = TruthValue
_CwsXcvrPluggableDeviceTechnologyTransmitterTunable_Object = MibTableColumn
cwsXcvrPluggableDeviceTechnologyTransmitterTunable = _CwsXcvrPluggableDeviceTechnologyTransmitterTunable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 9, 1, 3),
    _CwsXcvrPluggableDeviceTechnologyTransmitterTunable_Type()
)
cwsXcvrPluggableDeviceTechnologyTransmitterTunable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableDeviceTechnologyTransmitterTunable.setStatus("current")
_CwsXcvrPluggableDeviceTechnologyMaxCaseTemperature_Type = Unsigned32
_CwsXcvrPluggableDeviceTechnologyMaxCaseTemperature_Object = MibTableColumn
cwsXcvrPluggableDeviceTechnologyMaxCaseTemperature = _CwsXcvrPluggableDeviceTechnologyMaxCaseTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 9, 1, 4),
    _CwsXcvrPluggableDeviceTechnologyMaxCaseTemperature_Type()
)
cwsXcvrPluggableDeviceTechnologyMaxCaseTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableDeviceTechnologyMaxCaseTemperature.setStatus("current")
_CwsXcvrPluggableOptionsTable_Object = MibTable
cwsXcvrPluggableOptionsTable = _CwsXcvrPluggableOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 10)
)
if mibBuilder.loadTexts:
    cwsXcvrPluggableOptionsTable.setStatus("current")
_CwsXcvrPluggableOptionsEntry_Object = MibTableRow
cwsXcvrPluggableOptionsEntry = _CwsXcvrPluggableOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 10, 1)
)
cwsXcvrPluggableOptionsEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableOptionsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrPluggableOptionsEntry.setStatus("current")


class _CwsXcvrPluggableOptionsTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrPluggableOptionsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrPluggableOptionsTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrPluggableOptionsTableSnmpKey_Object = MibTableColumn
cwsXcvrPluggableOptionsTableSnmpKey = _CwsXcvrPluggableOptionsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 10, 1, 1),
    _CwsXcvrPluggableOptionsTableSnmpKey_Type()
)
cwsXcvrPluggableOptionsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrPluggableOptionsTableSnmpKey.setStatus("current")
_CwsXcvrPluggableOptionsOptionsRaw_Type = StringMaxl32
_CwsXcvrPluggableOptionsOptionsRaw_Object = MibTableColumn
cwsXcvrPluggableOptionsOptionsRaw = _CwsXcvrPluggableOptionsOptionsRaw_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 10, 1, 2),
    _CwsXcvrPluggableOptionsOptionsRaw_Type()
)
cwsXcvrPluggableOptionsOptionsRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableOptionsOptionsRaw.setStatus("current")
_CwsXcvrPluggableOptionsTxinpeqautoadaptcapable_Type = TruthValue
_CwsXcvrPluggableOptionsTxinpeqautoadaptcapable_Object = MibTableColumn
cwsXcvrPluggableOptionsTxinpeqautoadaptcapable = _CwsXcvrPluggableOptionsTxinpeqautoadaptcapable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 10, 1, 3),
    _CwsXcvrPluggableOptionsTxinpeqautoadaptcapable_Type()
)
cwsXcvrPluggableOptionsTxinpeqautoadaptcapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableOptionsTxinpeqautoadaptcapable.setStatus("current")
_CwsXcvrPluggableOptionsTxinpeqfixedprogramsetting_Type = TruthValue
_CwsXcvrPluggableOptionsTxinpeqfixedprogramsetting_Object = MibTableColumn
cwsXcvrPluggableOptionsTxinpeqfixedprogramsetting = _CwsXcvrPluggableOptionsTxinpeqfixedprogramsetting_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 10, 1, 4),
    _CwsXcvrPluggableOptionsTxinpeqfixedprogramsetting_Type()
)
cwsXcvrPluggableOptionsTxinpeqfixedprogramsetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableOptionsTxinpeqfixedprogramsetting.setStatus("current")
_CwsXcvrPluggableOptionsRxoutemfixedprogramsetting_Type = TruthValue
_CwsXcvrPluggableOptionsRxoutemfixedprogramsetting_Object = MibTableColumn
cwsXcvrPluggableOptionsRxoutemfixedprogramsetting = _CwsXcvrPluggableOptionsRxoutemfixedprogramsetting_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 10, 1, 5),
    _CwsXcvrPluggableOptionsRxoutemfixedprogramsetting_Type()
)
cwsXcvrPluggableOptionsRxoutemfixedprogramsetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableOptionsRxoutemfixedprogramsetting.setStatus("current")
_CwsXcvrPluggableOptionsRxoutamfixedprogramsetting_Type = TruthValue
_CwsXcvrPluggableOptionsRxoutamfixedprogramsetting_Object = MibTableColumn
cwsXcvrPluggableOptionsRxoutamfixedprogramsetting = _CwsXcvrPluggableOptionsRxoutamfixedprogramsetting_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 10, 1, 6),
    _CwsXcvrPluggableOptionsRxoutamfixedprogramsetting_Type()
)
cwsXcvrPluggableOptionsRxoutamfixedprogramsetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableOptionsRxoutamfixedprogramsetting.setStatus("current")
_CwsXcvrPluggableOptionsTxCdrLossOfLockFlag_Type = TruthValue
_CwsXcvrPluggableOptionsTxCdrLossOfLockFlag_Object = MibTableColumn
cwsXcvrPluggableOptionsTxCdrLossOfLockFlag = _CwsXcvrPluggableOptionsTxCdrLossOfLockFlag_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 10, 1, 7),
    _CwsXcvrPluggableOptionsTxCdrLossOfLockFlag_Type()
)
cwsXcvrPluggableOptionsTxCdrLossOfLockFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableOptionsTxCdrLossOfLockFlag.setStatus("current")
_CwsXcvrPluggableOptionsRxCdrLossOfLockFlag_Type = TruthValue
_CwsXcvrPluggableOptionsRxCdrLossOfLockFlag_Object = MibTableColumn
cwsXcvrPluggableOptionsRxCdrLossOfLockFlag = _CwsXcvrPluggableOptionsRxCdrLossOfLockFlag_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 10, 1, 8),
    _CwsXcvrPluggableOptionsRxCdrLossOfLockFlag_Type()
)
cwsXcvrPluggableOptionsRxCdrLossOfLockFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableOptionsRxCdrLossOfLockFlag.setStatus("current")
_CwsXcvrPluggableOptionsUserEepromPage02hProvided_Type = TruthValue
_CwsXcvrPluggableOptionsUserEepromPage02hProvided_Object = MibTableColumn
cwsXcvrPluggableOptionsUserEepromPage02hProvided = _CwsXcvrPluggableOptionsUserEepromPage02hProvided_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 10, 1, 9),
    _CwsXcvrPluggableOptionsUserEepromPage02hProvided_Type()
)
cwsXcvrPluggableOptionsUserEepromPage02hProvided.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableOptionsUserEepromPage02hProvided.setStatus("current")
_CwsXcvrPluggableOptionsAstPage01hProvided_Type = TruthValue
_CwsXcvrPluggableOptionsAstPage01hProvided_Object = MibTableColumn
cwsXcvrPluggableOptionsAstPage01hProvided = _CwsXcvrPluggableOptionsAstPage01hProvided_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 10, 1, 10),
    _CwsXcvrPluggableOptionsAstPage01hProvided_Type()
)
cwsXcvrPluggableOptionsAstPage01hProvided.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableOptionsAstPage01hProvided.setStatus("current")
_CwsXcvrPluggableSupplyVoltageTable_Object = MibTable
cwsXcvrPluggableSupplyVoltageTable = _CwsXcvrPluggableSupplyVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 11)
)
if mibBuilder.loadTexts:
    cwsXcvrPluggableSupplyVoltageTable.setStatus("current")
_CwsXcvrPluggableSupplyVoltageEntry_Object = MibTableRow
cwsXcvrPluggableSupplyVoltageEntry = _CwsXcvrPluggableSupplyVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 11, 1)
)
cwsXcvrPluggableSupplyVoltageEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableSupplyVoltageTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrPluggableSupplyVoltageEntry.setStatus("current")


class _CwsXcvrPluggableSupplyVoltageTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrPluggableSupplyVoltageTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrPluggableSupplyVoltageTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrPluggableSupplyVoltageTableSnmpKey_Object = MibTableColumn
cwsXcvrPluggableSupplyVoltageTableSnmpKey = _CwsXcvrPluggableSupplyVoltageTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 11, 1, 1),
    _CwsXcvrPluggableSupplyVoltageTableSnmpKey_Type()
)
cwsXcvrPluggableSupplyVoltageTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrPluggableSupplyVoltageTableSnmpKey.setStatus("current")
_CwsXcvrPluggableSupplyVoltageActual_Type = Decimal2Dig
_CwsXcvrPluggableSupplyVoltageActual_Object = MibTableColumn
cwsXcvrPluggableSupplyVoltageActual = _CwsXcvrPluggableSupplyVoltageActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 11, 1, 2),
    _CwsXcvrPluggableSupplyVoltageActual_Type()
)
cwsXcvrPluggableSupplyVoltageActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableSupplyVoltageActual.setStatus("current")
_CwsXcvrPluggableStatusTable_Object = MibTable
cwsXcvrPluggableStatusTable = _CwsXcvrPluggableStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 12)
)
if mibBuilder.loadTexts:
    cwsXcvrPluggableStatusTable.setStatus("current")
_CwsXcvrPluggableStatusEntry_Object = MibTableRow
cwsXcvrPluggableStatusEntry = _CwsXcvrPluggableStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 12, 1)
)
cwsXcvrPluggableStatusEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableStatusTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrPluggableStatusEntry.setStatus("current")


class _CwsXcvrPluggableStatusTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrPluggableStatusTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrPluggableStatusTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrPluggableStatusTableSnmpKey_Object = MibTableColumn
cwsXcvrPluggableStatusTableSnmpKey = _CwsXcvrPluggableStatusTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 12, 1, 1),
    _CwsXcvrPluggableStatusTableSnmpKey_Type()
)
cwsXcvrPluggableStatusTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrPluggableStatusTableSnmpKey.setStatus("current")
_CwsXcvrStatusHighAlarmStatus_Type = TruthValue
_CwsXcvrStatusHighAlarmStatus_Object = MibTableColumn
cwsXcvrStatusHighAlarmStatus = _CwsXcvrStatusHighAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 12, 1, 2),
    _CwsXcvrStatusHighAlarmStatus_Type()
)
cwsXcvrStatusHighAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrStatusHighAlarmStatus.setStatus("current")
_CwsXcvrStatusLowAlarmStatus_Type = TruthValue
_CwsXcvrStatusLowAlarmStatus_Object = MibTableColumn
cwsXcvrStatusLowAlarmStatus = _CwsXcvrStatusLowAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 12, 1, 3),
    _CwsXcvrStatusLowAlarmStatus_Type()
)
cwsXcvrStatusLowAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrStatusLowAlarmStatus.setStatus("current")
_CwsXcvrStatusHighWarningStatus_Type = TruthValue
_CwsXcvrStatusHighWarningStatus_Object = MibTableColumn
cwsXcvrStatusHighWarningStatus = _CwsXcvrStatusHighWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 12, 1, 4),
    _CwsXcvrStatusHighWarningStatus_Type()
)
cwsXcvrStatusHighWarningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrStatusHighWarningStatus.setStatus("current")
_CwsXcvrStatusLowWarningStatus_Type = TruthValue
_CwsXcvrStatusLowWarningStatus_Object = MibTableColumn
cwsXcvrStatusLowWarningStatus = _CwsXcvrStatusLowWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 12, 1, 5),
    _CwsXcvrStatusLowWarningStatus_Type()
)
cwsXcvrStatusLowWarningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrStatusLowWarningStatus.setStatus("current")
_CwsXcvrPluggableThresholdTable_Object = MibTable
cwsXcvrPluggableThresholdTable = _CwsXcvrPluggableThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 13)
)
if mibBuilder.loadTexts:
    cwsXcvrPluggableThresholdTable.setStatus("current")
_CwsXcvrPluggableThresholdEntry_Object = MibTableRow
cwsXcvrPluggableThresholdEntry = _CwsXcvrPluggableThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 13, 1)
)
cwsXcvrPluggableThresholdEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableThresholdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrPluggableThresholdEntry.setStatus("current")


class _CwsXcvrPluggableThresholdTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrPluggableThresholdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrPluggableThresholdTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrPluggableThresholdTableSnmpKey_Object = MibTableColumn
cwsXcvrPluggableThresholdTableSnmpKey = _CwsXcvrPluggableThresholdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 13, 1, 1),
    _CwsXcvrPluggableThresholdTableSnmpKey_Type()
)
cwsXcvrPluggableThresholdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrPluggableThresholdTableSnmpKey.setStatus("current")
_CwsXcvrThresholdHighAlarmThreshold_Type = Decimal2Dig
_CwsXcvrThresholdHighAlarmThreshold_Object = MibTableColumn
cwsXcvrThresholdHighAlarmThreshold = _CwsXcvrThresholdHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 13, 1, 2),
    _CwsXcvrThresholdHighAlarmThreshold_Type()
)
cwsXcvrThresholdHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrThresholdHighAlarmThreshold.setStatus("current")
_CwsXcvrThresholdLowAlarmThreshold_Type = Decimal2Dig
_CwsXcvrThresholdLowAlarmThreshold_Object = MibTableColumn
cwsXcvrThresholdLowAlarmThreshold = _CwsXcvrThresholdLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 13, 1, 3),
    _CwsXcvrThresholdLowAlarmThreshold_Type()
)
cwsXcvrThresholdLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrThresholdLowAlarmThreshold.setStatus("current")
_CwsXcvrThresholdHighWarningThreshold_Type = Decimal2Dig
_CwsXcvrThresholdHighWarningThreshold_Object = MibTableColumn
cwsXcvrThresholdHighWarningThreshold = _CwsXcvrThresholdHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 13, 1, 4),
    _CwsXcvrThresholdHighWarningThreshold_Type()
)
cwsXcvrThresholdHighWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrThresholdHighWarningThreshold.setStatus("current")
_CwsXcvrThresholdLowWarningThreshold_Type = Decimal2Dig
_CwsXcvrThresholdLowWarningThreshold_Object = MibTableColumn
cwsXcvrThresholdLowWarningThreshold = _CwsXcvrThresholdLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 13, 1, 5),
    _CwsXcvrThresholdLowWarningThreshold_Type()
)
cwsXcvrThresholdLowWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrThresholdLowWarningThreshold.setStatus("current")
_CwsXcvrAugXcvrPluggableChannelDiagnosticsTable_Object = MibTable
cwsXcvrAugXcvrPluggableChannelDiagnosticsTable = _CwsXcvrAugXcvrPluggableChannelDiagnosticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 14)
)
if mibBuilder.loadTexts:
    cwsXcvrAugXcvrPluggableChannelDiagnosticsTable.setStatus("current")
_CwsXcvrAugXcvrPluggableChannelDiagnosticsEntry_Object = MibTableRow
cwsXcvrAugXcvrPluggableChannelDiagnosticsEntry = _CwsXcvrAugXcvrPluggableChannelDiagnosticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 14, 1)
)
if mibBuilder.loadTexts:
    cwsXcvrAugXcvrPluggableChannelDiagnosticsEntry.setStatus("current")
_CwsXcvrPluggableChannelDiagnosticsTransmitterFault_Type = TruthValue
_CwsXcvrPluggableChannelDiagnosticsTransmitterFault_Object = MibTableColumn
cwsXcvrPluggableChannelDiagnosticsTransmitterFault = _CwsXcvrPluggableChannelDiagnosticsTransmitterFault_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 14, 1, 1),
    _CwsXcvrPluggableChannelDiagnosticsTransmitterFault_Type()
)
cwsXcvrPluggableChannelDiagnosticsTransmitterFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableChannelDiagnosticsTransmitterFault.setStatus("current")
_CwsXcvrPluggableChannelDiagnosticsTxAdaptiveEqFault_Type = TruthValue
_CwsXcvrPluggableChannelDiagnosticsTxAdaptiveEqFault_Object = MibTableColumn
cwsXcvrPluggableChannelDiagnosticsTxAdaptiveEqFault = _CwsXcvrPluggableChannelDiagnosticsTxAdaptiveEqFault_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 14, 1, 2),
    _CwsXcvrPluggableChannelDiagnosticsTxAdaptiveEqFault_Type()
)
cwsXcvrPluggableChannelDiagnosticsTxAdaptiveEqFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsXcvrPluggableChannelDiagnosticsTxAdaptiveEqFault.setStatus("current")
_CwsXcvrPluggableSerdesConfigTable_Object = MibTable
cwsXcvrPluggableSerdesConfigTable = _CwsXcvrPluggableSerdesConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 15)
)
if mibBuilder.loadTexts:
    cwsXcvrPluggableSerdesConfigTable.setStatus("current")
_CwsXcvrPluggableSerdesConfigEntry_Object = MibTableRow
cwsXcvrPluggableSerdesConfigEntry = _CwsXcvrPluggableSerdesConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 15, 1)
)
cwsXcvrPluggableSerdesConfigEntry.setIndexNames(
    (0, "CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrXcvrsXcvrIndex"),
    (0, "CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableSerdesConfigTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsXcvrPluggableSerdesConfigEntry.setStatus("current")


class _CwsXcvrPluggableSerdesConfigTableSnmpKey_Type(Integer32):
    """Custom type cwsXcvrPluggableSerdesConfigTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsXcvrPluggableSerdesConfigTableSnmpKey_Type.__name__ = "Integer32"
_CwsXcvrPluggableSerdesConfigTableSnmpKey_Object = MibTableColumn
cwsXcvrPluggableSerdesConfigTableSnmpKey = _CwsXcvrPluggableSerdesConfigTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 15, 1, 1),
    _CwsXcvrPluggableSerdesConfigTableSnmpKey_Type()
)
cwsXcvrPluggableSerdesConfigTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsXcvrPluggableSerdesConfigTableSnmpKey.setStatus("current")
_CwsXcvrSerdesConfigSerdesTxEq_Type = XcvrSerdesTxEq
_CwsXcvrSerdesConfigSerdesTxEq_Object = MibTableColumn
cwsXcvrSerdesConfigSerdesTxEq = _CwsXcvrSerdesConfigSerdesTxEq_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 15, 1, 2),
    _CwsXcvrSerdesConfigSerdesTxEq_Type()
)
cwsXcvrSerdesConfigSerdesTxEq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsXcvrSerdesConfigSerdesTxEq.setStatus("current")
_CwsXcvrSerdesConfigSerdesRxAmplitude_Type = XcvrSerdesRxAmplitude
_CwsXcvrSerdesConfigSerdesRxAmplitude_Object = MibTableColumn
cwsXcvrSerdesConfigSerdesRxAmplitude = _CwsXcvrSerdesConfigSerdesRxAmplitude_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 15, 1, 3),
    _CwsXcvrSerdesConfigSerdesRxAmplitude_Type()
)
cwsXcvrSerdesConfigSerdesRxAmplitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsXcvrSerdesConfigSerdesRxAmplitude.setStatus("current")
_CwsXcvrSerdesConfigSerdesRxEmphasis_Type = XcvrSerdesRxEmphasis
_CwsXcvrSerdesConfigSerdesRxEmphasis_Object = MibTableColumn
cwsXcvrSerdesConfigSerdesRxEmphasis = _CwsXcvrSerdesConfigSerdesRxEmphasis_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 15, 1, 4),
    _CwsXcvrSerdesConfigSerdesRxEmphasis_Type()
)
cwsXcvrSerdesConfigSerdesRxEmphasis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsXcvrSerdesConfigSerdesRxEmphasis.setStatus("current")
cwsXcvrVendorIdEntry.registerAugmentions(
    ("CIENA-WS-XCVR-PLUGGABLE-MIB",
     "cwsXcvrAugXcvrPluggableVendorIdEntry")
)
cwsXcvrAugXcvrPluggableVendorIdEntry.setIndexNames(*cwsXcvrVendorIdEntry.getIndexNames())
cwsXcvrDeviceIdEntry.registerAugmentions(
    ("CIENA-WS-XCVR-PLUGGABLE-MIB",
     "cwsXcvrAugXcvrPluggableDeviceIdEntry")
)
cwsXcvrAugXcvrPluggableDeviceIdEntry.setIndexNames(*cwsXcvrDeviceIdEntry.getIndexNames())
cwsXcvrVendorTransmitterEntry.registerAugmentions(
    ("CIENA-WS-XCVR-PLUGGABLE-MIB",
     "cwsXcvrAugXcvrPluggableVendorTransmitterEntry")
)
cwsXcvrAugXcvrPluggableVendorTransmitterEntry.setIndexNames(*cwsXcvrVendorTransmitterEntry.getIndexNames())
cwsXcvrVendorDiagnosticMonitoringEntry.registerAugmentions(
    ("CIENA-WS-XCVR-PLUGGABLE-MIB",
     "cwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringEntry")
)
cwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringEntry.setIndexNames(*cwsXcvrVendorDiagnosticMonitoringEntry.getIndexNames())
cwsXcvrChannelDiagnosticsEntry.registerAugmentions(
    ("CIENA-WS-XCVR-PLUGGABLE-MIB",
     "cwsXcvrAugXcvrPluggableChannelDiagnosticsEntry")
)
cwsXcvrAugXcvrPluggableChannelDiagnosticsEntry.setIndexNames(*cwsXcvrChannelDiagnosticsEntry.getIndexNames())

# Managed Objects groups

cienaWsXcvrPluggableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 2, 1, 1)
)
cienaWsXcvrPluggableGroup.setObjects(
      *(("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableVendorIdRevisionCompliance"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableDeviceIdIdentifier"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableDeviceIdIdentifierRaw"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableDeviceIdExtendedIdentifierRaw"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableDeviceIdPowerConsumption"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableDeviceIdClei"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableDeviceIdConnectorTypeRaw"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableVendorTransmitterWavelength"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableVendorTransmitterWavelengthRaw"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableVendorTransmitterEncodingDescription"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableVendorTransmitterEncodingRaw"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringTypeRaw"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringImplemented"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableTransceiverCodeSpecificationCompliance"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableTransceiverCodeTransceiverCodeRaw"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableDeviceTechnologyDeviceTechnologyRaw"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableDeviceTechnologyTransmitterTunable"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableDeviceTechnologyMaxCaseTemperature"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableOptionsOptionsRaw"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableOptionsTxinpeqautoadaptcapable"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableOptionsTxinpeqfixedprogramsetting"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableOptionsRxoutemfixedprogramsetting"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableOptionsRxoutamfixedprogramsetting"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableOptionsTxCdrLossOfLockFlag"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableOptionsRxCdrLossOfLockFlag"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableOptionsUserEepromPage02hProvided"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableOptionsAstPage01hProvided"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableSupplyVoltageActual"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrStatusHighAlarmStatus"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrStatusLowAlarmStatus"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrStatusHighWarningStatus"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrStatusLowWarningStatus"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrThresholdHighAlarmThreshold"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrThresholdLowAlarmThreshold"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrThresholdHighWarningThreshold"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrThresholdLowWarningThreshold"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableChannelDiagnosticsTransmitterFault"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrPluggableChannelDiagnosticsTxAdaptiveEqFault"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrSerdesConfigSerdesTxEq"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrSerdesConfigSerdesRxAmplitude"),
        ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cwsXcvrSerdesConfigSerdesRxEmphasis"))
)
if mibBuilder.loadTexts:
    cienaWsXcvrPluggableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cienaWsXcvrPluggableCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 17, 2, 2, 1)
)
cienaWsXcvrPluggableCompliance.setObjects(
    ("CIENA-WS-XCVR-PLUGGABLE-MIB", "cienaWsXcvrPluggableGroup")
)
if mibBuilder.loadTexts:
    cienaWsXcvrPluggableCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-XCVR-PLUGGABLE-MIB",
    **{"cienaWsXcvrPluggableMIB": cienaWsXcvrPluggableMIB,
       "cienaWsXcvrPluggableObjects": cienaWsXcvrPluggableObjects,
       "cienaWsXcvrPluggableConformance": cienaWsXcvrPluggableConformance,
       "cienaWsXcvrPluggableGroups": cienaWsXcvrPluggableGroups,
       "cienaWsXcvrPluggableGroup": cienaWsXcvrPluggableGroup,
       "cienaWsXcvrPluggableCompliances": cienaWsXcvrPluggableCompliances,
       "cienaWsXcvrPluggableCompliance": cienaWsXcvrPluggableCompliance,
       "cwsXcvrAugXcvrPluggableVendorIdTable": cwsXcvrAugXcvrPluggableVendorIdTable,
       "cwsXcvrAugXcvrPluggableVendorIdEntry": cwsXcvrAugXcvrPluggableVendorIdEntry,
       "cwsXcvrPluggableVendorIdRevisionCompliance": cwsXcvrPluggableVendorIdRevisionCompliance,
       "cwsXcvrPluggableVendorOuiTable": cwsXcvrPluggableVendorOuiTable,
       "cwsXcvrPluggableVendorOuiEntry": cwsXcvrPluggableVendorOuiEntry,
       "cwsXcvrPluggableVendorOuiTableSnmpKey": cwsXcvrPluggableVendorOuiTableSnmpKey,
       "cwsXcvrPluggableVendorOui": cwsXcvrPluggableVendorOui,
       "cwsXcvrAugXcvrPluggableDeviceIdTable": cwsXcvrAugXcvrPluggableDeviceIdTable,
       "cwsXcvrAugXcvrPluggableDeviceIdEntry": cwsXcvrAugXcvrPluggableDeviceIdEntry,
       "cwsXcvrPluggableDeviceIdIdentifier": cwsXcvrPluggableDeviceIdIdentifier,
       "cwsXcvrPluggableDeviceIdIdentifierRaw": cwsXcvrPluggableDeviceIdIdentifierRaw,
       "cwsXcvrPluggableDeviceIdExtendedIdentifierRaw": cwsXcvrPluggableDeviceIdExtendedIdentifierRaw,
       "cwsXcvrPluggableDeviceIdPowerConsumption": cwsXcvrPluggableDeviceIdPowerConsumption,
       "cwsXcvrPluggableDeviceIdClei": cwsXcvrPluggableDeviceIdClei,
       "cwsXcvrPluggableDeviceIdConnectorTypeRaw": cwsXcvrPluggableDeviceIdConnectorTypeRaw,
       "cwsXcvrAugXcvrPluggableVendorTransmitterTable": cwsXcvrAugXcvrPluggableVendorTransmitterTable,
       "cwsXcvrAugXcvrPluggableVendorTransmitterEntry": cwsXcvrAugXcvrPluggableVendorTransmitterEntry,
       "cwsXcvrPluggableVendorTransmitterWavelength": cwsXcvrPluggableVendorTransmitterWavelength,
       "cwsXcvrPluggableVendorTransmitterWavelengthRaw": cwsXcvrPluggableVendorTransmitterWavelengthRaw,
       "cwsXcvrPluggableVendorTransmitterEncodingDescription": cwsXcvrPluggableVendorTransmitterEncodingDescription,
       "cwsXcvrPluggableVendorTransmitterEncodingRaw": cwsXcvrPluggableVendorTransmitterEncodingRaw,
       "cwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringTable": cwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringTable,
       "cwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringEntry": cwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringEntry,
       "cwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringTypeRaw": cwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringTypeRaw,
       "cwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringImplemented": cwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringImplemented,
       "cwsXcvrPluggableTransceiverCodeTable": cwsXcvrPluggableTransceiverCodeTable,
       "cwsXcvrPluggableTransceiverCodeEntry": cwsXcvrPluggableTransceiverCodeEntry,
       "cwsXcvrPluggableTransceiverCodeTableSnmpKey": cwsXcvrPluggableTransceiverCodeTableSnmpKey,
       "cwsXcvrPluggableTransceiverCodeSpecificationCompliance": cwsXcvrPluggableTransceiverCodeSpecificationCompliance,
       "cwsXcvrPluggableTransceiverCodeTransceiverCodeRaw": cwsXcvrPluggableTransceiverCodeTransceiverCodeRaw,
       "cwsXcvrPluggableDeviceTechnologyTable": cwsXcvrPluggableDeviceTechnologyTable,
       "cwsXcvrPluggableDeviceTechnologyEntry": cwsXcvrPluggableDeviceTechnologyEntry,
       "cwsXcvrPluggableDeviceTechnologyTableSnmpKey": cwsXcvrPluggableDeviceTechnologyTableSnmpKey,
       "cwsXcvrPluggableDeviceTechnologyDeviceTechnologyRaw": cwsXcvrPluggableDeviceTechnologyDeviceTechnologyRaw,
       "cwsXcvrPluggableDeviceTechnologyTransmitterTunable": cwsXcvrPluggableDeviceTechnologyTransmitterTunable,
       "cwsXcvrPluggableDeviceTechnologyMaxCaseTemperature": cwsXcvrPluggableDeviceTechnologyMaxCaseTemperature,
       "cwsXcvrPluggableOptionsTable": cwsXcvrPluggableOptionsTable,
       "cwsXcvrPluggableOptionsEntry": cwsXcvrPluggableOptionsEntry,
       "cwsXcvrPluggableOptionsTableSnmpKey": cwsXcvrPluggableOptionsTableSnmpKey,
       "cwsXcvrPluggableOptionsOptionsRaw": cwsXcvrPluggableOptionsOptionsRaw,
       "cwsXcvrPluggableOptionsTxinpeqautoadaptcapable": cwsXcvrPluggableOptionsTxinpeqautoadaptcapable,
       "cwsXcvrPluggableOptionsTxinpeqfixedprogramsetting": cwsXcvrPluggableOptionsTxinpeqfixedprogramsetting,
       "cwsXcvrPluggableOptionsRxoutemfixedprogramsetting": cwsXcvrPluggableOptionsRxoutemfixedprogramsetting,
       "cwsXcvrPluggableOptionsRxoutamfixedprogramsetting": cwsXcvrPluggableOptionsRxoutamfixedprogramsetting,
       "cwsXcvrPluggableOptionsTxCdrLossOfLockFlag": cwsXcvrPluggableOptionsTxCdrLossOfLockFlag,
       "cwsXcvrPluggableOptionsRxCdrLossOfLockFlag": cwsXcvrPluggableOptionsRxCdrLossOfLockFlag,
       "cwsXcvrPluggableOptionsUserEepromPage02hProvided": cwsXcvrPluggableOptionsUserEepromPage02hProvided,
       "cwsXcvrPluggableOptionsAstPage01hProvided": cwsXcvrPluggableOptionsAstPage01hProvided,
       "cwsXcvrPluggableSupplyVoltageTable": cwsXcvrPluggableSupplyVoltageTable,
       "cwsXcvrPluggableSupplyVoltageEntry": cwsXcvrPluggableSupplyVoltageEntry,
       "cwsXcvrPluggableSupplyVoltageTableSnmpKey": cwsXcvrPluggableSupplyVoltageTableSnmpKey,
       "cwsXcvrPluggableSupplyVoltageActual": cwsXcvrPluggableSupplyVoltageActual,
       "cwsXcvrPluggableStatusTable": cwsXcvrPluggableStatusTable,
       "cwsXcvrPluggableStatusEntry": cwsXcvrPluggableStatusEntry,
       "cwsXcvrPluggableStatusTableSnmpKey": cwsXcvrPluggableStatusTableSnmpKey,
       "cwsXcvrStatusHighAlarmStatus": cwsXcvrStatusHighAlarmStatus,
       "cwsXcvrStatusLowAlarmStatus": cwsXcvrStatusLowAlarmStatus,
       "cwsXcvrStatusHighWarningStatus": cwsXcvrStatusHighWarningStatus,
       "cwsXcvrStatusLowWarningStatus": cwsXcvrStatusLowWarningStatus,
       "cwsXcvrPluggableThresholdTable": cwsXcvrPluggableThresholdTable,
       "cwsXcvrPluggableThresholdEntry": cwsXcvrPluggableThresholdEntry,
       "cwsXcvrPluggableThresholdTableSnmpKey": cwsXcvrPluggableThresholdTableSnmpKey,
       "cwsXcvrThresholdHighAlarmThreshold": cwsXcvrThresholdHighAlarmThreshold,
       "cwsXcvrThresholdLowAlarmThreshold": cwsXcvrThresholdLowAlarmThreshold,
       "cwsXcvrThresholdHighWarningThreshold": cwsXcvrThresholdHighWarningThreshold,
       "cwsXcvrThresholdLowWarningThreshold": cwsXcvrThresholdLowWarningThreshold,
       "cwsXcvrAugXcvrPluggableChannelDiagnosticsTable": cwsXcvrAugXcvrPluggableChannelDiagnosticsTable,
       "cwsXcvrAugXcvrPluggableChannelDiagnosticsEntry": cwsXcvrAugXcvrPluggableChannelDiagnosticsEntry,
       "cwsXcvrPluggableChannelDiagnosticsTransmitterFault": cwsXcvrPluggableChannelDiagnosticsTransmitterFault,
       "cwsXcvrPluggableChannelDiagnosticsTxAdaptiveEqFault": cwsXcvrPluggableChannelDiagnosticsTxAdaptiveEqFault,
       "cwsXcvrPluggableSerdesConfigTable": cwsXcvrPluggableSerdesConfigTable,
       "cwsXcvrPluggableSerdesConfigEntry": cwsXcvrPluggableSerdesConfigEntry,
       "cwsXcvrPluggableSerdesConfigTableSnmpKey": cwsXcvrPluggableSerdesConfigTableSnmpKey,
       "cwsXcvrSerdesConfigSerdesTxEq": cwsXcvrSerdesConfigSerdesTxEq,
       "cwsXcvrSerdesConfigSerdesRxAmplitude": cwsXcvrSerdesConfigSerdesRxAmplitude,
       "cwsXcvrSerdesConfigSerdesRxEmphasis": cwsXcvrSerdesConfigSerdesRxEmphasis}
)
