# SNMP MIB module (VOLIUS-OA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\volius\VOLIUS-OA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:41 2025
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



class VlsDeciCelsius(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class VlsDeciDb(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class VlsDeciDbm(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class VlsEdfaMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlsEdfaModeApc", 1),
          ("vlsEdfaModeAcc", 2))
    )



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
              27)
        )
    )
    namedValues = NamedValues(
        *(("vlsEventStartUp", 1),
          ("vlsEventPowerOff", 2),
          ("vlsEventSntpSync", 3),
          ("vlsEventFwUpload", 4),
          ("vlsEventEmissionOn", 5),
          ("vlsEventEmissionOff", 6),
          ("vlsEventLaserTempNorm", 7),
          ("vlsEventLaserTempLow", 8),
          ("vlsEventLaserTempHigh", 9),
          ("vlsEventLaserCurrentNorm", 10),
          ("vlsEventLaserCurrentHigh", 11),
          ("vlsEventInputLossOfSignal", 12),
          ("vlsEventInputPowerLow", 13),
          ("vlsEventInputPowerNorm", 14),
          ("vlsEventInputPowerHigh", 15),
          ("vlsEventOutputPowerNorm", 16),
          ("vlsEventOutputPowerLow", 17),
          ("vlsEventOutputPowerHigh", 18),
          ("vlsEventCaseTempNorm", 19),
          ("vlsEventCaseTempLow", 20),
          ("vlsEventCaseTempHigh", 21),
          ("vlsEventFanSpeedNorm", 22),
          ("vlsEventFanSpeedLow", 23),
          ("vlsEventCurrentProtectionSM", 24),
          ("vlsEventCurrentProtectionMM", 25),
          ("vlsEventSelectedInputA", 26),
          ("vlsEventSelectedInputB", 27))
    )



class VlsMillivolt(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-3"


class VlsPerMille(TextualConvention, Integer32):
    status = "current"


class VlsRPM(TextualConvention, Integer32):
    status = "current"


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
        *(("vlsSwitchForceA", 1),
          ("vlsSwitchForceB", 2),
          ("vlsSwitchPreferA", 3),
          ("vlsSwitchPreferB", 4),
          ("vlsSwitchPreferALatch", 5),
          ("vlsSwitchPreferBLatch", 6))
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
        *(("vlsSwitchStateA", 1),
          ("vlsSwitchStateB", 2))
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
    (0, "VOLIUS-OA-MIB", "vlsSupplyVoltageIndex"),
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
_VlsOperationMinutes_Type = Integer32
_VlsOperationMinutes_Object = MibScalar
vlsOperationMinutes = _VlsOperationMinutes_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 8),
    _VlsOperationMinutes_Type()
)
vlsOperationMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsOperationMinutes.setStatus("obsolete")
_VlsActivePowerSupply_Type = Integer32
_VlsActivePowerSupply_Object = MibScalar
vlsActivePowerSupply = _VlsActivePowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 9),
    _VlsActivePowerSupply_Type()
)
vlsActivePowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsActivePowerSupply.setStatus("obsolete")
_VlsBootLoaderVersion_Type = DisplayString
_VlsBootLoaderVersion_Object = MibScalar
vlsBootLoaderVersion = _VlsBootLoaderVersion_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 10),
    _VlsBootLoaderVersion_Type()
)
vlsBootLoaderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsBootLoaderVersion.setStatus("current")
_VlsFanSpeed_Type = VlsRPM
_VlsFanSpeed_Object = MibScalar
vlsFanSpeed = _VlsFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 11),
    _VlsFanSpeed_Type()
)
vlsFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsFanSpeed.setStatus("current")
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
vlsHttpEnabled.setMaxAccess("read-only")
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
    (0, "VOLIUS-OA-MIB", "vlsTrapDestIndex"),
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
    (0, "VOLIUS-OA-MIB", "vlsEventIndex"),
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
_VlsAlarms_ObjectIdentity = ObjectIdentity
vlsAlarms = _VlsAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34652, 2, 14)
)
_VlsAlarmsActiveMask_Type = Integer32
_VlsAlarmsActiveMask_Object = MibScalar
vlsAlarmsActiveMask = _VlsAlarmsActiveMask_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 14, 1),
    _VlsAlarmsActiveMask_Type()
)
vlsAlarmsActiveMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsAlarmsActiveMask.setStatus("current")
_VlsAlarmsResetMask_Type = Integer32
_VlsAlarmsResetMask_Object = MibScalar
vlsAlarmsResetMask = _VlsAlarmsResetMask_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 14, 2),
    _VlsAlarmsResetMask_Type()
)
vlsAlarmsResetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsAlarmsResetMask.setStatus("current")
_VlsAlarmsTable_Object = MibTable
vlsAlarmsTable = _VlsAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 14, 3)
)
if mibBuilder.loadTexts:
    vlsAlarmsTable.setStatus("current")
