# SNMP MIB module (VOLIUS-OS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\volius\VOLIUS-OS-MIB
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



class VlsDbuv(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class VlsDeciCelsius(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class VlsDeciDbm(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class VlsEvent(TextualConvention, Integer32):
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
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("vlsEventStartUp", 1),
          ("vlsEventPowerOff", 2),
          ("vlsEventSntpSync", 3),
          ("vlsEventFwUpload", 4),
          ("vlsEventIn1LoS", 5),
          ("vlsEventIn1LoQ", 6),
          ("vlsEventIn1Norm", 7),
          ("vlsEventIn2LoS", 8),
          ("vlsEventIn2LoQ", 9),
          ("vlsEventIn2Norm", 10),
          ("vlsEventSw1", 11),
          ("vlsEventSw2", 12))
    )



class VlsMillivolt(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-3"


class VlsSwitchMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("vlsForcePathA", 1),
          ("vlsForcePathB", 2),
          ("vlsPreferPathA", 3),
          ("vlsPreferPathB", 4),
          ("vlsAutoLatching", 5),
          ("vlsScript", 6))
    )



class VlsSwitchState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlsPathA", 1),
          ("vlsPathB", 2))
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
_VlsCaseTemperature_Type = VlsDeciCelsius
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
    (0, "VOLIUS-OS-MIB", "vlsSupplyVoltageIndex"),
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
_VlsSupplyVoltageNominal_Type = VlsMillivolt
_VlsSupplyVoltageNominal_Object = MibTableColumn
vlsSupplyVoltageNominal = _VlsSupplyVoltageNominal_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 7, 1, 2),
    _VlsSupplyVoltageNominal_Type()
)
vlsSupplyVoltageNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsSupplyVoltageNominal.setStatus("current")
_VlsSupplyVoltageActual_Type = VlsMillivolt
_VlsSupplyVoltageActual_Object = MibTableColumn
vlsSupplyVoltageActual = _VlsSupplyVoltageActual_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 7, 1, 3),
    _VlsSupplyVoltageActual_Type()
)
vlsSupplyVoltageActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsSupplyVoltageActual.setStatus("current")
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
vlsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsIpAddress.setStatus("current")
_VlsNetMask_Type = InetAddressIPv4
_VlsNetMask_Object = MibScalar
vlsNetMask = _VlsNetMask_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 5, 3),
    _VlsNetMask_Type()
)
vlsNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsNetMask.setStatus("current")
_VlsDefaultGateway_Type = InetAddressIPv4
_VlsDefaultGateway_Object = MibScalar
vlsDefaultGateway = _VlsDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 5, 4),
    _VlsDefaultGateway_Type()
)
vlsDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsDefaultGateway.setStatus("current")
_VlsHttp_ObjectIdentity = ObjectIdentity
vlsHttp = _VlsHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 6)
)


class _VlsHttpPassword_Type(DisplayString):
    """Custom type vlsHttpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VlsHttpPassword_Type.__name__ = "DisplayString"
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


class _VlsHttpPort_Type(Integer32):
    """Custom type vlsHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VlsHttpPort_Type.__name__ = "Integer32"
_VlsHttpPort_Object = MibScalar
vlsHttpPort = _VlsHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 6, 3),
    _VlsHttpPort_Type()
)
vlsHttpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsHttpPort.setStatus("current")
_VlsHttpEnabled_Type = TruthValue
_VlsHttpEnabled_Object = MibScalar
vlsHttpEnabled = _VlsHttpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 6, 4),
    _VlsHttpEnabled_Type()
)
vlsHttpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsHttpEnabled.setStatus("current")
_VlsSnmp_ObjectIdentity = ObjectIdentity
vlsSnmp = _VlsSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 7)
)


class _VlsSnmpPort_Type(Integer32):
    """Custom type vlsSnmpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VlsSnmpPort_Type.__name__ = "Integer32"
_VlsSnmpPort_Object = MibScalar
vlsSnmpPort = _VlsSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 7, 1),
    _VlsSnmpPort_Type()
)
vlsSnmpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsSnmpPort.setStatus("current")
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
    (0, "VOLIUS-OS-MIB", "vlsTrapDestIndex"),
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


class _VlsTrapDestPort_Type(Integer32):
    """Custom type vlsTrapDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VlsTrapDestPort_Type.__name__ = "Integer32"
_VlsTrapDestPort_Object = MibTableColumn
vlsTrapDestPort = _VlsTrapDestPort_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 7, 2, 1, 3),
    _VlsTrapDestPort_Type()
)
vlsTrapDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsTrapDestPort.setStatus("current")
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
vlsSntpServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsSntpServerAddr.setStatus("current")


