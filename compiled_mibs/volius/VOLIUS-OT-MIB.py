# SNMP MIB module (VOLIUS-OT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\volius\VOLIUS-OT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:43 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


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



class VlsDbm(TextualConvention, Integer32):
    status = "current"


class VlsDbuv(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class VlsDeciCelsius(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class VlsDeciDb(TextualConvention, Integer32):
    status = "current"


class VlsDeciDbm(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class VlsDeciDbo(TextualConvention, Integer32):
    status = "current"


class VlsEvent(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50)
        )
    )
    namedValues = NamedValues(
        *(("vlsEventStartUp", 1),
          ("vlsEventLaserOn", 20),
          ("vlsEventLaserOff", 21),
          ("vlsEventPout1Norm", 22),
          ("vlsEventPout1High", 23),
          ("vlsEventPout1Low", 24),
          ("vlsEventPout2Norm", 25),
          ("vlsEventPout2High", 26),
          ("vlsEventPout2Low", 27),
          ("vlsEventTcaseNorm", 28),
          ("vlsEventTcaseLow", 29),
          ("vlsEventTcaseHigh", 30),
          ("vlsEventRFinNorm", 31),
          ("vlsEventRFinLow", 32),
          ("vlsEventRFinHigh", 33),
          ("vlsEventLaserTempNorm", 34),
          ("vlsEventLaserTempLow", 35),
          ("vlsEventLaserTempHigh", 36),
          ("vlsEventTecCurrentNorm", 37),
          ("vlsEventTecCurrentLow", 38),
          ("vlsEventTecCurrentHigh", 39),
          ("vlsEventLaserCurrentNorm", 40),
          ("vlsEventLaserCurrentLow", 41),
          ("vlsEventLaserCurrentHigh", 42),
          ("vlsEventLaserPowerNorm", 43),
          ("vlsEventLaserPowerLow", 44),
          ("vlsEventLaserPowerHigh", 45),
          ("vlsEventOmiNorm", 46),
          ("vlsEventOmiLow", 47),
          ("vlsEventOmiHigh", 48),
          ("vlsEventFanNorm", 49),
          ("vlsEventFanLow", 50))
    )



class VlsMilliAmp(TextualConvention, Integer32):
    status = "current"


class VlsMillivolt(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-3"


class VlsOnOff(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlsOn", 1),
          ("vlsOff", 2))
    )



class VlsPerMille(TextualConvention, Integer32):
    status = "current"


class VlsPercent(TextualConvention, Integer32):
    status = "current"


class VlsRPM(TextualConvention, Integer32):
    status = "current"


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
_VlsBootLoaderVersion_Type = DisplayString
_VlsBootLoaderVersion_Object = MibScalar
vlsBootLoaderVersion = _VlsBootLoaderVersion_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 4),
    _VlsBootLoaderVersion_Type()
)
vlsBootLoaderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsBootLoaderVersion.setStatus("current")
_VlsDateAndTime_Type = DateAndTime
_VlsDateAndTime_Object = MibScalar
vlsDateAndTime = _VlsDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 5),
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
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 6),
    _VlsTimeZone_Type()
)
vlsTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsTimeZone.setStatus("current")
_VlsCaseTemperature_Type = VlsDeciCelsius
_VlsCaseTemperature_Object = MibScalar
vlsCaseTemperature = _VlsCaseTemperature_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 7),
    _VlsCaseTemperature_Type()
)
vlsCaseTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsCaseTemperature.setStatus("current")
_VlsFanSpeed_Type = VlsRPM
_VlsFanSpeed_Object = MibScalar
vlsFanSpeed = _VlsFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 8),
    _VlsFanSpeed_Type()
)
vlsFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsFanSpeed.setStatus("current")
_VlsSupplyVoltageTable_Object = MibTable
vlsSupplyVoltageTable = _VlsSupplyVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 9)
)
if mibBuilder.loadTexts:
    vlsSupplyVoltageTable.setStatus("current")
_VlsSupplyVoltageEntry_Object = MibTableRow
vlsSupplyVoltageEntry = _VlsSupplyVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 9, 1)
)
vlsSupplyVoltageEntry.setIndexNames(
    (0, "VOLIUS-OT-MIB", "vlsSupplyVoltageIndex"),
)
if mibBuilder.loadTexts:
    vlsSupplyVoltageEntry.setStatus("current")
