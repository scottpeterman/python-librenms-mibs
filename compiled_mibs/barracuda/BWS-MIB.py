# SNMP MIB module (BWS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\barracuda\BWS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:48 2025
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

(barracuda,) = mibBuilder.importSymbols(
    "BARRACUDA-REF",
    "barracuda")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

bws = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20632, 8)
)
if mibBuilder.loadTexts:
    bws.setRevisions(
        ("2019-02-12 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bwstraps_ObjectIdentity = ObjectIdentity
bwstraps = _Bwstraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1)
)
_TotalApplications_Type = Integer32
_TotalApplications_Object = MibScalar
totalApplications = _TotalApplications_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 2),
    _TotalApplications_Type()
)
totalApplications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalApplications.setStatus("current")
_TotalServers_Type = Integer32
_TotalServers_Object = MibScalar
totalServers = _TotalServers_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 3),
    _TotalServers_Type()
)
totalServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalServers.setStatus("current")
_TotalAttacks_Type = Integer32
_TotalAttacks_Object = MibScalar
totalAttacks = _TotalAttacks_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 4),
    _TotalAttacks_Type()
)
totalAttacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalAttacks.setStatus("current")
_ActiveApplications_Type = Integer32
_ActiveApplications_Object = MibScalar
activeApplications = _ActiveApplications_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 5),
    _ActiveApplications_Type()
)
activeApplications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeApplications.setStatus("current")
_ActiveServers_Type = Integer32
_ActiveServers_Object = MibScalar
activeServers = _ActiveServers_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 6),
    _ActiveServers_Type()
)
activeServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeServers.setStatus("current")
_BwsMessage_Type = OctetString
_BwsMessage_Object = MibScalar
bwsMessage = _BwsMessage_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 7),
    _BwsMessage_Type()
)
bwsMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bwsMessage.setStatus("current")
_SystemLoad_Type = Integer32
_SystemLoad_Object = MibScalar
systemLoad = _SystemLoad_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 8),
    _SystemLoad_Type()
)
systemLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemLoad.setStatus("current")
_CpuFanSpeed_Type = Integer32
_CpuFanSpeed_Object = MibScalar
cpuFanSpeed = _CpuFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 9),
    _CpuFanSpeed_Type()
)
cpuFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFanSpeed.setStatus("current")
_SystemFanSpeed_Type = Integer32
_SystemFanSpeed_Object = MibScalar
systemFanSpeed = _SystemFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 10),
    _SystemFanSpeed_Type()
)
systemFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFanSpeed.setStatus("current")
_CpuTemperature_Type = Integer32
_CpuTemperature_Object = MibScalar
cpuTemperature = _CpuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 11),
    _CpuTemperature_Type()
)
cpuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTemperature.setStatus("current")
_FirmwareStorage_Type = Integer32
_FirmwareStorage_Object = MibScalar
firmwareStorage = _FirmwareStorage_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 12),
    _FirmwareStorage_Type()
)
firmwareStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareStorage.setStatus("current")
_LogStorage_Type = Integer32
_LogStorage_Object = MibScalar
logStorage = _LogStorage_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 13),
    _LogStorage_Type()
)
logStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logStorage.setStatus("current")
_HighAvailabilityStatus_Type = OctetString
_HighAvailabilityStatus_Object = MibScalar
highAvailabilityStatus = _HighAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 14),
    _HighAvailabilityStatus_Type()
)
highAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highAvailabilityStatus.setStatus("current")
_OperationalMode_Type = OctetString
_OperationalMode_Object = MibScalar
operationalMode = _OperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 15),
    _OperationalMode_Type()
)
operationalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalMode.setStatus("current")
_DataPathStatus_Type = OctetString
_DataPathStatus_Object = MibScalar
dataPathStatus = _DataPathStatus_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 16),
    _DataPathStatus_Type()
)
dataPathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPathStatus.setStatus("current")
_LinkStatus_Type = OctetString
_LinkStatus_Object = MibScalar
linkStatus = _LinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 17),
    _LinkStatus_Type()
)
linkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatus.setStatus("current")
_VipStatus_Type = OctetString
_VipStatus_Object = MibScalar
vipStatus = _VipStatus_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 18),
    _VipStatus_Type()
)
vipStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vipStatus.setStatus("current")
_MemUtilization_Type = OctetString
_MemUtilization_Object = MibScalar
memUtilization = _MemUtilization_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 19),
    _MemUtilization_Type()
)
memUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memUtilization.setStatus("current")
_CpuUtilization_Type = OctetString
_CpuUtilization_Object = MibScalar
cpuUtilization = _CpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 20),
    _CpuUtilization_Type()
)
cpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilization.setStatus("current")
_TotalBandwidth_Type = OctetString
_TotalBandwidth_Object = MibScalar
totalBandwidth = _TotalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 21),
    _TotalBandwidth_Type()
)
totalBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBandwidth.setStatus("current")
_Uptime_Type = OctetString
_Uptime_Object = MibScalar
uptime = _Uptime_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 22),
    _Uptime_Type()
)
uptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uptime.setStatus("current")
_TotalMem_Type = OctetString
_TotalMem_Object = MibScalar
totalMem = _TotalMem_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 23),
    _TotalMem_Type()
)
totalMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalMem.setStatus("current")
_FreeMem_Type = OctetString
_FreeMem_Object = MibScalar
freeMem = _FreeMem_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 24),
    _FreeMem_Type()
)
freeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeMem.setStatus("current")


class _CurrentFirmwareVersion_Type(OctetString):
    """Custom type currentFirmwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CurrentFirmwareVersion_Type.__name__ = "OctetString"
_CurrentFirmwareVersion_Object = MibScalar
currentFirmwareVersion = _CurrentFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 25),
    _CurrentFirmwareVersion_Type()
)
currentFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFirmwareVersion.setStatus("current")


class _VirusDefUpdates_Type(OctetString):
    """Custom type virusDefUpdates based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_VirusDefUpdates_Type.__name__ = "OctetString"
_VirusDefUpdates_Object = MibScalar
virusDefUpdates = _VirusDefUpdates_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 26),
    _VirusDefUpdates_Type()
)
virusDefUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virusDefUpdates.setStatus("current")


class _SecurityDefUpdates_Type(OctetString):
    """Custom type securityDefUpdates based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SecurityDefUpdates_Type.__name__ = "OctetString"
_SecurityDefUpdates_Object = MibScalar
securityDefUpdates = _SecurityDefUpdates_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 27),
    _SecurityDefUpdates_Type()
)
securityDefUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityDefUpdates.setStatus("current")


class _SystemSerialNumber_Type(OctetString):
    """Custom type systemSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SystemSerialNumber_Type.__name__ = "OctetString"
_SystemSerialNumber_Object = MibScalar
systemSerialNumber = _SystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 28),
    _SystemSerialNumber_Type()
)
systemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSerialNumber.setStatus("current")
_BwsStats_ObjectIdentity = ObjectIdentity
bwsStats = _BwsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50)
)
_BwsHttpProxyStatsTable_Object = MibTable
bwsHttpProxyStatsTable = _BwsHttpProxyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 1)
)
if mibBuilder.loadTexts:
    bwsHttpProxyStatsTable.setStatus("current")
_BwsHttpProxyStatsEntry_Object = MibTableRow
bwsHttpProxyStatsEntry = _BwsHttpProxyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 1, 1)
)
bwsHttpProxyStatsEntry.setIndexNames(
    (0, "BWS-MIB", "httpProxyAddressType"),
    (0, "BWS-MIB", "httpProxyAddress"),
    (0, "BWS-MIB", "httpProxyPort"),
)
if mibBuilder.loadTexts:
    bwsHttpProxyStatsEntry.setStatus("current")
_HttpProxyAddressType_Type = InetAddressType
_HttpProxyAddressType_Object = MibTableColumn
httpProxyAddressType = _HttpProxyAddressType_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 1, 1, 1),
    _HttpProxyAddressType_Type()
)
httpProxyAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    httpProxyAddressType.setStatus("current")
_HttpProxyAddress_Type = InetAddress
_HttpProxyAddress_Object = MibTableColumn
httpProxyAddress = _HttpProxyAddress_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 1, 1, 2),
    _HttpProxyAddress_Type()
)
httpProxyAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    httpProxyAddress.setStatus("current")
_HttpProxyPort_Type = InetPortNumber
_HttpProxyPort_Object = MibTableColumn
httpProxyPort = _HttpProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 1, 1, 3),
    _HttpProxyPort_Type()
)
httpProxyPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    httpProxyPort.setStatus("current")
_HttpProxyActiveConn_Type = Counter32
_HttpProxyActiveConn_Object = MibTableColumn
httpProxyActiveConn = _HttpProxyActiveConn_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 1, 1, 4),
    _HttpProxyActiveConn_Type()
)
httpProxyActiveConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpProxyActiveConn.setStatus("current")
_HttpProxyTotalConn_Type = Counter32
_HttpProxyTotalConn_Object = MibTableColumn
httpProxyTotalConn = _HttpProxyTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 1, 1, 5),
    _HttpProxyTotalConn_Type()
)
httpProxyTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpProxyTotalConn.setStatus("current")
_HttpProxyTotalReq_Type = Counter32
_HttpProxyTotalReq_Object = MibTableColumn
httpProxyTotalReq = _HttpProxyTotalReq_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 1, 1, 6),
    _HttpProxyTotalReq_Type()
)
httpProxyTotalReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpProxyTotalReq.setStatus("current")
_HttpProxyServerReq_Type = Counter32
_HttpProxyServerReq_Object = MibTableColumn
httpProxyServerReq = _HttpProxyServerReq_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 1, 1, 7),
    _HttpProxyServerReq_Type()
)
httpProxyServerReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpProxyServerReq.setStatus("current")
_HttpProxyServerErr_Type = Counter32
_HttpProxyServerErr_Object = MibTableColumn
httpProxyServerErr = _HttpProxyServerErr_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 1, 1, 8),
    _HttpProxyServerErr_Type()
)
httpProxyServerErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpProxyServerErr.setStatus("current")
_HttpProxyClientAbrt_Type = Counter32
_HttpProxyClientAbrt_Object = MibTableColumn
httpProxyClientAbrt = _HttpProxyClientAbrt_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 1, 1, 9),
    _HttpProxyClientAbrt_Type()
)
httpProxyClientAbrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpProxyClientAbrt.setStatus("current")
_HttpProxyServerAbrt_Type = Counter32
_HttpProxyServerAbrt_Object = MibTableColumn
httpProxyServerAbrt = _HttpProxyServerAbrt_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 1, 1, 10),
    _HttpProxyServerAbrt_Type()
)
httpProxyServerAbrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpProxyServerAbrt.setStatus("current")
_HttpProxySessionTimeOut_Type = Counter32
_HttpProxySessionTimeOut_Object = MibTableColumn
httpProxySessionTimeOut = _HttpProxySessionTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 1, 1, 11),
    _HttpProxySessionTimeOut_Type()
)
httpProxySessionTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpProxySessionTimeOut.setStatus("current")
_HttpProxyParseErr_Type = Counter32
_HttpProxyParseErr_Object = MibTableColumn
httpProxyParseErr = _HttpProxyParseErr_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 1, 1, 12),
    _HttpProxyParseErr_Type()
)
httpProxyParseErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpProxyParseErr.setStatus("current")
_HttpProxyUnknownRsp_Type = Counter32
_HttpProxyUnknownRsp_Object = MibTableColumn
httpProxyUnknownRsp = _HttpProxyUnknownRsp_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 1, 1, 13),
    _HttpProxyUnknownRsp_Type()
)
httpProxyUnknownRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpProxyUnknownRsp.setStatus("current")
_HttpProxyInBytes_Type = Counter64
_HttpProxyInBytes_Object = MibTableColumn
httpProxyInBytes = _HttpProxyInBytes_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 1, 1, 14),
    _HttpProxyInBytes_Type()
)
httpProxyInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpProxyInBytes.setStatus("current")
_HttpProxyOutBytes_Type = Counter64
_HttpProxyOutBytes_Object = MibTableColumn
httpProxyOutBytes = _HttpProxyOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 1, 1, 15),
    _HttpProxyOutBytes_Type()
)
httpProxyOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpProxyOutBytes.setStatus("current")
_HttpProxyWAFBlockedIntrusions_Type = Counter32
_HttpProxyWAFBlockedIntrusions_Object = MibTableColumn
httpProxyWAFBlockedIntrusions = _HttpProxyWAFBlockedIntrusions_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 1, 1, 16),
    _HttpProxyWAFBlockedIntrusions_Type()
)
httpProxyWAFBlockedIntrusions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpProxyWAFBlockedIntrusions.setStatus("current")
_HttpProxyWAFMonitoredIntrusions_Type = Counter32
_HttpProxyWAFMonitoredIntrusions_Object = MibTableColumn
httpProxyWAFMonitoredIntrusions = _HttpProxyWAFMonitoredIntrusions_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 1, 1, 17),
    _HttpProxyWAFMonitoredIntrusions_Type()
)
httpProxyWAFMonitoredIntrusions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpProxyWAFMonitoredIntrusions.setStatus("current")
_HttpProxyWAFWarnings_Type = Counter32
_HttpProxyWAFWarnings_Object = MibTableColumn
httpProxyWAFWarnings = _HttpProxyWAFWarnings_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 1, 1, 18),
    _HttpProxyWAFWarnings_Type()
)
httpProxyWAFWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpProxyWAFWarnings.setStatus("current")
_BwsSslProxyStatsTable_Object = MibTable
bwsSslProxyStatsTable = _BwsSslProxyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 2)
)
if mibBuilder.loadTexts:
    bwsSslProxyStatsTable.setStatus("current")
_BwsSslProxyStatsEntry_Object = MibTableRow
bwsSslProxyStatsEntry = _BwsSslProxyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 2, 1)
)
bwsSslProxyStatsEntry.setIndexNames(
    (0, "BWS-MIB", "sslProxyAddressType"),
    (0, "BWS-MIB", "sslProxyAddress"),
    (0, "BWS-MIB", "sslProxyPort"),
)
if mibBuilder.loadTexts:
    bwsSslProxyStatsEntry.setStatus("current")
_SslProxyAddressType_Type = InetAddressType
_SslProxyAddressType_Object = MibTableColumn
sslProxyAddressType = _SslProxyAddressType_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 2, 1, 1),
    _SslProxyAddressType_Type()
)
sslProxyAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sslProxyAddressType.setStatus("current")
_SslProxyAddress_Type = InetAddress
_SslProxyAddress_Object = MibTableColumn
sslProxyAddress = _SslProxyAddress_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 2, 1, 2),
    _SslProxyAddress_Type()
)
sslProxyAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sslProxyAddress.setStatus("current")
_SslProxyPort_Type = InetPortNumber
_SslProxyPort_Object = MibTableColumn
sslProxyPort = _SslProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 2, 1, 3),
    _SslProxyPort_Type()
)
sslProxyPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sslProxyPort.setStatus("current")
_SslProxyActiveConn_Type = Counter32
_SslProxyActiveConn_Object = MibTableColumn
sslProxyActiveConn = _SslProxyActiveConn_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 2, 1, 4),
    _SslProxyActiveConn_Type()
)
sslProxyActiveConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyActiveConn.setStatus("current")
_SslProxyFullHandshakes_Type = Counter32
_SslProxyFullHandshakes_Object = MibTableColumn
sslProxyFullHandshakes = _SslProxyFullHandshakes_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 2, 1, 5),
    _SslProxyFullHandshakes_Type()
)
sslProxyFullHandshakes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyFullHandshakes.setStatus("current")
_SslProxyResumptionHandshakes_Type = Counter32
_SslProxyResumptionHandshakes_Object = MibTableColumn
sslProxyResumptionHandshakes = _SslProxyResumptionHandshakes_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 2, 1, 6),
    _SslProxyResumptionHandshakes_Type()
)
sslProxyResumptionHandshakes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyResumptionHandshakes.setStatus("current")
_SslProxyHandshakeAttempts_Type = Counter32
_SslProxyHandshakeAttempts_Object = MibTableColumn
sslProxyHandshakeAttempts = _SslProxyHandshakeAttempts_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 2, 1, 7),
    _SslProxyHandshakeAttempts_Type()
)
sslProxyHandshakeAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyHandshakeAttempts.setStatus("current")
_SslProxyCacheHits_Type = Counter32
_SslProxyCacheHits_Object = MibTableColumn
sslProxyCacheHits = _SslProxyCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 2, 1, 8),
    _SslProxyCacheHits_Type()
)
sslProxyCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyCacheHits.setStatus("current")
_SslProxyCacheMiss_Type = Counter32
_SslProxyCacheMiss_Object = MibTableColumn
sslProxyCacheMiss = _SslProxyCacheMiss_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 2, 1, 9),
    _SslProxyCacheMiss_Type()
)
sslProxyCacheMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyCacheMiss.setStatus("current")
_SslProxyCacheTimeouts_Type = Counter32
_SslProxyCacheTimeouts_Object = MibTableColumn
sslProxyCacheTimeouts = _SslProxyCacheTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 2, 1, 10),
    _SslProxyCacheTimeouts_Type()
)
sslProxyCacheTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyCacheTimeouts.setStatus("current")
_SslProxyErrPms_Type = Counter32
_SslProxyErrPms_Object = MibTableColumn
sslProxyErrPms = _SslProxyErrPms_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 2, 1, 11),
    _SslProxyErrPms_Type()
)
sslProxyErrPms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyErrPms.setStatus("current")
_SslProxyAuthBadCertErr_Type = Counter32
_SslProxyAuthBadCertErr_Object = MibTableColumn
sslProxyAuthBadCertErr = _SslProxyAuthBadCertErr_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 2, 1, 12),
    _SslProxyAuthBadCertErr_Type()
)
sslProxyAuthBadCertErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyAuthBadCertErr.setStatus("current")
_SslProxyAuthBadCNErr_Type = Counter32
_SslProxyAuthBadCNErr_Object = MibTableColumn
sslProxyAuthBadCNErr = _SslProxyAuthBadCNErr_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 2, 1, 13),
    _SslProxyAuthBadCNErr_Type()
)
sslProxyAuthBadCNErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyAuthBadCNErr.setStatus("current")
_SslProxyBadDNCErr_Type = Counter32
_SslProxyBadDNCErr_Object = MibTableColumn
sslProxyBadDNCErr = _SslProxyBadDNCErr_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 2, 1, 14),
    _SslProxyBadDNCErr_Type()
)
sslProxyBadDNCErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyBadDNCErr.setStatus("current")
_SslProxyBadCRLErr_Type = Counter32
_SslProxyBadCRLErr_Object = MibTableColumn
sslProxyBadCRLErr = _SslProxyBadCRLErr_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 2, 1, 15),
    _SslProxyBadCRLErr_Type()
)
sslProxyBadCRLErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyBadCRLErr.setStatus("current")
_SslProxyInBytes_Type = Counter64
_SslProxyInBytes_Object = MibTableColumn
sslProxyInBytes = _SslProxyInBytes_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 2, 1, 16),
    _SslProxyInBytes_Type()
)
sslProxyInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyInBytes.setStatus("current")
_SslProxyOutBytes_Type = Counter64
_SslProxyOutBytes_Object = MibTableColumn
sslProxyOutBytes = _SslProxyOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 2, 1, 17),
    _SslProxyOutBytes_Type()
)
sslProxyOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyOutBytes.setStatus("current")
_SslProxyTotalReq_Type = Counter32
_SslProxyTotalReq_Object = MibTableColumn
sslProxyTotalReq = _SslProxyTotalReq_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 2, 1, 18),
    _SslProxyTotalReq_Type()
)
sslProxyTotalReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyTotalReq.setStatus("current")
_SslProxyTotalConn_Type = Counter32
_SslProxyTotalConn_Object = MibTableColumn
sslProxyTotalConn = _SslProxyTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 2, 1, 19),
    _SslProxyTotalConn_Type()
)
sslProxyTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyTotalConn.setStatus("current")
_SslProxyCurrentConn_Type = Counter32
_SslProxyCurrentConn_Object = MibTableColumn
sslProxyCurrentConn = _SslProxyCurrentConn_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 2, 1, 20),
    _SslProxyCurrentConn_Type()
)
sslProxyCurrentConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyCurrentConn.setStatus("current")
_BwsCompressionStatsTable_Object = MibTable
bwsCompressionStatsTable = _BwsCompressionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 3)
)
if mibBuilder.loadTexts:
    bwsCompressionStatsTable.setStatus("current")
