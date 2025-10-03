# SNMP MIB module (VOLIUS-OR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\volius\VOLIUS-OR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:42 2025
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

(InetAddressIPv4,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

vlsGlobalModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34652, 1)
)
if mibBuilder.loadTexts:
    vlsGlobalModule.setRevisions(
        ("2011-05-31 15:43",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VlsDb(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class VlsEvent(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("vlsEventBlinking", 6),
          ("vlsEventFirmwareUpload", 7),
          ("vlsEventStartUp", 8),
          ("vlsEventPowerSw1", 27),
          ("vlsEventPowerSw2", 28))
    )



class VlsInputSwitchMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("vlsForce1", 1),
          ("vlsForce2", 2),
          ("vlsPrefer1", 3),
          ("vlsPrefer2", 4),
          ("vlsAutoLatching", 5))
    )



class VlsKiloHertz(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class VlsMilliVolt(TextualConvention, Integer32):
    status = "current"


class VlsPowerSwitchMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vlsForce1", 1),
          ("vlsForce2", 2),
          ("vlsAuto", 3))
    )



class VlsTenthCelsius(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class VlsTenthDb(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class VlsTenthVolt(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class VlsTvChannelType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("vlsTvChannelSkip", 1),
          ("vlsTvChannelAnalog", 2),
          ("vlsTvChannelDigital", 3),
          ("vlsTvChannelNoise", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Volius_ObjectIdentity = ObjectIdentity
volius = _Volius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34652)
)
_VlsSystem_ObjectIdentity = ObjectIdentity
vlsSystem = _VlsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34652, 2)
)
_VlsSystemGeneral_ObjectIdentity = ObjectIdentity
vlsSystemGeneral = _VlsSystemGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10)
)
_VlsModelName_Type = DisplayString
_VlsModelName_Object = MibScalar
vlsModelName = _VlsModelName_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 1),
    _VlsModelName_Type()
)
vlsModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsModelName.setStatus("current")
_VlsSerialNumber_Type = DisplayString
_VlsSerialNumber_Object = MibScalar
vlsSerialNumber = _VlsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 2),
    _VlsSerialNumber_Type()
)
vlsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsSerialNumber.setStatus("current")
_VlsFirmwareVersion_Type = DisplayString
_VlsFirmwareVersion_Object = MibScalar
vlsFirmwareVersion = _VlsFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 3),
    _VlsFirmwareVersion_Type()
)
vlsFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsFirmwareVersion.setStatus("current")
_VlsDateAndTime_Type = DateAndTime
_VlsDateAndTime_Object = MibScalar
vlsDateAndTime = _VlsDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 4),
    _VlsDateAndTime_Type()
)
vlsDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsDateAndTime.setStatus("current")