_VlsSupplyVoltageIndex_Type = Integer32
_VlsSupplyVoltageIndex_Object = MibTableColumn
vlsSupplyVoltageIndex = _VlsSupplyVoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 9, 1, 1),
    _VlsSupplyVoltageIndex_Type()
)
vlsSupplyVoltageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsSupplyVoltageIndex.setStatus("current")
_VlsSupplyVoltageNominal_Type = VlsMillivolt
_VlsSupplyVoltageNominal_Object = MibTableColumn
vlsSupplyVoltageNominal = _VlsSupplyVoltageNominal_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 9, 1, 2),
    _VlsSupplyVoltageNominal_Type()
)
vlsSupplyVoltageNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsSupplyVoltageNominal.setStatus("current")
_VlsSupplyVoltageActual_Type = VlsMillivolt
_VlsSupplyVoltageActual_Object = MibTableColumn
vlsSupplyVoltageActual = _VlsSupplyVoltageActual_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 10, 9, 1, 3),
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
vlsMacAddress.setMaxAccess("read-write")
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
_VlsHttp_ObjectIdentity = ObjectIdentity
vlsHttp = _VlsHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 6)
)


class _VlsHttpPort_Type(Integer32):
    """Custom type vlsHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VlsHttpPort_Type.__name__ = "Integer32"
_VlsHttpPort_Object = MibScalar
vlsHttpPort = _VlsHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 6, 1),
    _VlsHttpPort_Type()
)
vlsHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsHttpPort.setStatus("current")
_VlsHttpEnabled_Type = VlsOnOff
_VlsHttpEnabled_Object = MibScalar
vlsHttpEnabled = _VlsHttpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 6, 2),
    _VlsHttpEnabled_Type()
)
vlsHttpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsHttpEnabled.setStatus("current")
_VlsHttpPasswordEnabled_Type = VlsOnOff
_VlsHttpPasswordEnabled_Object = MibScalar
vlsHttpPasswordEnabled = _VlsHttpPasswordEnabled_Object(
    (1, 3, 6, 1, 4, 1, 34652, 2, 11, 6, 3),
    _VlsHttpPasswordEnabled_Type()
)
vlsHttpPasswordEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsHttpPasswordEnabled.setStatus("current")
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
vlsSnmpPort.setMaxAccess("read-write")
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
    (0, "VOLIUS-OT-MIB", "vlsTrapDestIndex"),
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
_VlsTrapDestEnable_Type = VlsOnOff
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
vlsSntpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsSntpServerPort.setStatus("current")
_VlsSntpEnabled_Type = VlsOnOff
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
    (0, "VOLIUS-OT-MIB", "vlsEventIndex"),
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
    (0, "VOLIUS-OT-MIB", "vlsAlarmIndex"),
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
_VlsAlarmState_Type = VlsOnOff
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
_VlsOpticalSwitch_ObjectIdentity = ObjectIdentity
vlsOpticalSwitch = _VlsOpticalSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34652, 4)
)
_VlsCatvTransmitter_ObjectIdentity = ObjectIdentity
vlsCatvTransmitter = _VlsCatvTransmitter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34652, 5)
)
_VlsTxEmissionState_Type = VlsOnOff
_VlsTxEmissionState_Object = MibScalar
vlsTxEmissionState = _VlsTxEmissionState_Object(
    (1, 3, 6, 1, 4, 1, 34652, 5, 1),
    _VlsTxEmissionState_Type()
)
vlsTxEmissionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsTxEmissionState.setStatus("current")
_VlsTxOutputTable_Object = MibTable
vlsTxOutputTable = _VlsTxOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 34652, 5, 2)
)
if mibBuilder.loadTexts:
    vlsTxOutputTable.setStatus("current")
_VlsTxOutputEntry_Object = MibTableRow
vlsTxOutputEntry = _VlsTxOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 34652, 5, 2, 1)
)
vlsTxOutputEntry.setIndexNames(
    (0, "VOLIUS-OT-MIB", "vlsTxOutputIndex"),
)
if mibBuilder.loadTexts:
    vlsTxOutputEntry.setStatus("current")
_VlsTxOutputIndex_Type = Integer32
_VlsTxOutputIndex_Object = MibTableColumn
vlsTxOutputIndex = _VlsTxOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 34652, 5, 2, 1, 1),
    _VlsTxOutputIndex_Type()
)
vlsTxOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsTxOutputIndex.setStatus("current")
_VlsTxOutputPower_Type = VlsDeciDbm
_VlsTxOutputPower_Object = MibTableColumn
vlsTxOutputPower = _VlsTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 34652, 5, 2, 1, 2),
    _VlsTxOutputPower_Type()
)
vlsTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsTxOutputPower.setStatus("current")
_VlsTxPoutLowAlarm_Type = VlsDeciDbm
_VlsTxPoutLowAlarm_Object = MibScalar
vlsTxPoutLowAlarm = _VlsTxPoutLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 34652, 5, 3),
    _VlsTxPoutLowAlarm_Type()
)
vlsTxPoutLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsTxPoutLowAlarm.setStatus("current")
_VlsTxPoutHighAlarm_Type = VlsDeciDbm
_VlsTxPoutHighAlarm_Object = MibScalar
vlsTxPoutHighAlarm = _VlsTxPoutHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 34652, 5, 4),
    _VlsTxPoutHighAlarm_Type()
)
vlsTxPoutHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsTxPoutHighAlarm.setStatus("current")
_VlsTxInputComposite_Type = VlsDbm
_VlsTxInputComposite_Object = MibScalar
vlsTxInputComposite = _VlsTxInputComposite_Object(
    (1, 3, 6, 1, 4, 1, 34652, 5, 5),
    _VlsTxInputComposite_Type()
)
vlsTxInputComposite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsTxInputComposite.setStatus("current")
_VlsTxInputPerChannel_Type = VlsDbuv
_VlsTxInputPerChannel_Object = MibScalar
vlsTxInputPerChannel = _VlsTxInputPerChannel_Object(
    (1, 3, 6, 1, 4, 1, 34652, 5, 6),
    _VlsTxInputPerChannel_Type()
)
vlsTxInputPerChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsTxInputPerChannel.setStatus("current")
_VlsTxChannelPwrFactor_Type = VlsDeciDb
_VlsTxChannelPwrFactor_Object = MibScalar
vlsTxChannelPwrFactor = _VlsTxChannelPwrFactor_Object(
    (1, 3, 6, 1, 4, 1, 34652, 5, 7),
    _VlsTxChannelPwrFactor_Type()
)
vlsTxChannelPwrFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsTxChannelPwrFactor.setStatus("current")
_VlsTxOmi_Type = VlsPerMille
_VlsTxOmi_Object = MibScalar
vlsTxOmi = _VlsTxOmi_Object(
    (1, 3, 6, 1, 4, 1, 34652, 5, 8),
    _VlsTxOmi_Type()
)
vlsTxOmi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsTxOmi.setStatus("current")
_VlsTxAtt_Type = VlsDeciDb
_VlsTxAtt_Object = MibScalar
vlsTxAtt = _VlsTxAtt_Object(
    (1, 3, 6, 1, 4, 1, 34652, 5, 9),
    _VlsTxAtt_Type()
)
vlsTxAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsTxAtt.setStatus("current")
_VlsTxLaserCurrent_Type = VlsPercent
_VlsTxLaserCurrent_Object = MibScalar
vlsTxLaserCurrent = _VlsTxLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 34652, 5, 10),
    _VlsTxLaserCurrent_Type()
)
vlsTxLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsTxLaserCurrent.setStatus("current")
_VlsTxLaserTecCurrent_Type = VlsPercent
_VlsTxLaserTecCurrent_Object = MibScalar
vlsTxLaserTecCurrent = _VlsTxLaserTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 34652, 5, 11),
    _VlsTxLaserTecCurrent_Type()
)
vlsTxLaserTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsTxLaserTecCurrent.setStatus("current")
_VlsTxLaserPower_Type = VlsDeciDbm
_VlsTxLaserPower_Object = MibScalar
vlsTxLaserPower = _VlsTxLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 34652, 5, 12),
    _VlsTxLaserPower_Type()
)
vlsTxLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsTxLaserPower.setStatus("current")
_VlsTxLaserTemperature_Type = VlsDeciCelsius
_VlsTxLaserTemperature_Object = MibScalar
vlsTxLaserTemperature = _VlsTxLaserTemperature_Object(
    (1, 3, 6, 1, 4, 1, 34652, 5, 13),
    _VlsTxLaserTemperature_Type()
)
vlsTxLaserTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlsTxLaserTemperature.setStatus("current")
_VlsTxAgc_Type = VlsOnOff
_VlsTxAgc_Object = MibScalar
vlsTxAgc = _VlsTxAgc_Object(
    (1, 3, 6, 1, 4, 1, 34652, 5, 14),
    _VlsTxAgc_Type()
)
vlsTxAgc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsTxAgc.setStatus("current")
_VlsTxSetOmi_Type = VlsPerMille
_VlsTxSetOmi_Object = MibScalar
vlsTxSetOmi = _VlsTxSetOmi_Object(
    (1, 3, 6, 1, 4, 1, 34652, 5, 15),
    _VlsTxSetOmi_Type()
)
vlsTxSetOmi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsTxSetOmi.setStatus("current")
_VlsTxSetAtt_Type = VlsDeciDb
_VlsTxSetAtt_Object = MibScalar
vlsTxSetAtt = _VlsTxSetAtt_Object(
    (1, 3, 6, 1, 4, 1, 34652, 5, 16),
    _VlsTxSetAtt_Type()
)
vlsTxSetAtt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsTxSetAtt.setStatus("current")
_VlsTxSetSbsThreshold_Type = VlsDbm
_VlsTxSetSbsThreshold_Object = MibScalar
vlsTxSetSbsThreshold = _VlsTxSetSbsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 34652, 5, 17),
    _VlsTxSetSbsThreshold_Type()
)
vlsTxSetSbsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlsTxSetSbsThreshold.setStatus("current")
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
    ("VOLIUS-OT-MIB", "vlsLastEventCode")
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
    "VOLIUS-OT-MIB",
    **{"VlsDbm": VlsDbm,
       "VlsDbuv": VlsDbuv,
       "VlsDeciCelsius": VlsDeciCelsius,
       "VlsDeciDb": VlsDeciDb,
       "VlsDeciDbm": VlsDeciDbm,
       "VlsDeciDbo": VlsDeciDbo,
       "VlsEvent": VlsEvent,
       "VlsMilliAmp": VlsMilliAmp,
       "VlsMillivolt": VlsMillivolt,
       "VlsOnOff": VlsOnOff,
       "VlsPerMille": VlsPerMille,
       "VlsPercent": VlsPercent,
       "VlsRPM": VlsRPM,
       "volius": volius,
       "vlsGlobalModule": vlsGlobalModule,
       "vlsSystem": vlsSystem,
       "vlsSystemGeneral": vlsSystemGeneral,
       "vlsModelName": vlsModelName,
       "vlsSerialNumber": vlsSerialNumber,
       "vlsFirmwareVersion": vlsFirmwareVersion,
       "vlsBootLoaderVersion": vlsBootLoaderVersion,
       "vlsDateAndTime": vlsDateAndTime,
       "vlsTimeZone": vlsTimeZone,
       "vlsCaseTemperature": vlsCaseTemperature,
       "vlsFanSpeed": vlsFanSpeed,
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
       "vlsHttpPort": vlsHttpPort,
       "vlsHttpEnabled": vlsHttpEnabled,
       "vlsHttpPasswordEnabled": vlsHttpPasswordEnabled,
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
       "vlsOpticalSwitch": vlsOpticalSwitch,
       "vlsCatvTransmitter": vlsCatvTransmitter,
       "vlsTxEmissionState": vlsTxEmissionState,
       "vlsTxOutputTable": vlsTxOutputTable,
       "vlsTxOutputEntry": vlsTxOutputEntry,
       "vlsTxOutputIndex": vlsTxOutputIndex,
       "vlsTxOutputPower": vlsTxOutputPower,
       "vlsTxPoutLowAlarm": vlsTxPoutLowAlarm,
       "vlsTxPoutHighAlarm": vlsTxPoutHighAlarm,
       "vlsTxInputComposite": vlsTxInputComposite,
       "vlsTxInputPerChannel": vlsTxInputPerChannel,
       "vlsTxChannelPwrFactor": vlsTxChannelPwrFactor,
       "vlsTxOmi": vlsTxOmi,
       "vlsTxAtt": vlsTxAtt,
       "vlsTxLaserCurrent": vlsTxLaserCurrent,
       "vlsTxLaserTecCurrent": vlsTxLaserTecCurrent,
       "vlsTxLaserPower": vlsTxLaserPower,
       "vlsTxLaserTemperature": vlsTxLaserTemperature,
       "vlsTxAgc": vlsTxAgc,
       "vlsTxSetOmi": vlsTxSetOmi,
       "vlsTxSetAtt": vlsTxSetAtt,
       "vlsTxSetSbsThreshold": vlsTxSetSbsThreshold,
       "vlsOpticalReceiver": vlsOpticalReceiver,
       "vlsCabinetMonitor": vlsCabinetMonitor,
       "vlsUpsMonitor": vlsUpsMonitor}
)