_BwsCompressionStatsEntry_Object = MibTableRow
bwsCompressionStatsEntry = _BwsCompressionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 3, 1)
)
bwsCompressionStatsEntry.setIndexNames(
    (0, "BWS-MIB", "webCmprProtocol"),
    (0, "BWS-MIB", "webCmprAddressType"),
    (0, "BWS-MIB", "webCmprAddress"),
    (0, "BWS-MIB", "webCmprPort"),
)
if mibBuilder.loadTexts:
    bwsCompressionStatsEntry.setStatus("current")


class _WebCmprProtocol_Type(Integer32):
    """Custom type webCmprProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WebCmprProtocol_Type.__name__ = "Integer32"
_WebCmprProtocol_Object = MibTableColumn
webCmprProtocol = _WebCmprProtocol_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 3, 1, 1),
    _WebCmprProtocol_Type()
)
webCmprProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    webCmprProtocol.setStatus("current")
_WebCmprAddressType_Type = InetAddressType
_WebCmprAddressType_Object = MibTableColumn
webCmprAddressType = _WebCmprAddressType_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 3, 1, 2),
    _WebCmprAddressType_Type()
)
webCmprAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    webCmprAddressType.setStatus("current")
_WebCmprAddress_Type = InetAddress
_WebCmprAddress_Object = MibTableColumn
webCmprAddress = _WebCmprAddress_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 3, 1, 3),
    _WebCmprAddress_Type()
)
webCmprAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    webCmprAddress.setStatus("current")
_WebCmprPort_Type = InetPortNumber
_WebCmprPort_Object = MibTableColumn
webCmprPort = _WebCmprPort_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 3, 1, 4),
    _WebCmprPort_Type()
)
webCmprPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    webCmprPort.setStatus("current")
_WebCmprNoOfReqCompressed_Type = Counter32
_WebCmprNoOfReqCompressed_Object = MibTableColumn
webCmprNoOfReqCompressed = _WebCmprNoOfReqCompressed_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 3, 1, 5),
    _WebCmprNoOfReqCompressed_Type()
)
webCmprNoOfReqCompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCmprNoOfReqCompressed.setStatus("current")
_WebCmprCompressibleDataSize_Type = Counter32
_WebCmprCompressibleDataSize_Object = MibTableColumn
webCmprCompressibleDataSize = _WebCmprCompressibleDataSize_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 3, 1, 6),
    _WebCmprCompressibleDataSize_Type()
)
webCmprCompressibleDataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCmprCompressibleDataSize.setStatus("current")
_WebCmprCompressedDataSize_Type = Counter32
_WebCmprCompressedDataSize_Object = MibTableColumn
webCmprCompressedDataSize = _WebCmprCompressedDataSize_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 3, 1, 7),
    _WebCmprCompressedDataSize_Type()
)
webCmprCompressedDataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCmprCompressedDataSize.setStatus("current")
_BwsCacheStatsTable_Object = MibTable
bwsCacheStatsTable = _BwsCacheStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 4)
)
if mibBuilder.loadTexts:
    bwsCacheStatsTable.setStatus("current")
_BwsCacheStatsEntry_Object = MibTableRow
bwsCacheStatsEntry = _BwsCacheStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 4, 1)
)
bwsCacheStatsEntry.setIndexNames(
    (0, "BWS-MIB", "webCacheProtocol"),
    (0, "BWS-MIB", "webCacheAddressType"),
    (0, "BWS-MIB", "webCacheAddress"),
    (0, "BWS-MIB", "webCachePort"),
)
if mibBuilder.loadTexts:
    bwsCacheStatsEntry.setStatus("current")


class _WebCacheProtocol_Type(Integer32):
    """Custom type webCacheProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WebCacheProtocol_Type.__name__ = "Integer32"
_WebCacheProtocol_Object = MibTableColumn
webCacheProtocol = _WebCacheProtocol_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 4, 1, 1),
    _WebCacheProtocol_Type()
)
webCacheProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    webCacheProtocol.setStatus("current")
_WebCacheAddressType_Type = InetAddressType
_WebCacheAddressType_Object = MibTableColumn
webCacheAddressType = _WebCacheAddressType_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 4, 1, 2),
    _WebCacheAddressType_Type()
)
webCacheAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    webCacheAddressType.setStatus("current")
_WebCacheAddress_Type = InetAddress
_WebCacheAddress_Object = MibTableColumn
webCacheAddress = _WebCacheAddress_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 4, 1, 3),
    _WebCacheAddress_Type()
)
webCacheAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    webCacheAddress.setStatus("current")
_WebCachePort_Type = InetPortNumber
_WebCachePort_Object = MibTableColumn
webCachePort = _WebCachePort_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 4, 1, 4),
    _WebCachePort_Type()
)
webCachePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    webCachePort.setStatus("current")
_WebCacheHits_Type = Counter32
_WebCacheHits_Object = MibTableColumn
webCacheHits = _WebCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 4, 1, 5),
    _WebCacheHits_Type()
)
webCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheHits.setStatus("current")
_WebCacheMiss_Type = Counter32
_WebCacheMiss_Object = MibTableColumn
webCacheMiss = _WebCacheMiss_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 4, 1, 6),
    _WebCacheMiss_Type()
)
webCacheMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheMiss.setStatus("current")
_WebCacheStale_Type = Counter32
_WebCacheStale_Object = MibTableColumn
webCacheStale = _WebCacheStale_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 4, 1, 7),
    _WebCacheStale_Type()
)
webCacheStale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheStale.setStatus("current")
_WebCacheCacheableRes_Type = Counter32
_WebCacheCacheableRes_Object = MibTableColumn
webCacheCacheableRes = _WebCacheCacheableRes_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 4, 1, 8),
    _WebCacheCacheableRes_Type()
)
webCacheCacheableRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheCacheableRes.setStatus("current")
_WebCacheReq_Type = Counter32
_WebCacheReq_Object = MibTableColumn
webCacheReq = _WebCacheReq_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 4, 1, 9),
    _WebCacheReq_Type()
)
webCacheReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheReq.setStatus("current")
_WebCacheCachedObjects_Type = Counter32
_WebCacheCachedObjects_Object = MibTableColumn
webCacheCachedObjects = _WebCacheCachedObjects_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 4, 1, 10),
    _WebCacheCachedObjects_Type()
)
webCacheCachedObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheCachedObjects.setStatus("current")
_WebCacheLongHdrs_Type = Counter32
_WebCacheLongHdrs_Object = MibTableColumn
webCacheLongHdrs = _WebCacheLongHdrs_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 4, 1, 11),
    _WebCacheLongHdrs_Type()
)
webCacheLongHdrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheLongHdrs.setStatus("current")
_WebCacheBytesOut_Type = Counter32
_WebCacheBytesOut_Object = MibTableColumn
webCacheBytesOut = _WebCacheBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 4, 1, 12),
    _WebCacheBytesOut_Type()
)
webCacheBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webCacheBytesOut.setStatus("current")
_BwsHttpSrvrStatsTable_Object = MibTable
bwsHttpSrvrStatsTable = _BwsHttpSrvrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5)
)
if mibBuilder.loadTexts:
    bwsHttpSrvrStatsTable.setStatus("current")
_BwsHttpSrvrStatsEntry_Object = MibTableRow
bwsHttpSrvrStatsEntry = _BwsHttpSrvrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1)
)
bwsHttpSrvrStatsEntry.setIndexNames(
    (0, "BWS-MIB", "httpSrvrSrvcAddressType"),
    (0, "BWS-MIB", "httpSrvrSrvcAddress"),
    (0, "BWS-MIB", "httpSrvrSrvcPort"),
    (0, "BWS-MIB", "httpSrvrAddressType"),
    (0, "BWS-MIB", "httpSrvrAddress"),
    (0, "BWS-MIB", "httpSrvrPort"),
)
if mibBuilder.loadTexts:
    bwsHttpSrvrStatsEntry.setStatus("current")
_HttpSrvrSrvcAddressType_Type = InetAddressType
_HttpSrvrSrvcAddressType_Object = MibTableColumn
httpSrvrSrvcAddressType = _HttpSrvrSrvcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 1),
    _HttpSrvrSrvcAddressType_Type()
)
httpSrvrSrvcAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    httpSrvrSrvcAddressType.setStatus("current")
_HttpSrvrSrvcAddress_Type = InetAddress
_HttpSrvrSrvcAddress_Object = MibTableColumn
httpSrvrSrvcAddress = _HttpSrvrSrvcAddress_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 2),
    _HttpSrvrSrvcAddress_Type()
)
httpSrvrSrvcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    httpSrvrSrvcAddress.setStatus("current")
_HttpSrvrSrvcPort_Type = InetPortNumber
_HttpSrvrSrvcPort_Object = MibTableColumn
httpSrvrSrvcPort = _HttpSrvrSrvcPort_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 3),
    _HttpSrvrSrvcPort_Type()
)
httpSrvrSrvcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    httpSrvrSrvcPort.setStatus("current")
_HttpSrvrAddressType_Type = InetAddressType
_HttpSrvrAddressType_Object = MibTableColumn
httpSrvrAddressType = _HttpSrvrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 4),
    _HttpSrvrAddressType_Type()
)
httpSrvrAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    httpSrvrAddressType.setStatus("current")
_HttpSrvrAddress_Type = InetAddress
_HttpSrvrAddress_Object = MibTableColumn
httpSrvrAddress = _HttpSrvrAddress_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 5),
    _HttpSrvrAddress_Type()
)
httpSrvrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    httpSrvrAddress.setStatus("current")
_HttpSrvrPort_Type = InetPortNumber
_HttpSrvrPort_Object = MibTableColumn
httpSrvrPort = _HttpSrvrPort_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 6),
    _HttpSrvrPort_Type()
)
httpSrvrPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    httpSrvrPort.setStatus("current")
_HttpSrvrTotReqAccepted_Type = Counter32
_HttpSrvrTotReqAccepted_Object = MibTableColumn
httpSrvrTotReqAccepted = _HttpSrvrTotReqAccepted_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 7),
    _HttpSrvrTotReqAccepted_Type()
)
httpSrvrTotReqAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpSrvrTotReqAccepted.setStatus("current")
_HttpSrvrTotReqActive_Type = Counter32
_HttpSrvrTotReqActive_Object = MibTableColumn
httpSrvrTotReqActive = _HttpSrvrTotReqActive_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 8),
    _HttpSrvrTotReqActive_Type()
)
httpSrvrTotReqActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpSrvrTotReqActive.setStatus("current")
_HttpSrvrTotReqRejected_Type = Counter32
_HttpSrvrTotReqRejected_Object = MibTableColumn
httpSrvrTotReqRejected = _HttpSrvrTotReqRejected_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 9),
    _HttpSrvrTotReqRejected_Type()
)
httpSrvrTotReqRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpSrvrTotReqRejected.setStatus("current")
_HttpSrvrTotSuccess_Type = Counter32
_HttpSrvrTotSuccess_Object = MibTableColumn
httpSrvrTotSuccess = _HttpSrvrTotSuccess_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 10),
    _HttpSrvrTotSuccess_Type()
)
httpSrvrTotSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpSrvrTotSuccess.setStatus("current")
_HttpSrvrTotRefused_Type = Counter32
_HttpSrvrTotRefused_Object = MibTableColumn
httpSrvrTotRefused = _HttpSrvrTotRefused_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 11),
    _HttpSrvrTotRefused_Type()
)
httpSrvrTotRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpSrvrTotRefused.setStatus("current")
_HttpSrvrTotTimedout_Type = Counter32
_HttpSrvrTotTimedout_Object = MibTableColumn
httpSrvrTotTimedout = _HttpSrvrTotTimedout_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 12),
    _HttpSrvrTotTimedout_Type()
)
httpSrvrTotTimedout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpSrvrTotTimedout.setStatus("current")
_HttpSrvrAvgReqPerConn_Type = Counter32
_HttpSrvrAvgReqPerConn_Object = MibTableColumn
httpSrvrAvgReqPerConn = _HttpSrvrAvgReqPerConn_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 13),
    _HttpSrvrAvgReqPerConn_Type()
)
httpSrvrAvgReqPerConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpSrvrAvgReqPerConn.setStatus("current")
_HttpSrvrTotResponse_Type = Counter32
_HttpSrvrTotResponse_Object = MibTableColumn
httpSrvrTotResponse = _HttpSrvrTotResponse_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 14),
    _HttpSrvrTotResponse_Type()
)
httpSrvrTotResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpSrvrTotResponse.setStatus("current")
_HttpSrvrAvgResTime_Type = Counter32
_HttpSrvrAvgResTime_Object = MibTableColumn
httpSrvrAvgResTime = _HttpSrvrAvgResTime_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 15),
    _HttpSrvrAvgResTime_Type()
)
httpSrvrAvgResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpSrvrAvgResTime.setStatus("current")
_HttpSrvrMaxResTime_Type = Counter32
_HttpSrvrMaxResTime_Object = MibTableColumn
httpSrvrMaxResTime = _HttpSrvrMaxResTime_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 16),
    _HttpSrvrMaxResTime_Type()
)
httpSrvrMaxResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpSrvrMaxResTime.setStatus("current")
_HttpSrvrMinResTime_Type = Counter32
_HttpSrvrMinResTime_Object = MibTableColumn
httpSrvrMinResTime = _HttpSrvrMinResTime_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 17),
    _HttpSrvrMinResTime_Type()
)
httpSrvrMinResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpSrvrMinResTime.setStatus("current")
_HttpSrvrNumReqEnqueue_Type = Counter32
_HttpSrvrNumReqEnqueue_Object = MibTableColumn
httpSrvrNumReqEnqueue = _HttpSrvrNumReqEnqueue_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 18),
    _HttpSrvrNumReqEnqueue_Type()
)
httpSrvrNumReqEnqueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpSrvrNumReqEnqueue.setStatus("current")
_HttpSrvrNumFreeConn_Type = Counter32
_HttpSrvrNumFreeConn_Object = MibTableColumn
httpSrvrNumFreeConn = _HttpSrvrNumFreeConn_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 19),
    _HttpSrvrNumFreeConn_Type()
)
httpSrvrNumFreeConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpSrvrNumFreeConn.setStatus("current")
_HttpSrvrNumOpeningConn_Type = Counter32
_HttpSrvrNumOpeningConn_Object = MibTableColumn
httpSrvrNumOpeningConn = _HttpSrvrNumOpeningConn_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 20),
    _HttpSrvrNumOpeningConn_Type()
)
httpSrvrNumOpeningConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpSrvrNumOpeningConn.setStatus("current")
_HttpSrvrNumConn_Type = Counter32
_HttpSrvrNumConn_Object = MibTableColumn
httpSrvrNumConn = _HttpSrvrNumConn_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 21),
    _HttpSrvrNumConn_Type()
)
httpSrvrNumConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpSrvrNumConn.setStatus("current")
_HttpSrvrNumIBDisabled_Type = Counter32
_HttpSrvrNumIBDisabled_Object = MibTableColumn
httpSrvrNumIBDisabled = _HttpSrvrNumIBDisabled_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 22),
    _HttpSrvrNumIBDisabled_Type()
)
httpSrvrNumIBDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpSrvrNumIBDisabled.setStatus("current")
_HttpSrvrNumOOBDisabled_Type = Counter32
_HttpSrvrNumOOBDisabled_Object = MibTableColumn
httpSrvrNumOOBDisabled = _HttpSrvrNumOOBDisabled_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 23),
    _HttpSrvrNumOOBDisabled_Type()
)
httpSrvrNumOOBDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpSrvrNumOOBDisabled.setStatus("current")
_HttpSrvrNumOOBEnabled_Type = Counter32
_HttpSrvrNumOOBEnabled_Object = MibTableColumn
httpSrvrNumOOBEnabled = _HttpSrvrNumOOBEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 24),
    _HttpSrvrNumOOBEnabled_Type()
)
httpSrvrNumOOBEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpSrvrNumOOBEnabled.setStatus("current")
_HttpSrvrLastDisabledTime_Type = TimeStamp
_HttpSrvrLastDisabledTime_Object = MibTableColumn
httpSrvrLastDisabledTime = _HttpSrvrLastDisabledTime_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 25),
    _HttpSrvrLastDisabledTime_Type()
)
httpSrvrLastDisabledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpSrvrLastDisabledTime.setStatus("current")
_HttpSrvrState_Type = Integer32
_HttpSrvrState_Object = MibTableColumn
httpSrvrState = _HttpSrvrState_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 26),
    _HttpSrvrState_Type()
)
httpSrvrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpSrvrState.setStatus("current")
_HttpSrvrInBytes_Type = Counter64
_HttpSrvrInBytes_Object = MibTableColumn
httpSrvrInBytes = _HttpSrvrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 27),
    _HttpSrvrInBytes_Type()
)
httpSrvrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpSrvrInBytes.setStatus("current")
_HttpSrvrOutBytes_Type = Counter64
_HttpSrvrOutBytes_Object = MibTableColumn
httpSrvrOutBytes = _HttpSrvrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 5, 1, 28),
    _HttpSrvrOutBytes_Type()
)
httpSrvrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpSrvrOutBytes.setStatus("current")
_BwsSslSrvrStatsTable_Object = MibTable
bwsSslSrvrStatsTable = _BwsSslSrvrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6)
)
if mibBuilder.loadTexts:
    bwsSslSrvrStatsTable.setStatus("current")