class _VlsTimeZone_Type(Integer32):
    """Custom type vlsTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-720, 780),
    )


_VlsTimeZone_Type.__name__ = "Integer32"
_VlsTimeZone_Object = MibScalar
vlsTimeZone = _VlsTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 5),
    _VlsTimeZone_Type()
)
vlsTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsTimeZone.setStatus("current")
_VlsCaseTemperature_Type = VlsTenthCelsius
_VlsCaseTemperature_Object = MibScalar
vlsCaseTemperature = _VlsCaseTemperature_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 6),
    _VlsCaseTemperature_Type()
)
vlsCaseTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsCaseTemperature.setStatus("current")
_VlsSupplyVoltageTable_Object = MibTable
vlsSupplyVoltageTable = _VlsSupplyVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 7)
)
if mibBuilder.loadTexts:
    vlsSupplyVoltageTable.setStatus("current")
_VlsSupplyVoltageEntry_Object = MibTableRow
vlsSupplyVoltageEntry = _VlsSupplyVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 7, 1)
)
vlsSupplyVoltageEntry.setIndexNames(
    (0, "VOLIUS-OR-MIB", "vlsSupplyVoltageIndex"),
)
if mibBuilder.loadTexts:
    vlsSupplyVoltageEntry.setStatus("current")
_VlsSupplyVoltageIndex_Type = Integer32
_VlsSupplyVoltageIndex_Object = MibTableColumn
vlsSupplyVoltageIndex = _VlsSupplyVoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 7, 1, 1),
    _VlsSupplyVoltageIndex_Type()
)
vlsSupplyVoltageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsSupplyVoltageIndex.setStatus("current")
_VlsSupplyVoltageNominal_Type = VlsMilliVolt
_VlsSupplyVoltageNominal_Object = MibTableColumn
vlsSupplyVoltageNominal = _VlsSupplyVoltageNominal_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 7, 1, 2),
    _VlsSupplyVoltageNominal_Type()
)
vlsSupplyVoltageNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsSupplyVoltageNominal.setStatus("current")
_VlsSupplyVoltageActual_Type = VlsMilliVolt
_VlsSupplyVoltageActual_Object = MibTableColumn
vlsSupplyVoltageActual = _VlsSupplyVoltageActual_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 7, 1, 3),
    _VlsSupplyVoltageActual_Type()
)
vlsSupplyVoltageActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsSupplyVoltageActual.setStatus("current")
_VlsSupplySelectMode_Type = VlsPowerSwitchMode
_VlsSupplySelectMode_Object = MibScalar
vlsSupplySelectMode = _VlsSupplySelectMode_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 8),
    _VlsSupplySelectMode_Type()
)
vlsSupplySelectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsSupplySelectMode.setStatus("current")


class _VlsSupplySelectedInput_Type(Integer32):
    """Custom type vlsSupplySelectedInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_VlsSupplySelectedInput_Type.__name__ = "Integer32"