class _VlsSntpServerPort_Type(Integer32):
    """Custom type vlsSntpServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VlsSntpServerPort_Type.__name__ = "Integer32"
_VlsSntpServerPort_Object = MibScalar
vlsSntpServerPort = _VlsSntpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 8, 2),
    _VlsSntpServerPort_Type()
)
vlsSntpServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsSntpServerPort.setStatus("current")
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
    (0, "VOLIUS-OS-MIB", "vlsEventIndex"),
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
_VlsSwitchInputTable_Object = MibTable
vlsSwitchInputTable = _VlsSwitchInputTable_Object(
    (1, 3, 6, 1, 4, 1, 34652, 4, 1)
)
if mibBuilder.loadTexts:
    vlsSwitchInputTable.setStatus("current")
_VlsSwitchInputEntry_Object = MibTableRow
vlsSwitchInputEntry = _VlsSwitchInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 34652, 4, 1, 1)
)
vlsSwitchInputEntry.setIndexNames(
    (0, "VOLIUS-OS-MIB", "vlsSwitchInputIndex"),
)
if mibBuilder.loadTexts:
    vlsSwitchInputEntry.setStatus("current")
_VlsSwitchInputIndex_Type = Integer32
_VlsSwitchInputIndex_Object = MibTableColumn
vlsSwitchInputIndex = _VlsSwitchInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 34652, 4, 1, 1, 1),
    _VlsSwitchInputIndex_Type()
)
vlsSwitchInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsSwitchInputIndex.setStatus("current")
_VlsSwitchInputPower_Type = VlsDeciDbm
_VlsSwitchInputPower_Object = MibTableColumn
vlsSwitchInputPower = _VlsSwitchInputPower_Object(
    (1, 3, 6, 1, 4, 1, 34652, 4, 1, 1, 2),
    _VlsSwitchInputPower_Type()
)
vlsSwitchInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsSwitchInputPower.setStatus("current")
_VlsSwitchLosThreshold_Type = VlsDeciDbm
_VlsSwitchLosThreshold_Object = MibTableColumn
vlsSwitchLosThreshold = _VlsSwitchLosThreshold_Object(
    (1, 3, 6, 1, 4, 1, 34652, 4, 1, 1, 3),
    _VlsSwitchLosThreshold_Type()
)
vlsSwitchLosThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsSwitchLosThreshold.setStatus("current")
_VlsSwitchLoqThreshold_Type = VlsDeciDbm
_VlsSwitchLoqThreshold_Object = MibTableColumn
vlsSwitchLoqThreshold = _VlsSwitchLoqThreshold_Object(
    (1, 3, 6, 1, 4, 1, 34652, 4, 1, 1, 4),
    _VlsSwitchLoqThreshold_Type()
)
vlsSwitchLoqThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsSwitchLoqThreshold.setStatus("current")
_VlsSwitchMode_Type = VlsSwitchMode
_VlsSwitchMode_Object = MibScalar
vlsSwitchMode = _VlsSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 34652, 4, 2),
    _VlsSwitchMode_Type()
)
vlsSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsSwitchMode.setStatus("current")
_VlsSwitchState_Type = VlsSwitchState
_VlsSwitchState_Object = MibScalar
vlsSwitchState = _VlsSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 34652, 4, 3),
    _VlsSwitchState_Type()
)
vlsSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsSwitchState.setStatus("current")

# Managed Objects groups


# Notification objects

vlsEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34652, 2, 13, 8)
)
vlsEventTrap.setObjects(
    ("VOLIUS-OS-MIB", "vlsLastEventCode")
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
    "VOLIUS-OS-MIB",
    **{"VlsDbuv": VlsDbuv,
       "VlsDeciCelsius": VlsDeciCelsius,
       "VlsDeciDbm": VlsDeciDbm,
       "VlsEvent": VlsEvent,
       "VlsMillivolt": VlsMillivolt,
       "VlsSwitchMode": VlsSwitchMode,
       "VlsSwitchState": VlsSwitchState,
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
       "vlsNetworkServices": vlsNetworkServices,
       "vlsNetworkAddress": vlsNetworkAddress,
       "vlsMacAddress": vlsMacAddress,
       "vlsIpAddress": vlsIpAddress,
       "vlsNetMask": vlsNetMask,
       "vlsDefaultGateway": vlsDefaultGateway,
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
       "vlsSwitchInputTable": vlsSwitchInputTable,
       "vlsSwitchInputEntry": vlsSwitchInputEntry,
       "vlsSwitchInputIndex": vlsSwitchInputIndex,
       "vlsSwitchInputPower": vlsSwitchInputPower,
       "vlsSwitchLosThreshold": vlsSwitchLosThreshold,
       "vlsSwitchLoqThreshold": vlsSwitchLoqThreshold,
       "vlsSwitchMode": vlsSwitchMode,
       "vlsSwitchState": vlsSwitchState}
)