_BwsSslSrvrStatsEntry_Object = MibTableRow
bwsSslSrvrStatsEntry = _BwsSslSrvrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1)
)
bwsSslSrvrStatsEntry.setIndexNames(
    (0, "BWS-MIB", "sslSrvrSrvcAddressType"),
    (0, "BWS-MIB", "sslSrvrSrvcAddress"),
    (0, "BWS-MIB", "sslSrvrSrvcPort"),
    (0, "BWS-MIB", "sslSrvrAddressType"),
    (0, "BWS-MIB", "sslSrvrAddress"),
    (0, "BWS-MIB", "sslSrvrPort"),
)
if mibBuilder.loadTexts:
    bwsSslSrvrStatsEntry.setStatus("current")
_SslSrvrSrvcAddressType_Type = InetAddressType
_SslSrvrSrvcAddressType_Object = MibTableColumn
sslSrvrSrvcAddressType = _SslSrvrSrvcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 1),
    _SslSrvrSrvcAddressType_Type()
)
sslSrvrSrvcAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sslSrvrSrvcAddressType.setStatus("current")
_SslSrvrSrvcAddress_Type = InetAddress
_SslSrvrSrvcAddress_Object = MibTableColumn
sslSrvrSrvcAddress = _SslSrvrSrvcAddress_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 2),
    _SslSrvrSrvcAddress_Type()
)
sslSrvrSrvcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sslSrvrSrvcAddress.setStatus("current")
_SslSrvrSrvcPort_Type = InetPortNumber
_SslSrvrSrvcPort_Object = MibTableColumn
sslSrvrSrvcPort = _SslSrvrSrvcPort_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 3),
    _SslSrvrSrvcPort_Type()
)
sslSrvrSrvcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sslSrvrSrvcPort.setStatus("current")
_SslSrvrAddressType_Type = InetAddressType
_SslSrvrAddressType_Object = MibTableColumn
sslSrvrAddressType = _SslSrvrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 4),
    _SslSrvrAddressType_Type()
)
sslSrvrAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sslSrvrAddressType.setStatus("current")
_SslSrvrAddress_Type = InetAddress
_SslSrvrAddress_Object = MibTableColumn
sslSrvrAddress = _SslSrvrAddress_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 5),
    _SslSrvrAddress_Type()
)
sslSrvrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sslSrvrAddress.setStatus("current")
_SslSrvrPort_Type = InetPortNumber
_SslSrvrPort_Object = MibTableColumn
sslSrvrPort = _SslSrvrPort_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 6),
    _SslSrvrPort_Type()
)
sslSrvrPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sslSrvrPort.setStatus("current")
_SslSrvrTotReqAccepted_Type = Counter32
_SslSrvrTotReqAccepted_Object = MibTableColumn
sslSrvrTotReqAccepted = _SslSrvrTotReqAccepted_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 7),
    _SslSrvrTotReqAccepted_Type()
)
sslSrvrTotReqAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSrvrTotReqAccepted.setStatus("current")
_SslSrvrTotReqActive_Type = Counter32
_SslSrvrTotReqActive_Object = MibTableColumn
sslSrvrTotReqActive = _SslSrvrTotReqActive_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 8),
    _SslSrvrTotReqActive_Type()
)
sslSrvrTotReqActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSrvrTotReqActive.setStatus("current")
_SslSrvrTotReqRejected_Type = Counter32
_SslSrvrTotReqRejected_Object = MibTableColumn
sslSrvrTotReqRejected = _SslSrvrTotReqRejected_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 9),
    _SslSrvrTotReqRejected_Type()
)
sslSrvrTotReqRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSrvrTotReqRejected.setStatus("current")
_SslSrvrTotSuccess_Type = Counter32
_SslSrvrTotSuccess_Object = MibTableColumn
sslSrvrTotSuccess = _SslSrvrTotSuccess_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 10),
    _SslSrvrTotSuccess_Type()
)
sslSrvrTotSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSrvrTotSuccess.setStatus("current")
_SslSrvrTotRefused_Type = Counter32
_SslSrvrTotRefused_Object = MibTableColumn
sslSrvrTotRefused = _SslSrvrTotRefused_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 11),
    _SslSrvrTotRefused_Type()
)
sslSrvrTotRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSrvrTotRefused.setStatus("current")
_SslSrvrTotTimedout_Type = Counter32
_SslSrvrTotTimedout_Object = MibTableColumn
sslSrvrTotTimedout = _SslSrvrTotTimedout_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 12),
    _SslSrvrTotTimedout_Type()
)
sslSrvrTotTimedout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSrvrTotTimedout.setStatus("current")
_SslSrvrAvgReqPerConn_Type = Counter32
_SslSrvrAvgReqPerConn_Object = MibTableColumn
sslSrvrAvgReqPerConn = _SslSrvrAvgReqPerConn_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 13),
    _SslSrvrAvgReqPerConn_Type()
)
sslSrvrAvgReqPerConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSrvrAvgReqPerConn.setStatus("current")
_SslSrvrTotResponse_Type = Counter32
_SslSrvrTotResponse_Object = MibTableColumn
sslSrvrTotResponse = _SslSrvrTotResponse_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 14),
    _SslSrvrTotResponse_Type()
)
sslSrvrTotResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSrvrTotResponse.setStatus("current")
_SslSrvrAvgResTime_Type = Counter32
_SslSrvrAvgResTime_Object = MibTableColumn
sslSrvrAvgResTime = _SslSrvrAvgResTime_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 15),
    _SslSrvrAvgResTime_Type()
)
sslSrvrAvgResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSrvrAvgResTime.setStatus("current")
_SslSrvrMaxResTime_Type = Counter32
_SslSrvrMaxResTime_Object = MibTableColumn
sslSrvrMaxResTime = _SslSrvrMaxResTime_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 16),
    _SslSrvrMaxResTime_Type()
)
sslSrvrMaxResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSrvrMaxResTime.setStatus("current")
_SslSrvrMinResTime_Type = Counter32
_SslSrvrMinResTime_Object = MibTableColumn
sslSrvrMinResTime = _SslSrvrMinResTime_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 17),
    _SslSrvrMinResTime_Type()
)
sslSrvrMinResTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSrvrMinResTime.setStatus("current")
_SslSrvrNumReqEnqueue_Type = Counter32
_SslSrvrNumReqEnqueue_Object = MibTableColumn
sslSrvrNumReqEnqueue = _SslSrvrNumReqEnqueue_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 18),
    _SslSrvrNumReqEnqueue_Type()
)
sslSrvrNumReqEnqueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSrvrNumReqEnqueue.setStatus("current")
_SslSrvrNumFreeConn_Type = Counter32
_SslSrvrNumFreeConn_Object = MibTableColumn
sslSrvrNumFreeConn = _SslSrvrNumFreeConn_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 19),
    _SslSrvrNumFreeConn_Type()
)
sslSrvrNumFreeConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSrvrNumFreeConn.setStatus("current")
_SslSrvrNumOpeningConn_Type = Counter32
_SslSrvrNumOpeningConn_Object = MibTableColumn
sslSrvrNumOpeningConn = _SslSrvrNumOpeningConn_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 20),
    _SslSrvrNumOpeningConn_Type()
)
sslSrvrNumOpeningConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSrvrNumOpeningConn.setStatus("current")
_SslSrvrNumConn_Type = Counter32
_SslSrvrNumConn_Object = MibTableColumn
sslSrvrNumConn = _SslSrvrNumConn_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 21),
    _SslSrvrNumConn_Type()
)
sslSrvrNumConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSrvrNumConn.setStatus("current")
_SslSrvrNumIBDisabled_Type = Counter32
_SslSrvrNumIBDisabled_Object = MibTableColumn
sslSrvrNumIBDisabled = _SslSrvrNumIBDisabled_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 22),
    _SslSrvrNumIBDisabled_Type()
)
sslSrvrNumIBDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSrvrNumIBDisabled.setStatus("current")
_SslSrvrNumOOBDisabled_Type = Counter32
_SslSrvrNumOOBDisabled_Object = MibTableColumn
sslSrvrNumOOBDisabled = _SslSrvrNumOOBDisabled_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 23),
    _SslSrvrNumOOBDisabled_Type()
)
sslSrvrNumOOBDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSrvrNumOOBDisabled.setStatus("current")
_SslSrvrNumOOBEnabled_Type = Counter32
_SslSrvrNumOOBEnabled_Object = MibTableColumn
sslSrvrNumOOBEnabled = _SslSrvrNumOOBEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 24),
    _SslSrvrNumOOBEnabled_Type()
)
sslSrvrNumOOBEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSrvrNumOOBEnabled.setStatus("current")
_SslSrvrLastDisabledTime_Type = TimeStamp
_SslSrvrLastDisabledTime_Object = MibTableColumn
sslSrvrLastDisabledTime = _SslSrvrLastDisabledTime_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 25),
    _SslSrvrLastDisabledTime_Type()
)
sslSrvrLastDisabledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSrvrLastDisabledTime.setStatus("current")
_SslSrvrState_Type = Integer32
_SslSrvrState_Object = MibTableColumn
sslSrvrState = _SslSrvrState_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 26),
    _SslSrvrState_Type()
)
sslSrvrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSrvrState.setStatus("current")
_SslSrvrInBytes_Type = Counter64
_SslSrvrInBytes_Object = MibTableColumn
sslSrvrInBytes = _SslSrvrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 27),
    _SslSrvrInBytes_Type()
)
sslSrvrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSrvrInBytes.setStatus("current")
_SslSrvrOutBytes_Type = Counter64
_SslSrvrOutBytes_Object = MibTableColumn
sslSrvrOutBytes = _SslSrvrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 6, 1, 28),
    _SslSrvrOutBytes_Type()
)
sslSrvrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSrvrOutBytes.setStatus("current")
_BwsIpsReqSrvcStatsTable_Object = MibTable
bwsIpsReqSrvcStatsTable = _BwsIpsReqSrvcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 7)
)
if mibBuilder.loadTexts:
    bwsIpsReqSrvcStatsTable.setStatus("current")
_BwsIpsReqSrvcStatsEntry_Object = MibTableRow
bwsIpsReqSrvcStatsEntry = _BwsIpsReqSrvcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 7, 1)
)
bwsIpsReqSrvcStatsEntry.setIndexNames(
    (0, "BWS-MIB", "ipsReqSrvcAddressType"),
    (0, "BWS-MIB", "ipsReqSrvcAddress"),
    (0, "BWS-MIB", "ipsReqSrvcPort"),
)
if mibBuilder.loadTexts:
    bwsIpsReqSrvcStatsEntry.setStatus("current")
_IpsReqSrvcAddressType_Type = InetAddressType
_IpsReqSrvcAddressType_Object = MibTableColumn
ipsReqSrvcAddressType = _IpsReqSrvcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 7, 1, 1),
    _IpsReqSrvcAddressType_Type()
)
ipsReqSrvcAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsReqSrvcAddressType.setStatus("current")
_IpsReqSrvcAddress_Type = InetAddress
_IpsReqSrvcAddress_Object = MibTableColumn
ipsReqSrvcAddress = _IpsReqSrvcAddress_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 7, 1, 2),
    _IpsReqSrvcAddress_Type()
)
ipsReqSrvcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsReqSrvcAddress.setStatus("current")
_IpsReqSrvcPort_Type = InetPortNumber
_IpsReqSrvcPort_Object = MibTableColumn
ipsReqSrvcPort = _IpsReqSrvcPort_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 7, 1, 3),
    _IpsReqSrvcPort_Type()
)
ipsReqSrvcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsReqSrvcPort.setStatus("current")
_IpsReqSrvcNoOfUrlProfMatched_Type = Counter64
_IpsReqSrvcNoOfUrlProfMatched_Object = MibTableColumn
ipsReqSrvcNoOfUrlProfMatched = _IpsReqSrvcNoOfUrlProfMatched_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 7, 1, 4),
    _IpsReqSrvcNoOfUrlProfMatched_Type()
)
ipsReqSrvcNoOfUrlProfMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsReqSrvcNoOfUrlProfMatched.setStatus("current")
_IpsReqSrvcNoOfAppProfViol_Type = Counter64
_IpsReqSrvcNoOfAppProfViol_Object = MibTableColumn
ipsReqSrvcNoOfAppProfViol = _IpsReqSrvcNoOfAppProfViol_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 7, 1, 5),
    _IpsReqSrvcNoOfAppProfViol_Type()
)
ipsReqSrvcNoOfAppProfViol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsReqSrvcNoOfAppProfViol.setStatus("current")
_IpsReqSrvcTotProfViol_Type = Counter64
_IpsReqSrvcTotProfViol_Object = MibTableColumn
ipsReqSrvcTotProfViol = _IpsReqSrvcTotProfViol_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 7, 1, 6),
    _IpsReqSrvcTotProfViol_Type()
)
ipsReqSrvcTotProfViol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsReqSrvcTotProfViol.setStatus("current")
_BwsIpsLrnSrvcStatsTable_Object = MibTable
bwsIpsLrnSrvcStatsTable = _BwsIpsLrnSrvcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 8)
)
if mibBuilder.loadTexts:
    bwsIpsLrnSrvcStatsTable.setStatus("current")
_BwsIpsLrnSrvcStatsEntry_Object = MibTableRow
bwsIpsLrnSrvcStatsEntry = _BwsIpsLrnSrvcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 8, 1)
)
bwsIpsLrnSrvcStatsEntry.setIndexNames(
    (0, "BWS-MIB", "ipsLrnSrvcAddressType"),
    (0, "BWS-MIB", "ipsLrnSrvcAddress"),
    (0, "BWS-MIB", "ipsLrnSrvcPort"),
)
if mibBuilder.loadTexts:
    bwsIpsLrnSrvcStatsEntry.setStatus("current")