_VlsSupplySelectedInput_Object = MibScalar
vlsSupplySelectedInput = _VlsSupplySelectedInput_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 9),
    _VlsSupplySelectedInput_Type()
)
vlsSupplySelectedInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsSupplySelectedInput.setStatus("current")
_VlsBootLoaderVersion_Type = DisplayString
_VlsBootLoaderVersion_Object = MibScalar
vlsBootLoaderVersion = _VlsBootLoaderVersion_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 10),
    _VlsBootLoaderVersion_Type()
)
vlsBootLoaderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsBootLoaderVersion.setStatus("current")
_VlsRfFwVer_Type = DisplayString
_VlsRfFwVer_Object = MibScalar
vlsRfFwVer = _VlsRfFwVer_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 11),
    _VlsRfFwVer_Type()
)
vlsRfFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsRfFwVer.setStatus("obsolete")
_VlsOperatingMinutes_Type = Integer32
_VlsOperatingMinutes_Object = MibScalar
vlsOperatingMinutes = _VlsOperatingMinutes_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 12),
    _VlsOperatingMinutes_Type()
)
vlsOperatingMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsOperatingMinutes.setStatus("current")
_VlsMonPcbRevision_Type = DisplayString
_VlsMonPcbRevision_Object = MibScalar
vlsMonPcbRevision = _VlsMonPcbRevision_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 14),
    _VlsMonPcbRevision_Type()
)
vlsMonPcbRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsMonPcbRevision.setStatus("obsolete")
_VlsRfPcbRevision_Type = DisplayString
_VlsRfPcbRevision_Object = MibScalar
vlsRfPcbRevision = _VlsRfPcbRevision_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 15),
    _VlsRfPcbRevision_Type()
)
vlsRfPcbRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsRfPcbRevision.setStatus("obsolete")
_VlsNumOpticalInputs_Type = Integer32
_VlsNumOpticalInputs_Object = MibScalar
vlsNumOpticalInputs = _VlsNumOpticalInputs_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 16),
    _VlsNumOpticalInputs_Type()
)
vlsNumOpticalInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsNumOpticalInputs.setStatus("current")
_VlsNetworkServices_ObjectIdentity = ObjectIdentity
vlsNetworkServices = _VlsNetworkServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11)
)
_VlsNetworkAddress_ObjectIdentity = ObjectIdentity
vlsNetworkAddress = _VlsNetworkAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 5)
)
_VlsMacAddress_Type = MacAddress
_VlsMacAddress_Object = MibScalar
vlsMacAddress = _VlsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 5, 1),
    _VlsMacAddress_Type()
)
vlsMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsMacAddress.setStatus("current")
_VlsIpAddress_Type = InetAddressIPv4
_VlsIpAddress_Object = MibScalar
vlsIpAddress = _VlsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 5, 2),
    _VlsIpAddress_Type()
)
vlsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsIpAddress.setStatus("current")
_VlsNetMask_Type = InetAddressIPv4
_VlsNetMask_Object = MibScalar
vlsNetMask = _VlsNetMask_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 5, 3),
    _VlsNetMask_Type()
)
vlsNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsNetMask.setStatus("current")
_VlsDefaultGateway_Type = InetAddressIPv4
_VlsDefaultGateway_Object = MibScalar
vlsDefaultGateway = _VlsDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 5, 4),
    _VlsDefaultGateway_Type()
)
vlsDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsDefaultGateway.setStatus("current")
_VlsDhcp_Type = TruthValue
_VlsDhcp_Object = MibScalar
vlsDhcp = _VlsDhcp_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 5, 5),
    _VlsDhcp_Type()
)
vlsDhcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsDhcp.setStatus("obsolete")
_VlsHttp_ObjectIdentity = ObjectIdentity
vlsHttp = _VlsHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 6)
)
_VlsHttpPassword_Type = DisplayString
_VlsHttpPassword_Object = MibScalar
vlsHttpPassword = _VlsHttpPassword_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 6, 1),
    _VlsHttpPassword_Type()
)
vlsHttpPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsHttpPassword.setStatus("obsolete")
_VlsHttpPasswordEnabled_Type = TruthValue
_VlsHttpPasswordEnabled_Object = MibScalar
vlsHttpPasswordEnabled = _VlsHttpPasswordEnabled_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 6, 2),
    _VlsHttpPasswordEnabled_Type()
)
vlsHttpPasswordEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsHttpPasswordEnabled.setStatus("current")
_VlsHttpPort_Type = Integer32
_VlsHttpPort_Object = MibScalar
vlsHttpPort = _VlsHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 6, 3),
    _VlsHttpPort_Type()
)
vlsHttpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsHttpPort.setStatus("deprecated")
_VlsHttpEnabled_Type = TruthValue
_VlsHttpEnabled_Object = MibScalar
vlsHttpEnabled = _VlsHttpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 6, 4),
    _VlsHttpEnabled_Type()
)
vlsHttpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsHttpEnabled.setStatus("deprecated")
_VlsSnmp_ObjectIdentity = ObjectIdentity
vlsSnmp = _VlsSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 7)
)
_VlsSnmpPort_Type = Integer32
_VlsSnmpPort_Object = MibScalar
vlsSnmpPort = _VlsSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 7, 1),
    _VlsSnmpPort_Type()
)
vlsSnmpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsSnmpPort.setStatus("deprecated")
_VlsTrapDestTable_Object = MibTable
vlsTrapDestTable = _VlsTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 7, 2)
)
if mibBuilder.loadTexts:
    vlsTrapDestTable.setStatus("current")
_VlsTrapDestEntry_Object = MibTableRow
vlsTrapDestEntry = _VlsTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 7, 2, 1)
)
vlsTrapDestEntry.setIndexNames(
    (0, "VOLIUS-OR-MIB", "vlsTrapDestIndex"),
)
if mibBuilder.loadTexts:
    vlsTrapDestEntry.setStatus("current")