_VlsAlarmsEntry_Object = MibTableRow
vlsAlarmsEntry = _VlsAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 14, 3, 1)
)
vlsAlarmsEntry.setIndexNames(
    (0, "VOLIUS-OA-MIB", "vlsAlarmIndex"),
)
if mibBuilder.loadTexts:
    vlsAlarmsEntry.setStatus("current")
_VlsAlarmIndex_Type = Integer32
_VlsAlarmIndex_Object = MibTableColumn
vlsAlarmIndex = _VlsAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 14, 3, 1, 1),
    _VlsAlarmIndex_Type()
)
vlsAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsAlarmIndex.setStatus("current")
_VlsAlarmState_Type = TruthValue
_VlsAlarmState_Object = MibTableColumn
vlsAlarmState = _VlsAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 14, 3, 1, 2),
    _VlsAlarmState_Type()
)
vlsAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsAlarmState.setStatus("current")
_VlsAlarmMessage_Type = DisplayString
_VlsAlarmMessage_Object = MibTableColumn
vlsAlarmMessage = _VlsAlarmMessage_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 14, 3, 1, 3),
    _VlsAlarmMessage_Type()
)
vlsAlarmMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsAlarmMessage.setStatus("current")
_VlsEdfa_ObjectIdentity = ObjectIdentity
vlsEdfa = _VlsEdfa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34652, 3)
)
_VlsKeyState_Type = TruthValue
_VlsKeyState_Object = MibScalar
vlsKeyState = _VlsKeyState_Object(
    (1, 3, 6, 1, 4, 1, 34652, 3, 1),
    _VlsKeyState_Type()
)
vlsKeyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsKeyState.setStatus("current")
_VlsEdfaEmissionState_Type = TruthValue
_VlsEdfaEmissionState_Object = MibScalar
vlsEdfaEmissionState = _VlsEdfaEmissionState_Object(
    (1, 3, 6, 1, 4, 1, 34652, 3, 2),
    _VlsEdfaEmissionState_Type()
)
vlsEdfaEmissionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsEdfaEmissionState.setStatus("current")
_VlsEdfaMode_Type = VlsEdfaMode
_VlsEdfaMode_Object = MibScalar
vlsEdfaMode = _VlsEdfaMode_Object(
    (1, 3, 6, 1, 4, 1, 34652, 3, 3),
    _VlsEdfaMode_Type()
)
vlsEdfaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsEdfaMode.setStatus("current")
_VlsEdfaPowerSetting_Type = VlsDeciDbm
_VlsEdfaPowerSetting_Object = MibScalar
vlsEdfaPowerSetting = _VlsEdfaPowerSetting_Object(
    (1, 3, 6, 1, 4, 1, 34652, 3, 4),
    _VlsEdfaPowerSetting_Type()
)
vlsEdfaPowerSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsEdfaPowerSetting.setStatus("current")
_VlsEdfaPumpCurrentSetting_Type = VlsPerMille
_VlsEdfaPumpCurrentSetting_Object = MibScalar
vlsEdfaPumpCurrentSetting = _VlsEdfaPumpCurrentSetting_Object(
    (1, 3, 6, 1, 4, 1, 34652, 3, 5),
    _VlsEdfaPumpCurrentSetting_Type()
)
vlsEdfaPumpCurrentSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsEdfaPumpCurrentSetting.setStatus("current")
_VlsEdfaGainSetting_Type = VlsDeciDb
_VlsEdfaGainSetting_Object = MibScalar
vlsEdfaGainSetting = _VlsEdfaGainSetting_Object(
    (1, 3, 6, 1, 4, 1, 34652, 3, 6),
    _VlsEdfaGainSetting_Type()
)
vlsEdfaGainSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsEdfaGainSetting.setStatus("obsolete")
_VlsEdfaInputTable_Object = MibTable
vlsEdfaInputTable = _VlsEdfaInputTable_Object(
    (1, 3, 6, 1, 4, 1, 34652, 3, 7)
)
if mibBuilder.loadTexts:
    vlsEdfaInputTable.setStatus("current")
_VlsEdfaInputEntry_Object = MibTableRow
vlsEdfaInputEntry = _VlsEdfaInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 34652, 3, 7, 1)
)
vlsEdfaInputEntry.setIndexNames(
    (0, "VOLIUS-OA-MIB", "vlsEdfaInputIndex"),
)
if mibBuilder.loadTexts:
    vlsEdfaInputEntry.setStatus("current")