_IpsLrnSrvcAddressType_Type = InetAddressType
_IpsLrnSrvcAddressType_Object = MibTableColumn
ipsLrnSrvcAddressType = _IpsLrnSrvcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 8, 1, 1),
    _IpsLrnSrvcAddressType_Type()
)
ipsLrnSrvcAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsLrnSrvcAddressType.setStatus("current")
_IpsLrnSrvcAddress_Type = InetAddress
_IpsLrnSrvcAddress_Object = MibTableColumn
ipsLrnSrvcAddress = _IpsLrnSrvcAddress_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 8, 1, 2),
    _IpsLrnSrvcAddress_Type()
)
ipsLrnSrvcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsLrnSrvcAddress.setStatus("current")
_IpsLrnSrvcPort_Type = InetPortNumber
_IpsLrnSrvcPort_Object = MibTableColumn
ipsLrnSrvcPort = _IpsLrnSrvcPort_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 8, 1, 3),
    _IpsLrnSrvcPort_Type()
)
ipsLrnSrvcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsLrnSrvcPort.setStatus("current")
_IpsLrnSrvcUpdatesByReq_Type = Counter64
_IpsLrnSrvcUpdatesByReq_Object = MibTableColumn
ipsLrnSrvcUpdatesByReq = _IpsLrnSrvcUpdatesByReq_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 8, 1, 4),
    _IpsLrnSrvcUpdatesByReq_Type()
)
ipsLrnSrvcUpdatesByReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsLrnSrvcUpdatesByReq.setStatus("current")
_IpsLrnSrvcUpdatesByRsp_Type = Counter64
_IpsLrnSrvcUpdatesByRsp_Object = MibTableColumn
ipsLrnSrvcUpdatesByRsp = _IpsLrnSrvcUpdatesByRsp_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 8, 1, 5),
    _IpsLrnSrvcUpdatesByRsp_Type()
)
ipsLrnSrvcUpdatesByRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsLrnSrvcUpdatesByRsp.setStatus("current")
_IpsLrnSrvcTotUpdatesByReq_Type = Counter64
_IpsLrnSrvcTotUpdatesByReq_Object = MibTableColumn
ipsLrnSrvcTotUpdatesByReq = _IpsLrnSrvcTotUpdatesByReq_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 8, 1, 6),
    _IpsLrnSrvcTotUpdatesByReq_Type()
)
ipsLrnSrvcTotUpdatesByReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsLrnSrvcTotUpdatesByReq.setStatus("current")
_IpsLrnSrvcTotUpdatesByRsp_Type = Counter64
_IpsLrnSrvcTotUpdatesByRsp_Object = MibTableColumn
ipsLrnSrvcTotUpdatesByRsp = _IpsLrnSrvcTotUpdatesByRsp_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 8, 1, 7),
    _IpsLrnSrvcTotUpdatesByRsp_Type()
)
ipsLrnSrvcTotUpdatesByRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsLrnSrvcTotUpdatesByRsp.setStatus("current")
_IpsLrnSrvcTotUrlUpdated_Type = Counter64
_IpsLrnSrvcTotUrlUpdated_Object = MibTableColumn
ipsLrnSrvcTotUrlUpdated = _IpsLrnSrvcTotUrlUpdated_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 8, 1, 8),
    _IpsLrnSrvcTotUrlUpdated_Type()
)
ipsLrnSrvcTotUrlUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsLrnSrvcTotUrlUpdated.setStatus("current")
_IpsLrnSrvcTotParamsLearned_Type = Counter64
_IpsLrnSrvcTotParamsLearned_Object = MibTableColumn
ipsLrnSrvcTotParamsLearned = _IpsLrnSrvcTotParamsLearned_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 8, 1, 9),
    _IpsLrnSrvcTotParamsLearned_Type()
)
ipsLrnSrvcTotParamsLearned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsLrnSrvcTotParamsLearned.setStatus("current")
_IpsLrnSrvcTimeLastUpdated_Type = TimeStamp
_IpsLrnSrvcTimeLastUpdated_Object = MibTableColumn
ipsLrnSrvcTimeLastUpdated = _IpsLrnSrvcTimeLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 8, 1, 10),
    _IpsLrnSrvcTimeLastUpdated_Type()
)
ipsLrnSrvcTimeLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsLrnSrvcTimeLastUpdated.setStatus("current")
_IpsLrnSrvcTimeLocked_Type = TimeStamp
_IpsLrnSrvcTimeLocked_Object = MibTableColumn
ipsLrnSrvcTimeLocked = _IpsLrnSrvcTimeLocked_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 8, 1, 11),
    _IpsLrnSrvcTimeLocked_Type()
)
ipsLrnSrvcTimeLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsLrnSrvcTimeLocked.setStatus("current")
_BwsIpsReqLimitStatsTable_Object = MibTable
bwsIpsReqLimitStatsTable = _BwsIpsReqLimitStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 9)
)
if mibBuilder.loadTexts:
    bwsIpsReqLimitStatsTable.setStatus("current")
_BwsIpsReqLimitStatsEntry_Object = MibTableRow
bwsIpsReqLimitStatsEntry = _BwsIpsReqLimitStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 9, 1)
)
bwsIpsReqLimitStatsEntry.setIndexNames(
    (0, "BWS-MIB", "ipsReqLimitAddressType"),
    (0, "BWS-MIB", "ipsReqLimitAddress"),
    (0, "BWS-MIB", "ipsReqLimitPort"),
)
if mibBuilder.loadTexts:
    bwsIpsReqLimitStatsEntry.setStatus("current")
_IpsReqLimitAddressType_Type = InetAddressType
_IpsReqLimitAddressType_Object = MibTableColumn
ipsReqLimitAddressType = _IpsReqLimitAddressType_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 9, 1, 1),
    _IpsReqLimitAddressType_Type()
)
ipsReqLimitAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsReqLimitAddressType.setStatus("current")
_IpsReqLimitAddress_Type = InetAddress
_IpsReqLimitAddress_Object = MibTableColumn
ipsReqLimitAddress = _IpsReqLimitAddress_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 9, 1, 2),
    _IpsReqLimitAddress_Type()
)
ipsReqLimitAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsReqLimitAddress.setStatus("current")
_IpsReqLimitPort_Type = InetPortNumber
_IpsReqLimitPort_Object = MibTableColumn
ipsReqLimitPort = _IpsReqLimitPort_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 9, 1, 3),
    _IpsReqLimitPort_Type()
)
ipsReqLimitPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsReqLimitPort.setStatus("current")
_IpsReqLimitUrlLenOFErr_Type = Counter32
_IpsReqLimitUrlLenOFErr_Object = MibTableColumn
ipsReqLimitUrlLenOFErr = _IpsReqLimitUrlLenOFErr_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 9, 1, 4),
    _IpsReqLimitUrlLenOFErr_Type()
)
ipsReqLimitUrlLenOFErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsReqLimitUrlLenOFErr.setStatus("current")
_IpsReqLimitQueryLenOFErr_Type = Counter32
_IpsReqLimitQueryLenOFErr_Object = MibTableColumn
ipsReqLimitQueryLenOFErr = _IpsReqLimitQueryLenOFErr_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 9, 1, 5),
    _IpsReqLimitQueryLenOFErr_Type()
)
ipsReqLimitQueryLenOFErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsReqLimitQueryLenOFErr.setStatus("current")
_IpsReqLimitReqLenOFErr_Type = Counter32
_IpsReqLimitReqLenOFErr_Object = MibTableColumn
ipsReqLimitReqLenOFErr = _IpsReqLimitReqLenOFErr_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 9, 1, 6),
    _IpsReqLimitReqLenOFErr_Type()
)
ipsReqLimitReqLenOFErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsReqLimitReqLenOFErr.setStatus("current")
_IpsReqLimitCookieLenOFErr_Type = Counter32
_IpsReqLimitCookieLenOFErr_Object = MibTableColumn
ipsReqLimitCookieLenOFErr = _IpsReqLimitCookieLenOFErr_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 9, 1, 7),
    _IpsReqLimitCookieLenOFErr_Type()
)
ipsReqLimitCookieLenOFErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsReqLimitCookieLenOFErr.setStatus("current")
_IpsReqLimitHdrCntOFErr_Type = Counter32
_IpsReqLimitHdrCntOFErr_Object = MibTableColumn
ipsReqLimitHdrCntOFErr = _IpsReqLimitHdrCntOFErr_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 9, 1, 8),
    _IpsReqLimitHdrCntOFErr_Type()
)
ipsReqLimitHdrCntOFErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsReqLimitHdrCntOFErr.setStatus("current")
_IpsReqLimitHdrLenOFErr_Type = Counter32
_IpsReqLimitHdrLenOFErr_Object = MibTableColumn
ipsReqLimitHdrLenOFErr = _IpsReqLimitHdrLenOFErr_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 9, 1, 9),
    _IpsReqLimitHdrLenOFErr_Type()
)
ipsReqLimitHdrLenOFErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsReqLimitHdrLenOFErr.setStatus("current")
_IpsReqLimitContentLenErr_Type = Counter32
_IpsReqLimitContentLenErr_Object = MibTableColumn
ipsReqLimitContentLenErr = _IpsReqLimitContentLenErr_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 9, 1, 10),
    _IpsReqLimitContentLenErr_Type()
)
ipsReqLimitContentLenErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsReqLimitContentLenErr.setStatus("current")
_IpsReqLimitBlkdMethodErr_Type = Counter32
_IpsReqLimitBlkdMethodErr_Object = MibTableColumn
ipsReqLimitBlkdMethodErr = _IpsReqLimitBlkdMethodErr_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 9, 1, 11),
    _IpsReqLimitBlkdMethodErr_Type()
)
ipsReqLimitBlkdMethodErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsReqLimitBlkdMethodErr.setStatus("current")
_BwsIpsUrlNormStatsTable_Object = MibTable
bwsIpsUrlNormStatsTable = _BwsIpsUrlNormStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 10)
)
if mibBuilder.loadTexts:
    bwsIpsUrlNormStatsTable.setStatus("current")
_BwsIpsUrlNormStatsEntry_Object = MibTableRow
bwsIpsUrlNormStatsEntry = _BwsIpsUrlNormStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 10, 1)
)
bwsIpsUrlNormStatsEntry.setIndexNames(
    (0, "BWS-MIB", "ipsUrlNormAddressType"),
    (0, "BWS-MIB", "ipsUrlNormAddress"),
    (0, "BWS-MIB", "ipsUrlNormPort"),
)
if mibBuilder.loadTexts:
    bwsIpsUrlNormStatsEntry.setStatus("current")
_IpsUrlNormAddressType_Type = InetAddressType
_IpsUrlNormAddressType_Object = MibTableColumn
ipsUrlNormAddressType = _IpsUrlNormAddressType_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 10, 1, 1),
    _IpsUrlNormAddressType_Type()
)
ipsUrlNormAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsUrlNormAddressType.setStatus("current")
_IpsUrlNormAddress_Type = InetAddress
_IpsUrlNormAddress_Object = MibTableColumn
ipsUrlNormAddress = _IpsUrlNormAddress_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 10, 1, 2),
    _IpsUrlNormAddress_Type()
)
ipsUrlNormAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsUrlNormAddress.setStatus("current")
_IpsUrlNormPort_Type = InetPortNumber
_IpsUrlNormPort_Object = MibTableColumn
ipsUrlNormPort = _IpsUrlNormPort_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 10, 1, 3),
    _IpsUrlNormPort_Type()
)
ipsUrlNormPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsUrlNormPort.setStatus("current")
_IpsUrlNormEncodingErr_Type = Counter32
_IpsUrlNormEncodingErr_Object = MibTableColumn
ipsUrlNormEncodingErr = _IpsUrlNormEncodingErr_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 10, 1, 4),
    _IpsUrlNormEncodingErr_Type()
)
ipsUrlNormEncodingErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsUrlNormEncodingErr.setStatus("current")
_IpsUrlNormSlashDotInUrlErr_Type = Counter32
_IpsUrlNormSlashDotInUrlErr_Object = MibTableColumn
ipsUrlNormSlashDotInUrlErr = _IpsUrlNormSlashDotInUrlErr_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 10, 1, 5),
    _IpsUrlNormSlashDotInUrlErr_Type()
)
ipsUrlNormSlashDotInUrlErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsUrlNormSlashDotInUrlErr.setStatus("current")
_IpsUrlNormTildaInUrl_Type = Counter32
_IpsUrlNormTildaInUrl_Object = MibTableColumn
ipsUrlNormTildaInUrl = _IpsUrlNormTildaInUrl_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 10, 1, 6),
    _IpsUrlNormTildaInUrl_Type()
)
ipsUrlNormTildaInUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsUrlNormTildaInUrl.setStatus("current")
_IpsUrlNormCharSetEncodingErr_Type = Counter32
_IpsUrlNormCharSetEncodingErr_Object = MibTableColumn
ipsUrlNormCharSetEncodingErr = _IpsUrlNormCharSetEncodingErr_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 10, 1, 7),
    _IpsUrlNormCharSetEncodingErr_Type()
)
ipsUrlNormCharSetEncodingErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsUrlNormCharSetEncodingErr.setStatus("current")
_BwsIpsCookieSecStatsTable_Object = MibTable
bwsIpsCookieSecStatsTable = _BwsIpsCookieSecStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 11)
)
if mibBuilder.loadTexts:
    bwsIpsCookieSecStatsTable.setStatus("current")
_BwsIpsCookieSecStatsEntry_Object = MibTableRow
bwsIpsCookieSecStatsEntry = _BwsIpsCookieSecStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 11, 1)
)
bwsIpsCookieSecStatsEntry.setIndexNames(
    (0, "BWS-MIB", "ipsCookieSecAddressType"),
    (0, "BWS-MIB", "ipsCookieSecAddress"),
    (0, "BWS-MIB", "ipsCookieSecPort"),
)
if mibBuilder.loadTexts:
    bwsIpsCookieSecStatsEntry.setStatus("current")
_IpsCookieSecAddressType_Type = InetAddressType
_IpsCookieSecAddressType_Object = MibTableColumn
ipsCookieSecAddressType = _IpsCookieSecAddressType_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 11, 1, 1),
    _IpsCookieSecAddressType_Type()
)
ipsCookieSecAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsCookieSecAddressType.setStatus("current")
_IpsCookieSecAddress_Type = InetAddress
_IpsCookieSecAddress_Object = MibTableColumn
ipsCookieSecAddress = _IpsCookieSecAddress_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 11, 1, 2),
    _IpsCookieSecAddress_Type()
)
ipsCookieSecAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsCookieSecAddress.setStatus("current")
_IpsCookieSecPort_Type = InetPortNumber
_IpsCookieSecPort_Object = MibTableColumn
ipsCookieSecPort = _IpsCookieSecPort_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 11, 1, 3),
    _IpsCookieSecPort_Type()
)
ipsCookieSecPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsCookieSecPort.setStatus("current")
_IpsCookieSecEncrypted_Type = Counter32
_IpsCookieSecEncrypted_Object = MibTableColumn
ipsCookieSecEncrypted = _IpsCookieSecEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 11, 1, 4),
    _IpsCookieSecEncrypted_Type()
)
ipsCookieSecEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsCookieSecEncrypted.setStatus("current")
_IpsCookieSecTampered_Type = Counter32
_IpsCookieSecTampered_Object = MibTableColumn
ipsCookieSecTampered = _IpsCookieSecTampered_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 11, 1, 5),
    _IpsCookieSecTampered_Type()
)
ipsCookieSecTampered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsCookieSecTampered.setStatus("current")
_IpsCookieSecNumCookieAllow_Type = Counter32
_IpsCookieSecNumCookieAllow_Object = MibTableColumn
ipsCookieSecNumCookieAllow = _IpsCookieSecNumCookieAllow_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 11, 1, 6),
    _IpsCookieSecNumCookieAllow_Type()
)
ipsCookieSecNumCookieAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsCookieSecNumCookieAllow.setStatus("current")
_IpsCookieSecNumCookieSet_Type = Counter32
_IpsCookieSecNumCookieSet_Object = MibTableColumn
ipsCookieSecNumCookieSet = _IpsCookieSecNumCookieSet_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 11, 1, 7),
    _IpsCookieSecNumCookieSet_Type()
)
ipsCookieSecNumCookieSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsCookieSecNumCookieSet.setStatus("current")
_IpsCookieSecNumCookieErr_Type = Counter32
_IpsCookieSecNumCookieErr_Object = MibTableColumn
ipsCookieSecNumCookieErr = _IpsCookieSecNumCookieErr_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 11, 1, 8),
    _IpsCookieSecNumCookieErr_Type()
)
ipsCookieSecNumCookieErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsCookieSecNumCookieErr.setStatus("current")
_IpsCookieSecCookieDecErr_Type = Counter32
_IpsCookieSecCookieDecErr_Object = MibTableColumn
ipsCookieSecCookieDecErr = _IpsCookieSecCookieDecErr_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 11, 1, 9),
    _IpsCookieSecCookieDecErr_Type()
)
ipsCookieSecCookieDecErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsCookieSecCookieDecErr.setStatus("current")
_IpsCookieSecCookieDecrypted_Type = Counter32
_IpsCookieSecCookieDecrypted_Object = MibTableColumn
ipsCookieSecCookieDecrypted = _IpsCookieSecCookieDecrypted_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 11, 1, 10),
    _IpsCookieSecCookieDecrypted_Type()
)
ipsCookieSecCookieDecrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsCookieSecCookieDecrypted.setStatus("current")
_BwsIpsUrlAclStatsTable_Object = MibTable
bwsIpsUrlAclStatsTable = _BwsIpsUrlAclStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 12)
)
if mibBuilder.loadTexts:
    bwsIpsUrlAclStatsTable.setStatus("current")
_BwsIpsUrlAclStatsEntry_Object = MibTableRow
bwsIpsUrlAclStatsEntry = _BwsIpsUrlAclStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 12, 1)
)
bwsIpsUrlAclStatsEntry.setIndexNames(
    (0, "BWS-MIB", "ipsUrlAclAddressType"),
    (0, "BWS-MIB", "ipsUrlAclAddress"),
    (0, "BWS-MIB", "ipsUrlAclPort"),
)
if mibBuilder.loadTexts:
    bwsIpsUrlAclStatsEntry.setStatus("current")