_VlsTrapDestIndex_Type = Integer32
_VlsTrapDestIndex_Object = MibTableColumn
vlsTrapDestIndex = _VlsTrapDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 7, 2, 1, 1),
    _VlsTrapDestIndex_Type()
)
vlsTrapDestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsTrapDestIndex.setStatus("current")
_VlsTrapDestAddr_Type = InetAddressIPv4
_VlsTrapDestAddr_Object = MibTableColumn
vlsTrapDestAddr = _VlsTrapDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 7, 2, 1, 2),
    _VlsTrapDestAddr_Type()
)
vlsTrapDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsTrapDestAddr.setStatus("current")
_VlsTrapDestPort_Type = Integer32
_VlsTrapDestPort_Object = MibTableColumn
vlsTrapDestPort = _VlsTrapDestPort_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 7, 2, 1, 3),
    _VlsTrapDestPort_Type()
)
vlsTrapDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsTrapDestPort.setStatus("deprecated")
_VlsTrapDestEnable_Type = TruthValue
_VlsTrapDestEnable_Object = MibTableColumn
vlsTrapDestEnable = _VlsTrapDestEnable_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 7, 2, 1, 4),
    _VlsTrapDestEnable_Type()
)
vlsTrapDestEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsTrapDestEnable.setStatus("current")
_VlsSntp_ObjectIdentity = ObjectIdentity
vlsSntp = _VlsSntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 8)
)
_VlsSntpServerAddr_Type = InetAddressIPv4
_VlsSntpServerAddr_Object = MibScalar
vlsSntpServerAddr = _VlsSntpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 8, 1),
    _VlsSntpServerAddr_Type()
)
vlsSntpServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsSntpServerAddr.setStatus("current")
_VlsSntpServerPort_Type = Integer32
_VlsSntpServerPort_Object = MibScalar
vlsSntpServerPort = _VlsSntpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 8, 2),
    _VlsSntpServerPort_Type()
)
vlsSntpServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsSntpServerPort.setStatus("deprecated")
_VlsSntpEnabled_Type = TruthValue
_VlsSntpEnabled_Object = MibScalar
vlsSntpEnabled = _VlsSntpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 8, 3),
    _VlsSntpEnabled_Type()
)
vlsSntpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsSntpEnabled.setStatus("current")
_VlsEventLog_ObjectIdentity = ObjectIdentity
vlsEventLog = _VlsEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34652, 2, 13)
)
_VlsLastEventCode_Type = VlsEvent
_VlsLastEventCode_Object = MibScalar
vlsLastEventCode = _VlsLastEventCode_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 13, 1),
    _VlsLastEventCode_Type()
)
vlsLastEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsLastEventCode.setStatus("current")
_VlsLastEventIndex_Type = Integer32
_VlsLastEventIndex_Object = MibScalar
vlsLastEventIndex = _VlsLastEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 13, 2),
    _VlsLastEventIndex_Type()
)
vlsLastEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsLastEventIndex.setStatus("current")
_VlsEventLogSize_Type = Integer32
_VlsEventLogSize_Object = MibScalar
vlsEventLogSize = _VlsEventLogSize_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 13, 3),
    _VlsEventLogSize_Type()
)
vlsEventLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsEventLogSize.setStatus("current")
_VlsEventLogTable_Object = MibTable
vlsEventLogTable = _VlsEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 13, 4)
)
if mibBuilder.loadTexts:
    vlsEventLogTable.setStatus("current")
_VlsEventLogEntry_Object = MibTableRow
vlsEventLogEntry = _VlsEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 13, 4, 1)
)
vlsEventLogEntry.setIndexNames(
    (0, "VOLIUS-OR-MIB", "vlsEventIndex"),
)
if mibBuilder.loadTexts:
    vlsEventLogEntry.setStatus("current")