_VlsEdfaInputIndex_Type = Integer32
_VlsEdfaInputIndex_Object = MibTableColumn
vlsEdfaInputIndex = _VlsEdfaInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 34652, 3, 7, 1, 1),
    _VlsEdfaInputIndex_Type()
)
vlsEdfaInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsEdfaInputIndex.setStatus("current")
_VlsEdfaInputPower_Type = VlsDeciDbm
_VlsEdfaInputPower_Object = MibTableColumn
vlsEdfaInputPower = _VlsEdfaInputPower_Object(
    (1, 3, 6, 1, 4, 1, 34652, 3, 7, 1, 2),
    _VlsEdfaInputPower_Type()
)
vlsEdfaInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsEdfaInputPower.setStatus("current")
_VlsEdfaOutputPowerTotal_Type = VlsDeciDbm
_VlsEdfaOutputPowerTotal_Object = MibScalar
vlsEdfaOutputPowerTotal = _VlsEdfaOutputPowerTotal_Object(
    (1, 3, 6, 1, 4, 1, 34652, 3, 8),
    _VlsEdfaOutputPowerTotal_Type()
)
vlsEdfaOutputPowerTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsEdfaOutputPowerTotal.setStatus("current")
_VlsEdfaOutputPowerPerChannel_Type = VlsDeciDbm
_VlsEdfaOutputPowerPerChannel_Object = MibScalar
vlsEdfaOutputPowerPerChannel = _VlsEdfaOutputPowerPerChannel_Object(
    (1, 3, 6, 1, 4, 1, 34652, 3, 9),
    _VlsEdfaOutputPowerPerChannel_Type()
)
vlsEdfaOutputPowerPerChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsEdfaOutputPowerPerChannel.setStatus("current")
_VlsEdfaSplitRatio_Type = VlsDeciDb
_VlsEdfaSplitRatio_Object = MibScalar
vlsEdfaSplitRatio = _VlsEdfaSplitRatio_Object(
    (1, 3, 6, 1, 4, 1, 34652, 3, 10),
    _VlsEdfaSplitRatio_Type()
)
vlsEdfaSplitRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsEdfaSplitRatio.setStatus("current")
_VlsEdfaPumpCurrent_Type = VlsPerMille
_VlsEdfaPumpCurrent_Object = MibScalar
vlsEdfaPumpCurrent = _VlsEdfaPumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 34652, 3, 11),
    _VlsEdfaPumpCurrent_Type()
)
vlsEdfaPumpCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsEdfaPumpCurrent.setStatus("current")
_VlsEdfaGain_Type = VlsDeciDb
_VlsEdfaGain_Object = MibScalar
vlsEdfaGain = _VlsEdfaGain_Object(
    (1, 3, 6, 1, 4, 1, 34652, 3, 12),
    _VlsEdfaGain_Type()
)
vlsEdfaGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsEdfaGain.setStatus("current")
_VlsEdfaBackReflection_Type = VlsDeciDbm
_VlsEdfaBackReflection_Object = MibScalar
vlsEdfaBackReflection = _VlsEdfaBackReflection_Object(
    (1, 3, 6, 1, 4, 1, 34652, 3, 13),
    _VlsEdfaBackReflection_Type()
)
vlsEdfaBackReflection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsEdfaBackReflection.setStatus("current")
_VlsEdfaBackReflectionThreshold_Type = VlsDeciDbm
_VlsEdfaBackReflectionThreshold_Object = MibScalar
vlsEdfaBackReflectionThreshold = _VlsEdfaBackReflectionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 34652, 3, 14),
    _VlsEdfaBackReflectionThreshold_Type()
)
vlsEdfaBackReflectionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsEdfaBackReflectionThreshold.setStatus("obsolete")
_VlsEdfaSwitchMode_Type = VlsSwitchMode
_VlsEdfaSwitchMode_Object = MibScalar
vlsEdfaSwitchMode = _VlsEdfaSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 34652, 3, 15),
    _VlsEdfaSwitchMode_Type()
)
vlsEdfaSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsEdfaSwitchMode.setStatus("current")
_VlsEdfaSwitchState_Type = VlsSwitchState
_VlsEdfaSwitchState_Object = MibScalar
vlsEdfaSwitchState = _VlsEdfaSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 34652, 3, 16),
    _VlsEdfaSwitchState_Type()
)
vlsEdfaSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsEdfaSwitchState.setStatus("current")
_VlsEdfaPumpTemperature_Type = VlsDeciCelsius
_VlsEdfaPumpTemperature_Object = MibScalar
vlsEdfaPumpTemperature = _VlsEdfaPumpTemperature_Object(
    (1, 3, 6, 1, 4, 1, 34652, 3, 17),
    _VlsEdfaPumpTemperature_Type()
)
vlsEdfaPumpTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsEdfaPumpTemperature.setStatus("current")
_VlsEdfaLosThreshold_Type = VlsDeciDbm
_VlsEdfaLosThreshold_Object = MibScalar
vlsEdfaLosThreshold = _VlsEdfaLosThreshold_Object(
    (1, 3, 6, 1, 4, 1, 34652, 3, 18),
    _VlsEdfaLosThreshold_Type()
)
vlsEdfaLosThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsEdfaLosThreshold.setStatus("current")
_VlsEdfaLoqThreshold_Type = VlsDeciDbm
_VlsEdfaLoqThreshold_Object = MibScalar
vlsEdfaLoqThreshold = _VlsEdfaLoqThreshold_Object(
    (1, 3, 6, 1, 4, 1, 34652, 3, 19),
    _VlsEdfaLoqThreshold_Type()
)
vlsEdfaLoqThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsEdfaLoqThreshold.setStatus("current")
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
_VlsCabinetMonitor_ObjectIdentity = ObjectIdentity
vlsCabinetMonitor = _VlsCabinetMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34652, 7)
)
_VlsUpsMonitor_ObjectIdentity = ObjectIdentity
vlsUpsMonitor = _VlsUpsMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34652, 8)
)