_IpsUrlAclAddressType_Type = InetAddressType
_IpsUrlAclAddressType_Object = MibTableColumn
ipsUrlAclAddressType = _IpsUrlAclAddressType_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 12, 1, 1),
    _IpsUrlAclAddressType_Type()
)
ipsUrlAclAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsUrlAclAddressType.setStatus("current")
_IpsUrlAclAddress_Type = InetAddress
_IpsUrlAclAddress_Object = MibTableColumn
ipsUrlAclAddress = _IpsUrlAclAddress_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 12, 1, 2),
    _IpsUrlAclAddress_Type()
)
ipsUrlAclAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsUrlAclAddress.setStatus("current")
_IpsUrlAclPort_Type = InetPortNumber
_IpsUrlAclPort_Object = MibTableColumn
ipsUrlAclPort = _IpsUrlAclPort_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 12, 1, 3),
    _IpsUrlAclPort_Type()
)
ipsUrlAclPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsUrlAclPort.setStatus("current")
_IpsUrlAclProcessAclHits_Type = Counter32
_IpsUrlAclProcessAclHits_Object = MibTableColumn
ipsUrlAclProcessAclHits = _IpsUrlAclProcessAclHits_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 12, 1, 4),
    _IpsUrlAclProcessAclHits_Type()
)
ipsUrlAclProcessAclHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsUrlAclProcessAclHits.setStatus("current")
_IpsUrlAclPolicyHits_Type = Counter32
_IpsUrlAclPolicyHits_Object = MibTableColumn
ipsUrlAclPolicyHits = _IpsUrlAclPolicyHits_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 12, 1, 5),
    _IpsUrlAclPolicyHits_Type()
)
ipsUrlAclPolicyHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsUrlAclPolicyHits.setStatus("current")
_IpsUrlAclTimeStamp_Type = TimeStamp
_IpsUrlAclTimeStamp_Object = MibTableColumn
ipsUrlAclTimeStamp = _IpsUrlAclTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 12, 1, 6),
    _IpsUrlAclTimeStamp_Type()
)
ipsUrlAclTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsUrlAclTimeStamp.setStatus("current")
_IpsUrlAclReserved_Type = OctetString
_IpsUrlAclReserved_Object = MibTableColumn
ipsUrlAclReserved = _IpsUrlAclReserved_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 12, 1, 7),
    _IpsUrlAclReserved_Type()
)
ipsUrlAclReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsUrlAclReserved.setStatus("current")
_IpsUrlAclAllowAclHits_Type = Counter32
_IpsUrlAclAllowAclHits_Object = MibTableColumn
ipsUrlAclAllowAclHits = _IpsUrlAclAllowAclHits_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 12, 1, 8),
    _IpsUrlAclAllowAclHits_Type()
)
ipsUrlAclAllowAclHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsUrlAclAllowAclHits.setStatus("current")
_BwsIpsHdrAclStatsTable_Object = MibTable
bwsIpsHdrAclStatsTable = _BwsIpsHdrAclStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 13)
)
if mibBuilder.loadTexts:
    bwsIpsHdrAclStatsTable.setStatus("current")
_BwsIpsHdrAclStatsEntry_Object = MibTableRow
bwsIpsHdrAclStatsEntry = _BwsIpsHdrAclStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 13, 1)
)
bwsIpsHdrAclStatsEntry.setIndexNames(
    (0, "BWS-MIB", "ipsHdrAclAddressType"),
    (0, "BWS-MIB", "ipsHdrAclAddress"),
    (0, "BWS-MIB", "ipsHdrAclPort"),
)
if mibBuilder.loadTexts:
    bwsIpsHdrAclStatsEntry.setStatus("current")
_IpsHdrAclAddressType_Type = InetAddressType
_IpsHdrAclAddressType_Object = MibTableColumn
ipsHdrAclAddressType = _IpsHdrAclAddressType_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 13, 1, 1),
    _IpsHdrAclAddressType_Type()
)
ipsHdrAclAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsHdrAclAddressType.setStatus("current")
_IpsHdrAclAddress_Type = InetAddress
_IpsHdrAclAddress_Object = MibTableColumn
ipsHdrAclAddress = _IpsHdrAclAddress_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 13, 1, 2),
    _IpsHdrAclAddress_Type()
)
ipsHdrAclAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsHdrAclAddress.setStatus("current")
_IpsHdrAclPort_Type = InetPortNumber
_IpsHdrAclPort_Object = MibTableColumn
ipsHdrAclPort = _IpsHdrAclPort_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 13, 1, 3),
    _IpsHdrAclPort_Type()
)
ipsHdrAclPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsHdrAclPort.setStatus("current")
_IpsHdrAclHits_Type = Counter32
_IpsHdrAclHits_Object = MibTableColumn
ipsHdrAclHits = _IpsHdrAclHits_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 13, 1, 4),
    _IpsHdrAclHits_Type()
)
ipsHdrAclHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsHdrAclHits.setStatus("current")
_IpsHdrAclTimeStamp_Type = TimeStamp
_IpsHdrAclTimeStamp_Object = MibTableColumn
ipsHdrAclTimeStamp = _IpsHdrAclTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 13, 1, 5),
    _IpsHdrAclTimeStamp_Type()
)
ipsHdrAclTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsHdrAclTimeStamp.setStatus("current")
_BwsIpsWebAddrTransStatsTable_Object = MibTable
bwsIpsWebAddrTransStatsTable = _BwsIpsWebAddrTransStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 14)
)
if mibBuilder.loadTexts:
    bwsIpsWebAddrTransStatsTable.setStatus("current")
_BwsIpsWebAddrTransStatsEntry_Object = MibTableRow
bwsIpsWebAddrTransStatsEntry = _BwsIpsWebAddrTransStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 14, 1)
)
bwsIpsWebAddrTransStatsEntry.setIndexNames(
    (0, "BWS-MIB", "ipsWebAddrTransAddressType"),
    (0, "BWS-MIB", "ipsWebAddrTransAddress"),
    (0, "BWS-MIB", "ipsWebAddrTransPort"),
)
if mibBuilder.loadTexts:
    bwsIpsWebAddrTransStatsEntry.setStatus("current")
_IpsWebAddrTransAddressType_Type = InetAddressType
_IpsWebAddrTransAddressType_Object = MibTableColumn
ipsWebAddrTransAddressType = _IpsWebAddrTransAddressType_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 14, 1, 1),
    _IpsWebAddrTransAddressType_Type()
)
ipsWebAddrTransAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsWebAddrTransAddressType.setStatus("current")
_IpsWebAddrTransAddress_Type = InetAddress
_IpsWebAddrTransAddress_Object = MibTableColumn
ipsWebAddrTransAddress = _IpsWebAddrTransAddress_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 14, 1, 2),
    _IpsWebAddrTransAddress_Type()
)
ipsWebAddrTransAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsWebAddrTransAddress.setStatus("current")
_IpsWebAddrTransPort_Type = InetPortNumber
_IpsWebAddrTransPort_Object = MibTableColumn
ipsWebAddrTransPort = _IpsWebAddrTransPort_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 14, 1, 3),
    _IpsWebAddrTransPort_Type()
)
ipsWebAddrTransPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsWebAddrTransPort.setStatus("current")
_IpsWebAddrTransReqUrlTrans_Type = Counter32
_IpsWebAddrTransReqUrlTrans_Object = MibTableColumn
ipsWebAddrTransReqUrlTrans = _IpsWebAddrTransReqUrlTrans_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 14, 1, 4),
    _IpsWebAddrTransReqUrlTrans_Type()
)
ipsWebAddrTransReqUrlTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsWebAddrTransReqUrlTrans.setStatus("current")
_IpsWebAddrTransRspUrlTrans_Type = Counter32
_IpsWebAddrTransRspUrlTrans_Object = MibTableColumn
ipsWebAddrTransRspUrlTrans = _IpsWebAddrTransRspUrlTrans_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 14, 1, 5),
    _IpsWebAddrTransRspUrlTrans_Type()
)
ipsWebAddrTransRspUrlTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsWebAddrTransRspUrlTrans.setStatus("current")
_IpsWebAddrTransReqUrlReWritten_Type = Counter32
_IpsWebAddrTransReqUrlReWritten_Object = MibTableColumn
ipsWebAddrTransReqUrlReWritten = _IpsWebAddrTransReqUrlReWritten_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 14, 1, 6),
    _IpsWebAddrTransReqUrlReWritten_Type()
)
ipsWebAddrTransReqUrlReWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsWebAddrTransReqUrlReWritten.setStatus("current")
_IpsWebAddrTransReqHdrReWritten_Type = Counter32
_IpsWebAddrTransReqHdrReWritten_Object = MibTableColumn
ipsWebAddrTransReqHdrReWritten = _IpsWebAddrTransReqHdrReWritten_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 14, 1, 7),
    _IpsWebAddrTransReqHdrReWritten_Type()
)
ipsWebAddrTransReqHdrReWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsWebAddrTransReqHdrReWritten.setStatus("current")
_IpsWebAddrTransRspHdrReWritten_Type = Counter32
_IpsWebAddrTransRspHdrReWritten_Object = MibTableColumn
ipsWebAddrTransRspHdrReWritten = _IpsWebAddrTransRspHdrReWritten_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 14, 1, 8),
    _IpsWebAddrTransRspHdrReWritten_Type()
)
ipsWebAddrTransRspHdrReWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsWebAddrTransRspHdrReWritten.setStatus("current")
_IpsWebAddrTransReqReDirection_Type = Counter32
_IpsWebAddrTransReqReDirection_Object = MibTableColumn
ipsWebAddrTransReqReDirection = _IpsWebAddrTransReqReDirection_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 14, 1, 9),
    _IpsWebAddrTransReqReDirection_Type()
)
ipsWebAddrTransReqReDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsWebAddrTransReqReDirection.setStatus("current")
_IpsWebAddrTransTimeStamp_Type = TimeStamp
_IpsWebAddrTransTimeStamp_Object = MibTableColumn
ipsWebAddrTransTimeStamp = _IpsWebAddrTransTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 14, 1, 10),
    _IpsWebAddrTransTimeStamp_Type()
)
ipsWebAddrTransTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsWebAddrTransTimeStamp.setStatus("current")
_BwsIpsAccessCtrlStatsTable_Object = MibTable
bwsIpsAccessCtrlStatsTable = _BwsIpsAccessCtrlStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 15)
)
if mibBuilder.loadTexts:
    bwsIpsAccessCtrlStatsTable.setStatus("current")
_BwsIpsAccessCtrlStatsEntry_Object = MibTableRow
bwsIpsAccessCtrlStatsEntry = _BwsIpsAccessCtrlStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 15, 1)
)
bwsIpsAccessCtrlStatsEntry.setIndexNames(
    (0, "BWS-MIB", "ipsAccessCtrlAddressType"),
    (0, "BWS-MIB", "ipsAccessCtrlAddress"),
    (0, "BWS-MIB", "ipsAccessCtrlPort"),
)
if mibBuilder.loadTexts:
    bwsIpsAccessCtrlStatsEntry.setStatus("current")
_IpsAccessCtrlAddressType_Type = InetAddressType
_IpsAccessCtrlAddressType_Object = MibTableColumn
ipsAccessCtrlAddressType = _IpsAccessCtrlAddressType_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 15, 1, 1),
    _IpsAccessCtrlAddressType_Type()
)
ipsAccessCtrlAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsAccessCtrlAddressType.setStatus("current")
_IpsAccessCtrlAddress_Type = InetAddress
_IpsAccessCtrlAddress_Object = MibTableColumn
ipsAccessCtrlAddress = _IpsAccessCtrlAddress_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 15, 1, 2),
    _IpsAccessCtrlAddress_Type()
)
ipsAccessCtrlAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsAccessCtrlAddress.setStatus("current")
_IpsAccessCtrlPort_Type = InetPortNumber
_IpsAccessCtrlPort_Object = MibTableColumn
ipsAccessCtrlPort = _IpsAccessCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 15, 1, 3),
    _IpsAccessCtrlPort_Type()
)
ipsAccessCtrlPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsAccessCtrlPort.setStatus("current")
_IpsAccessCtrlMissingCookie_Type = Counter32
_IpsAccessCtrlMissingCookie_Object = MibTableColumn
ipsAccessCtrlMissingCookie = _IpsAccessCtrlMissingCookie_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 15, 1, 4),
    _IpsAccessCtrlMissingCookie_Type()
)
ipsAccessCtrlMissingCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsAccessCtrlMissingCookie.setStatus("current")
_IpsAccessCtrlNoAuthHdr_Type = Counter32
_IpsAccessCtrlNoAuthHdr_Object = MibTableColumn
ipsAccessCtrlNoAuthHdr = _IpsAccessCtrlNoAuthHdr_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 15, 1, 5),
    _IpsAccessCtrlNoAuthHdr_Type()
)
ipsAccessCtrlNoAuthHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsAccessCtrlNoAuthHdr.setStatus("current")
_IpsAccessCtrlInvalidCookie_Type = Counter32
_IpsAccessCtrlInvalidCookie_Object = MibTableColumn
ipsAccessCtrlInvalidCookie = _IpsAccessCtrlInvalidCookie_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 15, 1, 6),
    _IpsAccessCtrlInvalidCookie_Type()
)
ipsAccessCtrlInvalidCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsAccessCtrlInvalidCookie.setStatus("current")
_IpsAccessCtrlExpiredCookie_Type = Counter32
_IpsAccessCtrlExpiredCookie_Object = MibTableColumn
ipsAccessCtrlExpiredCookie = _IpsAccessCtrlExpiredCookie_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 15, 1, 7),
    _IpsAccessCtrlExpiredCookie_Type()
)
ipsAccessCtrlExpiredCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsAccessCtrlExpiredCookie.setStatus("current")
_IpsAccessCtrlAccessDenied_Type = Counter32
_IpsAccessCtrlAccessDenied_Object = MibTableColumn
ipsAccessCtrlAccessDenied = _IpsAccessCtrlAccessDenied_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 15, 1, 8),
    _IpsAccessCtrlAccessDenied_Type()
)
ipsAccessCtrlAccessDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsAccessCtrlAccessDenied.setStatus("current")
_IpsAccessCtrlGenFailure_Type = Counter32
_IpsAccessCtrlGenFailure_Object = MibTableColumn
ipsAccessCtrlGenFailure = _IpsAccessCtrlGenFailure_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 15, 1, 9),
    _IpsAccessCtrlGenFailure_Type()
)
ipsAccessCtrlGenFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsAccessCtrlGenFailure.setStatus("current")
_IpsAccessCtrlAccessAttempts_Type = Counter32
_IpsAccessCtrlAccessAttempts_Object = MibTableColumn
ipsAccessCtrlAccessAttempts = _IpsAccessCtrlAccessAttempts_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 15, 1, 10),
    _IpsAccessCtrlAccessAttempts_Type()
)
ipsAccessCtrlAccessAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsAccessCtrlAccessAttempts.setStatus("current")
_IpsAccessCtrlAccessAttemptsTotRtt_Type = Counter32
_IpsAccessCtrlAccessAttemptsTotRtt_Object = MibTableColumn
ipsAccessCtrlAccessAttemptsTotRtt = _IpsAccessCtrlAccessAttemptsTotRtt_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 15, 1, 11),
    _IpsAccessCtrlAccessAttemptsTotRtt_Type()
)
ipsAccessCtrlAccessAttemptsTotRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsAccessCtrlAccessAttemptsTotRtt.setStatus("current")
_IpsAccessCtrlInvalidSrcIp_Type = Counter32
_IpsAccessCtrlInvalidSrcIp_Object = MibTableColumn
ipsAccessCtrlInvalidSrcIp = _IpsAccessCtrlInvalidSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 15, 1, 12),
    _IpsAccessCtrlInvalidSrcIp_Type()
)
ipsAccessCtrlInvalidSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsAccessCtrlInvalidSrcIp.setStatus("current")
_IpsAccessCtrlAuthCacheHits_Type = Counter32
_IpsAccessCtrlAuthCacheHits_Object = MibTableColumn
ipsAccessCtrlAuthCacheHits = _IpsAccessCtrlAuthCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 15, 1, 13),
    _IpsAccessCtrlAuthCacheHits_Type()
)
ipsAccessCtrlAuthCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsAccessCtrlAuthCacheHits.setStatus("current")
_IpsAccessCtrlAuthCacheMiss_Type = Counter32
_IpsAccessCtrlAuthCacheMiss_Object = MibTableColumn
ipsAccessCtrlAuthCacheMiss = _IpsAccessCtrlAuthCacheMiss_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 15, 1, 14),
    _IpsAccessCtrlAuthCacheMiss_Type()
)
ipsAccessCtrlAuthCacheMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsAccessCtrlAuthCacheMiss.setStatus("current")
_IpsAccessCtrlAuthCacheExp_Type = Counter32
_IpsAccessCtrlAuthCacheExp_Object = MibTableColumn
ipsAccessCtrlAuthCacheExp = _IpsAccessCtrlAuthCacheExp_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 15, 1, 15),
    _IpsAccessCtrlAuthCacheExp_Type()
)
ipsAccessCtrlAuthCacheExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsAccessCtrlAuthCacheExp.setStatus("current")
_IpsAccessCtrlTimeStamp_Type = TimeStamp
_IpsAccessCtrlTimeStamp_Object = MibTableColumn
ipsAccessCtrlTimeStamp = _IpsAccessCtrlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 15, 1, 16),
    _IpsAccessCtrlTimeStamp_Type()
)
ipsAccessCtrlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsAccessCtrlTimeStamp.setStatus("current")
_BwsIpsRCStatsTable_Object = MibTable
bwsIpsRCStatsTable = _BwsIpsRCStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 16)
)
if mibBuilder.loadTexts:
    bwsIpsRCStatsTable.setStatus("current")
_BwsIpsRCStatsEntry_Object = MibTableRow
bwsIpsRCStatsEntry = _BwsIpsRCStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 16, 1)
)
bwsIpsRCStatsEntry.setIndexNames(
    (0, "BWS-MIB", "ipsRCAddressType"),
    (0, "BWS-MIB", "ipsRCAddress"),
    (0, "BWS-MIB", "ipsRCPort"),
)
if mibBuilder.loadTexts:
    bwsIpsRCStatsEntry.setStatus("current")