_VlsEventIndex_Type = Integer32
_VlsEventIndex_Object = MibTableColumn
vlsEventIndex = _VlsEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 13, 4, 1, 1),
    _VlsEventIndex_Type()
)
vlsEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsEventIndex.setStatus("current")
_VlsEventCode_Type = VlsEvent
_VlsEventCode_Object = MibTableColumn
vlsEventCode = _VlsEventCode_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 13, 4, 1, 2),
    _VlsEventCode_Type()
)
vlsEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsEventCode.setStatus("current")
_VlsEventTimeStamp_Type = TimeTicks
_VlsEventTimeStamp_Object = MibTableColumn
vlsEventTimeStamp = _VlsEventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 13, 4, 1, 3),
    _VlsEventTimeStamp_Type()
)
vlsEventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsEventTimeStamp.setStatus("current")
_VlsEventDateTime_Type = DateAndTime
_VlsEventDateTime_Object = MibTableColumn
vlsEventDateTime = _VlsEventDateTime_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 13, 4, 1, 4),
    _VlsEventDateTime_Type()
)
vlsEventDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsEventDateTime.setStatus("current")
_VlsEventMessage_Type = DisplayString
_VlsEventMessage_Object = MibTableColumn
vlsEventMessage = _VlsEventMessage_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 13, 4, 1, 5),
    _VlsEventMessage_Type()
)
vlsEventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsEventMessage.setStatus("current")
_VlsEdfa_ObjectIdentity = ObjectIdentity
vlsEdfa = _VlsEdfa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34652, 3)
)
_VlsOpticalSwitch_ObjectIdentity = ObjectIdentity
vlsOpticalSwitch = _VlsOpticalSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34652, 4)
)
_VlsCatvTransmitter_ObjectIdentity = ObjectIdentity
vlsCatvTransmitter = _VlsCatvTransmitter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34652, 5)
)
_VlsOpticalReceiver_ObjectIdentity = ObjectIdentity
vlsOpticalReceiver = _VlsOpticalReceiver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34652, 6)
)
_VlsReceiverInputTable_Object = MibTable
vlsReceiverInputTable = _VlsReceiverInputTable_Object(
    (1, 3, 6, 1, 4, 1, 34652, 6, 1)
)
if mibBuilder.loadTexts:
    vlsReceiverInputTable.setStatus("current")
_VlsReceiverInputEntry_Object = MibTableRow
vlsReceiverInputEntry = _VlsReceiverInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 34652, 6, 1, 1)
)
vlsReceiverInputEntry.setIndexNames(
    (0, "VOLIUS-OR-MIB", "vlsReceiverInputIndex"),
)
if mibBuilder.loadTexts:
    vlsReceiverInputEntry.setStatus("current")
_VlsReceiverInputIndex_Type = Integer32
_VlsReceiverInputIndex_Object = MibTableColumn
vlsReceiverInputIndex = _VlsReceiverInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 34652, 6, 1, 1, 1),
    _VlsReceiverInputIndex_Type()
)
vlsReceiverInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsReceiverInputIndex.setStatus("current")
_VlsReceiverInputPower_Type = VlsTenthDb
_VlsReceiverInputPower_Object = MibTableColumn
vlsReceiverInputPower = _VlsReceiverInputPower_Object(
    (1, 3, 6, 1, 4, 1, 34652, 6, 1, 1, 2),
    _VlsReceiverInputPower_Type()
)
vlsReceiverInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsReceiverInputPower.setStatus("current")