# Managed Objects groups


# Notification objects

vlsEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34652, 2, 13, 8)
)
vlsEventTrap.setObjects(
    ("VOLIUS-OA-MIB", "vlsLastEventCode")
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
    "VOLIUS-OA-MIB",
    **{"VlsDeciCelsius": VlsDeciCelsius,
       "VlsDeciDb": VlsDeciDb,
       "VlsDeciDbm": VlsDeciDbm,
       "VlsEdfaMode": VlsEdfaMode,
       "VlsEvent": VlsEvent,
       "VlsMillivolt": VlsMillivolt,
       "VlsPerMille": VlsPerMille,
       "VlsRPM": VlsRPM,
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
       "vlsOperationMinutes": vlsOperationMinutes,
       "vlsActivePowerSupply": vlsActivePowerSupply,
       "vlsBootLoaderVersion": vlsBootLoaderVersion,
       "vlsFanSpeed": vlsFanSpeed,
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
       "vlsAlarms": vlsAlarms,
       "vlsAlarmsActiveMask": vlsAlarmsActiveMask,
       "vlsAlarmsResetMask": vlsAlarmsResetMask,
       "vlsAlarmsTable": vlsAlarmsTable,
       "vlsAlarmsEntry": vlsAlarmsEntry,
       "vlsAlarmIndex": vlsAlarmIndex,
       "vlsAlarmState": vlsAlarmState,
       "vlsAlarmMessage": vlsAlarmMessage,
       "vlsEdfa": vlsEdfa,
       "vlsKeyState": vlsKeyState,
       "vlsEdfaEmissionState": vlsEdfaEmissionState,
       "vlsEdfaMode": vlsEdfaMode,
       "vlsEdfaPowerSetting": vlsEdfaPowerSetting,
       "vlsEdfaPumpCurrentSetting": vlsEdfaPumpCurrentSetting,
       "vlsEdfaGainSetting": vlsEdfaGainSetting,
       "vlsEdfaInputTable": vlsEdfaInputTable,
       "vlsEdfaInputEntry": vlsEdfaInputEntry,
       "vlsEdfaInputIndex": vlsEdfaInputIndex,
       "vlsEdfaInputPower": vlsEdfaInputPower,
       "vlsEdfaOutputPowerTotal": vlsEdfaOutputPowerTotal,
       "vlsEdfaOutputPowerPerChannel": vlsEdfaOutputPowerPerChannel,
       "vlsEdfaSplitRatio": vlsEdfaSplitRatio,
       "vlsEdfaPumpCurrent": vlsEdfaPumpCurrent,
       "vlsEdfaGain": vlsEdfaGain,
       "vlsEdfaBackReflection": vlsEdfaBackReflection,
       "vlsEdfaBackReflectionThreshold": vlsEdfaBackReflectionThreshold,
       "vlsEdfaSwitchMode": vlsEdfaSwitchMode,
       "vlsEdfaSwitchState": vlsEdfaSwitchState,
       "vlsEdfaPumpTemperature": vlsEdfaPumpTemperature,
       "vlsEdfaLosThreshold": vlsEdfaLosThreshold,
       "vlsEdfaLoqThreshold": vlsEdfaLoqThreshold,
       "vlsOpticalSwitch": vlsOpticalSwitch,
       "vlsCatvTransmitter": vlsCatvTransmitter,
       "vlsOpticalReceiver": vlsOpticalReceiver,
       "vlsCabinetMonitor": vlsCabinetMonitor,
       "vlsUpsMonitor": vlsUpsMonitor}
)