_IpsRCAddressType_Type = InetAddressType
_IpsRCAddressType_Object = MibTableColumn
ipsRCAddressType = _IpsRCAddressType_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 16, 1, 1),
    _IpsRCAddressType_Type()
)
ipsRCAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsRCAddressType.setStatus("current")
_IpsRCAddress_Type = InetAddress
_IpsRCAddress_Object = MibTableColumn
ipsRCAddress = _IpsRCAddress_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 16, 1, 2),
    _IpsRCAddress_Type()
)
ipsRCAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsRCAddress.setStatus("current")
_IpsRCPort_Type = InetPortNumber
_IpsRCPort_Object = MibTableColumn
ipsRCPort = _IpsRCPort_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 16, 1, 3),
    _IpsRCPort_Type()
)
ipsRCPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsRCPort.setStatus("current")
_IpsRCTotServed_Type = Counter32
_IpsRCTotServed_Object = MibTableColumn
ipsRCTotServed = _IpsRCTotServed_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 16, 1, 4),
    _IpsRCTotServed_Type()
)
ipsRCTotServed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsRCTotServed.setStatus("current")
_IpsRCTotQueued_Type = Counter32
_IpsRCTotQueued_Object = MibTableColumn
ipsRCTotQueued = _IpsRCTotQueued_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 16, 1, 5),
    _IpsRCTotQueued_Type()
)
ipsRCTotQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsRCTotQueued.setStatus("current")
_IpsRCTotDropped_Type = Counter32
_IpsRCTotDropped_Object = MibTableColumn
ipsRCTotDropped = _IpsRCTotDropped_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 16, 1, 6),
    _IpsRCTotDropped_Type()
)
ipsRCTotDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsRCTotDropped.setStatus("current")
_IpsRCTotOutOfResource_Type = Counter32
_IpsRCTotOutOfResource_Object = MibTableColumn
ipsRCTotOutOfResource = _IpsRCTotOutOfResource_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 16, 1, 7),
    _IpsRCTotOutOfResource_Type()
)
ipsRCTotOutOfResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsRCTotOutOfResource.setStatus("current")
_IpsRCTimeStamp_Type = TimeStamp
_IpsRCTimeStamp_Object = MibTableColumn
ipsRCTimeStamp = _IpsRCTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 16, 1, 8),
    _IpsRCTimeStamp_Type()
)
ipsRCTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsRCTimeStamp.setStatus("current")
_BwsIpsUrlPolicyStatsTable_Object = MibTable
bwsIpsUrlPolicyStatsTable = _BwsIpsUrlPolicyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 17)
)
if mibBuilder.loadTexts:
    bwsIpsUrlPolicyStatsTable.setStatus("current")
_BwsIpsUrlPolicyStatsEntry_Object = MibTableRow
bwsIpsUrlPolicyStatsEntry = _BwsIpsUrlPolicyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 17, 1)
)
bwsIpsUrlPolicyStatsEntry.setIndexNames(
    (0, "BWS-MIB", "ipsUrlPolicyAddressType"),
    (0, "BWS-MIB", "ipsUrlPolicyAddress"),
    (0, "BWS-MIB", "ipsUrlPolicyPort"),
)
if mibBuilder.loadTexts:
    bwsIpsUrlPolicyStatsEntry.setStatus("current")
_IpsUrlPolicyAddressType_Type = InetAddressType
_IpsUrlPolicyAddressType_Object = MibTableColumn
ipsUrlPolicyAddressType = _IpsUrlPolicyAddressType_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 17, 1, 1),
    _IpsUrlPolicyAddressType_Type()
)
ipsUrlPolicyAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsUrlPolicyAddressType.setStatus("current")
_IpsUrlPolicyAddress_Type = InetAddress
_IpsUrlPolicyAddress_Object = MibTableColumn
ipsUrlPolicyAddress = _IpsUrlPolicyAddress_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 17, 1, 2),
    _IpsUrlPolicyAddress_Type()
)
ipsUrlPolicyAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsUrlPolicyAddress.setStatus("current")
_IpsUrlPolicyPort_Type = InetPortNumber
_IpsUrlPolicyPort_Object = MibTableColumn
ipsUrlPolicyPort = _IpsUrlPolicyPort_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 17, 1, 3),
    _IpsUrlPolicyPort_Type()
)
ipsUrlPolicyPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsUrlPolicyPort.setStatus("current")
_IpsUrlPolicyTotServed_Type = Counter32
_IpsUrlPolicyTotServed_Object = MibTableColumn
ipsUrlPolicyTotServed = _IpsUrlPolicyTotServed_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 17, 1, 4),
    _IpsUrlPolicyTotServed_Type()
)
ipsUrlPolicyTotServed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsUrlPolicyTotServed.setStatus("current")
_IpsUrlPolicyTotQueued_Type = Counter32
_IpsUrlPolicyTotQueued_Object = MibTableColumn
ipsUrlPolicyTotQueued = _IpsUrlPolicyTotQueued_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 17, 1, 5),
    _IpsUrlPolicyTotQueued_Type()
)
ipsUrlPolicyTotQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsUrlPolicyTotQueued.setStatus("current")
_IpsUrlPolicyTotDropped_Type = Counter32
_IpsUrlPolicyTotDropped_Object = MibTableColumn
ipsUrlPolicyTotDropped = _IpsUrlPolicyTotDropped_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 17, 1, 6),
    _IpsUrlPolicyTotDropped_Type()
)
ipsUrlPolicyTotDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsUrlPolicyTotDropped.setStatus("current")
_IpsUrlPolicyTotOutOfResource_Type = Counter32
_IpsUrlPolicyTotOutOfResource_Object = MibTableColumn
ipsUrlPolicyTotOutOfResource = _IpsUrlPolicyTotOutOfResource_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 17, 1, 7),
    _IpsUrlPolicyTotOutOfResource_Type()
)
ipsUrlPolicyTotOutOfResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsUrlPolicyTotOutOfResource.setStatus("current")
_IpsUrlPolicyEntryCtrlAuth_Type = Counter32
_IpsUrlPolicyEntryCtrlAuth_Object = MibTableColumn
ipsUrlPolicyEntryCtrlAuth = _IpsUrlPolicyEntryCtrlAuth_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 17, 1, 8),
    _IpsUrlPolicyEntryCtrlAuth_Type()
)
ipsUrlPolicyEntryCtrlAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsUrlPolicyEntryCtrlAuth.setStatus("current")
_IpsUrlPolicyTimeStamp_Type = TimeStamp
_IpsUrlPolicyTimeStamp_Object = MibTableColumn
ipsUrlPolicyTimeStamp = _IpsUrlPolicyTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 17, 1, 9),
    _IpsUrlPolicyTimeStamp_Type()
)
ipsUrlPolicyTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsUrlPolicyTimeStamp.setStatus("current")
_BwsSMUserSessionTable_Object = MibTable
bwsSMUserSessionTable = _BwsSMUserSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 18)
)
if mibBuilder.loadTexts:
    bwsSMUserSessionTable.setStatus("current")
_BwsSMUserSessionEntry_Object = MibTableRow
bwsSMUserSessionEntry = _BwsSMUserSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 18, 1)
)
bwsSMUserSessionEntry.setIndexNames(
    (0, "BWS-MIB", "smRealmName"),
)
if mibBuilder.loadTexts:
    bwsSMUserSessionEntry.setStatus("current")


class _SmRealmName_Type(OctetString):
    """Custom type smRealmName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_SmRealmName_Type.__name__ = "OctetString"
_SmRealmName_Object = MibTableColumn
smRealmName = _SmRealmName_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 18, 1, 1),
    _SmRealmName_Type()
)
smRealmName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smRealmName.setStatus("current")


class _SmAgentName_Type(OctetString):
    """Custom type smAgentName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_SmAgentName_Type.__name__ = "OctetString"
_SmAgentName_Object = MibTableColumn
smAgentName = _SmAgentName_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 18, 1, 2),
    _SmAgentName_Type()
)
smAgentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smAgentName.setStatus("current")
_SmNumUserSessions_Type = Integer32
_SmNumUserSessions_Object = MibTableColumn
smNumUserSessions = _SmNumUserSessions_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 18, 1, 3),
    _SmNumUserSessions_Type()
)
smNumUserSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smNumUserSessions.setStatus("current")
_BwsServiceStatusTable_Object = MibTable
bwsServiceStatusTable = _BwsServiceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 19)
)
if mibBuilder.loadTexts:
    bwsServiceStatusTable.setStatus("current")
_BwsServiceStatusEntry_Object = MibTableRow
bwsServiceStatusEntry = _BwsServiceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 19, 1)
)
bwsServiceStatusEntry.setIndexNames(
    (0, "BWS-MIB", "srvcName"),
)
if mibBuilder.loadTexts:
    bwsServiceStatusEntry.setStatus("current")
_SrvcName_Type = OctetString
_SrvcName_Object = MibTableColumn
srvcName = _SrvcName_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 19, 1, 1),
    _SrvcName_Type()
)
srvcName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srvcName.setStatus("current")
_ServiceName_Type = OctetString
_ServiceName_Object = MibTableColumn
serviceName = _ServiceName_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 19, 1, 2),
    _ServiceName_Type()
)
serviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceName.setStatus("current")
_ServiceAddress_Type = InetAddress
_ServiceAddress_Object = MibTableColumn
serviceAddress = _ServiceAddress_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 19, 1, 3),
    _ServiceAddress_Type()
)
serviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceAddress.setStatus("current")
_ServicePort_Type = InetPortNumber
_ServicePort_Object = MibTableColumn
servicePort = _ServicePort_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 19, 1, 4),
    _ServicePort_Type()
)
servicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servicePort.setStatus("current")
_ServiceStatus_Type = OctetString
_ServiceStatus_Object = MibTableColumn
serviceStatus = _ServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 20632, 8, 50, 19, 1, 5),
    _ServiceStatus_Type()
)
serviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceStatus.setStatus("current")
_BwsMIBConformance_ObjectIdentity = ObjectIdentity
bwsMIBConformance = _BwsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20632, 8, 51)
)
_BwsMIBCompliances_ObjectIdentity = ObjectIdentity
bwsMIBCompliances = _BwsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20632, 8, 51, 1)
)
_BwsMIBGroups_ObjectIdentity = ObjectIdentity
bwsMIBGroups = _BwsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20632, 8, 51, 2)
)

# Managed Objects groups

bwsStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20632, 8, 51, 2, 1)
)
bwsStatsGroup.setObjects(
      *(("BWS-MIB", "totalApplications"),
        ("BWS-MIB", "totalServers"),
        ("BWS-MIB", "totalAttacks"),
        ("BWS-MIB", "activeApplications"),
        ("BWS-MIB", "activeServers"),
        ("BWS-MIB", "bwsMessage"),
        ("BWS-MIB", "systemLoad"),
        ("BWS-MIB", "cpuFanSpeed"),
        ("BWS-MIB", "systemFanSpeed"),
        ("BWS-MIB", "cpuTemperature"),
        ("BWS-MIB", "firmwareStorage"),
        ("BWS-MIB", "logStorage"),
        ("BWS-MIB", "highAvailabilityStatus"),
        ("BWS-MIB", "operationalMode"),
        ("BWS-MIB", "dataPathStatus"),
        ("BWS-MIB", "linkStatus"),
        ("BWS-MIB", "vipStatus"),
        ("BWS-MIB", "memUtilization"),
        ("BWS-MIB", "cpuUtilization"),
        ("BWS-MIB", "totalBandwidth"),
        ("BWS-MIB", "uptime"),
        ("BWS-MIB", "totalMem"),
        ("BWS-MIB", "freeMem"),
        ("BWS-MIB", "currentFirmwareVersion"),
        ("BWS-MIB", "virusDefUpdates"),
        ("BWS-MIB", "securityDefUpdates"),
        ("BWS-MIB", "systemSerialNumber"),
        ("BWS-MIB", "httpProxyActiveConn"),
        ("BWS-MIB", "httpProxyTotalConn"),
        ("BWS-MIB", "httpProxyTotalReq"),
        ("BWS-MIB", "httpProxyServerReq"),
        ("BWS-MIB", "httpProxyServerErr"),
        ("BWS-MIB", "httpProxyClientAbrt"),
        ("BWS-MIB", "httpProxyServerAbrt"),
        ("BWS-MIB", "httpProxySessionTimeOut"),
        ("BWS-MIB", "httpProxyParseErr"),
        ("BWS-MIB", "httpProxyUnknownRsp"),
        ("BWS-MIB", "httpProxyInBytes"),
        ("BWS-MIB", "httpProxyOutBytes"),
        ("BWS-MIB", "httpProxyWAFBlockedIntrusions"),
        ("BWS-MIB", "httpProxyWAFMonitoredIntrusions"),
        ("BWS-MIB", "httpProxyWAFWarnings"),
        ("BWS-MIB", "sslProxyActiveConn"),
        ("BWS-MIB", "sslProxyFullHandshakes"),
        ("BWS-MIB", "sslProxyResumptionHandshakes"),
        ("BWS-MIB", "sslProxyHandshakeAttempts"),
        ("BWS-MIB", "sslProxyCacheHits"),
        ("BWS-MIB", "sslProxyCacheMiss"),
        ("BWS-MIB", "sslProxyCacheTimeouts"),
        ("BWS-MIB", "sslProxyErrPms"),
        ("BWS-MIB", "sslProxyAuthBadCertErr"),
        ("BWS-MIB", "sslProxyAuthBadCNErr"),
        ("BWS-MIB", "sslProxyBadDNCErr"),
        ("BWS-MIB", "sslProxyBadCRLErr"),
        ("BWS-MIB", "sslProxyInBytes"),
        ("BWS-MIB", "sslProxyOutBytes"),
        ("BWS-MIB", "sslProxyTotalReq"),
        ("BWS-MIB", "sslProxyTotalConn"),
        ("BWS-MIB", "sslProxyCurrentConn"),
        ("BWS-MIB", "webCmprNoOfReqCompressed"),
        ("BWS-MIB", "webCmprCompressibleDataSize"),
        ("BWS-MIB", "webCmprCompressedDataSize"),
        ("BWS-MIB", "webCacheHits"),
        ("BWS-MIB", "webCacheMiss"),
        ("BWS-MIB", "webCacheStale"),
        ("BWS-MIB", "webCacheCacheableRes"),
        ("BWS-MIB", "webCacheReq"),
        ("BWS-MIB", "webCacheCachedObjects"),
        ("BWS-MIB", "webCacheLongHdrs"),
        ("BWS-MIB", "webCacheBytesOut"),
        ("BWS-MIB", "httpSrvrTotReqAccepted"),
        ("BWS-MIB", "httpSrvrTotReqActive"),
        ("BWS-MIB", "httpSrvrTotReqRejected"),
        ("BWS-MIB", "httpSrvrTotSuccess"),
        ("BWS-MIB", "httpSrvrTotRefused"),
        ("BWS-MIB", "httpSrvrTotTimedout"),
        ("BWS-MIB", "httpSrvrAvgReqPerConn"),
        ("BWS-MIB", "httpSrvrTotResponse"),
        ("BWS-MIB", "httpSrvrAvgResTime"),
        ("BWS-MIB", "httpSrvrMaxResTime"),
        ("BWS-MIB", "httpSrvrMinResTime"),
        ("BWS-MIB", "httpSrvrNumReqEnqueue"),
        ("BWS-MIB", "httpSrvrNumFreeConn"),
        ("BWS-MIB", "httpSrvrNumOpeningConn"),
        ("BWS-MIB", "httpSrvrNumConn"),
        ("BWS-MIB", "httpSrvrNumIBDisabled"),
        ("BWS-MIB", "httpSrvrNumOOBDisabled"),
        ("BWS-MIB", "httpSrvrNumOOBEnabled"),
        ("BWS-MIB", "httpSrvrLastDisabledTime"),
        ("BWS-MIB", "httpSrvrState"),
        ("BWS-MIB", "httpSrvrInBytes"),
        ("BWS-MIB", "httpSrvrOutBytes"),
        ("BWS-MIB", "sslSrvrTotReqAccepted"),
        ("BWS-MIB", "sslSrvrTotReqActive"),
        ("BWS-MIB", "sslSrvrTotReqRejected"),
        ("BWS-MIB", "sslSrvrTotSuccess"),
        ("BWS-MIB", "sslSrvrTotRefused"),
        ("BWS-MIB", "sslSrvrTotTimedout"),
        ("BWS-MIB", "sslSrvrAvgReqPerConn"),
        ("BWS-MIB", "sslSrvrTotResponse"),
        ("BWS-MIB", "sslSrvrAvgResTime"),
        ("BWS-MIB", "sslSrvrMaxResTime"),
        ("BWS-MIB", "sslSrvrMinResTime"),
        ("BWS-MIB", "sslSrvrNumReqEnqueue"),
        ("BWS-MIB", "sslSrvrNumFreeConn"),
        ("BWS-MIB", "sslSrvrNumOpeningConn"),
        ("BWS-MIB", "sslSrvrNumConn"),
        ("BWS-MIB", "sslSrvrNumIBDisabled"),
        ("BWS-MIB", "sslSrvrNumOOBDisabled"),
        ("BWS-MIB", "sslSrvrNumOOBEnabled"),
        ("BWS-MIB", "sslSrvrLastDisabledTime"),
        ("BWS-MIB", "sslSrvrState"),
        ("BWS-MIB", "sslSrvrInBytes"),
        ("BWS-MIB", "sslSrvrOutBytes"),
        ("BWS-MIB", "ipsReqSrvcNoOfUrlProfMatched"),
        ("BWS-MIB", "ipsReqSrvcNoOfAppProfViol"),
        ("BWS-MIB", "ipsReqSrvcTotProfViol"),
        ("BWS-MIB", "ipsLrnSrvcUpdatesByReq"),
        ("BWS-MIB", "ipsLrnSrvcUpdatesByRsp"),
        ("BWS-MIB", "ipsLrnSrvcTotUpdatesByReq"),
        ("BWS-MIB", "ipsLrnSrvcTotUpdatesByRsp"),
        ("BWS-MIB", "ipsLrnSrvcTotUrlUpdated"),
        ("BWS-MIB", "ipsLrnSrvcTotParamsLearned"),
        ("BWS-MIB", "ipsLrnSrvcTimeLastUpdated"),
        ("BWS-MIB", "ipsLrnSrvcTimeLocked"),
        ("BWS-MIB", "ipsReqLimitUrlLenOFErr"),
        ("BWS-MIB", "ipsReqLimitQueryLenOFErr"),
        ("BWS-MIB", "ipsReqLimitReqLenOFErr"),
        ("BWS-MIB", "ipsReqLimitCookieLenOFErr"),
        ("BWS-MIB", "ipsReqLimitHdrCntOFErr"),
        ("BWS-MIB", "ipsReqLimitHdrLenOFErr"),
        ("BWS-MIB", "ipsReqLimitContentLenErr"),
        ("BWS-MIB", "ipsReqLimitBlkdMethodErr"),
        ("BWS-MIB", "ipsUrlNormEncodingErr"),
        ("BWS-MIB", "ipsUrlNormSlashDotInUrlErr"),
        ("BWS-MIB", "ipsUrlNormTildaInUrl"),
        ("BWS-MIB", "ipsUrlNormCharSetEncodingErr"),
        ("BWS-MIB", "ipsCookieSecEncrypted"),
        ("BWS-MIB", "ipsCookieSecTampered"),
        ("BWS-MIB", "ipsCookieSecNumCookieAllow"),
        ("BWS-MIB", "ipsCookieSecNumCookieSet"),
        ("BWS-MIB", "ipsCookieSecNumCookieErr"),
        ("BWS-MIB", "ipsCookieSecCookieDecErr"),
        ("BWS-MIB", "ipsCookieSecCookieDecrypted"),
        ("BWS-MIB", "ipsUrlAclProcessAclHits"),
        ("BWS-MIB", "ipsUrlAclPolicyHits"),
        ("BWS-MIB", "ipsUrlAclTimeStamp"),
        ("BWS-MIB", "ipsUrlAclReserved"),
        ("BWS-MIB", "ipsUrlAclAllowAclHits"),
        ("BWS-MIB", "ipsHdrAclHits"),
        ("BWS-MIB", "ipsHdrAclTimeStamp"),
        ("BWS-MIB", "ipsWebAddrTransReqUrlTrans"),
        ("BWS-MIB", "ipsWebAddrTransRspUrlTrans"),
        ("BWS-MIB", "ipsWebAddrTransReqUrlReWritten"),
        ("BWS-MIB", "ipsWebAddrTransReqHdrReWritten"),
        ("BWS-MIB", "ipsWebAddrTransRspHdrReWritten"),
        ("BWS-MIB", "ipsWebAddrTransReqReDirection"),
        ("BWS-MIB", "ipsWebAddrTransTimeStamp"),
        ("BWS-MIB", "ipsAccessCtrlMissingCookie"),
        ("BWS-MIB", "ipsAccessCtrlNoAuthHdr"),
        ("BWS-MIB", "ipsAccessCtrlInvalidCookie"),
        ("BWS-MIB", "ipsAccessCtrlExpiredCookie"),
        ("BWS-MIB", "ipsAccessCtrlAccessDenied"),
        ("BWS-MIB", "ipsAccessCtrlGenFailure"),
        ("BWS-MIB", "ipsAccessCtrlAccessAttempts"),
        ("BWS-MIB", "ipsAccessCtrlAccessAttemptsTotRtt"),
        ("BWS-MIB", "ipsAccessCtrlInvalidSrcIp"),
        ("BWS-MIB", "ipsAccessCtrlAuthCacheHits"),
        ("BWS-MIB", "ipsAccessCtrlAuthCacheMiss"),
        ("BWS-MIB", "ipsAccessCtrlAuthCacheExp"),
        ("BWS-MIB", "ipsAccessCtrlTimeStamp"),
        ("BWS-MIB", "ipsRCTotServed"),
        ("BWS-MIB", "ipsRCTotQueued"),
        ("BWS-MIB", "ipsRCTotDropped"),
        ("BWS-MIB", "ipsRCTotOutOfResource"),
        ("BWS-MIB", "ipsRCTimeStamp"),
        ("BWS-MIB", "ipsUrlPolicyTotServed"),
        ("BWS-MIB", "ipsUrlPolicyTotQueued"),
        ("BWS-MIB", "ipsUrlPolicyTotDropped"),
        ("BWS-MIB", "ipsUrlPolicyTotOutOfResource"),
        ("BWS-MIB", "ipsUrlPolicyEntryCtrlAuth"),
        ("BWS-MIB", "ipsUrlPolicyTimeStamp"),
        ("BWS-MIB", "serviceName"),
        ("BWS-MIB", "serviceAddress"),
        ("BWS-MIB", "servicePort"),
        ("BWS-MIB", "serviceStatus"),
        ("BWS-MIB", "smAgentName"),
        ("BWS-MIB", "smNumUserSessions"))
)
if mibBuilder.loadTexts:
    bwsStatsGroup.setStatus("current")