class _VlsReceiverSelectedInput_Type(Integer32):
    """Custom type vlsReceiverSelectedInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_VlsReceiverSelectedInput_Type.__name__ = "Integer32"
_VlsReceiverSelectedInput_Object = MibScalar
vlsReceiverSelectedInput = _VlsReceiverSelectedInput_Object(
    (1, 3, 6, 1, 4, 1, 34652, 6, 2),
    _VlsReceiverSelectedInput_Type()
)
vlsReceiverSelectedInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsReceiverSelectedInput.setStatus("current")
_VlsReceiverRfOutputPower_Type = VlsDb
_VlsReceiverRfOutputPower_Object = MibScalar
vlsReceiverRfOutputPower = _VlsReceiverRfOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 34652, 6, 3),
    _VlsReceiverRfOutputPower_Type()
)
vlsReceiverRfOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsReceiverRfOutputPower.setStatus("current")
_VlsReceiverSwitchMode_Type = VlsInputSwitchMode
_VlsReceiverSwitchMode_Object = MibScalar
vlsReceiverSwitchMode = _VlsReceiverSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 34652, 6, 4),
    _VlsReceiverSwitchMode_Type()
)
vlsReceiverSwitchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsReceiverSwitchMode.setStatus("current")
_VlsReceiverInputLowThreshold_Type = VlsTenthDb
_VlsReceiverInputLowThreshold_Object = MibScalar
vlsReceiverInputLowThreshold = _VlsReceiverInputLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 34652, 6, 5),
    _VlsReceiverInputLowThreshold_Type()
)
vlsReceiverInputLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsReceiverInputLowThreshold.setStatus("current")
_VlsReceiverInputHighThreshold_Type = VlsTenthDb
_VlsReceiverInputHighThreshold_Object = MibScalar
vlsReceiverInputHighThreshold = _VlsReceiverInputHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 34652, 6, 6),
    _VlsReceiverInputHighThreshold_Type()
)
vlsReceiverInputHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsReceiverInputHighThreshold.setStatus("current")


class _VlsReceiverManualGain_Type(VlsTenthDb):
    """Custom type vlsReceiverManualGain based on VlsTenthDb"""
    subtypeSpec = VlsTenthDb.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 150),
    )


_VlsReceiverManualGain_Type.__name__ = "VlsTenthDb"
_VlsReceiverManualGain_Object = MibScalar
vlsReceiverManualGain = _VlsReceiverManualGain_Object(
    (1, 3, 6, 1, 4, 1, 34652, 6, 7),
    _VlsReceiverManualGain_Type()
)
vlsReceiverManualGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsReceiverManualGain.setStatus("current")


class _VlsReceiverAgcOffset_Type(VlsTenthDb):
    """Custom type vlsReceiverAgcOffset based on VlsTenthDb"""
    subtypeSpec = VlsTenthDb.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 150),
    )


_VlsReceiverAgcOffset_Type.__name__ = "VlsTenthDb"
_VlsReceiverAgcOffset_Object = MibScalar
vlsReceiverAgcOffset = _VlsReceiverAgcOffset_Object(
    (1, 3, 6, 1, 4, 1, 34652, 6, 9),
    _VlsReceiverAgcOffset_Type()
)
vlsReceiverAgcOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsReceiverAgcOffset.setStatus("current")
_VlsReceiverAgcState_Type = TruthValue
_VlsReceiverAgcState_Object = MibScalar
vlsReceiverAgcState = _VlsReceiverAgcState_Object(
    (1, 3, 6, 1, 4, 1, 34652, 6, 10),
    _VlsReceiverAgcState_Type()
)
vlsReceiverAgcState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsReceiverAgcState.setStatus("current")


class _VlsReceiverCurrentGain_Type(VlsTenthDb):
    """Custom type vlsReceiverCurrentGain based on VlsTenthDb"""
    subtypeSpec = VlsTenthDb.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 150),
    )


_VlsReceiverCurrentGain_Type.__name__ = "VlsTenthDb"
_VlsReceiverCurrentGain_Object = MibScalar
vlsReceiverCurrentGain = _VlsReceiverCurrentGain_Object(
    (1, 3, 6, 1, 4, 1, 34652, 6, 11),
    _VlsReceiverCurrentGain_Type()
)
vlsReceiverCurrentGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsReceiverCurrentGain.setStatus("current")


class _VlsReceiverEqualizer_Type(VlsTenthDb):
    """Custom type vlsReceiverEqualizer based on VlsTenthDb"""
    subtypeSpec = VlsTenthDb.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_VlsReceiverEqualizer_Type.__name__ = "VlsTenthDb"
_VlsReceiverEqualizer_Object = MibScalar
vlsReceiverEqualizer = _VlsReceiverEqualizer_Object(
    (1, 3, 6, 1, 4, 1, 34652, 6, 12),
    _VlsReceiverEqualizer_Type()
)
vlsReceiverEqualizer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsReceiverEqualizer.setStatus("current")
_VlsReceiverSpectrumTable_Object = MibTable
vlsReceiverSpectrumTable = _VlsReceiverSpectrumTable_Object(
    (1, 3, 6, 1, 4, 1, 34652, 6, 15)
)
if mibBuilder.loadTexts:
    vlsReceiverSpectrumTable.setStatus("current")
_VlsReceiverSpectrumEntry_Object = MibTableRow
vlsReceiverSpectrumEntry = _VlsReceiverSpectrumEntry_Object(
    (1, 3, 6, 1, 4, 1, 34652, 6, 15, 1)
)
vlsReceiverSpectrumEntry.setIndexNames(
    (0, "VOLIUS-OR-MIB", "vlsReceiverSpectrumIndex"),
)
if mibBuilder.loadTexts:
    vlsReceiverSpectrumEntry.setStatus("current")
_VlsReceiverSpectrumIndex_Type = Integer32
_VlsReceiverSpectrumIndex_Object = MibTableColumn
vlsReceiverSpectrumIndex = _VlsReceiverSpectrumIndex_Object(
    (1, 3, 6, 1, 4, 1, 34652, 6, 15, 1, 1),
    _VlsReceiverSpectrumIndex_Type()
)
vlsReceiverSpectrumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsReceiverSpectrumIndex.setStatus("current")
_VlsCenterFrequency_Type = VlsKiloHertz
_VlsCenterFrequency_Object = MibTableColumn
vlsCenterFrequency = _VlsCenterFrequency_Object(
    (1, 3, 6, 1, 4, 1, 34652, 6, 15, 1, 2),
    _VlsCenterFrequency_Type()
)
vlsCenterFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsCenterFrequency.setStatus("current")
_VlsChannelType_Type = VlsTvChannelType
_VlsChannelType_Object = MibTableColumn
vlsChannelType = _VlsChannelType_Object(
    (1, 3, 6, 1, 4, 1, 34652, 6, 15, 1, 3),
    _VlsChannelType_Type()
)
vlsChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsChannelType.setStatus("current")
_VlsChannelLevel_Type = VlsTenthDb
_VlsChannelLevel_Object = MibTableColumn
vlsChannelLevel = _VlsChannelLevel_Object(
    (1, 3, 6, 1, 4, 1, 34652, 6, 15, 1, 4),
    _VlsChannelLevel_Type()
)
vlsChannelLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsChannelLevel.setStatus("current")

# Managed Objects groups


# Notification objects

vlsEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34652, 2, 13, 8)
)
vlsEventTrap.setObjects(
    ("VOLIUS-OR-MIB", "vlsLastEventCode")
)
if mibBuilder.loadTexts:
    vlsEventTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VOLIUS-OR-MIB",
    **{"VlsDb": VlsDb,
       "VlsEvent": VlsEvent,
       "VlsInputSwitchMode": VlsInputSwitchMode,
       "VlsKiloHertz": VlsKiloHertz,
       "VlsMilliVolt": VlsMilliVolt,
       "VlsPowerSwitchMode": VlsPowerSwitchMode,
       "VlsTenthCelsius": VlsTenthCelsius,
       "VlsTenthDb": VlsTenthDb,
       "VlsTenthVolt": VlsTenthVolt,
       "VlsTvChannelType": VlsTvChannelType,
       "volius": volius,
       "vlsGlobalModule": vlsGlobalModule,
       "vlsSystem": vlsSystem,
       "vlsSystemGeneral": vlsSystemGeneral,
       "vlsModelName": vlsModelName,
       "vlsSerialNumber": vlsSerialNumber,
       "vlsFirmwareVersion": vlsFirmwareVersion,
       "vlsDateAndTime": vlsDateAndTime,
       "vlsTimeZone": vlsTimeZone,
       "vlsCaseTemperature": vlsCaseTemperature,
       "vlsSupplyVoltageTable": vlsSupplyVoltageTable,
       "vlsSupplyVoltageEntry": vlsSupplyVoltageEntry,
       "vlsSupplyVoltageIndex": vlsSupplyVoltageIndex,
       "vlsSupplyVoltageNominal": vlsSupplyVoltageNominal,
       "vlsSupplyVoltageActual": vlsSupplyVoltageActual,
       "vlsSupplySelectMode": vlsSupplySelectMode,
       "vlsSupplySelectedInput": vlsSupplySelectedInput,
       "vlsBootLoaderVersion": vlsBootLoaderVersion,
       "vlsRfFwVer": vlsRfFwVer,
       "vlsOperatingMinutes": vlsOperatingMinutes,
       "vlsMonPcbRevision": vlsMonPcbRevision,
       "vlsRfPcbRevision": vlsRfPcbRevision,
       "vlsNumOpticalInputs": vlsNumOpticalInputs,
       "vlsNetworkServices": vlsNetworkServices,
       "vlsNetworkAddress": vlsNetworkAddress,
       "vlsMacAddress": vlsMacAddress,
       "vlsIpAddress": vlsIpAddress,
       "vlsNetMask": vlsNetMask,
       "vlsDefaultGateway": vlsDefaultGateway,
       "vlsDhcp": vlsDhcp,
       "vlsHttp": vlsHttp,
       "vlsHttpPassword": vlsHttpPassword,
       "vlsHttpPasswordEnabled": vlsHttpPasswordEnabled,
       "vlsHttpPort": vlsHttpPort,
       "vlsHttpEnabled": vlsHttpEnabled,
       "vlsSnmp": vlsSnmp,
       "vlsSnmpPort": vlsSnmpPort,
       "vlsTrapDestTable": vlsTrapDestTable,
       "vlsTrapDestEntry": vlsTrapDestEntry,
       "vlsTrapDestIndex": vlsTrapDestIndex,
       "vlsTrapDestAddr": vlsTrapDestAddr,
       "vlsTrapDestPort": vlsTrapDestPort,
       "vlsTrapDestEnable": vlsTrapDestEnable,
       "vlsSntp": vlsSntp,
       "vlsSntpServerAddr": vlsSntpServerAddr,
       "vlsSntpServerPort": vlsSntpServerPort,
       "vlsSntpEnabled": vlsSntpEnabled,
       "vlsEventLog": vlsEventLog,
       "vlsLastEventCode": vlsLastEventCode,
       "vlsLastEventIndex": vlsLastEventIndex,
       "vlsEventLogSize": vlsEventLogSize,
       "vlsEventLogTable": vlsEventLogTable,
       "vlsEventLogEntry": vlsEventLogEntry,
       "vlsEventIndex": vlsEventIndex,
       "vlsEventCode": vlsEventCode,
       "vlsEventTimeStamp": vlsEventTimeStamp,
       "vlsEventDateTime": vlsEventDateTime,
       "vlsEventMessage": vlsEventMessage,
       "vlsEventTrap": vlsEventTrap,
       "vlsEdfa": vlsEdfa,
       "vlsOpticalSwitch": vlsOpticalSwitch,
       "vlsCatvTransmitter": vlsCatvTransmitter,
       "vlsOpticalReceiver": vlsOpticalReceiver,
       "vlsReceiverInputTable": vlsReceiverInputTable,
       "vlsReceiverInputEntry": vlsReceiverInputEntry,
       "vlsReceiverInputIndex": vlsReceiverInputIndex,
       "vlsReceiverInputPower": vlsReceiverInputPower,
       "vlsReceiverSelectedInput": vlsReceiverSelectedInput,
       "vlsReceiverRfOutputPower": vlsReceiverRfOutputPower,
       "vlsReceiverSwitchMode": vlsReceiverSwitchMode,
       "vlsReceiverInputLowThreshold": vlsReceiverInputLowThreshold,
       "vlsReceiverInputHighThreshold": vlsReceiverInputHighThreshold,
       "vlsReceiverManualGain": vlsReceiverManualGain,
       "vlsReceiverAgcOffset": vlsReceiverAgcOffset,
       "vlsReceiverAgcState": vlsReceiverAgcState,
       "vlsReceiverCurrentGain": vlsReceiverCurrentGain,
       "vlsReceiverEqualizer": vlsReceiverEqualizer,
       "vlsReceiverSpectrumTable": vlsReceiverSpectrumTable,
       "vlsReceiverSpectrumEntry": vlsReceiverSpectrumEntry,
       "vlsReceiverSpectrumIndex": vlsReceiverSpectrumIndex,
       "vlsCenterFrequency": vlsCenterFrequency,
       "vlsChannelType": vlsChannelType,
       "vlsChannelLevel": vlsChannelLevel}
)