# Notification objects

tempCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1, 3)
)
tempCritical.setObjects(
    ("BWS-MIB", "bwsMessage")
)
if mibBuilder.loadTexts:
    tempCritical.setStatus(
        "current"
    )

tempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1, 4)
)
tempHigh.setObjects(
    ("BWS-MIB", "bwsMessage")
)
if mibBuilder.loadTexts:
    tempHigh.setStatus(
        "current"
    )

systemFailOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1, 5)
)
systemFailOver.setObjects(
    ("BWS-MIB", "bwsMessage")
)
if mibBuilder.loadTexts:
    systemFailOver.setStatus(
        "current"
    )

switchingToMaintMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1, 6)
)
switchingToMaintMode.setObjects(
    ("BWS-MIB", "bwsMessage")
)
if mibBuilder.loadTexts:
    switchingToMaintMode.setStatus(
        "current"
    )

fanDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1, 7)
)
fanDead.setObjects(
    ("BWS-MIB", "bwsMessage")
)
if mibBuilder.loadTexts:
    fanDead.setStatus(
        "current"
    )

dataPortLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1, 8)
)
dataPortLinkDown.setObjects(
    ("BWS-MIB", "bwsMessage")
)
if mibBuilder.loadTexts:
    dataPortLinkDown.setStatus(
        "current"
    )

serverDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1, 9)
)
serverDown.setObjects(
    ("BWS-MIB", "bwsMessage")
)
if mibBuilder.loadTexts:
    serverDown.setStatus(
        "current"
    )

peerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1, 10)
)
peerDown.setObjects(
    ("BWS-MIB", "bwsMessage")
)
if mibBuilder.loadTexts:
    peerDown.setStatus(
        "current"
    )

dataPortLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1, 11)
)
dataPortLinkUp.setObjects(
    ("BWS-MIB", "bwsMessage")
)
if mibBuilder.loadTexts:
    dataPortLinkUp.setStatus(
        "current"
    )

serverUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1, 12)
)
serverUp.setObjects(
    ("BWS-MIB", "bwsMessage")
)
if mibBuilder.loadTexts:
    serverUp.setStatus(
        "current"
    )

peerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1, 13)
)
peerUp.setObjects(
    ("BWS-MIB", "bwsMessage")
)
if mibBuilder.loadTexts:
    peerUp.setStatus(
        "current"
    )

switchingToBypassMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1, 14)
)
switchingToBypassMode.setObjects(
    ("BWS-MIB", "bwsMessage")
)
if mibBuilder.loadTexts:
    switchingToBypassMode.setStatus(
        "current"
    )

switchingToInlineMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1, 15)
)
switchingToInlineMode.setObjects(
    ("BWS-MIB", "bwsMessage")
)
if mibBuilder.loadTexts:
    switchingToInlineMode.setStatus(
        "current"
    )

sharedSecretKeyAboutToExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1, 16)
)
sharedSecretKeyAboutToExpire.setObjects(
    ("BWS-MIB", "bwsMessage")
)
if mibBuilder.loadTexts:
    sharedSecretKeyAboutToExpire.setStatus(
        "current"
    )

sharedSecretKeyExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1, 17)
)
sharedSecretKeyExpired.setObjects(
    ("BWS-MIB", "bwsMessage")
)
if mibBuilder.loadTexts:
    sharedSecretKeyExpired.setStatus(
        "current"
    )

firmwareStorageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1, 18)
)
firmwareStorageHigh.setObjects(
    ("BWS-MIB", "bwsMessage")
)
if mibBuilder.loadTexts:
    firmwareStorageHigh.setStatus(
        "current"
    )

logStorageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1, 19)
)
logStorageHigh.setObjects(
    ("BWS-MIB", "bwsMessage")
)
if mibBuilder.loadTexts:
    logStorageHigh.setStatus(
        "current"
    )

raidDegrading = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1, 20)
)
raidDegrading.setObjects(
    ("BWS-MIB", "bwsMessage")
)
if mibBuilder.loadTexts:
    raidDegrading.setStatus(
        "current"
    )

energizeUpdateExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1, 21)
)
energizeUpdateExpire.setObjects(
    ("BWS-MIB", "bwsMessage")
)
if mibBuilder.loadTexts:
    energizeUpdateExpire.setStatus(
        "current"
    )

firmwareUpdateAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1, 22)
)
firmwareUpdateAvailable.setObjects(
    ("BWS-MIB", "bwsMessage")
)
if mibBuilder.loadTexts:
    firmwareUpdateAvailable.setStatus(
        "current"
    )

attackDefinitionUpdateAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1, 24)
)
attackDefinitionUpdateAvailable.setObjects(
    ("BWS-MIB", "bwsMessage")
)
if mibBuilder.loadTexts:
    attackDefinitionUpdateAvailable.setStatus(
        "current"
    )

processCountHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1, 25)
)
processCountHigh.setObjects(
    ("BWS-MIB", "bwsMessage")
)
if mibBuilder.loadTexts:
    processCountHigh.setStatus(
        "current"
    )

memoryUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1, 26)
)
memoryUsageHigh.setObjects(
    ("BWS-MIB", "bwsMessage")
)
if mibBuilder.loadTexts:
    memoryUsageHigh.setStatus(
        "current"
    )

newAttackDefinitionInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1, 27)
)
newAttackDefinitionInstalled.setObjects(
    ("BWS-MIB", "bwsMessage")
)
if mibBuilder.loadTexts:
    newAttackDefinitionInstalled.setStatus(
        "current"
    )

systemFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 8, 1, 28)
)
systemFailure.setObjects(
    ("BWS-MIB", "bwsMessage")
)
if mibBuilder.loadTexts:
    systemFailure.setStatus(
        "current"
    )


# Notifications groups

bwsTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 20632, 8, 51, 2, 2)
)
bwsTrapGroup.setObjects(
      *(("BWS-MIB", "tempCritical"),
        ("BWS-MIB", "tempHigh"),
        ("BWS-MIB", "systemFailOver"),
        ("BWS-MIB", "switchingToMaintMode"),
        ("BWS-MIB", "fanDead"),
        ("BWS-MIB", "dataPortLinkDown"),
        ("BWS-MIB", "serverDown"),
        ("BWS-MIB", "peerDown"),
        ("BWS-MIB", "dataPortLinkUp"),
        ("BWS-MIB", "serverUp"),
        ("BWS-MIB", "peerUp"),
        ("BWS-MIB", "switchingToBypassMode"),
        ("BWS-MIB", "switchingToInlineMode"),
        ("BWS-MIB", "sharedSecretKeyAboutToExpire"),
        ("BWS-MIB", "sharedSecretKeyExpired"),
        ("BWS-MIB", "firmwareStorageHigh"),
        ("BWS-MIB", "logStorageHigh"),
        ("BWS-MIB", "raidDegrading"),
        ("BWS-MIB", "energizeUpdateExpire"),
        ("BWS-MIB", "firmwareUpdateAvailable"),
        ("BWS-MIB", "processCountHigh"),
        ("BWS-MIB", "memoryUsageHigh"),
        ("BWS-MIB", "attackDefinitionUpdateAvailable"),
        ("BWS-MIB", "newAttackDefinitionInstalled"),
        ("BWS-MIB", "systemFailure"))
)
if mibBuilder.loadTexts:
    bwsTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

bwsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 20632, 8, 51, 1, 1)
)
bwsMIBCompliance.setObjects(
      *(("BWS-MIB", "bwsStatsGroup"),
        ("BWS-MIB", "bwsTrapGroup"))
)
if mibBuilder.loadTexts:
    bwsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BWS-MIB",
    **{"bws": bws,
       "bwstraps": bwstraps,
       "tempCritical": tempCritical,
       "tempHigh": tempHigh,
       "systemFailOver": systemFailOver,
       "switchingToMaintMode": switchingToMaintMode,
       "fanDead": fanDead,
       "dataPortLinkDown": dataPortLinkDown,
       "serverDown": serverDown,
       "peerDown": peerDown,
       "dataPortLinkUp": dataPortLinkUp,
       "serverUp": serverUp,
       "peerUp": peerUp,
       "switchingToBypassMode": switchingToBypassMode,
       "switchingToInlineMode": switchingToInlineMode,
       "sharedSecretKeyAboutToExpire": sharedSecretKeyAboutToExpire,
       "sharedSecretKeyExpired": sharedSecretKeyExpired,
       "firmwareStorageHigh": firmwareStorageHigh,
       "logStorageHigh": logStorageHigh,
       "raidDegrading": raidDegrading,
       "energizeUpdateExpire": energizeUpdateExpire,
       "firmwareUpdateAvailable": firmwareUpdateAvailable,
       "attackDefinitionUpdateAvailable": attackDefinitionUpdateAvailable,
       "processCountHigh": processCountHigh,
       "memoryUsageHigh": memoryUsageHigh,
       "newAttackDefinitionInstalled": newAttackDefinitionInstalled,
       "systemFailure": systemFailure,
       "totalApplications": totalApplications,
       "totalServers": totalServers,
       "totalAttacks": totalAttacks,
       "activeApplications": activeApplications,
       "activeServers": activeServers,
       "bwsMessage": bwsMessage,
       "systemLoad": systemLoad,
       "cpuFanSpeed": cpuFanSpeed,
       "systemFanSpeed": systemFanSpeed,
       "cpuTemperature": cpuTemperature,
       "firmwareStorage": firmwareStorage,
       "logStorage": logStorage,
       "highAvailabilityStatus": highAvailabilityStatus,
       "operationalMode": operationalMode,
       "dataPathStatus": dataPathStatus,
       "linkStatus": linkStatus,
       "vipStatus": vipStatus,
       "memUtilization": memUtilization,
       "cpuUtilization": cpuUtilization,
       "totalBandwidth": totalBandwidth,
       "uptime": uptime,
       "totalMem": totalMem,
       "freeMem": freeMem,
       "currentFirmwareVersion": currentFirmwareVersion,
       "virusDefUpdates": virusDefUpdates,
       "securityDefUpdates": securityDefUpdates,
       "systemSerialNumber": systemSerialNumber,
       "bwsStats": bwsStats,
       "bwsHttpProxyStatsTable": bwsHttpProxyStatsTable,
       "bwsHttpProxyStatsEntry": bwsHttpProxyStatsEntry,
       "httpProxyAddressType": httpProxyAddressType,
       "httpProxyAddress": httpProxyAddress,
       "httpProxyPort": httpProxyPort,
       "httpProxyActiveConn": httpProxyActiveConn,
       "httpProxyTotalConn": httpProxyTotalConn,
       "httpProxyTotalReq": httpProxyTotalReq,
       "httpProxyServerReq": httpProxyServerReq,
       "httpProxyServerErr": httpProxyServerErr,
       "httpProxyClientAbrt": httpProxyClientAbrt,
       "httpProxyServerAbrt": httpProxyServerAbrt,
       "httpProxySessionTimeOut": httpProxySessionTimeOut,
       "httpProxyParseErr": httpProxyParseErr,
       "httpProxyUnknownRsp": httpProxyUnknownRsp,
       "httpProxyInBytes": httpProxyInBytes,
       "httpProxyOutBytes": httpProxyOutBytes,
       "httpProxyWAFBlockedIntrusions": httpProxyWAFBlockedIntrusions,
       "httpProxyWAFMonitoredIntrusions": httpProxyWAFMonitoredIntrusions,
       "httpProxyWAFWarnings": httpProxyWAFWarnings,
       "bwsSslProxyStatsTable": bwsSslProxyStatsTable,
       "bwsSslProxyStatsEntry": bwsSslProxyStatsEntry,
       "sslProxyAddressType": sslProxyAddressType,
       "sslProxyAddress": sslProxyAddress,
       "sslProxyPort": sslProxyPort,
       "sslProxyActiveConn": sslProxyActiveConn,
       "sslProxyFullHandshakes": sslProxyFullHandshakes,
       "sslProxyResumptionHandshakes": sslProxyResumptionHandshakes,
       "sslProxyHandshakeAttempts": sslProxyHandshakeAttempts,
       "sslProxyCacheHits": sslProxyCacheHits,
       "sslProxyCacheMiss": sslProxyCacheMiss,
       "sslProxyCacheTimeouts": sslProxyCacheTimeouts,
       "sslProxyErrPms": sslProxyErrPms,
       "sslProxyAuthBadCertErr": sslProxyAuthBadCertErr,
       "sslProxyAuthBadCNErr": sslProxyAuthBadCNErr,
       "sslProxyBadDNCErr": sslProxyBadDNCErr,
       "sslProxyBadCRLErr": sslProxyBadCRLErr,
       "sslProxyInBytes": sslProxyInBytes,
       "sslProxyOutBytes": sslProxyOutBytes,
       "sslProxyTotalReq": sslProxyTotalReq,
       "sslProxyTotalConn": sslProxyTotalConn,
       "sslProxyCurrentConn": sslProxyCurrentConn,
       "bwsCompressionStatsTable": bwsCompressionStatsTable,
       "bwsCompressionStatsEntry": bwsCompressionStatsEntry,
       "webCmprProtocol": webCmprProtocol,
       "webCmprAddressType": webCmprAddressType,
       "webCmprAddress": webCmprAddress,
       "webCmprPort": webCmprPort,
       "webCmprNoOfReqCompressed": webCmprNoOfReqCompressed,
       "webCmprCompressibleDataSize": webCmprCompressibleDataSize,
       "webCmprCompressedDataSize": webCmprCompressedDataSize,
       "bwsCacheStatsTable": bwsCacheStatsTable,
       "bwsCacheStatsEntry": bwsCacheStatsEntry,
       "webCacheProtocol": webCacheProtocol,
       "webCacheAddressType": webCacheAddressType,
       "webCacheAddress": webCacheAddress,
       "webCachePort": webCachePort,
       "webCacheHits": webCacheHits,
       "webCacheMiss": webCacheMiss,
       "webCacheStale": webCacheStale,
       "webCacheCacheableRes": webCacheCacheableRes,
       "webCacheReq": webCacheReq,
       "webCacheCachedObjects": webCacheCachedObjects,
       "webCacheLongHdrs": webCacheLongHdrs,
       "webCacheBytesOut": webCacheBytesOut,
       "bwsHttpSrvrStatsTable": bwsHttpSrvrStatsTable,
       "bwsHttpSrvrStatsEntry": bwsHttpSrvrStatsEntry,
       "httpSrvrSrvcAddressType": httpSrvrSrvcAddressType,
       "httpSrvrSrvcAddress": httpSrvrSrvcAddress,
       "httpSrvrSrvcPort": httpSrvrSrvcPort,
       "httpSrvrAddressType": httpSrvrAddressType,
       "httpSrvrAddress": httpSrvrAddress,
       "httpSrvrPort": httpSrvrPort,
       "httpSrvrTotReqAccepted": httpSrvrTotReqAccepted,
       "httpSrvrTotReqActive": httpSrvrTotReqActive,
       "httpSrvrTotReqRejected": httpSrvrTotReqRejected,
       "httpSrvrTotSuccess": httpSrvrTotSuccess,
       "httpSrvrTotRefused": httpSrvrTotRefused,
       "httpSrvrTotTimedout": httpSrvrTotTimedout,
       "httpSrvrAvgReqPerConn": httpSrvrAvgReqPerConn,
       "httpSrvrTotResponse": httpSrvrTotResponse,
       "httpSrvrAvgResTime": httpSrvrAvgResTime,
       "httpSrvrMaxResTime": httpSrvrMaxResTime,
       "httpSrvrMinResTime": httpSrvrMinResTime,
       "httpSrvrNumReqEnqueue": httpSrvrNumReqEnqueue,
       "httpSrvrNumFreeConn": httpSrvrNumFreeConn,
       "httpSrvrNumOpeningConn": httpSrvrNumOpeningConn,
       "httpSrvrNumConn": httpSrvrNumConn,
       "httpSrvrNumIBDisabled": httpSrvrNumIBDisabled,
       "httpSrvrNumOOBDisabled": httpSrvrNumOOBDisabled,
       "httpSrvrNumOOBEnabled": httpSrvrNumOOBEnabled,
       "httpSrvrLastDisabledTime": httpSrvrLastDisabledTime,
       "httpSrvrState": httpSrvrState,
       "httpSrvrInBytes": httpSrvrInBytes,
       "httpSrvrOutBytes": httpSrvrOutBytes,
       "bwsSslSrvrStatsTable": bwsSslSrvrStatsTable,
       "bwsSslSrvrStatsEntry": bwsSslSrvrStatsEntry,
       "sslSrvrSrvcAddressType": sslSrvrSrvcAddressType,
       "sslSrvrSrvcAddress": sslSrvrSrvcAddress,
       "sslSrvrSrvcPort": sslSrvrSrvcPort,
       "sslSrvrAddressType": sslSrvrAddressType,
       "sslSrvrAddress": sslSrvrAddress,
       "sslSrvrPort": sslSrvrPort,
       "sslSrvrTotReqAccepted": sslSrvrTotReqAccepted,
       "sslSrvrTotReqActive": sslSrvrTotReqActive,
       "sslSrvrTotReqRejected": sslSrvrTotReqRejected,
       "sslSrvrTotSuccess": sslSrvrTotSuccess,
       "sslSrvrTotRefused": sslSrvrTotRefused,
       "sslSrvrTotTimedout": sslSrvrTotTimedout,
       "sslSrvrAvgReqPerConn": sslSrvrAvgReqPerConn,
       "sslSrvrTotResponse": sslSrvrTotResponse,
       "sslSrvrAvgResTime": sslSrvrAvgResTime,
       "sslSrvrMaxResTime": sslSrvrMaxResTime,
       "sslSrvrMinResTime": sslSrvrMinResTime,
       "sslSrvrNumReqEnqueue": sslSrvrNumReqEnqueue,
       "sslSrvrNumFreeConn": sslSrvrNumFreeConn,
       "sslSrvrNumOpeningConn": sslSrvrNumOpeningConn,
       "sslSrvrNumConn": sslSrvrNumConn,
       "sslSrvrNumIBDisabled": sslSrvrNumIBDisabled,
       "sslSrvrNumOOBDisabled": sslSrvrNumOOBDisabled,
       "sslSrvrNumOOBEnabled": sslSrvrNumOOBEnabled,
       "sslSrvrLastDisabledTime": sslSrvrLastDisabledTime,
       "sslSrvrState": sslSrvrState,
       "sslSrvrInBytes": sslSrvrInBytes,
       "sslSrvrOutBytes": sslSrvrOutBytes,
       "bwsIpsReqSrvcStatsTable": bwsIpsReqSrvcStatsTable,
       "bwsIpsReqSrvcStatsEntry": bwsIpsReqSrvcStatsEntry,
       "ipsReqSrvcAddressType": ipsReqSrvcAddressType,
       "ipsReqSrvcAddress": ipsReqSrvcAddress,
       "ipsReqSrvcPort": ipsReqSrvcPort,
       "ipsReqSrvcNoOfUrlProfMatched": ipsReqSrvcNoOfUrlProfMatched,
       "ipsReqSrvcNoOfAppProfViol": ipsReqSrvcNoOfAppProfViol,
       "ipsReqSrvcTotProfViol": ipsReqSrvcTotProfViol,
       "bwsIpsLrnSrvcStatsTable": bwsIpsLrnSrvcStatsTable,
       "bwsIpsLrnSrvcStatsEntry": bwsIpsLrnSrvcStatsEntry,
       "ipsLrnSrvcAddressType": ipsLrnSrvcAddressType,
       "ipsLrnSrvcAddress": ipsLrnSrvcAddress,
       "ipsLrnSrvcPort": ipsLrnSrvcPort,
       "ipsLrnSrvcUpdatesByReq": ipsLrnSrvcUpdatesByReq,
       "ipsLrnSrvcUpdatesByRsp": ipsLrnSrvcUpdatesByRsp,
       "ipsLrnSrvcTotUpdatesByReq": ipsLrnSrvcTotUpdatesByReq,
       "ipsLrnSrvcTotUpdatesByRsp": ipsLrnSrvcTotUpdatesByRsp,
       "ipsLrnSrvcTotUrlUpdated": ipsLrnSrvcTotUrlUpdated,
       "ipsLrnSrvcTotParamsLearned": ipsLrnSrvcTotParamsLearned,
       "ipsLrnSrvcTimeLastUpdated": ipsLrnSrvcTimeLastUpdated,
       "ipsLrnSrvcTimeLocked": ipsLrnSrvcTimeLocked,
       "bwsIpsReqLimitStatsTable": bwsIpsReqLimitStatsTable,
       "bwsIpsReqLimitStatsEntry": bwsIpsReqLimitStatsEntry,
       "ipsReqLimitAddressType": ipsReqLimitAddressType,
       "ipsReqLimitAddress": ipsReqLimitAddress,
       "ipsReqLimitPort": ipsReqLimitPort,
       "ipsReqLimitUrlLenOFErr": ipsReqLimitUrlLenOFErr,
       "ipsReqLimitQueryLenOFErr": ipsReqLimitQueryLenOFErr,
       "ipsReqLimitReqLenOFErr": ipsReqLimitReqLenOFErr,
       "ipsReqLimitCookieLenOFErr": ipsReqLimitCookieLenOFErr,
       "ipsReqLimitHdrCntOFErr": ipsReqLimitHdrCntOFErr,
       "ipsReqLimitHdrLenOFErr": ipsReqLimitHdrLenOFErr,
       "ipsReqLimitContentLenErr": ipsReqLimitContentLenErr,
       "ipsReqLimitBlkdMethodErr": ipsReqLimitBlkdMethodErr,
       "bwsIpsUrlNormStatsTable": bwsIpsUrlNormStatsTable,
       "bwsIpsUrlNormStatsEntry": bwsIpsUrlNormStatsEntry,
       "ipsUrlNormAddressType": ipsUrlNormAddressType,
       "ipsUrlNormAddress": ipsUrlNormAddress,
       "ipsUrlNormPort": ipsUrlNormPort,
       "ipsUrlNormEncodingErr": ipsUrlNormEncodingErr,
       "ipsUrlNormSlashDotInUrlErr": ipsUrlNormSlashDotInUrlErr,
       "ipsUrlNormTildaInUrl": ipsUrlNormTildaInUrl,
       "ipsUrlNormCharSetEncodingErr": ipsUrlNormCharSetEncodingErr,
       "bwsIpsCookieSecStatsTable": bwsIpsCookieSecStatsTable,
       "bwsIpsCookieSecStatsEntry": bwsIpsCookieSecStatsEntry,
       "ipsCookieSecAddressType": ipsCookieSecAddressType,
       "ipsCookieSecAddress": ipsCookieSecAddress,
       "ipsCookieSecPort": ipsCookieSecPort,
       "ipsCookieSecEncrypted": ipsCookieSecEncrypted,
       "ipsCookieSecTampered": ipsCookieSecTampered,
       "ipsCookieSecNumCookieAllow": ipsCookieSecNumCookieAllow,
       "ipsCookieSecNumCookieSet": ipsCookieSecNumCookieSet,
       "ipsCookieSecNumCookieErr": ipsCookieSecNumCookieErr,
       "ipsCookieSecCookieDecErr": ipsCookieSecCookieDecErr,
       "ipsCookieSecCookieDecrypted": ipsCookieSecCookieDecrypted,
       "bwsIpsUrlAclStatsTable": bwsIpsUrlAclStatsTable,
       "bwsIpsUrlAclStatsEntry": bwsIpsUrlAclStatsEntry,
       "ipsUrlAclAddressType": ipsUrlAclAddressType,
       "ipsUrlAclAddress": ipsUrlAclAddress,
       "ipsUrlAclPort": ipsUrlAclPort,
       "ipsUrlAclProcessAclHits": ipsUrlAclProcessAclHits,
       "ipsUrlAclPolicyHits": ipsUrlAclPolicyHits,
       "ipsUrlAclTimeStamp": ipsUrlAclTimeStamp,
       "ipsUrlAclReserved": ipsUrlAclReserved,
       "ipsUrlAclAllowAclHits": ipsUrlAclAllowAclHits,
       "bwsIpsHdrAclStatsTable": bwsIpsHdrAclStatsTable,
       "bwsIpsHdrAclStatsEntry": bwsIpsHdrAclStatsEntry,
       "ipsHdrAclAddressType": ipsHdrAclAddressType,
       "ipsHdrAclAddress": ipsHdrAclAddress,
       "ipsHdrAclPort": ipsHdrAclPort,
       "ipsHdrAclHits": ipsHdrAclHits,
       "ipsHdrAclTimeStamp": ipsHdrAclTimeStamp,
       "bwsIpsWebAddrTransStatsTable": bwsIpsWebAddrTransStatsTable,
       "bwsIpsWebAddrTransStatsEntry": bwsIpsWebAddrTransStatsEntry,
       "ipsWebAddrTransAddressType": ipsWebAddrTransAddressType,
       "ipsWebAddrTransAddress": ipsWebAddrTransAddress,
       "ipsWebAddrTransPort": ipsWebAddrTransPort,
       "ipsWebAddrTransReqUrlTrans": ipsWebAddrTransReqUrlTrans,
       "ipsWebAddrTransRspUrlTrans": ipsWebAddrTransRspUrlTrans,
       "ipsWebAddrTransReqUrlReWritten": ipsWebAddrTransReqUrlReWritten,
       "ipsWebAddrTransReqHdrReWritten": ipsWebAddrTransReqHdrReWritten,
       "ipsWebAddrTransRspHdrReWritten": ipsWebAddrTransRspHdrReWritten,
       "ipsWebAddrTransReqReDirection": ipsWebAddrTransReqReDirection,
       "ipsWebAddrTransTimeStamp": ipsWebAddrTransTimeStamp,
       "bwsIpsAccessCtrlStatsTable": bwsIpsAccessCtrlStatsTable,
       "bwsIpsAccessCtrlStatsEntry": bwsIpsAccessCtrlStatsEntry,
       "ipsAccessCtrlAddressType": ipsAccessCtrlAddressType,
       "ipsAccessCtrlAddress": ipsAccessCtrlAddress,
       "ipsAccessCtrlPort": ipsAccessCtrlPort,
       "ipsAccessCtrlMissingCookie": ipsAccessCtrlMissingCookie,
       "ipsAccessCtrlNoAuthHdr": ipsAccessCtrlNoAuthHdr,
       "ipsAccessCtrlInvalidCookie": ipsAccessCtrlInvalidCookie,
       "ipsAccessCtrlExpiredCookie": ipsAccessCtrlExpiredCookie,
       "ipsAccessCtrlAccessDenied": ipsAccessCtrlAccessDenied,
       "ipsAccessCtrlGenFailure": ipsAccessCtrlGenFailure,
       "ipsAccessCtrlAccessAttempts": ipsAccessCtrlAccessAttempts,
       "ipsAccessCtrlAccessAttemptsTotRtt": ipsAccessCtrlAccessAttemptsTotRtt,
       "ipsAccessCtrlInvalidSrcIp": ipsAccessCtrlInvalidSrcIp,
       "ipsAccessCtrlAuthCacheHits": ipsAccessCtrlAuthCacheHits,
       "ipsAccessCtrlAuthCacheMiss": ipsAccessCtrlAuthCacheMiss,
       "ipsAccessCtrlAuthCacheExp": ipsAccessCtrlAuthCacheExp,
       "ipsAccessCtrlTimeStamp": ipsAccessCtrlTimeStamp,
       "bwsIpsRCStatsTable": bwsIpsRCStatsTable,
       "bwsIpsRCStatsEntry": bwsIpsRCStatsEntry,
       "ipsRCAddressType": ipsRCAddressType,
       "ipsRCAddress": ipsRCAddress,
       "ipsRCPort": ipsRCPort,
       "ipsRCTotServed": ipsRCTotServed,
       "ipsRCTotQueued": ipsRCTotQueued,
       "ipsRCTotDropped": ipsRCTotDropped,
       "ipsRCTotOutOfResource": ipsRCTotOutOfResource,
       "ipsRCTimeStamp": ipsRCTimeStamp,
       "bwsIpsUrlPolicyStatsTable": bwsIpsUrlPolicyStatsTable,
       "bwsIpsUrlPolicyStatsEntry": bwsIpsUrlPolicyStatsEntry,
       "ipsUrlPolicyAddressType": ipsUrlPolicyAddressType,
       "ipsUrlPolicyAddress": ipsUrlPolicyAddress,
       "ipsUrlPolicyPort": ipsUrlPolicyPort,
       "ipsUrlPolicyTotServed": ipsUrlPolicyTotServed,
       "ipsUrlPolicyTotQueued": ipsUrlPolicyTotQueued,
       "ipsUrlPolicyTotDropped": ipsUrlPolicyTotDropped,
       "ipsUrlPolicyTotOutOfResource": ipsUrlPolicyTotOutOfResource,
       "ipsUrlPolicyEntryCtrlAuth": ipsUrlPolicyEntryCtrlAuth,
       "ipsUrlPolicyTimeStamp": ipsUrlPolicyTimeStamp,
       "bwsSMUserSessionTable": bwsSMUserSessionTable,
       "bwsSMUserSessionEntry": bwsSMUserSessionEntry,
       "smRealmName": smRealmName,
       "smAgentName": smAgentName,
       "smNumUserSessions": smNumUserSessions,
       "bwsServiceStatusTable": bwsServiceStatusTable,
       "bwsServiceStatusEntry": bwsServiceStatusEntry,
       "srvcName": srvcName,
       "serviceName": serviceName,
       "serviceAddress": serviceAddress,
       "servicePort": servicePort,
       "serviceStatus": serviceStatus,
       "bwsMIBConformance": bwsMIBConformance,
       "bwsMIBCompliances": bwsMIBCompliances,
       "bwsMIBCompliance": bwsMIBCompliance,
       "bwsMIBGroups": bwsMIBGroups,
       "bwsStatsGroup": bwsStatsGroup,
       "bwsTrapGroup": bwsTrapGroup}
)
