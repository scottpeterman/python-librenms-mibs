# SNMP MIB module (TIMETRA-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\TIMETRA-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:17:57 2025
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

(smLaunchEntry,
 smLaunchError,
 smLaunchName,
 smLaunchOwner,
 smLaunchScriptName,
 smLaunchScriptOwner,
 smRunEntry,
 smRunIndex) = mibBuilder.importSymbols(
    "DISMAN-SCRIPT-MIB",
    "smLaunchEntry",
    "smLaunchError",
    "smLaunchName",
    "smLaunchOwner",
    "smLaunchScriptName",
    "smLaunchScriptOwner",
    "smRunEntry",
    "smRunIndex")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InetAddress,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(snmpCommunityEntry,) = mibBuilder.importSymbols(
    "SNMP-COMMUNITY-MIB",
    "snmpCommunityEntry")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(TmnxSlotNum,
 tmnxChassisBaseMacAddress,
 tmnxChassisIndex,
 tmnxChassisNotifyHwIndex,
 tmnxCpmCardNum,
 tmnxCpmCardSlotNum,
 tmnxFabricSlotNum,
 tmnxHwClass,
 tmnxHwID) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxSlotNum",
    "tmnxChassisBaseMacAddress",
    "tmnxChassisIndex",
    "tmnxChassisNotifyHwIndex",
    "tmnxCpmCardNum",
    "tmnxCpmCardSlotNum",
    "tmnxFabricSlotNum",
    "tmnxHwClass",
    "tmnxHwID")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(tmnxEhsHEntryMinDelay,
 tmnxEhsHEntryMinDelayInterval,
 tmnxEhsHEntryScriptPlcyName,
 tmnxEhsHEntryScriptPlcyOwner,
 tmnxEhsHandlerDescription,
 tmnxLogExecRollbackOpIndex,
 tmnxLogExecRollbackOpType) = mibBuilder.importSymbols(
    "TIMETRA-LOG-MIB",
    "tmnxEhsHEntryMinDelay",
    "tmnxEhsHEntryMinDelayInterval",
    "tmnxEhsHEntryScriptPlcyName",
    "tmnxEhsHEntryScriptPlcyOwner",
    "tmnxEhsHandlerDescription",
    "tmnxLogExecRollbackOpIndex",
    "tmnxLogExecRollbackOpType")

(IpAddressPrefixLength,
 TDSCPNameOrEmpty,
 TItemDescription,
 TLDisplayString,
 TLNamedItem,
 TLNamedItemOrEmpty,
 TNamedItem,
 TNamedItemOrEmpty,
 TTcpUdpPort,
 TmnxActionType,
 TmnxAdminState,
 TmnxAdminStateTruthValue,
 TmnxCliEngine,
 TmnxDisplayStringURL,
 TmnxEnabledDisabled,
 TmnxEnabledDisabledAdminState,
 TmnxLongDisplayString,
 TmnxOperState,
 TmnxScriptAuthType,
 TmnxServId,
 TmnxUuid,
 TmnxVRtrID,
 TmnxVRtrIDOrZero) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "IpAddressPrefixLength",
    "TDSCPNameOrEmpty",
    "TItemDescription",
    "TLDisplayString",
    "TLNamedItem",
    "TLNamedItemOrEmpty",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TTcpUdpPort",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxAdminStateTruthValue",
    "TmnxCliEngine",
    "TmnxDisplayStringURL",
    "TmnxEnabledDisabled",
    "TmnxEnabledDisabledAdminState",
    "TmnxLongDisplayString",
    "TmnxOperState",
    "TmnxScriptAuthType",
    "TmnxServId",
    "TmnxUuid",
    "TmnxVRtrID",
    "TmnxVRtrIDOrZero")


# MODULE-IDENTITY

timetraSysMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    timetraSysMIBModule.setRevisions(
        ("2017-01-01 00:00",
         "2016-01-01 00:00",
         "2014-06-01 00:00",
         "2014-01-01 00:00",
         "2011-02-01 00:00",
         "2010-01-01 00:00",
         "2009-02-28 00:00",
         "2008-01-01 00:00",
         "2007-01-01 00:00",
         "2006-03-15 00:00",
         "2005-08-31 00:00",
         "2005-01-24 00:00",
         "2004-01-15 00:00",
         "2003-08-15 00:00",
         "2003-01-20 00:00",
         "2000-08-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxSsiSyncMode(TextualConvention, Integer32):
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
        *(("none", 1),
          ("config", 2),
          ("bootEnv", 3))
    )



class TmnxSsiSyncRollbackMode(TextualConvention, Integer32):
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
        *(("none", 1),
          ("rollbackSingle", 2),
          ("rollbackAll", 3))
    )



class TmnxSysLicenseApplication(TextualConvention, Integer32):
    status = "current"
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
          ("nat", 1),
          ("wlanGw", 2),
          ("lns", 3),
          ("subMgmt", 4),
          ("aa", 5),
          ("ipsec", 6))
    )



class TmnxSysLicenseAppStatsType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              1000,
              1001,
              2000,
              2001,
              3000,
              4000,
              4001,
              5000,
              5001,
              5002,
              5003)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("lsnSubscribers", 1),
          ("lsnBandwidth", 2),
          ("wlanGwUserEquipment", 1000),
          ("wlanGwGtpBearers", 1001),
          ("lnsTunnels", 2000),
          ("lnsSessions", 2001),
          ("subscriberHosts", 3000),
          ("aaSubscribers", 4000),
          ("aaBandwidth", 4001),
          ("ipsecTunnels", 5000),
          ("ipsecTnlBandwidth", 5001),
          ("ipTunnels", 5002),
          ("ipTnlBandwidth", 5003))
    )



class TmnxSysLicensingGroup(TextualConvention, Integer32):
    status = "current"
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
        *(("system", 0),
          ("services", 1),
          ("nsp", 2),
          ("isa", 3),
          ("iom", 4),
          ("mda", 5),
          ("ports", 6))
    )



class TmnxSysMonSampleTime(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(300, 300),
    )



class TmnxSysMonUtilization(TextualConvention, Gauge32):
    status = "current"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )



class TmnxSysMgmtIfDstoreLockState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2))
    )



class TmnxSysNeid(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(3, 3),
    )



class TmnxConfigFileFormatType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("classicCli", 1),
          ("mdCli", 2))
    )



class TmnxSchemaPathState(TextualConvention, Integer32):
    status = "current"
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
        *(("ok", 0),
          ("errConnection", 1),
          ("errTooLong", 2),
          ("errInvalid", 3))
    )



class TmnxSysRmtMgmtLastRegStatus(TextualConvention, Integer32):
    status = "current"
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("succeeded", 1),
          ("cancelled", 2),
          ("unreachable", 3),
          ("refused", 4),
          ("dnsResolutionFailed", 5),
          ("outOfResources", 6),
          ("internal", 100))
    )



class TmnxSysRmtMgmtSrcDefaultPort(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("grpc", -1),
          ("none", 0))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxSysConformance_ObjectIdentity = ObjectIdentity
tmnxSysConformance = _TmnxSysConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1)
)
_TmnxSysCompliances_ObjectIdentity = ObjectIdentity
tmnxSysCompliances = _TmnxSysCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1)
)
_TmnxSysGroups_ObjectIdentity = ObjectIdentity
tmnxSysGroups = _TmnxSysGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2)
)
_TmnxSysV12v0Groups_ObjectIdentity = ObjectIdentity
tmnxSysV12v0Groups = _TmnxSysV12v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 60)
)
_TmnxSysV14v0Groups_ObjectIdentity = ObjectIdentity
tmnxSysV14v0Groups = _TmnxSysV14v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 72)
)
_TmnxSysV15v0Groups_ObjectIdentity = ObjectIdentity
tmnxSysV15v0Groups = _TmnxSysV15v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 76)
)
_TmnxSysV15v1Groups_ObjectIdentity = ObjectIdentity
tmnxSysV15v1Groups = _TmnxSysV15v1Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 77)
)
_TmnxSysV16v0Groups_ObjectIdentity = ObjectIdentity
tmnxSysV16v0Groups = _TmnxSysV16v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 78)
)
_TmnxSysV19v0Groups_ObjectIdentity = ObjectIdentity
tmnxSysV19v0Groups = _TmnxSysV19v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 79)
)
_TmnxSysV20v0Groups_ObjectIdentity = ObjectIdentity
tmnxSysV20v0Groups = _TmnxSysV20v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 80)
)
_TmnxSysV21v0Groups_ObjectIdentity = ObjectIdentity
tmnxSysV21v0Groups = _TmnxSysV21v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 81)
)
_TmnxSysV22v0Groups_ObjectIdentity = ObjectIdentity
tmnxSysV22v0Groups = _TmnxSysV22v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 82)
)
_TmnxSysMGGroups_ObjectIdentity = ObjectIdentity
tmnxSysMGGroups = _TmnxSysMGGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 3)
)
_TmnxSysMGCompliances_ObjectIdentity = ObjectIdentity
tmnxSysMGCompliances = _TmnxSysMGCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 4)
)
_TmnxSysDCCompliance_ObjectIdentity = ObjectIdentity
tmnxSysDCCompliance = _TmnxSysDCCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 5)
)
_TmnxSysDCGroups_ObjectIdentity = ObjectIdentity
tmnxSysDCGroups = _TmnxSysDCGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 6)
)
_TmnxSysNspProxyCompliances_ObjectIdentity = ObjectIdentity
tmnxSysNspProxyCompliances = _TmnxSysNspProxyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 7)
)
_TmnxSysNspProxyGroups_ObjectIdentity = ObjectIdentity
tmnxSysNspProxyGroups = _TmnxSysNspProxyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 8)
)
_TmnxSysObjs_ObjectIdentity = ObjectIdentity
tmnxSysObjs = _TmnxSysObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1)
)
_SysGenInfo_ObjectIdentity = ObjectIdentity
sysGenInfo = _SysGenInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1)
)


class _SgiCpuUsage_Type(Unsigned32):
    """Custom type sgiCpuUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SgiCpuUsage_Type.__name__ = "Unsigned32"
_SgiCpuUsage_Object = MibScalar
sgiCpuUsage = _SgiCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 1),
    _SgiCpuUsage_Type()
)
sgiCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgiCpuUsage.setStatus("current")
if mibBuilder.loadTexts:
    sgiCpuUsage.setUnits("percent")
_SgiMemoryUsed_Type = Unsigned32
_SgiMemoryUsed_Object = MibScalar
sgiMemoryUsed = _SgiMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 2),
    _SgiMemoryUsed_Type()
)
sgiMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgiMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    sgiMemoryUsed.setUnits("bytes")
_SgiMemoryAvailable_Type = Unsigned32
_SgiMemoryAvailable_Object = MibScalar
sgiMemoryAvailable = _SgiMemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 3),
    _SgiMemoryAvailable_Type()
)
sgiMemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgiMemoryAvailable.setStatus("current")
if mibBuilder.loadTexts:
    sgiMemoryAvailable.setUnits("bytes")
_SgiMemoryPoolAllocated_Type = Unsigned32
_SgiMemoryPoolAllocated_Object = MibScalar
sgiMemoryPoolAllocated = _SgiMemoryPoolAllocated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 4),
    _SgiMemoryPoolAllocated_Type()
)
sgiMemoryPoolAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgiMemoryPoolAllocated.setStatus("current")
if mibBuilder.loadTexts:
    sgiMemoryPoolAllocated.setUnits("bytes")
_SgiSwMajorVersion_Type = Unsigned32
_SgiSwMajorVersion_Object = MibScalar
sgiSwMajorVersion = _SgiSwMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 5),
    _SgiSwMajorVersion_Type()
)
sgiSwMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgiSwMajorVersion.setStatus("current")
_SgiSwMinorVersion_Type = Unsigned32
_SgiSwMinorVersion_Object = MibScalar
sgiSwMinorVersion = _SgiSwMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 6),
    _SgiSwMinorVersion_Type()
)
sgiSwMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgiSwMinorVersion.setStatus("current")


class _SgiSwVersionModifier_Type(OctetString):
    """Custom type sgiSwVersionModifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SgiSwVersionModifier_Type.__name__ = "OctetString"
_SgiSwVersionModifier_Object = MibScalar
sgiSwVersionModifier = _SgiSwVersionModifier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 7),
    _SgiSwVersionModifier_Type()
)
sgiSwVersionModifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgiSwVersionModifier.setStatus("current")
_SgiSnmpInGetBulks_Type = Counter32
_SgiSnmpInGetBulks_Object = MibScalar
sgiSnmpInGetBulks = _SgiSnmpInGetBulks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 8),
    _SgiSnmpInGetBulks_Type()
)
sgiSnmpInGetBulks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgiSnmpInGetBulks.setStatus("current")
_SgiKbMemoryUsed_Type = Unsigned32
_SgiKbMemoryUsed_Object = MibScalar
sgiKbMemoryUsed = _SgiKbMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 9),
    _SgiKbMemoryUsed_Type()
)
sgiKbMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgiKbMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    sgiKbMemoryUsed.setUnits("kilobytes")
_SgiKbMemoryAvailable_Type = Unsigned32
_SgiKbMemoryAvailable_Object = MibScalar
sgiKbMemoryAvailable = _SgiKbMemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 10),
    _SgiKbMemoryAvailable_Type()
)
sgiKbMemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgiKbMemoryAvailable.setStatus("current")
if mibBuilder.loadTexts:
    sgiKbMemoryAvailable.setUnits("kilobytes")
_SgiKbMemoryPoolAllocated_Type = Unsigned32
_SgiKbMemoryPoolAllocated_Object = MibScalar
sgiKbMemoryPoolAllocated = _SgiKbMemoryPoolAllocated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 11),
    _SgiKbMemoryPoolAllocated_Type()
)
sgiKbMemoryPoolAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgiKbMemoryPoolAllocated.setStatus("current")
if mibBuilder.loadTexts:
    sgiKbMemoryPoolAllocated.setUnits("kilobytes")
_TmnxSysCpuMonTable_Object = MibTable
tmnxSysCpuMonTable = _TmnxSysCpuMonTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 12)
)
if mibBuilder.loadTexts:
    tmnxSysCpuMonTable.setStatus("current")
_TmnxSysCpuMonEntry_Object = MibTableRow
tmnxSysCpuMonEntry = _TmnxSysCpuMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 12, 1)
)
tmnxSysCpuMonEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysCpuMonSampleTime"),
)
if mibBuilder.loadTexts:
    tmnxSysCpuMonEntry.setStatus("current")
_TmnxSysCpuMonSampleTime_Type = TmnxSysMonSampleTime
_TmnxSysCpuMonSampleTime_Object = MibTableColumn
tmnxSysCpuMonSampleTime = _TmnxSysCpuMonSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 12, 1, 1),
    _TmnxSysCpuMonSampleTime_Type()
)
tmnxSysCpuMonSampleTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysCpuMonSampleTime.setStatus("current")
_TmnxSysCpuMonCpuIdle_Type = TmnxSysMonUtilization
_TmnxSysCpuMonCpuIdle_Object = MibTableColumn
tmnxSysCpuMonCpuIdle = _TmnxSysCpuMonCpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 12, 1, 2),
    _TmnxSysCpuMonCpuIdle_Type()
)
tmnxSysCpuMonCpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCpuMonCpuIdle.setStatus("current")
_TmnxSysCpuMonBusyCoreUtil_Type = TmnxSysMonUtilization
_TmnxSysCpuMonBusyCoreUtil_Object = MibTableColumn
tmnxSysCpuMonBusyCoreUtil = _TmnxSysCpuMonBusyCoreUtil_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 12, 1, 3),
    _TmnxSysCpuMonBusyCoreUtil_Type()
)
tmnxSysCpuMonBusyCoreUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCpuMonBusyCoreUtil.setStatus("current")


class _TmnxSysCpuMonBusyGroupName_Type(OctetString):
    """Custom type tmnxSysCpuMonBusyGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxSysCpuMonBusyGroupName_Type.__name__ = "OctetString"
_TmnxSysCpuMonBusyGroupName_Object = MibTableColumn
tmnxSysCpuMonBusyGroupName = _TmnxSysCpuMonBusyGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 12, 1, 4),
    _TmnxSysCpuMonBusyGroupName_Type()
)
tmnxSysCpuMonBusyGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCpuMonBusyGroupName.setStatus("current")
_TmnxSysCpuMonBusyGroupUtil_Type = TmnxSysMonUtilization
_TmnxSysCpuMonBusyGroupUtil_Object = MibTableColumn
tmnxSysCpuMonBusyGroupUtil = _TmnxSysCpuMonBusyGroupUtil_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 12, 1, 5),
    _TmnxSysCpuMonBusyGroupUtil_Type()
)
tmnxSysCpuMonBusyGroupUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCpuMonBusyGroupUtil.setStatus("current")
_SgiGroupingIDs_ObjectIdentity = ObjectIdentity
sgiGroupingIDs = _SgiGroupingIDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 13)
)


class _SgiSystemGroupID_Type(Unsigned32):
    """Custom type sgiSystemGroupID based on Unsigned32"""
    defaultValue = 0


_SgiSystemGroupID_Type.__name__ = "Unsigned32"
_SgiSystemGroupID_Object = MibScalar
sgiSystemGroupID = _SgiSystemGroupID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 13, 1),
    _SgiSystemGroupID_Type()
)
sgiSystemGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sgiSystemGroupID.setStatus("current")


class _SgiSystemSubGroupID_Type(Unsigned32):
    """Custom type sgiSystemSubGroupID based on Unsigned32"""
    defaultValue = 0


_SgiSystemSubGroupID_Type.__name__ = "Unsigned32"
_SgiSystemSubGroupID_Object = MibScalar
sgiSystemSubGroupID = _SgiSystemSubGroupID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 13, 2),
    _SgiSystemSubGroupID_Type()
)
sgiSystemSubGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sgiSystemSubGroupID.setStatus("current")
_SgiSnmpFailedSets_Type = Counter32
_SgiSnmpFailedSets_Object = MibScalar
sgiSnmpFailedSets = _SgiSnmpFailedSets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 14),
    _SgiSnmpFailedSets_Type()
)
sgiSnmpFailedSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgiSnmpFailedSets.setStatus("current")
_SgiCryptoModVersion_Type = DisplayString
_SgiCryptoModVersion_Object = MibScalar
sgiCryptoModVersion = _SgiCryptoModVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 1, 15),
    _SgiCryptoModVersion_Type()
)
sgiCryptoModVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgiCryptoModVersion.setStatus("current")
_SysTimeInfo_ObjectIdentity = ObjectIdentity
sysTimeInfo = _SysTimeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2)
)


class _StiDateAndTime_Type(DateAndTime):
    """Custom type stiDateAndTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_StiDateAndTime_Type.__name__ = "DateAndTime"
_StiDateAndTime_Object = MibScalar
stiDateAndTime = _StiDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 1),
    _StiDateAndTime_Type()
)
stiDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stiDateAndTime.setStatus("current")


class _StiActiveZone_Type(DisplayString):
    """Custom type stiActiveZone based on DisplayString"""
    defaultValue = OctetString("UTC")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_StiActiveZone_Type.__name__ = "DisplayString"
_StiActiveZone_Object = MibScalar
stiActiveZone = _StiActiveZone_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 2),
    _StiActiveZone_Type()
)
stiActiveZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stiActiveZone.setStatus("current")


class _StiHoursOffset_Type(Integer32):
    """Custom type stiHoursOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-11, 12),
    )


_StiHoursOffset_Type.__name__ = "Integer32"
_StiHoursOffset_Object = MibScalar
stiHoursOffset = _StiHoursOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 3),
    _StiHoursOffset_Type()
)
stiHoursOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stiHoursOffset.setStatus("current")
if mibBuilder.loadTexts:
    stiHoursOffset.setUnits("hours")


class _StiMinutesOffset_Type(Integer32):
    """Custom type stiMinutesOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_StiMinutesOffset_Type.__name__ = "Integer32"
_StiMinutesOffset_Object = MibScalar
stiMinutesOffset = _StiMinutesOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 4),
    _StiMinutesOffset_Type()
)
stiMinutesOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stiMinutesOffset.setStatus("current")
if mibBuilder.loadTexts:
    stiMinutesOffset.setUnits("minutes")


class _StiZoneType_Type(Integer32):
    """Custom type stiZoneType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("system", 1),
          ("user", 2))
    )


_StiZoneType_Type.__name__ = "Integer32"
_StiZoneType_Object = MibScalar
stiZoneType = _StiZoneType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 5),
    _StiZoneType_Type()
)
stiZoneType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stiZoneType.setStatus("current")
_StiSummerZoneTable_Object = MibTable
stiSummerZoneTable = _StiSummerZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    stiSummerZoneTable.setStatus("current")
_StiSummerZoneEntry_Object = MibTableRow
stiSummerZoneEntry = _StiSummerZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1)
)
stiSummerZoneEntry.setIndexNames(
    (1, "TIMETRA-SYSTEM-MIB", "stiSummerZoneName"),
)
if mibBuilder.loadTexts:
    stiSummerZoneEntry.setStatus("current")


class _StiSummerZoneName_Type(OctetString):
    """Custom type stiSummerZoneName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_StiSummerZoneName_Type.__name__ = "OctetString"
_StiSummerZoneName_Object = MibTableColumn
stiSummerZoneName = _StiSummerZoneName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 1),
    _StiSummerZoneName_Type()
)
stiSummerZoneName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stiSummerZoneName.setStatus("current")
_StiSummerZoneRowStatus_Type = RowStatus
_StiSummerZoneRowStatus_Object = MibTableColumn
stiSummerZoneRowStatus = _StiSummerZoneRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 2),
    _StiSummerZoneRowStatus_Type()
)
stiSummerZoneRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneRowStatus.setStatus("current")


class _StiSummerZoneStartDate_Type(DateAndTime):
    """Custom type stiSummerZoneStartDate based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_StiSummerZoneStartDate_Type.__name__ = "DateAndTime"
_StiSummerZoneStartDate_Object = MibTableColumn
stiSummerZoneStartDate = _StiSummerZoneStartDate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 3),
    _StiSummerZoneStartDate_Type()
)
stiSummerZoneStartDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneStartDate.setStatus("obsolete")


class _StiSummerZoneEndDate_Type(DateAndTime):
    """Custom type stiSummerZoneEndDate based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_StiSummerZoneEndDate_Type.__name__ = "DateAndTime"
_StiSummerZoneEndDate_Object = MibTableColumn
stiSummerZoneEndDate = _StiSummerZoneEndDate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 4),
    _StiSummerZoneEndDate_Type()
)
stiSummerZoneEndDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneEndDate.setStatus("obsolete")


class _StiSummerZoneOffset_Type(Unsigned32):
    """Custom type stiSummerZoneOffset based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_StiSummerZoneOffset_Type.__name__ = "Unsigned32"
_StiSummerZoneOffset_Object = MibTableColumn
stiSummerZoneOffset = _StiSummerZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 5),
    _StiSummerZoneOffset_Type()
)
stiSummerZoneOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneOffset.setStatus("current")
if mibBuilder.loadTexts:
    stiSummerZoneOffset.setUnits("minutes")


class _StiSummerZoneStartDay_Type(Integer32):
    """Custom type stiSummerZoneStartDay based on Integer32"""
    defaultValue = 0

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
        *(("sunday", 0),
          ("monday", 1),
          ("tuesday", 2),
          ("wednesday", 3),
          ("thursday", 4),
          ("friday", 5),
          ("saturday", 6))
    )


_StiSummerZoneStartDay_Type.__name__ = "Integer32"
_StiSummerZoneStartDay_Object = MibTableColumn
stiSummerZoneStartDay = _StiSummerZoneStartDay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 6),
    _StiSummerZoneStartDay_Type()
)
stiSummerZoneStartDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneStartDay.setStatus("current")


class _StiSummerZoneStartWeek_Type(Integer32):
    """Custom type stiSummerZoneStartWeek based on Integer32"""
    defaultValue = 0

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
        *(("first", 0),
          ("second", 1),
          ("third", 2),
          ("fourth", 3),
          ("last", 4))
    )


_StiSummerZoneStartWeek_Type.__name__ = "Integer32"
_StiSummerZoneStartWeek_Object = MibTableColumn
stiSummerZoneStartWeek = _StiSummerZoneStartWeek_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 7),
    _StiSummerZoneStartWeek_Type()
)
stiSummerZoneStartWeek.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneStartWeek.setStatus("current")


class _StiSummerZoneStartMonth_Type(Integer32):
    """Custom type stiSummerZoneStartMonth based on Integer32"""
    defaultValue = 0

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
              11)
        )
    )
    namedValues = NamedValues(
        *(("january", 0),
          ("february", 1),
          ("march", 2),
          ("april", 3),
          ("may", 4),
          ("june", 5),
          ("july", 6),
          ("august", 7),
          ("september", 8),
          ("october", 9),
          ("november", 10),
          ("december", 11))
    )


_StiSummerZoneStartMonth_Type.__name__ = "Integer32"
_StiSummerZoneStartMonth_Object = MibTableColumn
stiSummerZoneStartMonth = _StiSummerZoneStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 8),
    _StiSummerZoneStartMonth_Type()
)
stiSummerZoneStartMonth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneStartMonth.setStatus("current")


class _StiSummerZoneStartHour_Type(Unsigned32):
    """Custom type stiSummerZoneStartHour based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_StiSummerZoneStartHour_Type.__name__ = "Unsigned32"
_StiSummerZoneStartHour_Object = MibTableColumn
stiSummerZoneStartHour = _StiSummerZoneStartHour_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 9),
    _StiSummerZoneStartHour_Type()
)
stiSummerZoneStartHour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneStartHour.setStatus("current")
if mibBuilder.loadTexts:
    stiSummerZoneStartHour.setUnits("hours")


class _StiSummerZoneStartMinute_Type(Unsigned32):
    """Custom type stiSummerZoneStartMinute based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_StiSummerZoneStartMinute_Type.__name__ = "Unsigned32"
_StiSummerZoneStartMinute_Object = MibTableColumn
stiSummerZoneStartMinute = _StiSummerZoneStartMinute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 10),
    _StiSummerZoneStartMinute_Type()
)
stiSummerZoneStartMinute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneStartMinute.setStatus("current")
if mibBuilder.loadTexts:
    stiSummerZoneStartMinute.setUnits("minutes")


class _StiSummerZoneEndDay_Type(Integer32):
    """Custom type stiSummerZoneEndDay based on Integer32"""
    defaultValue = 0

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
        *(("sunday", 0),
          ("monday", 1),
          ("tuesday", 2),
          ("wednesday", 3),
          ("thursday", 4),
          ("friday", 5),
          ("saturday", 6))
    )


_StiSummerZoneEndDay_Type.__name__ = "Integer32"
_StiSummerZoneEndDay_Object = MibTableColumn
stiSummerZoneEndDay = _StiSummerZoneEndDay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 11),
    _StiSummerZoneEndDay_Type()
)
stiSummerZoneEndDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneEndDay.setStatus("current")


class _StiSummerZoneEndWeek_Type(Integer32):
    """Custom type stiSummerZoneEndWeek based on Integer32"""
    defaultValue = 0

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
        *(("first", 0),
          ("second", 1),
          ("third", 2),
          ("fourth", 3),
          ("last", 4))
    )


_StiSummerZoneEndWeek_Type.__name__ = "Integer32"
_StiSummerZoneEndWeek_Object = MibTableColumn
stiSummerZoneEndWeek = _StiSummerZoneEndWeek_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 12),
    _StiSummerZoneEndWeek_Type()
)
stiSummerZoneEndWeek.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneEndWeek.setStatus("current")


class _StiSummerZoneEndMonth_Type(Integer32):
    """Custom type stiSummerZoneEndMonth based on Integer32"""
    defaultValue = 0

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
              11)
        )
    )
    namedValues = NamedValues(
        *(("january", 0),
          ("february", 1),
          ("march", 2),
          ("april", 3),
          ("may", 4),
          ("june", 5),
          ("july", 6),
          ("august", 7),
          ("september", 8),
          ("october", 9),
          ("november", 10),
          ("december", 11))
    )


_StiSummerZoneEndMonth_Type.__name__ = "Integer32"
_StiSummerZoneEndMonth_Object = MibTableColumn
stiSummerZoneEndMonth = _StiSummerZoneEndMonth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 13),
    _StiSummerZoneEndMonth_Type()
)
stiSummerZoneEndMonth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneEndMonth.setStatus("current")


class _StiSummerZoneEndHour_Type(Unsigned32):
    """Custom type stiSummerZoneEndHour based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_StiSummerZoneEndHour_Type.__name__ = "Unsigned32"
_StiSummerZoneEndHour_Object = MibTableColumn
stiSummerZoneEndHour = _StiSummerZoneEndHour_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 14),
    _StiSummerZoneEndHour_Type()
)
stiSummerZoneEndHour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneEndHour.setStatus("current")
if mibBuilder.loadTexts:
    stiSummerZoneEndHour.setUnits("hours")


class _StiSummerZoneEndMinute_Type(Unsigned32):
    """Custom type stiSummerZoneEndMinute based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_StiSummerZoneEndMinute_Type.__name__ = "Unsigned32"
_StiSummerZoneEndMinute_Object = MibTableColumn
stiSummerZoneEndMinute = _StiSummerZoneEndMinute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 6, 1, 15),
    _StiSummerZoneEndMinute_Type()
)
stiSummerZoneEndMinute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stiSummerZoneEndMinute.setStatus("current")
if mibBuilder.loadTexts:
    stiSummerZoneEndMinute.setUnits("minutes")


class _StiPreferLocalTime_Type(TruthValue):
    """Custom type stiPreferLocalTime based on TruthValue"""
    defaultValue = 2


_StiPreferLocalTime_Type.__name__ = "TruthValue"
_StiPreferLocalTime_Object = MibScalar
stiPreferLocalTime = _StiPreferLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 2, 7),
    _StiPreferLocalTime_Type()
)
stiPreferLocalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stiPreferLocalTime.setStatus("current")
_SysSntpInfo_ObjectIdentity = ObjectIdentity
sysSntpInfo = _SysSntpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 3)
)


class _SntpState_Type(Integer32):
    """Custom type sntpState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("broadcast", 2))
    )


_SntpState_Type.__name__ = "Integer32"
_SntpState_Object = MibScalar
sntpState = _SntpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 3, 1),
    _SntpState_Type()
)
sntpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpState.setStatus("current")
_SntpServerTable_Object = MibTable
sntpServerTable = _SntpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    sntpServerTable.setStatus("current")
_SntpServerEntry_Object = MibTableRow
sntpServerEntry = _SntpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 3, 2, 1)
)
sntpServerEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "sntpServerAddress"),
)
if mibBuilder.loadTexts:
    sntpServerEntry.setStatus("current")
_SntpServerAddress_Type = IpAddress
_SntpServerAddress_Object = MibTableColumn
sntpServerAddress = _SntpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 3, 2, 1, 1),
    _SntpServerAddress_Type()
)
sntpServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sntpServerAddress.setStatus("current")
_SntpServerRowStatus_Type = RowStatus
_SntpServerRowStatus_Object = MibTableColumn
sntpServerRowStatus = _SntpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 3, 2, 1, 2),
    _SntpServerRowStatus_Type()
)
sntpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sntpServerRowStatus.setStatus("current")


class _SntpServerVersion_Type(Integer32):
    """Custom type sntpServerVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SntpServerVersion_Type.__name__ = "Integer32"
_SntpServerVersion_Object = MibTableColumn
sntpServerVersion = _SntpServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 3, 2, 1, 3),
    _SntpServerVersion_Type()
)
sntpServerVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sntpServerVersion.setStatus("current")


class _SntpServerPreference_Type(Integer32):
    """Custom type sntpServerPreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("preferred", 2))
    )


_SntpServerPreference_Type.__name__ = "Integer32"
_SntpServerPreference_Object = MibTableColumn
sntpServerPreference = _SntpServerPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 3, 2, 1, 4),
    _SntpServerPreference_Type()
)
sntpServerPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sntpServerPreference.setStatus("current")


class _SntpServerInterval_Type(Unsigned32):
    """Custom type sntpServerInterval based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1024),
    )


_SntpServerInterval_Type.__name__ = "Unsigned32"
_SntpServerInterval_Object = MibTableColumn
sntpServerInterval = _SntpServerInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 3, 2, 1, 5),
    _SntpServerInterval_Type()
)
sntpServerInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sntpServerInterval.setStatus("current")
if mibBuilder.loadTexts:
    sntpServerInterval.setUnits("seconds")


class _SntpAdminState_Type(Integer32):
    """Custom type sntpAdminState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("inService", 2),
          ("outOfService", 3))
    )


_SntpAdminState_Type.__name__ = "Integer32"
_SntpAdminState_Object = MibScalar
sntpAdminState = _SntpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 3, 3),
    _SntpAdminState_Type()
)
sntpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpAdminState.setStatus("current")
_SntpOperStatus_Type = TmnxOperState
_SntpOperStatus_Object = MibScalar
sntpOperStatus = _SntpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 3, 4),
    _SntpOperStatus_Type()
)
sntpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpOperStatus.setStatus("current")
_SysSyncInfo_ObjectIdentity = ObjectIdentity
sysSyncInfo = _SysSyncInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4)
)


class _SsiSaveConfig_Type(TmnxActionType):
    """Custom type ssiSaveConfig based on TmnxActionType"""
    defaultValue = 2


_SsiSaveConfig_Type.__name__ = "TmnxActionType"
_SsiSaveConfig_Object = MibScalar
ssiSaveConfig = _SsiSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 15),
    _SsiSaveConfig_Type()
)
ssiSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssiSaveConfig.setStatus("current")


class _SsiSyncMode_Type(TmnxSsiSyncMode):
    """Custom type ssiSyncMode based on TmnxSsiSyncMode"""
    defaultValue = 1


_SsiSyncMode_Type.__name__ = "TmnxSsiSyncMode"
_SsiSyncMode_Object = MibScalar
ssiSyncMode = _SsiSyncMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 16),
    _SsiSyncMode_Type()
)
ssiSyncMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssiSyncMode.setStatus("current")


class _SsiSyncForce_Type(TmnxSsiSyncMode):
    """Custom type ssiSyncForce based on TmnxSsiSyncMode"""
    defaultValue = 1


_SsiSyncForce_Type.__name__ = "TmnxSsiSyncMode"
_SsiSyncForce_Object = MibScalar
ssiSyncForce = _SsiSyncForce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 17),
    _SsiSyncForce_Type()
)
ssiSyncForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssiSyncForce.setStatus("current")


class _SsiSyncStatus_Type(Integer32):
    """Custom type ssiSyncStatus based on Integer32"""
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
        *(("unknown", 0),
          ("configOnly", 1),
          ("bootEnv", 2),
          ("configFail", 3),
          ("bootEnvFail", 4),
          ("configInProgress", 5),
          ("bootEnvInProgress", 6))
    )


_SsiSyncStatus_Type.__name__ = "Integer32"
_SsiSyncStatus_Object = MibScalar
ssiSyncStatus = _SsiSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 18),
    _SsiSyncStatus_Type()
)
ssiSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiSyncStatus.setStatus("current")
_SsiSyncConfigLastTime_Type = TimeStamp
_SsiSyncConfigLastTime_Object = MibScalar
ssiSyncConfigLastTime = _SsiSyncConfigLastTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 19),
    _SsiSyncConfigLastTime_Type()
)
ssiSyncConfigLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiSyncConfigLastTime.setStatus("current")
_SsiSyncBootEnvLastTime_Type = TimeStamp
_SsiSyncBootEnvLastTime_Object = MibScalar
ssiSyncBootEnvLastTime = _SsiSyncBootEnvLastTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 20),
    _SsiSyncBootEnvLastTime_Type()
)
ssiSyncBootEnvLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiSyncBootEnvLastTime.setStatus("current")


class _SsiConfigMaxBackupRevisions_Type(Unsigned32):
    """Custom type ssiConfigMaxBackupRevisions based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_SsiConfigMaxBackupRevisions_Type.__name__ = "Unsigned32"
_SsiConfigMaxBackupRevisions_Object = MibScalar
ssiConfigMaxBackupRevisions = _SsiConfigMaxBackupRevisions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 21),
    _SsiConfigMaxBackupRevisions_Type()
)
ssiConfigMaxBackupRevisions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssiConfigMaxBackupRevisions.setStatus("current")


class _SsiSaveConfigResult_Type(Integer32):
    """Custom type ssiSaveConfigResult based on Integer32"""
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
        *(("none", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4))
    )


_SsiSaveConfigResult_Type.__name__ = "Integer32"
_SsiSaveConfigResult_Object = MibScalar
ssiSaveConfigResult = _SsiSaveConfigResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 22),
    _SsiSaveConfigResult_Type()
)
ssiSaveConfigResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiSaveConfigResult.setStatus("current")


class _SsiSaveBof_Type(TmnxActionType):
    """Custom type ssiSaveBof based on TmnxActionType"""
    defaultValue = 2


_SsiSaveBof_Type.__name__ = "TmnxActionType"
_SsiSaveBof_Object = MibScalar
ssiSaveBof = _SsiSaveBof_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 23),
    _SsiSaveBof_Type()
)
ssiSaveBof.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssiSaveBof.setStatus("current")


class _SsiSaveBofResult_Type(Integer32):
    """Custom type ssiSaveBofResult based on Integer32"""
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
        *(("none", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4))
    )


_SsiSaveBofResult_Type.__name__ = "Integer32"
_SsiSaveBofResult_Object = MibScalar
ssiSaveBofResult = _SsiSaveBofResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 24),
    _SsiSaveBofResult_Type()
)
ssiSaveBofResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiSaveBofResult.setStatus("current")


class _SsiSaveConfigDest_Type(TmnxDisplayStringURL):
    """Custom type ssiSaveConfigDest based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_SsiSaveConfigDest_Type.__name__ = "TmnxDisplayStringURL"
_SsiSaveConfigDest_Object = MibScalar
ssiSaveConfigDest = _SsiSaveConfigDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 25),
    _SsiSaveConfigDest_Type()
)
ssiSaveConfigDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssiSaveConfigDest.setStatus("current")


class _SsiSaveConfigDetail_Type(TruthValue):
    """Custom type ssiSaveConfigDetail based on TruthValue"""
    defaultValue = 2


_SsiSaveConfigDetail_Type.__name__ = "TruthValue"
_SsiSaveConfigDetail_Object = MibScalar
ssiSaveConfigDetail = _SsiSaveConfigDetail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 26),
    _SsiSaveConfigDetail_Type()
)
ssiSaveConfigDetail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssiSaveConfigDetail.setStatus("current")
_SsiRedFailoverTime_Type = TimeStamp
_SsiRedFailoverTime_Object = MibScalar
ssiRedFailoverTime = _SsiRedFailoverTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 27),
    _SsiRedFailoverTime_Type()
)
ssiRedFailoverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiRedFailoverTime.setStatus("current")


class _SsiRedFailoverReason_Type(DisplayString):
    """Custom type ssiRedFailoverReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SsiRedFailoverReason_Type.__name__ = "DisplayString"
_SsiRedFailoverReason_Object = MibScalar
ssiRedFailoverReason = _SsiRedFailoverReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 28),
    _SsiRedFailoverReason_Type()
)
ssiRedFailoverReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiRedFailoverReason.setStatus("current")
_SsiSyncRollbackLastTime_Type = TimeStamp
_SsiSyncRollbackLastTime_Object = MibScalar
ssiSyncRollbackLastTime = _SsiSyncRollbackLastTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 29),
    _SsiSyncRollbackLastTime_Type()
)
ssiSyncRollbackLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiSyncRollbackLastTime.setStatus("current")


class _SsiSyncRollbackMode_Type(TmnxSsiSyncRollbackMode):
    """Custom type ssiSyncRollbackMode based on TmnxSsiSyncRollbackMode"""
    defaultValue = 1


_SsiSyncRollbackMode_Type.__name__ = "TmnxSsiSyncRollbackMode"
_SsiSyncRollbackMode_Object = MibScalar
ssiSyncRollbackMode = _SsiSyncRollbackMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 30),
    _SsiSyncRollbackMode_Type()
)
ssiSyncRollbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssiSyncRollbackMode.setStatus("current")


class _SsiSyncRollbackForce_Type(TmnxSsiSyncRollbackMode):
    """Custom type ssiSyncRollbackForce based on TmnxSsiSyncRollbackMode"""
    defaultValue = 1


_SsiSyncRollbackForce_Type.__name__ = "TmnxSsiSyncRollbackMode"
_SsiSyncRollbackForce_Object = MibScalar
ssiSyncRollbackForce = _SsiSyncRollbackForce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 31),
    _SsiSyncRollbackForce_Type()
)
ssiSyncRollbackForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssiSyncRollbackForce.setStatus("current")


class _SsiSyncRollbackStatus_Type(Integer32):
    """Custom type ssiSyncRollbackStatus based on Integer32"""
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
        *(("unknown", 0),
          ("rollbackFail", 1),
          ("rollbackInProgress", 2),
          ("rollbackSuccess", 3))
    )


_SsiSyncRollbackStatus_Type.__name__ = "Integer32"
_SsiSyncRollbackStatus_Object = MibScalar
ssiSyncRollbackStatus = _SsiSyncRollbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 32),
    _SsiSyncRollbackStatus_Type()
)
ssiSyncRollbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiSyncRollbackStatus.setStatus("current")
_SsiSyncCertLastTime_Type = TimeStamp
_SsiSyncCertLastTime_Object = MibScalar
ssiSyncCertLastTime = _SsiSyncCertLastTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 33),
    _SsiSyncCertLastTime_Type()
)
ssiSyncCertLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiSyncCertLastTime.setStatus("current")


class _SsiSyncCertMode_Type(TruthValue):
    """Custom type ssiSyncCertMode based on TruthValue"""
    defaultValue = 1


_SsiSyncCertMode_Type.__name__ = "TruthValue"
_SsiSyncCertMode_Object = MibScalar
ssiSyncCertMode = _SsiSyncCertMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 34),
    _SsiSyncCertMode_Type()
)
ssiSyncCertMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssiSyncCertMode.setStatus("current")


class _SsiSyncCertForce_Type(TmnxActionType):
    """Custom type ssiSyncCertForce based on TmnxActionType"""
    defaultValue = 2


_SsiSyncCertForce_Type.__name__ = "TmnxActionType"
_SsiSyncCertForce_Object = MibScalar
ssiSyncCertForce = _SsiSyncCertForce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 35),
    _SsiSyncCertForce_Type()
)
ssiSyncCertForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssiSyncCertForce.setStatus("current")


class _SsiSyncCertStatus_Type(Integer32):
    """Custom type ssiSyncCertStatus based on Integer32"""
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
        *(("unknown", 0),
          ("fail", 1),
          ("inProgress", 2),
          ("success", 3))
    )


_SsiSyncCertStatus_Type.__name__ = "Integer32"
_SsiSyncCertStatus_Object = MibScalar
ssiSyncCertStatus = _SsiSyncCertStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 4, 36),
    _SsiSyncCertStatus_Type()
)
ssiSyncCertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiSyncCertStatus.setStatus("current")
_SysBootInfo_ObjectIdentity = ObjectIdentity
sysBootInfo = _SysBootInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5)
)


class _SbiConfigStatus_Type(Integer32):
    """Custom type sbiConfigStatus based on Integer32"""
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
        *(("configRead", 1),
          ("configOK", 2),
          ("defaultBooted", 3),
          ("bootConfigFailed", 4),
          ("bootRestoreFailed", 5),
          ("auto-provisioning", 6))
    )


_SbiConfigStatus_Type.__name__ = "Integer32"
_SbiConfigStatus_Object = MibScalar
sbiConfigStatus = _SbiConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 1),
    _SbiConfigStatus_Type()
)
sbiConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbiConfigStatus.setStatus("current")


class _SbiPersistStatus_Type(Integer32):
    """Custom type sbiPersistStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("persistOK", 1),
          ("noPersistFile", 2),
          ("persistMismatch", 3),
          ("persistIndexFailure", 4),
          ("persistDisabled", 5),
          ("persistInvalid", 6),
          ("persistBoot", 7),
          ("persistInit", 8),
          ("persistInProgress", 9))
    )


_SbiPersistStatus_Type.__name__ = "Integer32"
_SbiPersistStatus_Object = MibScalar
sbiPersistStatus = _SbiPersistStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 2),
    _SbiPersistStatus_Type()
)
sbiPersistStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbiPersistStatus.setStatus("current")
_SbiPersistIndex_Type = TruthValue
_SbiPersistIndex_Object = MibScalar
sbiPersistIndex = _SbiPersistIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 3),
    _SbiPersistIndex_Type()
)
sbiPersistIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbiPersistIndex.setStatus("current")


class _SbiSnmpdAdminStatus_Type(TmnxAdminState):
    """Custom type sbiSnmpdAdminStatus based on TmnxAdminState"""
    defaultValue = 2


_SbiSnmpdAdminStatus_Type.__name__ = "TmnxAdminState"
_SbiSnmpdAdminStatus_Object = MibScalar
sbiSnmpdAdminStatus = _SbiSnmpdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 4),
    _SbiSnmpdAdminStatus_Type()
)
sbiSnmpdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiSnmpdAdminStatus.setStatus("current")
_SbiSnmpdOperStatus_Type = TmnxOperState
_SbiSnmpdOperStatus_Object = MibScalar
sbiSnmpdOperStatus = _SbiSnmpdOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 5),
    _SbiSnmpdOperStatus_Type()
)
sbiSnmpdOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbiSnmpdOperStatus.setStatus("current")


class _SbiSnmpdMaxPktSize_Type(Integer32):
    """Custom type sbiSnmpdMaxPktSize based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(484, 9216),
    )


_SbiSnmpdMaxPktSize_Type.__name__ = "Integer32"
_SbiSnmpdMaxPktSize_Object = MibScalar
sbiSnmpdMaxPktSize = _SbiSnmpdMaxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 6),
    _SbiSnmpdMaxPktSize_Type()
)
sbiSnmpdMaxPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiSnmpdMaxPktSize.setStatus("current")


class _SbiSnmpdPortNum_Type(TTcpUdpPort):
    """Custom type sbiSnmpdPortNum based on TTcpUdpPort"""
    defaultValue = 161


_SbiSnmpdPortNum_Type.__name__ = "TTcpUdpPort"
_SbiSnmpdPortNum_Object = MibScalar
sbiSnmpdPortNum = _SbiSnmpdPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 7),
    _SbiSnmpdPortNum_Type()
)
sbiSnmpdPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiSnmpdPortNum.setStatus("current")


class _SbiBootConfigOKScript_Type(DisplayString):
    """Custom type sbiBootConfigOKScript based on DisplayString"""
    defaultHexValue = ""


_SbiBootConfigOKScript_Type.__name__ = "DisplayString"
_SbiBootConfigOKScript_Object = MibScalar
sbiBootConfigOKScript = _SbiBootConfigOKScript_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 8),
    _SbiBootConfigOKScript_Type()
)
sbiBootConfigOKScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiBootConfigOKScript.setStatus("current")


class _SbiConfigOKScriptStatus_Type(Integer32):
    """Custom type sbiConfigOKScriptStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRun", 0),
          ("success", 1),
          ("fail", 2))
    )


_SbiConfigOKScriptStatus_Type.__name__ = "Integer32"
_SbiConfigOKScriptStatus_Object = MibScalar
sbiConfigOKScriptStatus = _SbiConfigOKScriptStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 9),
    _SbiConfigOKScriptStatus_Type()
)
sbiConfigOKScriptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbiConfigOKScriptStatus.setStatus("current")


class _SbiBootConfigFailScript_Type(DisplayString):
    """Custom type sbiBootConfigFailScript based on DisplayString"""
    defaultHexValue = ""


_SbiBootConfigFailScript_Type.__name__ = "DisplayString"
_SbiBootConfigFailScript_Object = MibScalar
sbiBootConfigFailScript = _SbiBootConfigFailScript_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 10),
    _SbiBootConfigFailScript_Type()
)
sbiBootConfigFailScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiBootConfigFailScript.setStatus("current")


class _SbiConfigFailScriptStatus_Type(Integer32):
    """Custom type sbiConfigFailScriptStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRun", 0),
          ("success", 1),
          ("fail", 2))
    )


_SbiConfigFailScriptStatus_Type.__name__ = "Integer32"
_SbiConfigFailScriptStatus_Object = MibScalar
sbiConfigFailScriptStatus = _SbiConfigFailScriptStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 11),
    _SbiConfigFailScriptStatus_Type()
)
sbiConfigFailScriptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbiConfigFailScriptStatus.setStatus("current")


class _SbiRedSwitchoverScript_Type(DisplayString):
    """Custom type sbiRedSwitchoverScript based on DisplayString"""
    defaultHexValue = ""


_SbiRedSwitchoverScript_Type.__name__ = "DisplayString"
_SbiRedSwitchoverScript_Object = MibScalar
sbiRedSwitchoverScript = _SbiRedSwitchoverScript_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 12),
    _SbiRedSwitchoverScript_Type()
)
sbiRedSwitchoverScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiRedSwitchoverScript.setStatus("current")


class _SbiRedSwitchoverScriptStatus_Type(Integer32):
    """Custom type sbiRedSwitchoverScriptStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRun", 0),
          ("success", 1),
          ("fail", 2))
    )


_SbiRedSwitchoverScriptStatus_Type.__name__ = "Integer32"
_SbiRedSwitchoverScriptStatus_Object = MibScalar
sbiRedSwitchoverScriptStatus = _SbiRedSwitchoverScriptStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 13),
    _SbiRedSwitchoverScriptStatus_Type()
)
sbiRedSwitchoverScriptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbiRedSwitchoverScriptStatus.setStatus("current")


class _SbiAllowBootLicenseViolations_Type(TruthValue):
    """Custom type sbiAllowBootLicenseViolations based on TruthValue"""
    defaultValue = 1


_SbiAllowBootLicenseViolations_Type.__name__ = "TruthValue"
_SbiAllowBootLicenseViolations_Object = MibScalar
sbiAllowBootLicenseViolations = _SbiAllowBootLicenseViolations_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 5, 14),
    _SbiAllowBootLicenseViolations_Type()
)
sbiAllowBootLicenseViolations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAllowBootLicenseViolations.setStatus("current")
_SysRadiusInfo_ObjectIdentity = ObjectIdentity
sysRadiusInfo = _SysRadiusInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 6)
)


class _RadiusOperStatus_Type(Integer32):
    """Custom type radiusOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_RadiusOperStatus_Type.__name__ = "Integer32"
_RadiusOperStatus_Object = MibScalar
radiusOperStatus = _RadiusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 6, 1),
    _RadiusOperStatus_Type()
)
radiusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusOperStatus.setStatus("current")
_RadiusServerTable_Object = MibTable
radiusServerTable = _RadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    radiusServerTable.setStatus("current")
_RadiusServerEntry_Object = MibTableRow
radiusServerEntry = _RadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 6, 2, 1)
)
radiusServerEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "radiusServerIndex"),
)
if mibBuilder.loadTexts:
    radiusServerEntry.setStatus("current")


class _RadiusServerIndex_Type(Unsigned32):
    """Custom type radiusServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_RadiusServerIndex_Type.__name__ = "Unsigned32"
_RadiusServerIndex_Object = MibTableColumn
radiusServerIndex = _RadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 6, 2, 1, 1),
    _RadiusServerIndex_Type()
)
radiusServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusServerIndex.setStatus("current")
_RadiusServerAddress_Type = IpAddress
_RadiusServerAddress_Object = MibTableColumn
radiusServerAddress = _RadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 6, 2, 1, 2),
    _RadiusServerAddress_Type()
)
radiusServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusServerAddress.setStatus("obsolete")


class _RadiusServerOperStatus_Type(Integer32):
    """Custom type radiusServerOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_RadiusServerOperStatus_Type.__name__ = "Integer32"
_RadiusServerOperStatus_Object = MibTableColumn
radiusServerOperStatus = _RadiusServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 6, 2, 1, 3),
    _RadiusServerOperStatus_Type()
)
radiusServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusServerOperStatus.setStatus("current")
_RadiusServerInetAddressType_Type = InetAddressType
_RadiusServerInetAddressType_Object = MibTableColumn
radiusServerInetAddressType = _RadiusServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 6, 2, 1, 4),
    _RadiusServerInetAddressType_Type()
)
radiusServerInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusServerInetAddressType.setStatus("current")


class _RadiusServerInetAddress_Type(InetAddress):
    """Custom type radiusServerInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_RadiusServerInetAddress_Type.__name__ = "InetAddress"
_RadiusServerInetAddress_Object = MibTableColumn
radiusServerInetAddress = _RadiusServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 6, 2, 1, 5),
    _RadiusServerInetAddress_Type()
)
radiusServerInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusServerInetAddress.setStatus("current")
_TmnxSysNotifyObjs_ObjectIdentity = ObjectIdentity
tmnxSysNotifyObjs = _TmnxSysNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7)
)
_TmnxNotifyRow_Type = RowPointer
_TmnxNotifyRow_Object = MibScalar
tmnxNotifyRow = _TmnxNotifyRow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 1),
    _TmnxNotifyRow_Type()
)
tmnxNotifyRow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNotifyRow.setStatus("current")
_TmnxNotifyRowAdminState_Type = TmnxAdminState
_TmnxNotifyRowAdminState_Object = MibScalar
tmnxNotifyRowAdminState = _TmnxNotifyRowAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 2),
    _TmnxNotifyRowAdminState_Type()
)
tmnxNotifyRowAdminState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNotifyRowAdminState.setStatus("current")
_TmnxNotifyRowOperState_Type = TmnxOperState
_TmnxNotifyRowOperState_Object = MibScalar
tmnxNotifyRowOperState = _TmnxNotifyRowOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 3),
    _TmnxNotifyRowOperState_Type()
)
tmnxNotifyRowOperState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNotifyRowOperState.setStatus("current")
_TmnxMemoryModule_Type = TNamedItem
_TmnxMemoryModule_Object = MibScalar
tmnxMemoryModule = _TmnxMemoryModule_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 4),
    _TmnxMemoryModule_Type()
)
tmnxMemoryModule.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMemoryModule.setStatus("current")
_TmnxModuleMallocSize_Type = Unsigned32
_TmnxModuleMallocSize_Object = MibScalar
tmnxModuleMallocSize = _TmnxModuleMallocSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 5),
    _TmnxModuleMallocSize_Type()
)
tmnxModuleMallocSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxModuleMallocSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxModuleMallocSize.setUnits("bytes")
_TmnxDroppedTrapID_Type = ObjectIdentifier
_TmnxDroppedTrapID_Object = MibScalar
tmnxDroppedTrapID = _TmnxDroppedTrapID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 6),
    _TmnxDroppedTrapID_Type()
)
tmnxDroppedTrapID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDroppedTrapID.setStatus("current")


class _TmnxTrapDroppedReasonCode_Type(Integer32):
    """Custom type tmnxTrapDroppedReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("frequencyExceeded", 1)
    )


_TmnxTrapDroppedReasonCode_Type.__name__ = "Integer32"
_TmnxTrapDroppedReasonCode_Object = MibScalar
tmnxTrapDroppedReasonCode = _TmnxTrapDroppedReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 7),
    _TmnxTrapDroppedReasonCode_Type()
)
tmnxTrapDroppedReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTrapDroppedReasonCode.setStatus("current")
_TmnxTrapDroppedEntryID_Type = ObjectIdentifier
_TmnxTrapDroppedEntryID_Object = MibScalar
tmnxTrapDroppedEntryID = _TmnxTrapDroppedEntryID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 8),
    _TmnxTrapDroppedEntryID_Type()
)
tmnxTrapDroppedEntryID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTrapDroppedEntryID.setStatus("current")
_TmnxNotifyEntryOID_Type = ObjectIdentifier
_TmnxNotifyEntryOID_Object = MibScalar
tmnxNotifyEntryOID = _TmnxNotifyEntryOID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 9),
    _TmnxNotifyEntryOID_Type()
)
tmnxNotifyEntryOID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNotifyEntryOID.setStatus("current")
_TmnxSnmpdErrorMsg_Type = DisplayString
_TmnxSnmpdErrorMsg_Object = MibScalar
tmnxSnmpdErrorMsg = _TmnxSnmpdErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 10),
    _TmnxSnmpdErrorMsg_Type()
)
tmnxSnmpdErrorMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSnmpdErrorMsg.setStatus("current")
_TmnxPersistencyClient_Type = DisplayString
_TmnxPersistencyClient_Object = MibScalar
tmnxPersistencyClient = _TmnxPersistencyClient_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 11),
    _TmnxPersistencyClient_Type()
)
tmnxPersistencyClient.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPersistencyClient.setStatus("current")
_TmnxPersistencyFileLocator_Type = DisplayString
_TmnxPersistencyFileLocator_Object = MibScalar
tmnxPersistencyFileLocator = _TmnxPersistencyFileLocator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 12),
    _TmnxPersistencyFileLocator_Type()
)
tmnxPersistencyFileLocator.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPersistencyFileLocator.setStatus("current")
_TmnxPersistencyNotifyMsg_Type = DisplayString
_TmnxPersistencyNotifyMsg_Object = MibScalar
tmnxPersistencyNotifyMsg = _TmnxPersistencyNotifyMsg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 13),
    _TmnxPersistencyNotifyMsg_Type()
)
tmnxPersistencyNotifyMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPersistencyNotifyMsg.setStatus("current")
_TmnxPersistenceAffectedCpm_Type = DisplayString
_TmnxPersistenceAffectedCpm_Object = MibScalar
tmnxPersistenceAffectedCpm = _TmnxPersistenceAffectedCpm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 14),
    _TmnxPersistenceAffectedCpm_Type()
)
tmnxPersistenceAffectedCpm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPersistenceAffectedCpm.setStatus("current")


class _TmnxSysTimeSetBy_Type(Integer32):
    """Custom type tmnxSysTimeSetBy based on Integer32"""
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
        *(("ntp", 1),
          ("sntp", 2),
          ("snmp", 3),
          ("manually", 4),
          ("rtc", 5))
    )


_TmnxSysTimeSetBy_Type.__name__ = "Integer32"
_TmnxSysTimeSetBy_Object = MibScalar
tmnxSysTimeSetBy = _TmnxSysTimeSetBy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 15),
    _TmnxSysTimeSetBy_Type()
)
tmnxSysTimeSetBy.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSysTimeSetBy.setStatus("current")
_TmnxFtpFailureMsg_Type = DisplayString
_TmnxFtpFailureMsg_Object = MibScalar
tmnxFtpFailureMsg = _TmnxFtpFailureMsg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 16),
    _TmnxFtpFailureMsg_Type()
)
tmnxFtpFailureMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxFtpFailureMsg.setStatus("current")
_TmnxFtpFailureDestAddressType_Type = InetAddressType
_TmnxFtpFailureDestAddressType_Object = MibScalar
tmnxFtpFailureDestAddressType = _TmnxFtpFailureDestAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 17),
    _TmnxFtpFailureDestAddressType_Type()
)
tmnxFtpFailureDestAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxFtpFailureDestAddressType.setStatus("current")


class _TmnxFtpFailureDestAddress_Type(InetAddress):
    """Custom type tmnxFtpFailureDestAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxFtpFailureDestAddress_Type.__name__ = "InetAddress"
_TmnxFtpFailureDestAddress_Object = MibScalar
tmnxFtpFailureDestAddress = _TmnxFtpFailureDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 18),
    _TmnxFtpFailureDestAddress_Type()
)
tmnxFtpFailureDestAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxFtpFailureDestAddress.setStatus("current")
_TmnxNotifyObjectName_Type = DisplayString
_TmnxNotifyObjectName_Object = MibScalar
tmnxNotifyObjectName = _TmnxNotifyObjectName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 19),
    _TmnxNotifyObjectName_Type()
)
tmnxNotifyObjectName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNotifyObjectName.setStatus("current")
_TmnxSyncFailureReason_Type = DisplayString
_TmnxSyncFailureReason_Object = MibScalar
tmnxSyncFailureReason = _TmnxSyncFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 20),
    _TmnxSyncFailureReason_Type()
)
tmnxSyncFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSyncFailureReason.setStatus("current")
_TmnxSysExecScript_Type = DisplayString
_TmnxSysExecScript_Object = MibScalar
tmnxSysExecScript = _TmnxSysExecScript_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 21),
    _TmnxSysExecScript_Type()
)
tmnxSysExecScript.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSysExecScript.setStatus("current")


class _TmnxSysExecResult_Type(Integer32):
    """Custom type tmnxSysExecResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("success", 1),
          ("fail", 2))
    )


_TmnxSysExecResult_Type.__name__ = "Integer32"
_TmnxSysExecResult_Object = MibScalar
tmnxSysExecResult = _TmnxSysExecResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 22),
    _TmnxSysExecResult_Type()
)
tmnxSysExecResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSysExecResult.setStatus("current")


class _TmnxSysRollbackFileType_Type(Integer32):
    """Custom type tmnxSysRollbackFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rollback", 1),
          ("rescue", 2))
    )


_TmnxSysRollbackFileType_Type.__name__ = "Integer32"
_TmnxSysRollbackFileType_Object = MibScalar
tmnxSysRollbackFileType = _TmnxSysRollbackFileType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 23),
    _TmnxSysRollbackFileType_Type()
)
tmnxSysRollbackFileType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSysRollbackFileType.setStatus("current")


class _TmnxSysFileErrorType_Type(Integer32):
    """Custom type tmnxSysFileErrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read", 1),
          ("write", 2))
    )


_TmnxSysFileErrorType_Type.__name__ = "Integer32"
_TmnxSysFileErrorType_Object = MibScalar
tmnxSysFileErrorType = _TmnxSysFileErrorType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 24),
    _TmnxSysFileErrorType_Type()
)
tmnxSysFileErrorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSysFileErrorType.setStatus("current")
_TmnxTrapDroppedCount_Type = Unsigned32
_TmnxTrapDroppedCount_Object = MibScalar
tmnxTrapDroppedCount = _TmnxTrapDroppedCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 25),
    _TmnxTrapDroppedCount_Type()
)
tmnxTrapDroppedCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTrapDroppedCount.setStatus("current")
_TmnxSysDNSSecDomainName_Type = TmnxDisplayStringURL
_TmnxSysDNSSecDomainName_Object = MibScalar
tmnxSysDNSSecDomainName = _TmnxSysDNSSecDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 26),
    _TmnxSysDNSSecDomainName_Type()
)
tmnxSysDNSSecDomainName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSysDNSSecDomainName.setStatus("current")
_TmnxSysLicenseErrorReason_Type = TItemDescription
_TmnxSysLicenseErrorReason_Object = MibScalar
tmnxSysLicenseErrorReason = _TmnxSysLicenseErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 27),
    _TmnxSysLicenseErrorReason_Type()
)
tmnxSysLicenseErrorReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSysLicenseErrorReason.setStatus("current")
_TmnxSysLicenseTimeLeft_Type = Unsigned32
_TmnxSysLicenseTimeLeft_Object = MibScalar
tmnxSysLicenseTimeLeft = _TmnxSysLicenseTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 28),
    _TmnxSysLicenseTimeLeft_Type()
)
tmnxSysLicenseTimeLeft.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSysLicenseTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSysLicenseTimeLeft.setUnits("minutes")
_TmnxSysNotifVsdServerName_Type = TLDisplayString
_TmnxSysNotifVsdServerName_Object = MibScalar
tmnxSysNotifVsdServerName = _TmnxSysNotifVsdServerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 30),
    _TmnxSysNotifVsdServerName_Type()
)
tmnxSysNotifVsdServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSysNotifVsdServerName.setStatus("current")


class _TmnxSysNotifXmppServerName_Type(DisplayString):
    """Custom type tmnxSysNotifXmppServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxSysNotifXmppServerName_Type.__name__ = "DisplayString"
_TmnxSysNotifXmppServerName_Object = MibScalar
tmnxSysNotifXmppServerName = _TmnxSysNotifXmppServerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 31),
    _TmnxSysNotifXmppServerName_Type()
)
tmnxSysNotifXmppServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSysNotifXmppServerName.setStatus("current")
_TmnxSysLicenseErrorAction_Type = TItemDescription
_TmnxSysLicenseErrorAction_Object = MibScalar
tmnxSysLicenseErrorAction = _TmnxSysLicenseErrorAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 32),
    _TmnxSysLicenseErrorAction_Type()
)
tmnxSysLicenseErrorAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSysLicenseErrorAction.setStatus("current")
_TmnxSysNotifAppStatsApplication_Type = TmnxSysLicenseApplication
_TmnxSysNotifAppStatsApplication_Object = MibScalar
tmnxSysNotifAppStatsApplication = _TmnxSysNotifAppStatsApplication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 33),
    _TmnxSysNotifAppStatsApplication_Type()
)
tmnxSysNotifAppStatsApplication.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSysNotifAppStatsApplication.setStatus("current")
_TmnxSysNotifAppStatsType_Type = TmnxSysLicenseAppStatsType
_TmnxSysNotifAppStatsType_Object = MibScalar
tmnxSysNotifAppStatsType = _TmnxSysNotifAppStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 34),
    _TmnxSysNotifAppStatsType_Type()
)
tmnxSysNotifAppStatsType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSysNotifAppStatsType.setStatus("current")
_TmnxSysNotifAppStatsTime_Type = DateAndTime
_TmnxSysNotifAppStatsTime_Object = MibScalar
tmnxSysNotifAppStatsTime = _TmnxSysNotifAppStatsTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 35),
    _TmnxSysNotifAppStatsTime_Type()
)
tmnxSysNotifAppStatsTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSysNotifAppStatsTime.setStatus("current")


class _TmnxNotifySysMgmtIfOriginalMode_Type(Integer32):
    """Custom type tmnxNotifySysMgmtIfOriginalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("classic", 1),
          ("modelDriven", 2),
          ("mixed", 3))
    )


_TmnxNotifySysMgmtIfOriginalMode_Type.__name__ = "Integer32"
_TmnxNotifySysMgmtIfOriginalMode_Object = MibScalar
tmnxNotifySysMgmtIfOriginalMode = _TmnxNotifySysMgmtIfOriginalMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 36),
    _TmnxNotifySysMgmtIfOriginalMode_Type()
)
tmnxNotifySysMgmtIfOriginalMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNotifySysMgmtIfOriginalMode.setStatus("current")
_TmnxSysLicensingNotifyGroup_Type = TmnxSysLicensingGroup
_TmnxSysLicensingNotifyGroup_Object = MibScalar
tmnxSysLicensingNotifyGroup = _TmnxSysLicensingNotifyGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 37),
    _TmnxSysLicensingNotifyGroup_Type()
)
tmnxSysLicensingNotifyGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSysLicensingNotifyGroup.setStatus("current")
_TmnxSysLicensedNotifyAppName_Type = TNamedItem
_TmnxSysLicensedNotifyAppName_Object = MibScalar
tmnxSysLicensedNotifyAppName = _TmnxSysLicensedNotifyAppName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 38),
    _TmnxSysLicensedNotifyAppName_Type()
)
tmnxSysLicensedNotifyAppName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSysLicensedNotifyAppName.setStatus("current")
_TmnxPrimaryConfigFileFormatType_Type = TmnxConfigFileFormatType
_TmnxPrimaryConfigFileFormatType_Object = MibScalar
tmnxPrimaryConfigFileFormatType = _TmnxPrimaryConfigFileFormatType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 39),
    _TmnxPrimaryConfigFileFormatType_Type()
)
tmnxPrimaryConfigFileFormatType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPrimaryConfigFileFormatType.setStatus("current")
_TmnxLiConfigFileFormatType_Type = TmnxConfigFileFormatType
_TmnxLiConfigFileFormatType_Object = MibScalar
tmnxLiConfigFileFormatType = _TmnxLiConfigFileFormatType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 7, 40),
    _TmnxLiConfigFileFormatType_Type()
)
tmnxLiConfigFileFormatType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLiConfigFileFormatType.setStatus("current")
_SysLoginControlInfo_ObjectIdentity = ObjectIdentity
sysLoginControlInfo = _SysLoginControlInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8)
)


class _SlcFtpInboundMaxSessions_Type(Unsigned32):
    """Custom type slcFtpInboundMaxSessions based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_SlcFtpInboundMaxSessions_Type.__name__ = "Unsigned32"
_SlcFtpInboundMaxSessions_Object = MibScalar
slcFtpInboundMaxSessions = _SlcFtpInboundMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 1),
    _SlcFtpInboundMaxSessions_Type()
)
slcFtpInboundMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcFtpInboundMaxSessions.setStatus("current")


class _SlcTelnetInboundMaxSessions_Type(Unsigned32):
    """Custom type slcTelnetInboundMaxSessions based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_SlcTelnetInboundMaxSessions_Type.__name__ = "Unsigned32"
_SlcTelnetInboundMaxSessions_Object = MibScalar
slcTelnetInboundMaxSessions = _SlcTelnetInboundMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 2),
    _SlcTelnetInboundMaxSessions_Type()
)
slcTelnetInboundMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcTelnetInboundMaxSessions.setStatus("current")


class _SlcTelnetOutboundMaxSessions_Type(Unsigned32):
    """Custom type slcTelnetOutboundMaxSessions based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SlcTelnetOutboundMaxSessions_Type.__name__ = "Unsigned32"
_SlcTelnetOutboundMaxSessions_Object = MibScalar
slcTelnetOutboundMaxSessions = _SlcTelnetOutboundMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 3),
    _SlcTelnetOutboundMaxSessions_Type()
)
slcTelnetOutboundMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcTelnetOutboundMaxSessions.setStatus("current")


class _SlcPreLoginMessage_Type(TmnxLongDisplayString):
    """Custom type slcPreLoginMessage based on TmnxLongDisplayString"""
    defaultHexValue = ""

    subtypeSpec = TmnxLongDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 900),
    )


_SlcPreLoginMessage_Type.__name__ = "TmnxLongDisplayString"
_SlcPreLoginMessage_Object = MibScalar
slcPreLoginMessage = _SlcPreLoginMessage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 4),
    _SlcPreLoginMessage_Type()
)
slcPreLoginMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcPreLoginMessage.setStatus("current")


class _SlcPreLoginMessageInclName_Type(TruthValue):
    """Custom type slcPreLoginMessageInclName based on TruthValue"""
    defaultValue = 2


_SlcPreLoginMessageInclName_Type.__name__ = "TruthValue"
_SlcPreLoginMessageInclName_Object = MibScalar
slcPreLoginMessageInclName = _SlcPreLoginMessageInclName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 5),
    _SlcPreLoginMessageInclName_Type()
)
slcPreLoginMessageInclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcPreLoginMessageInclName.setStatus("current")


class _SlcMessageOfTheDay_Type(TmnxLongDisplayString):
    """Custom type slcMessageOfTheDay based on TmnxLongDisplayString"""
    defaultHexValue = ""

    subtypeSpec = TmnxLongDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 900),
    )


_SlcMessageOfTheDay_Type.__name__ = "TmnxLongDisplayString"
_SlcMessageOfTheDay_Object = MibScalar
slcMessageOfTheDay = _SlcMessageOfTheDay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 6),
    _SlcMessageOfTheDay_Type()
)
slcMessageOfTheDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcMessageOfTheDay.setStatus("current")


class _SlcMessageOfTheDayType_Type(Integer32):
    """Custom type slcMessageOfTheDayType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("motd-type-none", 0),
          ("motd-type-url", 1),
          ("motd-type-text", 2))
    )


_SlcMessageOfTheDayType_Type.__name__ = "Integer32"
_SlcMessageOfTheDayType_Object = MibScalar
slcMessageOfTheDayType = _SlcMessageOfTheDayType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 7),
    _SlcMessageOfTheDayType_Type()
)
slcMessageOfTheDayType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcMessageOfTheDayType.setStatus("current")


class _SlcLoginBanner_Type(TruthValue):
    """Custom type slcLoginBanner based on TruthValue"""
    defaultValue = 2


_SlcLoginBanner_Type.__name__ = "TruthValue"
_SlcLoginBanner_Object = MibScalar
slcLoginBanner = _SlcLoginBanner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 8),
    _SlcLoginBanner_Type()
)
slcLoginBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcLoginBanner.setStatus("current")


class _SlcLoginExponentialBackOff_Type(TruthValue):
    """Custom type slcLoginExponentialBackOff based on TruthValue"""
    defaultValue = 2


_SlcLoginExponentialBackOff_Type.__name__ = "TruthValue"
_SlcLoginExponentialBackOff_Object = MibScalar
slcLoginExponentialBackOff = _SlcLoginExponentialBackOff_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 9),
    _SlcLoginExponentialBackOff_Type()
)
slcLoginExponentialBackOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcLoginExponentialBackOff.setStatus("current")


class _SlcTelnetGracefulShutdown_Type(TruthValue):
    """Custom type slcTelnetGracefulShutdown based on TruthValue"""
    defaultValue = 2


_SlcTelnetGracefulShutdown_Type.__name__ = "TruthValue"
_SlcTelnetGracefulShutdown_Object = MibScalar
slcTelnetGracefulShutdown = _SlcTelnetGracefulShutdown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 10),
    _SlcTelnetGracefulShutdown_Type()
)
slcTelnetGracefulShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcTelnetGracefulShutdown.setStatus("current")


class _SlcSSHGracefulShutdown_Type(TruthValue):
    """Custom type slcSSHGracefulShutdown based on TruthValue"""
    defaultValue = 1


_SlcSSHGracefulShutdown_Type.__name__ = "TruthValue"
_SlcSSHGracefulShutdown_Object = MibScalar
slcSSHGracefulShutdown = _SlcSSHGracefulShutdown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 11),
    _SlcSSHGracefulShutdown_Type()
)
slcSSHGracefulShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcSSHGracefulShutdown.setStatus("current")


class _SlcTelnetMinTTLValue_Type(Unsigned32):
    """Custom type slcTelnetMinTTLValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlcTelnetMinTTLValue_Type.__name__ = "Unsigned32"
_SlcTelnetMinTTLValue_Object = MibScalar
slcTelnetMinTTLValue = _SlcTelnetMinTTLValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 12),
    _SlcTelnetMinTTLValue_Type()
)
slcTelnetMinTTLValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcTelnetMinTTLValue.setStatus("current")


class _SlcSSHMinTTLValue_Type(Unsigned32):
    """Custom type slcSSHMinTTLValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlcSSHMinTTLValue_Type.__name__ = "Unsigned32"
_SlcSSHMinTTLValue_Object = MibScalar
slcSSHMinTTLValue = _SlcSSHMinTTLValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 13),
    _SlcSSHMinTTLValue_Type()
)
slcSSHMinTTLValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcSSHMinTTLValue.setStatus("current")


class _SlcSSHInboundMaxSessions_Type(Unsigned32):
    """Custom type slcSSHInboundMaxSessions based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_SlcSSHInboundMaxSessions_Type.__name__ = "Unsigned32"
_SlcSSHInboundMaxSessions_Object = MibScalar
slcSSHInboundMaxSessions = _SlcSSHInboundMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 14),
    _SlcSSHInboundMaxSessions_Type()
)
slcSSHInboundMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcSSHInboundMaxSessions.setStatus("current")


class _SlcSSHOutboundMaxSessions_Type(Unsigned32):
    """Custom type slcSSHOutboundMaxSessions based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SlcSSHOutboundMaxSessions_Type.__name__ = "Unsigned32"
_SlcSSHOutboundMaxSessions_Object = MibScalar
slcSSHOutboundMaxSessions = _SlcSSHOutboundMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 15),
    _SlcSSHOutboundMaxSessions_Type()
)
slcSSHOutboundMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcSSHOutboundMaxSessions.setStatus("current")


class _SlcIdleTimeout_Type(Unsigned32):
    """Custom type slcIdleTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
        ValueRangeConstraint(9999, 9999),
    )


_SlcIdleTimeout_Type.__name__ = "Unsigned32"
_SlcIdleTimeout_Object = MibScalar
slcIdleTimeout = _SlcIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 16),
    _SlcIdleTimeout_Type()
)
slcIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    slcIdleTimeout.setUnits("minutes")


class _SlcLoginScriptGlobal_Type(TmnxDisplayStringURL):
    """Custom type slcLoginScriptGlobal based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_SlcLoginScriptGlobal_Type.__name__ = "TmnxDisplayStringURL"
_SlcLoginScriptGlobal_Object = MibScalar
slcLoginScriptGlobal = _SlcLoginScriptGlobal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 17),
    _SlcLoginScriptGlobal_Type()
)
slcLoginScriptGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcLoginScriptGlobal.setStatus("current")


class _SlcLoginScriptPerUserDirectory_Type(TmnxDisplayStringURL):
    """Custom type slcLoginScriptPerUserDirectory based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_SlcLoginScriptPerUserDirectory_Type.__name__ = "TmnxDisplayStringURL"
_SlcLoginScriptPerUserDirectory_Object = MibScalar
slcLoginScriptPerUserDirectory = _SlcLoginScriptPerUserDirectory_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 18),
    _SlcLoginScriptPerUserDirectory_Type()
)
slcLoginScriptPerUserDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcLoginScriptPerUserDirectory.setStatus("current")


class _SlcLoginScriptPerUserFilename_Type(DisplayString):
    """Custom type slcLoginScriptPerUserFilename based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_SlcLoginScriptPerUserFilename_Type.__name__ = "DisplayString"
_SlcLoginScriptPerUserFilename_Object = MibScalar
slcLoginScriptPerUserFilename = _SlcLoginScriptPerUserFilename_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 8, 19),
    _SlcLoginScriptPerUserFilename_Type()
)
slcLoginScriptPerUserFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcLoginScriptPerUserFilename.setStatus("current")
_SysLACPInfo_ObjectIdentity = ObjectIdentity
sysLACPInfo = _SysLACPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 9)
)


class _SysLACPSystemPriority_Type(Unsigned32):
    """Custom type sysLACPSystemPriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SysLACPSystemPriority_Type.__name__ = "Unsigned32"
_SysLACPSystemPriority_Object = MibScalar
sysLACPSystemPriority = _SysLACPSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 9, 1),
    _SysLACPSystemPriority_Type()
)
sysLACPSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLACPSystemPriority.setStatus("current")
_SysTacplusInfo_ObjectIdentity = ObjectIdentity
sysTacplusInfo = _SysTacplusInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 10)
)


class _TacplusOperStatus_Type(Integer32):
    """Custom type tacplusOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_TacplusOperStatus_Type.__name__ = "Integer32"
_TacplusOperStatus_Object = MibScalar
tacplusOperStatus = _TacplusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 10, 1),
    _TacplusOperStatus_Type()
)
tacplusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacplusOperStatus.setStatus("current")
_TacplusServerTable_Object = MibTable
tacplusServerTable = _TacplusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 10, 2)
)
if mibBuilder.loadTexts:
    tacplusServerTable.setStatus("current")
_TacplusServerEntry_Object = MibTableRow
tacplusServerEntry = _TacplusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 10, 2, 1)
)
tacplusServerEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tacplusServerIndex"),
)
if mibBuilder.loadTexts:
    tacplusServerEntry.setStatus("current")


class _TacplusServerIndex_Type(Unsigned32):
    """Custom type tacplusServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TacplusServerIndex_Type.__name__ = "Unsigned32"
_TacplusServerIndex_Object = MibTableColumn
tacplusServerIndex = _TacplusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 10, 2, 1, 1),
    _TacplusServerIndex_Type()
)
tacplusServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tacplusServerIndex.setStatus("current")
_TacplusServerAddress_Type = IpAddress
_TacplusServerAddress_Object = MibTableColumn
tacplusServerAddress = _TacplusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 10, 2, 1, 2),
    _TacplusServerAddress_Type()
)
tacplusServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacplusServerAddress.setStatus("obsolete")


class _TacplusServerOperStatus_Type(Integer32):
    """Custom type tacplusServerOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_TacplusServerOperStatus_Type.__name__ = "Integer32"
_TacplusServerOperStatus_Object = MibTableColumn
tacplusServerOperStatus = _TacplusServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 10, 2, 1, 3),
    _TacplusServerOperStatus_Type()
)
tacplusServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacplusServerOperStatus.setStatus("current")
_TacPlusServerInetAddressType_Type = InetAddressType
_TacPlusServerInetAddressType_Object = MibTableColumn
tacPlusServerInetAddressType = _TacPlusServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 10, 2, 1, 4),
    _TacPlusServerInetAddressType_Type()
)
tacPlusServerInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacPlusServerInetAddressType.setStatus("current")


class _TacPlusServerInetAddress_Type(InetAddress):
    """Custom type tacPlusServerInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TacPlusServerInetAddress_Type.__name__ = "InetAddress"
_TacPlusServerInetAddress_Object = MibTableColumn
tacPlusServerInetAddress = _TacPlusServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 10, 2, 1, 5),
    _TacPlusServerInetAddress_Type()
)
tacPlusServerInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacPlusServerInetAddress.setStatus("current")
_SysBofInfo_ObjectIdentity = ObjectIdentity
sysBofInfo = _SysBofInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11)
)
_SbiActiveIpAddr_Type = IpAddress
_SbiActiveIpAddr_Object = MibScalar
sbiActiveIpAddr = _SbiActiveIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 1),
    _SbiActiveIpAddr_Type()
)
sbiActiveIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiActiveIpAddr.setStatus("current")


class _SbiActiveIpMask_Type(IpAddressPrefixLength):
    """Custom type sbiActiveIpMask based on IpAddressPrefixLength"""
    defaultValue = 0


_SbiActiveIpMask_Type.__name__ = "IpAddressPrefixLength"
_SbiActiveIpMask_Object = MibScalar
sbiActiveIpMask = _SbiActiveIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 2),
    _SbiActiveIpMask_Type()
)
sbiActiveIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiActiveIpMask.setStatus("current")
_SbiStandbyIpAddr_Type = IpAddress
_SbiStandbyIpAddr_Object = MibScalar
sbiStandbyIpAddr = _SbiStandbyIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 3),
    _SbiStandbyIpAddr_Type()
)
sbiStandbyIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiStandbyIpAddr.setStatus("current")


class _SbiStandbyIpMask_Type(IpAddressPrefixLength):
    """Custom type sbiStandbyIpMask based on IpAddressPrefixLength"""
    defaultValue = 0


_SbiStandbyIpMask_Type.__name__ = "IpAddressPrefixLength"
_SbiStandbyIpMask_Object = MibScalar
sbiStandbyIpMask = _SbiStandbyIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 4),
    _SbiStandbyIpMask_Type()
)
sbiStandbyIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiStandbyIpMask.setStatus("current")


class _SbiPrimaryImage_Type(TmnxDisplayStringURL):
    """Custom type sbiPrimaryImage based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_SbiPrimaryImage_Type.__name__ = "TmnxDisplayStringURL"
_SbiPrimaryImage_Object = MibScalar
sbiPrimaryImage = _SbiPrimaryImage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 5),
    _SbiPrimaryImage_Type()
)
sbiPrimaryImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiPrimaryImage.setStatus("current")


class _SbiSecondaryImage_Type(TmnxDisplayStringURL):
    """Custom type sbiSecondaryImage based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_SbiSecondaryImage_Type.__name__ = "TmnxDisplayStringURL"
_SbiSecondaryImage_Object = MibScalar
sbiSecondaryImage = _SbiSecondaryImage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 6),
    _SbiSecondaryImage_Type()
)
sbiSecondaryImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiSecondaryImage.setStatus("current")


class _SbiTertiaryImage_Type(TmnxDisplayStringURL):
    """Custom type sbiTertiaryImage based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_SbiTertiaryImage_Type.__name__ = "TmnxDisplayStringURL"
_SbiTertiaryImage_Object = MibScalar
sbiTertiaryImage = _SbiTertiaryImage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 7),
    _SbiTertiaryImage_Type()
)
sbiTertiaryImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiTertiaryImage.setStatus("current")


class _SbiPrimaryConfigFile_Type(TmnxDisplayStringURL):
    """Custom type sbiPrimaryConfigFile based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_SbiPrimaryConfigFile_Type.__name__ = "TmnxDisplayStringURL"
_SbiPrimaryConfigFile_Object = MibScalar
sbiPrimaryConfigFile = _SbiPrimaryConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 8),
    _SbiPrimaryConfigFile_Type()
)
sbiPrimaryConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiPrimaryConfigFile.setStatus("current")


class _SbiSecondaryConfigFile_Type(TmnxDisplayStringURL):
    """Custom type sbiSecondaryConfigFile based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_SbiSecondaryConfigFile_Type.__name__ = "TmnxDisplayStringURL"
_SbiSecondaryConfigFile_Object = MibScalar
sbiSecondaryConfigFile = _SbiSecondaryConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 9),
    _SbiSecondaryConfigFile_Type()
)
sbiSecondaryConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiSecondaryConfigFile.setStatus("current")


class _SbiTertiaryConfigFile_Type(TmnxDisplayStringURL):
    """Custom type sbiTertiaryConfigFile based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_SbiTertiaryConfigFile_Type.__name__ = "TmnxDisplayStringURL"
_SbiTertiaryConfigFile_Object = MibScalar
sbiTertiaryConfigFile = _SbiTertiaryConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 10),
    _SbiTertiaryConfigFile_Type()
)
sbiTertiaryConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiTertiaryConfigFile.setStatus("current")


class _SbiPersist_Type(TruthValue):
    """Custom type sbiPersist based on TruthValue"""
    defaultValue = 2


_SbiPersist_Type.__name__ = "TruthValue"
_SbiPersist_Object = MibScalar
sbiPersist = _SbiPersist_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 11),
    _SbiPersist_Type()
)
sbiPersist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiPersist.setStatus("current")


class _SbiConsoleSpeed_Type(Unsigned32):
    """Custom type sbiConsoleSpeed based on Unsigned32"""
    defaultValue = 115200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 9600),
        ValueRangeConstraint(19200, 19200),
        ValueRangeConstraint(38400, 38400),
        ValueRangeConstraint(57600, 57600),
        ValueRangeConstraint(115200, 115200),
    )


_SbiConsoleSpeed_Type.__name__ = "Unsigned32"
_SbiConsoleSpeed_Object = MibScalar
sbiConsoleSpeed = _SbiConsoleSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 12),
    _SbiConsoleSpeed_Type()
)
sbiConsoleSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiConsoleSpeed.setStatus("current")
if mibBuilder.loadTexts:
    sbiConsoleSpeed.setUnits("bps")


class _SbiAutoNegotiate_Type(TruthValue):
    """Custom type sbiAutoNegotiate based on TruthValue"""
    defaultValue = 1


_SbiAutoNegotiate_Type.__name__ = "TruthValue"
_SbiAutoNegotiate_Object = MibScalar
sbiAutoNegotiate = _SbiAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 13),
    _SbiAutoNegotiate_Type()
)
sbiAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoNegotiate.setStatus("current")


class _SbiSpeed_Type(Unsigned32):
    """Custom type sbiSpeed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
    )


_SbiSpeed_Type.__name__ = "Unsigned32"
_SbiSpeed_Object = MibScalar
sbiSpeed = _SbiSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 14),
    _SbiSpeed_Type()
)
sbiSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiSpeed.setStatus("current")
if mibBuilder.loadTexts:
    sbiSpeed.setUnits("megabps")


class _SbiDuplex_Type(Integer32):
    """Custom type sbiDuplex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_SbiDuplex_Type.__name__ = "Integer32"
_SbiDuplex_Object = MibScalar
sbiDuplex = _SbiDuplex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 15),
    _SbiDuplex_Type()
)
sbiDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiDuplex.setStatus("current")
_SbiPrimaryDns_Type = IpAddress
_SbiPrimaryDns_Object = MibScalar
sbiPrimaryDns = _SbiPrimaryDns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 16),
    _SbiPrimaryDns_Type()
)
sbiPrimaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiPrimaryDns.setStatus("current")
_SbiSecondaryDns_Type = IpAddress
_SbiSecondaryDns_Object = MibScalar
sbiSecondaryDns = _SbiSecondaryDns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 17),
    _SbiSecondaryDns_Type()
)
sbiSecondaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiSecondaryDns.setStatus("current")
_SbiTertiaryDns_Type = IpAddress
_SbiTertiaryDns_Object = MibScalar
sbiTertiaryDns = _SbiTertiaryDns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 18),
    _SbiTertiaryDns_Type()
)
sbiTertiaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiTertiaryDns.setStatus("current")


class _SbiDnsDomain_Type(DisplayString):
    """Custom type sbiDnsDomain based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 178),
    )


_SbiDnsDomain_Type.__name__ = "DisplayString"
_SbiDnsDomain_Object = MibScalar
sbiDnsDomain = _SbiDnsDomain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 19),
    _SbiDnsDomain_Type()
)
sbiDnsDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiDnsDomain.setStatus("current")


class _SbiWait_Type(Unsigned32):
    """Custom type sbiWait based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SbiWait_Type.__name__ = "Unsigned32"
_SbiWait_Object = MibScalar
sbiWait = _SbiWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 20),
    _SbiWait_Type()
)
sbiWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiWait.setStatus("current")
if mibBuilder.loadTexts:
    sbiWait.setUnits("seconds")
_SbiStaticRouteTable_Object = MibTable
sbiStaticRouteTable = _SbiStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 21)
)
if mibBuilder.loadTexts:
    sbiStaticRouteTable.setStatus("current")
_SbiStaticRouteEntry_Object = MibTableRow
sbiStaticRouteEntry = _SbiStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 21, 1)
)
sbiStaticRouteEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "sbiStaticRouteDest"),
    (0, "TIMETRA-SYSTEM-MIB", "sbiStaticRouteMask"),
)
if mibBuilder.loadTexts:
    sbiStaticRouteEntry.setStatus("current")
_SbiStaticRouteDest_Type = IpAddress
_SbiStaticRouteDest_Object = MibTableColumn
sbiStaticRouteDest = _SbiStaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 21, 1, 1),
    _SbiStaticRouteDest_Type()
)
sbiStaticRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sbiStaticRouteDest.setStatus("current")
_SbiStaticRouteMask_Type = IpAddressPrefixLength
_SbiStaticRouteMask_Object = MibTableColumn
sbiStaticRouteMask = _SbiStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 21, 1, 2),
    _SbiStaticRouteMask_Type()
)
sbiStaticRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sbiStaticRouteMask.setStatus("current")
_SbiStaticRouteNextHop_Type = IpAddress
_SbiStaticRouteNextHop_Object = MibTableColumn
sbiStaticRouteNextHop = _SbiStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 21, 1, 3),
    _SbiStaticRouteNextHop_Type()
)
sbiStaticRouteNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbiStaticRouteNextHop.setStatus("current")
_SbiStaticRouteRowStatus_Type = RowStatus
_SbiStaticRouteRowStatus_Object = MibTableColumn
sbiStaticRouteRowStatus = _SbiStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 21, 1, 4),
    _SbiStaticRouteRowStatus_Type()
)
sbiStaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbiStaticRouteRowStatus.setStatus("current")


class _SbiActiveIPv6Addr_Type(InetAddressIPv6):
    """Custom type sbiActiveIPv6Addr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_SbiActiveIPv6Addr_Type.__name__ = "InetAddressIPv6"
_SbiActiveIPv6Addr_Object = MibScalar
sbiActiveIPv6Addr = _SbiActiveIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 22),
    _SbiActiveIPv6Addr_Type()
)
sbiActiveIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiActiveIPv6Addr.setStatus("current")


class _SbiActiveIPv6PfxLen_Type(InetAddressPrefixLength):
    """Custom type sbiActiveIPv6PfxLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SbiActiveIPv6PfxLen_Type.__name__ = "InetAddressPrefixLength"
_SbiActiveIPv6PfxLen_Object = MibScalar
sbiActiveIPv6PfxLen = _SbiActiveIPv6PfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 23),
    _SbiActiveIPv6PfxLen_Type()
)
sbiActiveIPv6PfxLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiActiveIPv6PfxLen.setStatus("current")


class _SbiStandbyIPv6Addr_Type(InetAddressIPv6):
    """Custom type sbiStandbyIPv6Addr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_SbiStandbyIPv6Addr_Type.__name__ = "InetAddressIPv6"
_SbiStandbyIPv6Addr_Object = MibScalar
sbiStandbyIPv6Addr = _SbiStandbyIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 24),
    _SbiStandbyIPv6Addr_Type()
)
sbiStandbyIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiStandbyIPv6Addr.setStatus("current")


class _SbiStandbyIPv6PfxLen_Type(InetAddressPrefixLength):
    """Custom type sbiStandbyIPv6PfxLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SbiStandbyIPv6PfxLen_Type.__name__ = "InetAddressPrefixLength"
_SbiStandbyIPv6PfxLen_Object = MibScalar
sbiStandbyIPv6PfxLen = _SbiStandbyIPv6PfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 25),
    _SbiStandbyIPv6PfxLen_Type()
)
sbiStandbyIPv6PfxLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiStandbyIPv6PfxLen.setStatus("current")


class _SbiPrimaryDnsIPv6Addr_Type(InetAddressIPv6):
    """Custom type sbiPrimaryDnsIPv6Addr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_SbiPrimaryDnsIPv6Addr_Type.__name__ = "InetAddressIPv6"
_SbiPrimaryDnsIPv6Addr_Object = MibScalar
sbiPrimaryDnsIPv6Addr = _SbiPrimaryDnsIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 26),
    _SbiPrimaryDnsIPv6Addr_Type()
)
sbiPrimaryDnsIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiPrimaryDnsIPv6Addr.setStatus("current")


class _SbiSecondaryDnsIPv6Addr_Type(InetAddressIPv6):
    """Custom type sbiSecondaryDnsIPv6Addr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_SbiSecondaryDnsIPv6Addr_Type.__name__ = "InetAddressIPv6"
_SbiSecondaryDnsIPv6Addr_Object = MibScalar
sbiSecondaryDnsIPv6Addr = _SbiSecondaryDnsIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 27),
    _SbiSecondaryDnsIPv6Addr_Type()
)
sbiSecondaryDnsIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiSecondaryDnsIPv6Addr.setStatus("current")


class _SbiTertiaryDnsIPv6Addr_Type(InetAddressIPv6):
    """Custom type sbiTertiaryDnsIPv6Addr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_SbiTertiaryDnsIPv6Addr_Type.__name__ = "InetAddressIPv6"
_SbiTertiaryDnsIPv6Addr_Object = MibScalar
sbiTertiaryDnsIPv6Addr = _SbiTertiaryDnsIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 28),
    _SbiTertiaryDnsIPv6Addr_Type()
)
sbiTertiaryDnsIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiTertiaryDnsIPv6Addr.setStatus("current")
_SbiStaticRouteIPv6Table_Object = MibTable
sbiStaticRouteIPv6Table = _SbiStaticRouteIPv6Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 29)
)
if mibBuilder.loadTexts:
    sbiStaticRouteIPv6Table.setStatus("current")
_SbiStaticRouteIPv6Entry_Object = MibTableRow
sbiStaticRouteIPv6Entry = _SbiStaticRouteIPv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 29, 1)
)
sbiStaticRouteIPv6Entry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "sbiStaticRouteIPv6Dest"),
    (0, "TIMETRA-SYSTEM-MIB", "sbiStaticRouteIPv6PfxLen"),
)
if mibBuilder.loadTexts:
    sbiStaticRouteIPv6Entry.setStatus("current")
_SbiStaticRouteIPv6Dest_Type = InetAddressIPv6
_SbiStaticRouteIPv6Dest_Object = MibTableColumn
sbiStaticRouteIPv6Dest = _SbiStaticRouteIPv6Dest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 29, 1, 1),
    _SbiStaticRouteIPv6Dest_Type()
)
sbiStaticRouteIPv6Dest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sbiStaticRouteIPv6Dest.setStatus("current")


class _SbiStaticRouteIPv6PfxLen_Type(InetAddressPrefixLength):
    """Custom type sbiStaticRouteIPv6PfxLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SbiStaticRouteIPv6PfxLen_Type.__name__ = "InetAddressPrefixLength"
_SbiStaticRouteIPv6PfxLen_Object = MibTableColumn
sbiStaticRouteIPv6PfxLen = _SbiStaticRouteIPv6PfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 29, 1, 2),
    _SbiStaticRouteIPv6PfxLen_Type()
)
sbiStaticRouteIPv6PfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sbiStaticRouteIPv6PfxLen.setStatus("current")
_SbiStaticRouteIPv6NextHop_Type = InetAddressIPv6
_SbiStaticRouteIPv6NextHop_Object = MibTableColumn
sbiStaticRouteIPv6NextHop = _SbiStaticRouteIPv6NextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 29, 1, 3),
    _SbiStaticRouteIPv6NextHop_Type()
)
sbiStaticRouteIPv6NextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbiStaticRouteIPv6NextHop.setStatus("current")
_SbiStaticRouteIPv6RowStatus_Type = RowStatus
_SbiStaticRouteIPv6RowStatus_Object = MibTableColumn
sbiStaticRouteIPv6RowStatus = _SbiStaticRouteIPv6RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 29, 1, 4),
    _SbiStaticRouteIPv6RowStatus_Type()
)
sbiStaticRouteIPv6RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbiStaticRouteIPv6RowStatus.setStatus("current")


class _SbiLiSeparate_Type(TruthValue):
    """Custom type sbiLiSeparate based on TruthValue"""
    defaultValue = 2


_SbiLiSeparate_Type.__name__ = "TruthValue"
_SbiLiSeparate_Object = MibScalar
sbiLiSeparate = _SbiLiSeparate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 30),
    _SbiLiSeparate_Type()
)
sbiLiSeparate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiLiSeparate.setStatus("current")


class _SbiLiLocalSave_Type(TruthValue):
    """Custom type sbiLiLocalSave based on TruthValue"""
    defaultValue = 1


_SbiLiLocalSave_Type.__name__ = "TruthValue"
_SbiLiLocalSave_Object = MibScalar
sbiLiLocalSave = _SbiLiLocalSave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 31),
    _SbiLiLocalSave_Type()
)
sbiLiLocalSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiLiLocalSave.setStatus("current")


class _SbiLicenseFile_Type(TmnxDisplayStringURL):
    """Custom type sbiLicenseFile based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_SbiLicenseFile_Type.__name__ = "TmnxDisplayStringURL"
_SbiLicenseFile_Object = MibScalar
sbiLicenseFile = _SbiLicenseFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 32),
    _SbiLicenseFile_Type()
)
sbiLicenseFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiLicenseFile.setStatus("current")


class _SbiFips1402Level1_Type(TruthValue):
    """Custom type sbiFips1402Level1 based on TruthValue"""
    defaultValue = 2


_SbiFips1402Level1_Type.__name__ = "TruthValue"
_SbiFips1402Level1_Object = MibScalar
sbiFips1402Level1 = _SbiFips1402Level1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 34),
    _SbiFips1402Level1_Type()
)
sbiFips1402Level1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbiFips1402Level1.setStatus("current")


class _SbiSystemBaseMacAddress_Type(MacAddress):
    """Custom type sbiSystemBaseMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_SbiSystemBaseMacAddress_Type.__name__ = "MacAddress"
_SbiSystemBaseMacAddress_Object = MibScalar
sbiSystemBaseMacAddress = _SbiSystemBaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 35),
    _SbiSystemBaseMacAddress_Type()
)
sbiSystemBaseMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiSystemBaseMacAddress.setStatus("current")


class _SbiEssSystemType_Type(TruthValue):
    """Custom type sbiEssSystemType based on TruthValue"""
    defaultValue = 2


_SbiEssSystemType_Type.__name__ = "TruthValue"
_SbiEssSystemType_Object = MibScalar
sbiEssSystemType = _SbiEssSystemType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 36),
    _SbiEssSystemType_Type()
)
sbiEssSystemType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiEssSystemType.setStatus("current")


class _SbiSystemProfile_Type(Integer32):
    """Custom type sbiSystemProfile based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("profileA", 1),
          ("profileB", 2))
    )


_SbiSystemProfile_Type.__name__ = "Integer32"
_SbiSystemProfile_Object = MibScalar
sbiSystemProfile = _SbiSystemProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 37),
    _SbiSystemProfile_Type()
)
sbiSystemProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiSystemProfile.setStatus("current")


class _SbiAutoBoot_Type(TruthValue):
    """Custom type sbiAutoBoot based on TruthValue"""
    defaultValue = 2


_SbiAutoBoot_Type.__name__ = "TruthValue"
_SbiAutoBoot_Object = MibScalar
sbiAutoBoot = _SbiAutoBoot_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 38),
    _SbiAutoBoot_Type()
)
sbiAutoBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoBoot.setStatus("current")


class _SbiAutoBootClientId_Type(OctetString):
    """Custom type sbiAutoBootClientId based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 58),
    )


_SbiAutoBootClientId_Type.__name__ = "OctetString"
_SbiAutoBootClientId_Object = MibScalar
sbiAutoBootClientId = _SbiAutoBootClientId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 39),
    _SbiAutoBootClientId_Type()
)
sbiAutoBootClientId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoBootClientId.setStatus("current")


class _SbiAutoBootClientIdType_Type(Integer32):
    """Custom type sbiAutoBootClientIdType based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("ascii", 2),
          ("hex", 3),
          ("mac", 4))
    )


_SbiAutoBootClientIdType_Type.__name__ = "Integer32"
_SbiAutoBootClientIdType_Object = MibScalar
sbiAutoBootClientIdType = _SbiAutoBootClientIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 40),
    _SbiAutoBootClientIdType_Type()
)
sbiAutoBootClientIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoBootClientIdType.setStatus("current")


class _SbiAutoBootUsingMgmt_Type(TruthValue):
    """Custom type sbiAutoBootUsingMgmt based on TruthValue"""
    defaultValue = 2


_SbiAutoBootUsingMgmt_Type.__name__ = "TruthValue"
_SbiAutoBootUsingMgmt_Object = MibScalar
sbiAutoBootUsingMgmt = _SbiAutoBootUsingMgmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 41),
    _SbiAutoBootUsingMgmt_Type()
)
sbiAutoBootUsingMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoBootUsingMgmt.setStatus("current")


class _SbiAutoBootUsingInband_Type(TruthValue):
    """Custom type sbiAutoBootUsingInband based on TruthValue"""
    defaultValue = 2


_SbiAutoBootUsingInband_Type.__name__ = "TruthValue"
_SbiAutoBootUsingInband_Object = MibScalar
sbiAutoBootUsingInband = _SbiAutoBootUsingInband_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 42),
    _SbiAutoBootUsingInband_Type()
)
sbiAutoBootUsingInband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoBootUsingInband.setStatus("current")


class _SbiAutoBootInbandVlan_Type(Unsigned32):
    """Custom type sbiAutoBootInbandVlan based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_SbiAutoBootInbandVlan_Type.__name__ = "Unsigned32"
_SbiAutoBootInbandVlan_Object = MibScalar
sbiAutoBootInbandVlan = _SbiAutoBootInbandVlan_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 43),
    _SbiAutoBootInbandVlan_Type()
)
sbiAutoBootInbandVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoBootInbandVlan.setStatus("current")


class _SbiAutoBootUsingIpv4_Type(TruthValue):
    """Custom type sbiAutoBootUsingIpv4 based on TruthValue"""
    defaultValue = 2


_SbiAutoBootUsingIpv4_Type.__name__ = "TruthValue"
_SbiAutoBootUsingIpv4_Object = MibScalar
sbiAutoBootUsingIpv4 = _SbiAutoBootUsingIpv4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 44),
    _SbiAutoBootUsingIpv4_Type()
)
sbiAutoBootUsingIpv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoBootUsingIpv4.setStatus("current")


class _SbiAutoBootUsingIpv6_Type(TruthValue):
    """Custom type sbiAutoBootUsingIpv6 based on TruthValue"""
    defaultValue = 2


_SbiAutoBootUsingIpv6_Type.__name__ = "TruthValue"
_SbiAutoBootUsingIpv6_Object = MibScalar
sbiAutoBootUsingIpv6 = _SbiAutoBootUsingIpv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 45),
    _SbiAutoBootUsingIpv6_Type()
)
sbiAutoBootUsingIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoBootUsingIpv6.setStatus("current")


class _SbiAutoBootIncludeUserClass_Type(TruthValue):
    """Custom type sbiAutoBootIncludeUserClass based on TruthValue"""
    defaultValue = 2


_SbiAutoBootIncludeUserClass_Type.__name__ = "TruthValue"
_SbiAutoBootIncludeUserClass_Object = MibScalar
sbiAutoBootIncludeUserClass = _SbiAutoBootIncludeUserClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 46),
    _SbiAutoBootIncludeUserClass_Type()
)
sbiAutoBootIncludeUserClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoBootIncludeUserClass.setStatus("current")


class _SbiAutoBootVlanDiscovery_Type(TruthValue):
    """Custom type sbiAutoBootVlanDiscovery based on TruthValue"""
    defaultValue = 2


_SbiAutoBootVlanDiscovery_Type.__name__ = "TruthValue"
_SbiAutoBootVlanDiscovery_Object = MibScalar
sbiAutoBootVlanDiscovery = _SbiAutoBootVlanDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 47),
    _SbiAutoBootVlanDiscovery_Type()
)
sbiAutoBootVlanDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoBootVlanDiscovery.setStatus("current")


class _SbiAutoBootMode_Type(Integer32):
    """Custom type sbiAutoBootMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("ospf", 2))
    )


_SbiAutoBootMode_Type.__name__ = "Integer32"
_SbiAutoBootMode_Object = MibScalar
sbiAutoBootMode = _SbiAutoBootMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 48),
    _SbiAutoBootMode_Type()
)
sbiAutoBootMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoBootMode.setStatus("current")
_SbiAutoBootInfo_ObjectIdentity = ObjectIdentity
sbiAutoBootInfo = _SbiAutoBootInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 49)
)


class _SbiAutoBootPortMtu_Type(Unsigned32):
    """Custom type sbiAutoBootPortMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9800),
    )


_SbiAutoBootPortMtu_Type.__name__ = "Unsigned32"
_SbiAutoBootPortMtu_Object = MibScalar
sbiAutoBootPortMtu = _SbiAutoBootPortMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 49, 2),
    _SbiAutoBootPortMtu_Type()
)
sbiAutoBootPortMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoBootPortMtu.setStatus("current")
if mibBuilder.loadTexts:
    sbiAutoBootPortMtu.setUnits("bytes")
_SbiAutoBootOspf_ObjectIdentity = ObjectIdentity
sbiAutoBootOspf = _SbiAutoBootOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 49, 3)
)


class _SbiAutoBootOspfNeid_Type(TmnxSysNeid):
    """Custom type sbiAutoBootOspfNeid based on TmnxSysNeid"""
    defaultHexValue = ""


_SbiAutoBootOspfNeid_Type.__name__ = "TmnxSysNeid"
_SbiAutoBootOspfNeid_Object = MibScalar
sbiAutoBootOspfNeid = _SbiAutoBootOspfNeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 49, 3, 1),
    _SbiAutoBootOspfNeid_Type()
)
sbiAutoBootOspfNeid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoBootOspfNeid.setStatus("current")


class _SbiAutoBootOspfVendorId_Type(Unsigned32):
    """Custom type sbiAutoBootOspfVendorId based on Unsigned32"""
    defaultValue = 140

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_SbiAutoBootOspfVendorId_Type.__name__ = "Unsigned32"
_SbiAutoBootOspfVendorId_Object = MibScalar
sbiAutoBootOspfVendorId = _SbiAutoBootOspfVendorId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 49, 3, 2),
    _SbiAutoBootOspfVendorId_Type()
)
sbiAutoBootOspfVendorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoBootOspfVendorId.setStatus("current")


class _SbiAutoBootOspfNeipV4Type_Type(InetAddressType):
    """Custom type sbiAutoBootOspfNeipV4Type based on InetAddressType"""
    defaultValue = 0


_SbiAutoBootOspfNeipV4Type_Type.__name__ = "InetAddressType"
_SbiAutoBootOspfNeipV4Type_Object = MibScalar
sbiAutoBootOspfNeipV4Type = _SbiAutoBootOspfNeipV4Type_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 49, 3, 3),
    _SbiAutoBootOspfNeipV4Type_Type()
)
sbiAutoBootOspfNeipV4Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoBootOspfNeipV4Type.setStatus("current")


class _SbiAutoBootOspfNeipV4_Type(InetAddress):
    """Custom type sbiAutoBootOspfNeipV4 based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_SbiAutoBootOspfNeipV4_Type.__name__ = "InetAddress"
_SbiAutoBootOspfNeipV4_Object = MibScalar
sbiAutoBootOspfNeipV4 = _SbiAutoBootOspfNeipV4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 49, 3, 4),
    _SbiAutoBootOspfNeipV4_Type()
)
sbiAutoBootOspfNeipV4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoBootOspfNeipV4.setStatus("current")


class _SbiAutoBootOspfNeipV6Type_Type(InetAddressType):
    """Custom type sbiAutoBootOspfNeipV6Type based on InetAddressType"""
    defaultValue = 0


_SbiAutoBootOspfNeipV6Type_Type.__name__ = "InetAddressType"
_SbiAutoBootOspfNeipV6Type_Object = MibScalar
sbiAutoBootOspfNeipV6Type = _SbiAutoBootOspfNeipV6Type_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 49, 3, 5),
    _SbiAutoBootOspfNeipV6Type_Type()
)
sbiAutoBootOspfNeipV6Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoBootOspfNeipV6Type.setStatus("current")


class _SbiAutoBootOspfNeipV6_Type(InetAddress):
    """Custom type sbiAutoBootOspfNeipV6 based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_SbiAutoBootOspfNeipV6_Type.__name__ = "InetAddress"
_SbiAutoBootOspfNeipV6_Object = MibScalar
sbiAutoBootOspfNeipV6 = _SbiAutoBootOspfNeipV6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 49, 3, 6),
    _SbiAutoBootOspfNeipV6_Type()
)
sbiAutoBootOspfNeipV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoBootOspfNeipV6.setStatus("current")


class _SbiAutoBootOspfMtu_Type(Unsigned32):
    """Custom type sbiAutoBootOspfMtu based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9786),
    )


_SbiAutoBootOspfMtu_Type.__name__ = "Unsigned32"
_SbiAutoBootOspfMtu_Object = MibScalar
sbiAutoBootOspfMtu = _SbiAutoBootOspfMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 49, 3, 7),
    _SbiAutoBootOspfMtu_Type()
)
sbiAutoBootOspfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoBootOspfMtu.setStatus("current")
if mibBuilder.loadTexts:
    sbiAutoBootOspfMtu.setUnits("bytes")
_SbiAutoConfigure_ObjectIdentity = ObjectIdentity
sbiAutoConfigure = _SbiAutoConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 54)
)
_SbiAutoIpv4_ObjectIdentity = ObjectIdentity
sbiAutoIpv4 = _SbiAutoIpv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 54, 1)
)


class _SbiAutoIpv4Dhcp_Type(TruthValue):
    """Custom type sbiAutoIpv4Dhcp based on TruthValue"""
    defaultValue = 2


_SbiAutoIpv4Dhcp_Type.__name__ = "TruthValue"
_SbiAutoIpv4Dhcp_Object = MibScalar
sbiAutoIpv4Dhcp = _SbiAutoIpv4Dhcp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 54, 1, 1),
    _SbiAutoIpv4Dhcp_Type()
)
sbiAutoIpv4Dhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoIpv4Dhcp.setStatus("current")


class _SbiAutoIpv4DhcpClientIdType_Type(Integer32):
    """Custom type sbiAutoIpv4DhcpClientIdType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("ascii", 2),
          ("hex", 3))
    )


_SbiAutoIpv4DhcpClientIdType_Type.__name__ = "Integer32"
_SbiAutoIpv4DhcpClientIdType_Object = MibScalar
sbiAutoIpv4DhcpClientIdType = _SbiAutoIpv4DhcpClientIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 54, 1, 3),
    _SbiAutoIpv4DhcpClientIdType_Type()
)
sbiAutoIpv4DhcpClientIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoIpv4DhcpClientIdType.setStatus("current")


class _SbiAutoIpv4DhcpClientId_Type(OctetString):
    """Custom type sbiAutoIpv4DhcpClientId based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SbiAutoIpv4DhcpClientId_Type.__name__ = "OctetString"
_SbiAutoIpv4DhcpClientId_Object = MibScalar
sbiAutoIpv4DhcpClientId = _SbiAutoIpv4DhcpClientId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 54, 1, 4),
    _SbiAutoIpv4DhcpClientId_Type()
)
sbiAutoIpv4DhcpClientId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoIpv4DhcpClientId.setStatus("current")


class _SbiAutoIpv4DhcpOptUserClass_Type(TruthValue):
    """Custom type sbiAutoIpv4DhcpOptUserClass based on TruthValue"""
    defaultValue = 2


_SbiAutoIpv4DhcpOptUserClass_Type.__name__ = "TruthValue"
_SbiAutoIpv4DhcpOptUserClass_Object = MibScalar
sbiAutoIpv4DhcpOptUserClass = _SbiAutoIpv4DhcpOptUserClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 54, 1, 5),
    _SbiAutoIpv4DhcpOptUserClass_Type()
)
sbiAutoIpv4DhcpOptUserClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoIpv4DhcpOptUserClass.setStatus("current")


class _SbiAutoIpv4DhcpTimeout_Type(Unsigned32):
    """Custom type sbiAutoIpv4DhcpTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SbiAutoIpv4DhcpTimeout_Type.__name__ = "Unsigned32"
_SbiAutoIpv4DhcpTimeout_Object = MibScalar
sbiAutoIpv4DhcpTimeout = _SbiAutoIpv4DhcpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 54, 1, 6),
    _SbiAutoIpv4DhcpTimeout_Type()
)
sbiAutoIpv4DhcpTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbiAutoIpv4DhcpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    sbiAutoIpv4DhcpTimeout.setUnits("seconds")
_SbiAutoIpv6_ObjectIdentity = ObjectIdentity
sbiAutoIpv6 = _SbiAutoIpv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 54, 2)
)


class _SbiAutoIpv6Dhcp_Type(TruthValue):
    """Custom type sbiAutoIpv6Dhcp based on TruthValue"""
    defaultValue = 2


_SbiAutoIpv6Dhcp_Type.__name__ = "TruthValue"
_SbiAutoIpv6Dhcp_Object = MibScalar
sbiAutoIpv6Dhcp = _SbiAutoIpv6Dhcp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 54, 2, 1),
    _SbiAutoIpv6Dhcp_Type()
)
sbiAutoIpv6Dhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoIpv6Dhcp.setStatus("current")


class _SbiAutoIpv6DhcpClientIdType_Type(Integer32):
    """Custom type sbiAutoIpv6DhcpClientIdType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("duidEnterprise", 2),
          ("duidLinkLocal", 3))
    )


_SbiAutoIpv6DhcpClientIdType_Type.__name__ = "Integer32"
_SbiAutoIpv6DhcpClientIdType_Object = MibScalar
sbiAutoIpv6DhcpClientIdType = _SbiAutoIpv6DhcpClientIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 54, 2, 2),
    _SbiAutoIpv6DhcpClientIdType_Type()
)
sbiAutoIpv6DhcpClientIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoIpv6DhcpClientIdType.setStatus("current")


class _SbiAutoIpv6DhcpClientIdDuidType_Type(Integer32):
    """Custom type sbiAutoIpv6DhcpClientIdDuidType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ascii", 2),
          ("hex", 3))
    )


_SbiAutoIpv6DhcpClientIdDuidType_Type.__name__ = "Integer32"
_SbiAutoIpv6DhcpClientIdDuidType_Object = MibScalar
sbiAutoIpv6DhcpClientIdDuidType = _SbiAutoIpv6DhcpClientIdDuidType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 54, 2, 3),
    _SbiAutoIpv6DhcpClientIdDuidType_Type()
)
sbiAutoIpv6DhcpClientIdDuidType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoIpv6DhcpClientIdDuidType.setStatus("current")


class _SbiAutoIpv6DhcpClientIdDuid_Type(OctetString):
    """Custom type sbiAutoIpv6DhcpClientIdDuid based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 124),
    )


_SbiAutoIpv6DhcpClientIdDuid_Type.__name__ = "OctetString"
_SbiAutoIpv6DhcpClientIdDuid_Object = MibScalar
sbiAutoIpv6DhcpClientIdDuid = _SbiAutoIpv6DhcpClientIdDuid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 54, 2, 4),
    _SbiAutoIpv6DhcpClientIdDuid_Type()
)
sbiAutoIpv6DhcpClientIdDuid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoIpv6DhcpClientIdDuid.setStatus("current")


class _SbiAutoIpv6DhcpOptUserClass_Type(TruthValue):
    """Custom type sbiAutoIpv6DhcpOptUserClass based on TruthValue"""
    defaultValue = 2


_SbiAutoIpv6DhcpOptUserClass_Type.__name__ = "TruthValue"
_SbiAutoIpv6DhcpOptUserClass_Object = MibScalar
sbiAutoIpv6DhcpOptUserClass = _SbiAutoIpv6DhcpOptUserClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 54, 2, 5),
    _SbiAutoIpv6DhcpOptUserClass_Type()
)
sbiAutoIpv6DhcpOptUserClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiAutoIpv6DhcpOptUserClass.setStatus("current")


class _SbiAutoIpv6DhcpTimeout_Type(Unsigned32):
    """Custom type sbiAutoIpv6DhcpTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SbiAutoIpv6DhcpTimeout_Type.__name__ = "Unsigned32"
_SbiAutoIpv6DhcpTimeout_Object = MibScalar
sbiAutoIpv6DhcpTimeout = _SbiAutoIpv6DhcpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 54, 2, 6),
    _SbiAutoIpv6DhcpTimeout_Type()
)
sbiAutoIpv6DhcpTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbiAutoIpv6DhcpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    sbiAutoIpv6DhcpTimeout.setUnits("seconds")
_SbiStandbyAIpAddr_Type = IpAddress
_SbiStandbyAIpAddr_Object = MibScalar
sbiStandbyAIpAddr = _SbiStandbyAIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 55),
    _SbiStandbyAIpAddr_Type()
)
sbiStandbyAIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiStandbyAIpAddr.setStatus("current")


class _SbiStandbyAIpMask_Type(IpAddressPrefixLength):
    """Custom type sbiStandbyAIpMask based on IpAddressPrefixLength"""
    defaultValue = 0


_SbiStandbyAIpMask_Type.__name__ = "IpAddressPrefixLength"
_SbiStandbyAIpMask_Object = MibScalar
sbiStandbyAIpMask = _SbiStandbyAIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 56),
    _SbiStandbyAIpMask_Type()
)
sbiStandbyAIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiStandbyAIpMask.setStatus("current")


class _SbiStandbyAIPv6Addr_Type(InetAddressIPv6):
    """Custom type sbiStandbyAIPv6Addr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_SbiStandbyAIPv6Addr_Type.__name__ = "InetAddressIPv6"
_SbiStandbyAIPv6Addr_Object = MibScalar
sbiStandbyAIPv6Addr = _SbiStandbyAIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 57),
    _SbiStandbyAIPv6Addr_Type()
)
sbiStandbyAIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiStandbyAIPv6Addr.setStatus("current")


class _SbiStandbyAIPv6PfxLen_Type(InetAddressPrefixLength):
    """Custom type sbiStandbyAIPv6PfxLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SbiStandbyAIPv6PfxLen_Type.__name__ = "InetAddressPrefixLength"
_SbiStandbyAIPv6PfxLen_Object = MibScalar
sbiStandbyAIPv6PfxLen = _SbiStandbyAIPv6PfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 58),
    _SbiStandbyAIPv6PfxLen_Type()
)
sbiStandbyAIPv6PfxLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiStandbyAIPv6PfxLen.setStatus("current")
_SbiStandbyBIpAddr_Type = IpAddress
_SbiStandbyBIpAddr_Object = MibScalar
sbiStandbyBIpAddr = _SbiStandbyBIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 59),
    _SbiStandbyBIpAddr_Type()
)
sbiStandbyBIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiStandbyBIpAddr.setStatus("current")


class _SbiStandbyBIpMask_Type(IpAddressPrefixLength):
    """Custom type sbiStandbyBIpMask based on IpAddressPrefixLength"""
    defaultValue = 0


_SbiStandbyBIpMask_Type.__name__ = "IpAddressPrefixLength"
_SbiStandbyBIpMask_Object = MibScalar
sbiStandbyBIpMask = _SbiStandbyBIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 60),
    _SbiStandbyBIpMask_Type()
)
sbiStandbyBIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiStandbyBIpMask.setStatus("current")


class _SbiStandbyBIPv6Addr_Type(InetAddressIPv6):
    """Custom type sbiStandbyBIPv6Addr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_SbiStandbyBIPv6Addr_Type.__name__ = "InetAddressIPv6"
_SbiStandbyBIPv6Addr_Object = MibScalar
sbiStandbyBIPv6Addr = _SbiStandbyBIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 61),
    _SbiStandbyBIPv6Addr_Type()
)
sbiStandbyBIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiStandbyBIPv6Addr.setStatus("current")


class _SbiStandbyBIPv6PfxLen_Type(InetAddressPrefixLength):
    """Custom type sbiStandbyBIPv6PfxLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SbiStandbyBIPv6PfxLen_Type.__name__ = "InetAddressPrefixLength"
_SbiStandbyBIPv6PfxLen_Object = MibScalar
sbiStandbyBIPv6PfxLen = _SbiStandbyBIPv6PfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 62),
    _SbiStandbyBIPv6PfxLen_Type()
)
sbiStandbyBIPv6PfxLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiStandbyBIPv6PfxLen.setStatus("current")
_SbiStandbyCIpAddr_Type = IpAddress
_SbiStandbyCIpAddr_Object = MibScalar
sbiStandbyCIpAddr = _SbiStandbyCIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 63),
    _SbiStandbyCIpAddr_Type()
)
sbiStandbyCIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiStandbyCIpAddr.setStatus("current")


class _SbiStandbyCIpMask_Type(IpAddressPrefixLength):
    """Custom type sbiStandbyCIpMask based on IpAddressPrefixLength"""
    defaultValue = 0


_SbiStandbyCIpMask_Type.__name__ = "IpAddressPrefixLength"
_SbiStandbyCIpMask_Object = MibScalar
sbiStandbyCIpMask = _SbiStandbyCIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 64),
    _SbiStandbyCIpMask_Type()
)
sbiStandbyCIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiStandbyCIpMask.setStatus("current")


class _SbiStandbyCIPv6Addr_Type(InetAddressIPv6):
    """Custom type sbiStandbyCIPv6Addr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_SbiStandbyCIPv6Addr_Type.__name__ = "InetAddressIPv6"
_SbiStandbyCIPv6Addr_Object = MibScalar
sbiStandbyCIPv6Addr = _SbiStandbyCIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 65),
    _SbiStandbyCIPv6Addr_Type()
)
sbiStandbyCIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiStandbyCIPv6Addr.setStatus("current")


class _SbiStandbyCIPv6PfxLen_Type(InetAddressPrefixLength):
    """Custom type sbiStandbyCIPv6PfxLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SbiStandbyCIPv6PfxLen_Type.__name__ = "InetAddressPrefixLength"
_SbiStandbyCIPv6PfxLen_Object = MibScalar
sbiStandbyCIPv6PfxLen = _SbiStandbyCIPv6PfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 66),
    _SbiStandbyCIPv6PfxLen_Type()
)
sbiStandbyCIPv6PfxLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiStandbyCIPv6PfxLen.setStatus("current")
_SbiStandbyDIpAddr_Type = IpAddress
_SbiStandbyDIpAddr_Object = MibScalar
sbiStandbyDIpAddr = _SbiStandbyDIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 67),
    _SbiStandbyDIpAddr_Type()
)
sbiStandbyDIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiStandbyDIpAddr.setStatus("current")


class _SbiStandbyDIpMask_Type(IpAddressPrefixLength):
    """Custom type sbiStandbyDIpMask based on IpAddressPrefixLength"""
    defaultValue = 0


_SbiStandbyDIpMask_Type.__name__ = "IpAddressPrefixLength"
_SbiStandbyDIpMask_Object = MibScalar
sbiStandbyDIpMask = _SbiStandbyDIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 68),
    _SbiStandbyDIpMask_Type()
)
sbiStandbyDIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiStandbyDIpMask.setStatus("current")


class _SbiStandbyDIPv6Addr_Type(InetAddressIPv6):
    """Custom type sbiStandbyDIPv6Addr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_SbiStandbyDIPv6Addr_Type.__name__ = "InetAddressIPv6"
_SbiStandbyDIPv6Addr_Object = MibScalar
sbiStandbyDIPv6Addr = _SbiStandbyDIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 69),
    _SbiStandbyDIPv6Addr_Type()
)
sbiStandbyDIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiStandbyDIPv6Addr.setStatus("current")


class _SbiStandbyDIPv6PfxLen_Type(InetAddressPrefixLength):
    """Custom type sbiStandbyDIPv6PfxLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SbiStandbyDIPv6PfxLen_Type.__name__ = "InetAddressPrefixLength"
_SbiStandbyDIPv6PfxLen_Object = MibScalar
sbiStandbyDIPv6PfxLen = _SbiStandbyDIPv6PfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 70),
    _SbiStandbyDIPv6PfxLen_Type()
)
sbiStandbyDIPv6PfxLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiStandbyDIPv6PfxLen.setStatus("current")


class _SbiMgmtIfIpMtu_Type(Unsigned32):
    """Custom type sbiMgmtIfIpMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9786),
    )


_SbiMgmtIfIpMtu_Type.__name__ = "Unsigned32"
_SbiMgmtIfIpMtu_Object = MibScalar
sbiMgmtIfIpMtu = _SbiMgmtIfIpMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 11, 71),
    _SbiMgmtIfIpMtu_Type()
)
sbiMgmtIfIpMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiMgmtIfIpMtu.setStatus("current")
if mibBuilder.loadTexts:
    sbiMgmtIfIpMtu.setUnits("bytes")
_SysPersistenceInfo_ObjectIdentity = ObjectIdentity
sysPersistenceInfo = _SysPersistenceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12)
)
_SysPersistenceDhcpL2Info_ObjectIdentity = ObjectIdentity
sysPersistenceDhcpL2Info = _SysPersistenceDhcpL2Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 1)
)


class _SpiDhcpL2PersistenceFileLocation_Type(Unsigned32):
    """Custom type spiDhcpL2PersistenceFileLocation based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SpiDhcpL2PersistenceFileLocation_Type.__name__ = "Unsigned32"
_SpiDhcpL2PersistenceFileLocation_Object = MibScalar
spiDhcpL2PersistenceFileLocation = _SpiDhcpL2PersistenceFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 1, 1),
    _SpiDhcpL2PersistenceFileLocation_Type()
)
spiDhcpL2PersistenceFileLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiDhcpL2PersistenceFileLocation.setStatus("obsolete")


class _SpiDhcpL2PersistenceDescription_Type(TItemDescription):
    """Custom type spiDhcpL2PersistenceDescription based on TItemDescription"""
    defaultValue = OctetString("")


_SpiDhcpL2PersistenceDescription_Type.__name__ = "TItemDescription"
_SpiDhcpL2PersistenceDescription_Object = MibScalar
spiDhcpL2PersistenceDescription = _SpiDhcpL2PersistenceDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 1, 2),
    _SpiDhcpL2PersistenceDescription_Type()
)
spiDhcpL2PersistenceDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiDhcpL2PersistenceDescription.setStatus("obsolete")
_SysPersistenceDhcpL3Info_ObjectIdentity = ObjectIdentity
sysPersistenceDhcpL3Info = _SysPersistenceDhcpL3Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 2)
)


class _SpiDhcpL3PersistenceFileLocation_Type(Unsigned32):
    """Custom type spiDhcpL3PersistenceFileLocation based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SpiDhcpL3PersistenceFileLocation_Type.__name__ = "Unsigned32"
_SpiDhcpL3PersistenceFileLocation_Object = MibScalar
spiDhcpL3PersistenceFileLocation = _SpiDhcpL3PersistenceFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 2, 1),
    _SpiDhcpL3PersistenceFileLocation_Type()
)
spiDhcpL3PersistenceFileLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiDhcpL3PersistenceFileLocation.setStatus("obsolete")


class _SpiDhcpL3PersistenceDescription_Type(TItemDescription):
    """Custom type spiDhcpL3PersistenceDescription based on TItemDescription"""
    defaultValue = OctetString("")


_SpiDhcpL3PersistenceDescription_Type.__name__ = "TItemDescription"
_SpiDhcpL3PersistenceDescription_Object = MibScalar
spiDhcpL3PersistenceDescription = _SpiDhcpL3PersistenceDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 2, 2),
    _SpiDhcpL3PersistenceDescription_Type()
)
spiDhcpL3PersistenceDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiDhcpL3PersistenceDescription.setStatus("obsolete")
_SysPersistenceSubMgmtInfo_ObjectIdentity = ObjectIdentity
sysPersistenceSubMgmtInfo = _SysPersistenceSubMgmtInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 3)
)


class _SpiSubMgmtPersistenceFileLocation_Type(Unsigned32):
    """Custom type spiSubMgmtPersistenceFileLocation based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SpiSubMgmtPersistenceFileLocation_Type.__name__ = "Unsigned32"
_SpiSubMgmtPersistenceFileLocation_Object = MibScalar
spiSubMgmtPersistenceFileLocation = _SpiSubMgmtPersistenceFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 3, 1),
    _SpiSubMgmtPersistenceFileLocation_Type()
)
spiSubMgmtPersistenceFileLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiSubMgmtPersistenceFileLocation.setStatus("current")


class _SpiSubMgmtPersistenceDescription_Type(TItemDescription):
    """Custom type spiSubMgmtPersistenceDescription based on TItemDescription"""
    defaultValue = OctetString("")


_SpiSubMgmtPersistenceDescription_Type.__name__ = "TItemDescription"
_SpiSubMgmtPersistenceDescription_Object = MibScalar
spiSubMgmtPersistenceDescription = _SpiSubMgmtPersistenceDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 3, 2),
    _SpiSubMgmtPersistenceDescription_Type()
)
spiSubMgmtPersistenceDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiSubMgmtPersistenceDescription.setStatus("current")
_SysPersistenceDhcpSrvInfo_ObjectIdentity = ObjectIdentity
sysPersistenceDhcpSrvInfo = _SysPersistenceDhcpSrvInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 4)
)


class _SpiDhcpSrvPersistenceFileLoc_Type(Unsigned32):
    """Custom type spiDhcpSrvPersistenceFileLoc based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SpiDhcpSrvPersistenceFileLoc_Type.__name__ = "Unsigned32"
_SpiDhcpSrvPersistenceFileLoc_Object = MibScalar
spiDhcpSrvPersistenceFileLoc = _SpiDhcpSrvPersistenceFileLoc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 4, 1),
    _SpiDhcpSrvPersistenceFileLoc_Type()
)
spiDhcpSrvPersistenceFileLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiDhcpSrvPersistenceFileLoc.setStatus("current")


class _SpiDhcpSrvPersistenceDescr_Type(TItemDescription):
    """Custom type spiDhcpSrvPersistenceDescr based on TItemDescription"""
    defaultValue = OctetString("")


_SpiDhcpSrvPersistenceDescr_Type.__name__ = "TItemDescription"
_SpiDhcpSrvPersistenceDescr_Object = MibScalar
spiDhcpSrvPersistenceDescr = _SpiDhcpSrvPersistenceDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 4, 2),
    _SpiDhcpSrvPersistenceDescr_Type()
)
spiDhcpSrvPersistenceDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiDhcpSrvPersistenceDescr.setStatus("current")
_SysPersistenceNatInfo_ObjectIdentity = ObjectIdentity
sysPersistenceNatInfo = _SysPersistenceNatInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 5)
)


class _SpiNatFwdPersistenceFileLoc_Type(Unsigned32):
    """Custom type spiNatFwdPersistenceFileLoc based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SpiNatFwdPersistenceFileLoc_Type.__name__ = "Unsigned32"
_SpiNatFwdPersistenceFileLoc_Object = MibScalar
spiNatFwdPersistenceFileLoc = _SpiNatFwdPersistenceFileLoc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 5, 1),
    _SpiNatFwdPersistenceFileLoc_Type()
)
spiNatFwdPersistenceFileLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiNatFwdPersistenceFileLoc.setStatus("current")


class _SpiNatFwdPersistenceDescr_Type(TItemDescription):
    """Custom type spiNatFwdPersistenceDescr based on TItemDescription"""
    defaultValue = OctetString("")


_SpiNatFwdPersistenceDescr_Type.__name__ = "TItemDescription"
_SpiNatFwdPersistenceDescr_Object = MibScalar
spiNatFwdPersistenceDescr = _SpiNatFwdPersistenceDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 5, 2),
    _SpiNatFwdPersistenceDescr_Type()
)
spiNatFwdPersistenceDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiNatFwdPersistenceDescr.setStatus("current")
_SysPersistenceAAInfo_ObjectIdentity = ObjectIdentity
sysPersistenceAAInfo = _SysPersistenceAAInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 6)
)


class _SpiAAPersistenceFileLoc_Type(Unsigned32):
    """Custom type spiAAPersistenceFileLoc based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SpiAAPersistenceFileLoc_Type.__name__ = "Unsigned32"
_SpiAAPersistenceFileLoc_Object = MibScalar
spiAAPersistenceFileLoc = _SpiAAPersistenceFileLoc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 6, 1),
    _SpiAAPersistenceFileLoc_Type()
)
spiAAPersistenceFileLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiAAPersistenceFileLoc.setStatus("current")


class _SpiAAPersistenceDescr_Type(TItemDescription):
    """Custom type spiAAPersistenceDescr based on TItemDescription"""
    defaultValue = OctetString("")


_SpiAAPersistenceDescr_Type.__name__ = "TItemDescription"
_SpiAAPersistenceDescr_Object = MibScalar
spiAAPersistenceDescr = _SpiAAPersistenceDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 6, 2),
    _SpiAAPersistenceDescr_Type()
)
spiAAPersistenceDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiAAPersistenceDescr.setStatus("current")
_SysPersistenceAncpInfo_ObjectIdentity = ObjectIdentity
sysPersistenceAncpInfo = _SysPersistenceAncpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 7)
)


class _SpiAncpPersistenceFileLoc_Type(Unsigned32):
    """Custom type spiAncpPersistenceFileLoc based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SpiAncpPersistenceFileLoc_Type.__name__ = "Unsigned32"
_SpiAncpPersistenceFileLoc_Object = MibScalar
spiAncpPersistenceFileLoc = _SpiAncpPersistenceFileLoc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 7, 1),
    _SpiAncpPersistenceFileLoc_Type()
)
spiAncpPersistenceFileLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiAncpPersistenceFileLoc.setStatus("current")


class _SpiAncpPersistenceDescr_Type(TItemDescription):
    """Custom type spiAncpPersistenceDescr based on TItemDescription"""
    defaultValue = OctetString("")


_SpiAncpPersistenceDescr_Type.__name__ = "TItemDescription"
_SpiAncpPersistenceDescr_Object = MibScalar
spiAncpPersistenceDescr = _SpiAncpPersistenceDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 7, 2),
    _SpiAncpPersistenceDescr_Type()
)
spiAncpPersistenceDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiAncpPersistenceDescr.setStatus("current")
_SysPersistencePythonInfo_ObjectIdentity = ObjectIdentity
sysPersistencePythonInfo = _SysPersistencePythonInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 8)
)


class _SpiPythonPersistenceFileLoc_Type(Unsigned32):
    """Custom type spiPythonPersistenceFileLoc based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SpiPythonPersistenceFileLoc_Type.__name__ = "Unsigned32"
_SpiPythonPersistenceFileLoc_Object = MibScalar
spiPythonPersistenceFileLoc = _SpiPythonPersistenceFileLoc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 8, 1),
    _SpiPythonPersistenceFileLoc_Type()
)
spiPythonPersistenceFileLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiPythonPersistenceFileLoc.setStatus("current")


class _SpiPythonPersistenceDescr_Type(TItemDescription):
    """Custom type spiPythonPersistenceDescr based on TItemDescription"""
    defaultValue = OctetString("")


_SpiPythonPersistenceDescr_Type.__name__ = "TItemDescription"
_SpiPythonPersistenceDescr_Object = MibScalar
spiPythonPersistenceDescr = _SpiPythonPersistenceDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 8, 2),
    _SpiPythonPersistenceDescr_Type()
)
spiPythonPersistenceDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiPythonPersistenceDescr.setStatus("current")


class _TmnxDhcpLeaseTimeModeThreshold_Type(Unsigned32):
    """Custom type tmnxDhcpLeaseTimeModeThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 631152000),
    )


_TmnxDhcpLeaseTimeModeThreshold_Type.__name__ = "Unsigned32"
_TmnxDhcpLeaseTimeModeThreshold_Object = MibScalar
tmnxDhcpLeaseTimeModeThreshold = _TmnxDhcpLeaseTimeModeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 12, 20),
    _TmnxDhcpLeaseTimeModeThreshold_Type()
)
tmnxDhcpLeaseTimeModeThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpLeaseTimeModeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDhcpLeaseTimeModeThreshold.setUnits("seconds")
_SysLiInfo_ObjectIdentity = ObjectIdentity
sysLiInfo = _SysLiInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 13)
)


class _SliConfigStatus_Type(Integer32):
    """Custom type sliConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRun", 0),
          ("success", 1),
          ("fail", 2))
    )


_SliConfigStatus_Type.__name__ = "Integer32"
_SliConfigStatus_Object = MibScalar
sliConfigStatus = _SliConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 13, 1),
    _SliConfigStatus_Type()
)
sliConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliConfigStatus.setStatus("current")


class _SliSaveConfig_Type(TmnxActionType):
    """Custom type sliSaveConfig based on TmnxActionType"""
    defaultValue = 2


_SliSaveConfig_Type.__name__ = "TmnxActionType"
_SliSaveConfig_Object = MibScalar
sliSaveConfig = _SliSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 13, 2),
    _SliSaveConfig_Type()
)
sliSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sliSaveConfig.setStatus("current")


class _SliSaveConfigResult_Type(Integer32):
    """Custom type sliSaveConfigResult based on Integer32"""
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
        *(("none", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4))
    )


_SliSaveConfigResult_Type.__name__ = "Integer32"
_SliSaveConfigResult_Object = MibScalar
sliSaveConfigResult = _SliSaveConfigResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 13, 3),
    _SliSaveConfigResult_Type()
)
sliSaveConfigResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliSaveConfigResult.setStatus("current")
_SliConfigLastModified_Type = DateAndTime
_SliConfigLastModified_Object = MibScalar
sliConfigLastModified = _SliConfigLastModified_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 13, 4),
    _SliConfigLastModified_Type()
)
sliConfigLastModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliConfigLastModified.setStatus("current")
_SliConfigLastSaved_Type = DateAndTime
_SliConfigLastSaved_Object = MibScalar
sliConfigLastSaved = _SliConfigLastSaved_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 13, 5),
    _SliConfigLastSaved_Type()
)
sliConfigLastSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliConfigLastSaved.setStatus("current")


class _SliFilterLock_Type(Integer32):
    """Custom type sliFilterLock based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("unlockedForLiUsers", 1),
          ("unlockedForAll", 2))
    )


_SliFilterLock_Type.__name__ = "Integer32"
_SliFilterLock_Object = MibScalar
sliFilterLock = _SliFilterLock_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 13, 6),
    _SliFilterLock_Type()
)
sliFilterLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sliFilterLock.setStatus("current")
_SysDNSInfo_ObjectIdentity = ObjectIdentity
sysDNSInfo = _SysDNSInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 14)
)
_SysDNSInfoLastChanged_Type = TimeStamp
_SysDNSInfoLastChanged_Object = MibScalar
sysDNSInfoLastChanged = _SysDNSInfoLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 14, 1),
    _SysDNSInfoLastChanged_Type()
)
sysDNSInfoLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDNSInfoLastChanged.setStatus("current")


class _SysDNSAddressResolvePref_Type(Integer32):
    """Custom type sysDNSAddressResolvePref based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4Only", 1),
          ("ipv6First", 2))
    )


_SysDNSAddressResolvePref_Type.__name__ = "Integer32"
_SysDNSAddressResolvePref_Object = MibScalar
sysDNSAddressResolvePref = _SysDNSAddressResolvePref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 14, 2),
    _SysDNSAddressResolvePref_Type()
)
sysDNSAddressResolvePref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDNSAddressResolvePref.setStatus("current")


class _SysDNSSecAdValidation_Type(TruthValue):
    """Custom type sysDNSSecAdValidation based on TruthValue"""
    defaultValue = 2


_SysDNSSecAdValidation_Type.__name__ = "TruthValue"
_SysDNSSecAdValidation_Object = MibScalar
sysDNSSecAdValidation = _SysDNSSecAdValidation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 14, 3),
    _SysDNSSecAdValidation_Type()
)
sysDNSSecAdValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDNSSecAdValidation.setStatus("current")


class _SysDNSSecRespCtrl_Type(Integer32):
    """Custom type sysDNSSecRespCtrl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fallThrough", 1),
          ("drop", 2))
    )


_SysDNSSecRespCtrl_Type.__name__ = "Integer32"
_SysDNSSecRespCtrl_Object = MibScalar
sysDNSSecRespCtrl = _SysDNSSecRespCtrl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 14, 4),
    _SysDNSSecRespCtrl_Type()
)
sysDNSSecRespCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDNSSecRespCtrl.setStatus("current")
_SysIcmpVSInfo_ObjectIdentity = ObjectIdentity
sysIcmpVSInfo = _SysIcmpVSInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 15)
)


class _SysIcmpVSEnhancement_Type(TmnxEnabledDisabled):
    """Custom type sysIcmpVSEnhancement based on TmnxEnabledDisabled"""
    defaultValue = 2


_SysIcmpVSEnhancement_Type.__name__ = "TmnxEnabledDisabled"
_SysIcmpVSEnhancement_Object = MibScalar
sysIcmpVSEnhancement = _SysIcmpVSEnhancement_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 15, 1),
    _SysIcmpVSEnhancement_Type()
)
sysIcmpVSEnhancement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIcmpVSEnhancement.setStatus("current")
_SysEthInfo_ObjectIdentity = ObjectIdentity
sysEthInfo = _SysEthInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 16)
)


class _SysNewQinqUntaggedSap_Type(TruthValue):
    """Custom type sysNewQinqUntaggedSap based on TruthValue"""
    defaultValue = 2


_SysNewQinqUntaggedSap_Type.__name__ = "TruthValue"
_SysNewQinqUntaggedSap_Object = MibScalar
sysNewQinqUntaggedSap = _SysNewQinqUntaggedSap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 16, 1),
    _SysNewQinqUntaggedSap_Type()
)
sysNewQinqUntaggedSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNewQinqUntaggedSap.setStatus("current")
_TmnxSysRollbackInfo_ObjectIdentity = ObjectIdentity
tmnxSysRollbackInfo = _TmnxSysRollbackInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17)
)


class _TmnxSysRollbackIndex_Type(Unsigned32):
    """Custom type tmnxSysRollbackIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_TmnxSysRollbackIndex_Type.__name__ = "Unsigned32"
_TmnxSysRollbackIndex_Object = MibScalar
tmnxSysRollbackIndex = _TmnxSysRollbackIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 1),
    _TmnxSysRollbackIndex_Type()
)
tmnxSysRollbackIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackIndex.setStatus("current")


class _TmnxSysRollbackStart_Type(TmnxActionType):
    """Custom type tmnxSysRollbackStart based on TmnxActionType"""
    defaultValue = 2


_TmnxSysRollbackStart_Type.__name__ = "TmnxActionType"
_TmnxSysRollbackStart_Object = MibScalar
tmnxSysRollbackStart = _TmnxSysRollbackStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 2),
    _TmnxSysRollbackStart_Type()
)
tmnxSysRollbackStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackStart.setStatus("current")


class _TmnxSysRollbackResult_Type(Integer32):
    """Custom type tmnxSysRollbackResult based on Integer32"""
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
        *(("none", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4),
          ("interrupted", 5))
    )


_TmnxSysRollbackResult_Type.__name__ = "Integer32"
_TmnxSysRollbackResult_Object = MibScalar
tmnxSysRollbackResult = _TmnxSysRollbackResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 3),
    _TmnxSysRollbackResult_Type()
)
tmnxSysRollbackResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackResult.setStatus("current")


class _TmnxSysRollbackSave_Type(TmnxActionType):
    """Custom type tmnxSysRollbackSave based on TmnxActionType"""
    defaultValue = 2


_TmnxSysRollbackSave_Type.__name__ = "TmnxActionType"
_TmnxSysRollbackSave_Object = MibScalar
tmnxSysRollbackSave = _TmnxSysRollbackSave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 4),
    _TmnxSysRollbackSave_Type()
)
tmnxSysRollbackSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackSave.setStatus("current")


class _TmnxSysRollbackSaveResult_Type(Integer32):
    """Custom type tmnxSysRollbackSaveResult based on Integer32"""
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
        *(("none", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4))
    )


_TmnxSysRollbackSaveResult_Type.__name__ = "Integer32"
_TmnxSysRollbackSaveResult_Object = MibScalar
tmnxSysRollbackSaveResult = _TmnxSysRollbackSaveResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 5),
    _TmnxSysRollbackSaveResult_Type()
)
tmnxSysRollbackSaveResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackSaveResult.setStatus("current")


class _TmnxSysRollbackLocation_Type(TmnxDisplayStringURL):
    """Custom type tmnxSysRollbackLocation based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_TmnxSysRollbackLocation_Type.__name__ = "TmnxDisplayStringURL"
_TmnxSysRollbackLocation_Object = MibScalar
tmnxSysRollbackLocation = _TmnxSysRollbackLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 6),
    _TmnxSysRollbackLocation_Type()
)
tmnxSysRollbackLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackLocation.setStatus("current")


class _TmnxSysRollbackRevertIndex_Type(Unsigned32):
    """Custom type tmnxSysRollbackRevertIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_TmnxSysRollbackRevertIndex_Type.__name__ = "Unsigned32"
_TmnxSysRollbackRevertIndex_Object = MibScalar
tmnxSysRollbackRevertIndex = _TmnxSysRollbackRevertIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 7),
    _TmnxSysRollbackRevertIndex_Type()
)
tmnxSysRollbackRevertIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRevertIndex.setStatus("current")
_TmnxSysRollbackRevertEndTime_Type = DateAndTime
_TmnxSysRollbackRevertEndTime_Object = MibScalar
tmnxSysRollbackRevertEndTime = _TmnxSysRollbackRevertEndTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 8),
    _TmnxSysRollbackRevertEndTime_Type()
)
tmnxSysRollbackRevertEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRevertEndTime.setStatus("current")
_TmnxSysRollbackSavedTime_Type = DateAndTime
_TmnxSysRollbackSavedTime_Object = MibScalar
tmnxSysRollbackSavedTime = _TmnxSysRollbackSavedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 9),
    _TmnxSysRollbackSavedTime_Type()
)
tmnxSysRollbackSavedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackSavedTime.setStatus("current")
_TmnxSysRollbackRevertStartTime_Type = DateAndTime
_TmnxSysRollbackRevertStartTime_Object = MibScalar
tmnxSysRollbackRevertStartTime = _TmnxSysRollbackRevertStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 10),
    _TmnxSysRollbackRevertStartTime_Type()
)
tmnxSysRollbackRevertStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRevertStartTime.setStatus("current")


class _TmnxSysRollbackRevertUserName_Type(TNamedItemOrEmpty):
    """Custom type tmnxSysRollbackRevertUserName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxSysRollbackRevertUserName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxSysRollbackRevertUserName_Object = MibScalar
tmnxSysRollbackRevertUserName = _TmnxSysRollbackRevertUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 11),
    _TmnxSysRollbackRevertUserName_Type()
)
tmnxSysRollbackRevertUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRevertUserName.setStatus("current")


class _TmnxSysRollbackRevertFilename_Type(TmnxDisplayStringURL):
    """Custom type tmnxSysRollbackRevertFilename based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_TmnxSysRollbackRevertFilename_Type.__name__ = "TmnxDisplayStringURL"
_TmnxSysRollbackRevertFilename_Object = MibScalar
tmnxSysRollbackRevertFilename = _TmnxSysRollbackRevertFilename_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 12),
    _TmnxSysRollbackRevertFilename_Type()
)
tmnxSysRollbackRevertFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRevertFilename.setStatus("current")


class _TmnxSysRollbackSaveComment_Type(DisplayString):
    """Custom type tmnxSysRollbackSaveComment based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxSysRollbackSaveComment_Type.__name__ = "DisplayString"
_TmnxSysRollbackSaveComment_Object = MibScalar
tmnxSysRollbackSaveComment = _TmnxSysRollbackSaveComment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 13),
    _TmnxSysRollbackSaveComment_Type()
)
tmnxSysRollbackSaveComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackSaveComment.setStatus("current")


class _TmnxSysRollbackFileDelete_Type(TmnxActionType):
    """Custom type tmnxSysRollbackFileDelete based on TmnxActionType"""
    defaultValue = 2


_TmnxSysRollbackFileDelete_Type.__name__ = "TmnxActionType"
_TmnxSysRollbackFileDelete_Object = MibScalar
tmnxSysRollbackFileDelete = _TmnxSysRollbackFileDelete_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 14),
    _TmnxSysRollbackFileDelete_Type()
)
tmnxSysRollbackFileDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackFileDelete.setStatus("current")


class _TmnxSysRollbackFileDeleteResult_Type(Integer32):
    """Custom type tmnxSysRollbackFileDeleteResult based on Integer32"""
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
        *(("none", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4))
    )


_TmnxSysRollbackFileDeleteResult_Type.__name__ = "Integer32"
_TmnxSysRollbackFileDeleteResult_Object = MibScalar
tmnxSysRollbackFileDeleteResult = _TmnxSysRollbackFileDeleteResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 15),
    _TmnxSysRollbackFileDeleteResult_Type()
)
tmnxSysRollbackFileDeleteResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackFileDeleteResult.setStatus("current")


class _TmnxSysRollbackAbortRevert_Type(TmnxActionType):
    """Custom type tmnxSysRollbackAbortRevert based on TmnxActionType"""
    defaultValue = 2


_TmnxSysRollbackAbortRevert_Type.__name__ = "TmnxActionType"
_TmnxSysRollbackAbortRevert_Object = MibScalar
tmnxSysRollbackAbortRevert = _TmnxSysRollbackAbortRevert_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 16),
    _TmnxSysRollbackAbortRevert_Type()
)
tmnxSysRollbackAbortRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackAbortRevert.setStatus("current")


class _TmnxSysRollbackRescueLocation_Type(TmnxDisplayStringURL):
    """Custom type tmnxSysRollbackRescueLocation based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_TmnxSysRollbackRescueLocation_Type.__name__ = "TmnxDisplayStringURL"
_TmnxSysRollbackRescueLocation_Object = MibScalar
tmnxSysRollbackRescueLocation = _TmnxSysRollbackRescueLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 17),
    _TmnxSysRollbackRescueLocation_Type()
)
tmnxSysRollbackRescueLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueLocation.setStatus("current")


class _TmnxSysRollbackRescueRevert_Type(TmnxActionType):
    """Custom type tmnxSysRollbackRescueRevert based on TmnxActionType"""
    defaultValue = 2


_TmnxSysRollbackRescueRevert_Type.__name__ = "TmnxActionType"
_TmnxSysRollbackRescueRevert_Object = MibScalar
tmnxSysRollbackRescueRevert = _TmnxSysRollbackRescueRevert_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 18),
    _TmnxSysRollbackRescueRevert_Type()
)
tmnxSysRollbackRescueRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueRevert.setStatus("current")


class _TmnxSysRollbackRescueSave_Type(TmnxActionType):
    """Custom type tmnxSysRollbackRescueSave based on TmnxActionType"""
    defaultValue = 2


_TmnxSysRollbackRescueSave_Type.__name__ = "TmnxActionType"
_TmnxSysRollbackRescueSave_Object = MibScalar
tmnxSysRollbackRescueSave = _TmnxSysRollbackRescueSave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 19),
    _TmnxSysRollbackRescueSave_Type()
)
tmnxSysRollbackRescueSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueSave.setStatus("current")


class _TmnxSysRollbackRescueDelete_Type(TmnxActionType):
    """Custom type tmnxSysRollbackRescueDelete based on TmnxActionType"""
    defaultValue = 2


_TmnxSysRollbackRescueDelete_Type.__name__ = "TmnxActionType"
_TmnxSysRollbackRescueDelete_Object = MibScalar
tmnxSysRollbackRescueDelete = _TmnxSysRollbackRescueDelete_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 20),
    _TmnxSysRollbackRescueDelete_Type()
)
tmnxSysRollbackRescueDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueDelete.setStatus("current")


class _TmnxSysRollbackRescueSaveRes_Type(Integer32):
    """Custom type tmnxSysRollbackRescueSaveRes based on Integer32"""
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
        *(("none", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4))
    )


_TmnxSysRollbackRescueSaveRes_Type.__name__ = "Integer32"
_TmnxSysRollbackRescueSaveRes_Object = MibScalar
tmnxSysRollbackRescueSaveRes = _TmnxSysRollbackRescueSaveRes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 21),
    _TmnxSysRollbackRescueSaveRes_Type()
)
tmnxSysRollbackRescueSaveRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueSaveRes.setStatus("current")


class _TmnxSysRollbackRescueRevertRes_Type(Integer32):
    """Custom type tmnxSysRollbackRescueRevertRes based on Integer32"""
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
        *(("none", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4),
          ("interrupted", 5))
    )


_TmnxSysRollbackRescueRevertRes_Type.__name__ = "Integer32"
_TmnxSysRollbackRescueRevertRes_Object = MibScalar
tmnxSysRollbackRescueRevertRes = _TmnxSysRollbackRescueRevertRes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 22),
    _TmnxSysRollbackRescueRevertRes_Type()
)
tmnxSysRollbackRescueRevertRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueRevertRes.setStatus("current")


class _TmnxSysRollbackRescueDeleteRes_Type(Integer32):
    """Custom type tmnxSysRollbackRescueDeleteRes based on Integer32"""
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
        *(("none", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4))
    )


_TmnxSysRollbackRescueDeleteRes_Type.__name__ = "Integer32"
_TmnxSysRollbackRescueDeleteRes_Object = MibScalar
tmnxSysRollbackRescueDeleteRes = _TmnxSysRollbackRescueDeleteRes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 23),
    _TmnxSysRollbackRescueDeleteRes_Type()
)
tmnxSysRollbackRescueDeleteRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueDeleteRes.setStatus("current")
_TmnxSysRollbackRescueSavedTime_Type = DateAndTime
_TmnxSysRollbackRescueSavedTime_Object = MibScalar
tmnxSysRollbackRescueSavedTime = _TmnxSysRollbackRescueSavedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 24),
    _TmnxSysRollbackRescueSavedTime_Type()
)
tmnxSysRollbackRescueSavedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueSavedTime.setStatus("current")
_TmnxSysRollbackRescueRevStTime_Type = DateAndTime
_TmnxSysRollbackRescueRevStTime_Object = MibScalar
tmnxSysRollbackRescueRevStTime = _TmnxSysRollbackRescueRevStTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 25),
    _TmnxSysRollbackRescueRevStTime_Type()
)
tmnxSysRollbackRescueRevStTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueRevStTime.setStatus("current")
_TmnxSysRollbackRescueRevEdTime_Type = DateAndTime
_TmnxSysRollbackRescueRevEdTime_Object = MibScalar
tmnxSysRollbackRescueRevEdTime = _TmnxSysRollbackRescueRevEdTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 26),
    _TmnxSysRollbackRescueRevEdTime_Type()
)
tmnxSysRollbackRescueRevEdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueRevEdTime.setStatus("current")


class _TmnxSysRollbackRescueRevUser_Type(TNamedItemOrEmpty):
    """Custom type tmnxSysRollbackRescueRevUser based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxSysRollbackRescueRevUser_Type.__name__ = "TNamedItemOrEmpty"
_TmnxSysRollbackRescueRevUser_Object = MibScalar
tmnxSysRollbackRescueRevUser = _TmnxSysRollbackRescueRevUser_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 27),
    _TmnxSysRollbackRescueRevUser_Type()
)
tmnxSysRollbackRescueRevUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueRevUser.setStatus("current")


class _TmnxSysRollbackRescueSaveComment_Type(DisplayString):
    """Custom type tmnxSysRollbackRescueSaveComment based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxSysRollbackRescueSaveComment_Type.__name__ = "DisplayString"
_TmnxSysRollbackRescueSaveComment_Object = MibScalar
tmnxSysRollbackRescueSaveComment = _TmnxSysRollbackRescueSaveComment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 28),
    _TmnxSysRollbackRescueSaveComment_Type()
)
tmnxSysRollbackRescueSaveComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueSaveComment.setStatus("current")


class _TmnxSysRollbackRescueAbortRevert_Type(TmnxActionType):
    """Custom type tmnxSysRollbackRescueAbortRevert based on TmnxActionType"""
    defaultValue = 2


_TmnxSysRollbackRescueAbortRevert_Type.__name__ = "TmnxActionType"
_TmnxSysRollbackRescueAbortRevert_Object = MibScalar
tmnxSysRollbackRescueAbortRevert = _TmnxSysRollbackRescueAbortRevert_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 29),
    _TmnxSysRollbackRescueAbortRevert_Type()
)
tmnxSysRollbackRescueAbortRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueAbortRevert.setStatus("current")


class _TmnxSysRollbackRescueFileExists_Type(TruthValue):
    """Custom type tmnxSysRollbackRescueFileExists based on TruthValue"""
    defaultValue = 2


_TmnxSysRollbackRescueFileExists_Type.__name__ = "TruthValue"
_TmnxSysRollbackRescueFileExists_Object = MibScalar
tmnxSysRollbackRescueFileExists = _TmnxSysRollbackRescueFileExists_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 30),
    _TmnxSysRollbackRescueFileExists_Type()
)
tmnxSysRollbackRescueFileExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueFileExists.setStatus("current")


class _TmnxSysRollbackMaxLocalFiles_Type(Unsigned32):
    """Custom type tmnxSysRollbackMaxLocalFiles based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_TmnxSysRollbackMaxLocalFiles_Type.__name__ = "Unsigned32"
_TmnxSysRollbackMaxLocalFiles_Object = MibScalar
tmnxSysRollbackMaxLocalFiles = _TmnxSysRollbackMaxLocalFiles_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 31),
    _TmnxSysRollbackMaxLocalFiles_Type()
)
tmnxSysRollbackMaxLocalFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackMaxLocalFiles.setStatus("current")


class _TmnxSysRollbackMaxRemoteFiles_Type(Unsigned32):
    """Custom type tmnxSysRollbackMaxRemoteFiles based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_TmnxSysRollbackMaxRemoteFiles_Type.__name__ = "Unsigned32"
_TmnxSysRollbackMaxRemoteFiles_Object = MibScalar
tmnxSysRollbackMaxRemoteFiles = _TmnxSysRollbackMaxRemoteFiles_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 17, 32),
    _TmnxSysRollbackMaxRemoteFiles_Type()
)
tmnxSysRollbackMaxRemoteFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRollbackMaxRemoteFiles.setStatus("current")
_TmnxSysRollbackTableLastChanged_Type = TimeStamp
_TmnxSysRollbackTableLastChanged_Object = MibScalar
tmnxSysRollbackTableLastChanged = _TmnxSysRollbackTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 18),
    _TmnxSysRollbackTableLastChanged_Type()
)
tmnxSysRollbackTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackTableLastChanged.setStatus("current")
_TmnxSysRollbackFileTable_Object = MibTable
tmnxSysRollbackFileTable = _TmnxSysRollbackFileTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 19)
)
if mibBuilder.loadTexts:
    tmnxSysRollbackFileTable.setStatus("current")
_TmnxSysRollbackFileEntry_Object = MibTableRow
tmnxSysRollbackFileEntry = _TmnxSysRollbackFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 19, 1)
)
tmnxSysRollbackFileEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileIndex"),
)
if mibBuilder.loadTexts:
    tmnxSysRollbackFileEntry.setStatus("current")


class _TmnxSysRollbackFileIndex_Type(Unsigned32):
    """Custom type tmnxSysRollbackFileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_TmnxSysRollbackFileIndex_Type.__name__ = "Unsigned32"
_TmnxSysRollbackFileIndex_Object = MibTableColumn
tmnxSysRollbackFileIndex = _TmnxSysRollbackFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 19, 1, 1),
    _TmnxSysRollbackFileIndex_Type()
)
tmnxSysRollbackFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysRollbackFileIndex.setStatus("current")
_TmnxSysRollbackFileCreationTime_Type = DateAndTime
_TmnxSysRollbackFileCreationTime_Object = MibTableColumn
tmnxSysRollbackFileCreationTime = _TmnxSysRollbackFileCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 19, 1, 2),
    _TmnxSysRollbackFileCreationTime_Type()
)
tmnxSysRollbackFileCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackFileCreationTime.setStatus("current")


class _TmnxSysRollbackFileComment_Type(DisplayString):
    """Custom type tmnxSysRollbackFileComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxSysRollbackFileComment_Type.__name__ = "DisplayString"
_TmnxSysRollbackFileComment_Object = MibTableColumn
tmnxSysRollbackFileComment = _TmnxSysRollbackFileComment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 19, 1, 3),
    _TmnxSysRollbackFileComment_Type()
)
tmnxSysRollbackFileComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackFileComment.setStatus("current")
_TmnxSysRollbackFileUserName_Type = TNamedItemOrEmpty
_TmnxSysRollbackFileUserName_Object = MibTableColumn
tmnxSysRollbackFileUserName = _TmnxSysRollbackFileUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 19, 1, 4),
    _TmnxSysRollbackFileUserName_Type()
)
tmnxSysRollbackFileUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackFileUserName.setStatus("current")


class _TmnxSysRollbackFileVersion_Type(DisplayString):
    """Custom type tmnxSysRollbackFileVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxSysRollbackFileVersion_Type.__name__ = "DisplayString"
_TmnxSysRollbackFileVersion_Object = MibTableColumn
tmnxSysRollbackFileVersion = _TmnxSysRollbackFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 19, 1, 5),
    _TmnxSysRollbackFileVersion_Type()
)
tmnxSysRollbackFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRollbackFileVersion.setStatus("current")
_SysBootedBofInfo_ObjectIdentity = ObjectIdentity
sysBootedBofInfo = _SysBootedBofInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 20)
)
_SbbiLiSeparate_Type = TruthValue
_SbbiLiSeparate_Object = MibScalar
sbbiLiSeparate = _SbbiLiSeparate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 20, 1),
    _SbbiLiSeparate_Type()
)
sbbiLiSeparate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbbiLiSeparate.setStatus("current")
_SbbiLiLocalSave_Type = TruthValue
_SbbiLiLocalSave_Object = MibScalar
sbbiLiLocalSave = _SbbiLiLocalSave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 20, 2),
    _SbbiLiLocalSave_Type()
)
sbbiLiLocalSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbbiLiLocalSave.setStatus("current")
_SbbiEncryptConfig_Type = TruthValue
_SbbiEncryptConfig_Object = MibScalar
sbbiEncryptConfig = _SbbiEncryptConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 20, 3),
    _SbbiEncryptConfig_Type()
)
sbbiEncryptConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbbiEncryptConfig.setStatus("current")
_SysMGMCSwitchOverInfo_ObjectIdentity = ObjectIdentity
sysMGMCSwitchOverInfo = _SysMGMCSwitchOverInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 21)
)
_TmnxSysCandidateCfgInfo_ObjectIdentity = ObjectIdentity
tmnxSysCandidateCfgInfo = _TmnxSysCandidateCfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 22)
)


class _TmnxSysCandidateCfgState_Type(Integer32):
    """Custom type tmnxSysCandidateCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unmodified", 0),
          ("modified", 1),
          ("unconfirmed", 2))
    )


_TmnxSysCandidateCfgState_Type.__name__ = "Integer32"
_TmnxSysCandidateCfgState_Object = MibScalar
tmnxSysCandidateCfgState = _TmnxSysCandidateCfgState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 22, 1),
    _TmnxSysCandidateCfgState_Type()
)
tmnxSysCandidateCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCandidateCfgState.setStatus("current")
_TmnxSysCandidateCfgEditors_Type = Integer32
_TmnxSysCandidateCfgEditors_Object = MibScalar
tmnxSysCandidateCfgEditors = _TmnxSysCandidateCfgEditors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 22, 2),
    _TmnxSysCandidateCfgEditors_Type()
)
tmnxSysCandidateCfgEditors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCandidateCfgEditors.setStatus("current")


class _TmnxSysCandidateCfgCommitState_Type(Integer32):
    """Custom type tmnxSysCandidateCfgCommitState based on Integer32"""
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
        *(("none", 0),
          ("in-progress", 1),
          ("success", 2),
          ("revert-pending", 3),
          ("failed", 4),
          ("revert-in-progress", 5),
          ("reverted", 6),
          ("revert-failed", 7))
    )


_TmnxSysCandidateCfgCommitState_Type.__name__ = "Integer32"
_TmnxSysCandidateCfgCommitState_Object = MibScalar
tmnxSysCandidateCfgCommitState = _TmnxSysCandidateCfgCommitState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 22, 3),
    _TmnxSysCandidateCfgCommitState_Type()
)
tmnxSysCandidateCfgCommitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCandidateCfgCommitState.setStatus("current")
_TmnxSysCandidateCfgCommitTime_Type = DateAndTime
_TmnxSysCandidateCfgCommitTime_Object = MibScalar
tmnxSysCandidateCfgCommitTime = _TmnxSysCandidateCfgCommitTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 22, 4),
    _TmnxSysCandidateCfgCommitTime_Type()
)
tmnxSysCandidateCfgCommitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCandidateCfgCommitTime.setStatus("current")
_TmnxSysCandidateCfgRevertTime_Type = DateAndTime
_TmnxSysCandidateCfgRevertTime_Object = MibScalar
tmnxSysCandidateCfgRevertTime = _TmnxSysCandidateCfgRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 22, 5),
    _TmnxSysCandidateCfgRevertTime_Type()
)
tmnxSysCandidateCfgRevertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCandidateCfgRevertTime.setStatus("current")
_TmnxSysCandidateCfgChckptCreated_Type = TruthValue
_TmnxSysCandidateCfgChckptCreated_Object = MibScalar
tmnxSysCandidateCfgChckptCreated = _TmnxSysCandidateCfgChckptCreated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 22, 6),
    _TmnxSysCandidateCfgChckptCreated_Type()
)
tmnxSysCandidateCfgChckptCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCandidateCfgChckptCreated.setStatus("current")
_TmnxSysCandidateCfgUser_Type = TNamedItemOrEmpty
_TmnxSysCandidateCfgUser_Object = MibScalar
tmnxSysCandidateCfgUser = _TmnxSysCandidateCfgUser_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 22, 7),
    _TmnxSysCandidateCfgUser_Type()
)
tmnxSysCandidateCfgUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCandidateCfgUser.setStatus("current")
_TmnxSysCandidateCfgExclusiveUsr_Type = TNamedItemOrEmpty
_TmnxSysCandidateCfgExclusiveUsr_Object = MibScalar
tmnxSysCandidateCfgExclusiveUsr = _TmnxSysCandidateCfgExclusiveUsr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 22, 8),
    _TmnxSysCandidateCfgExclusiveUsr_Type()
)
tmnxSysCandidateCfgExclusiveUsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCandidateCfgExclusiveUsr.setStatus("current")
_TmnxSysNetconfInfo_ObjectIdentity = ObjectIdentity
tmnxSysNetconfInfo = _TmnxSysNetconfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23)
)


class _TmnxSysNetconfAdminStatus_Type(TmnxAdminState):
    """Custom type tmnxSysNetconfAdminStatus based on TmnxAdminState"""
    defaultValue = 3


_TmnxSysNetconfAdminStatus_Type.__name__ = "TmnxAdminState"
_TmnxSysNetconfAdminStatus_Object = MibScalar
tmnxSysNetconfAdminStatus = _TmnxSysNetconfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 1),
    _TmnxSysNetconfAdminStatus_Type()
)
tmnxSysNetconfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysNetconfAdminStatus.setStatus("current")
_TmnxSysNetconfOperStatus_Type = TmnxOperState
_TmnxSysNetconfOperStatus_Object = MibScalar
tmnxSysNetconfOperStatus = _TmnxSysNetconfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 2),
    _TmnxSysNetconfOperStatus_Type()
)
tmnxSysNetconfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysNetconfOperStatus.setStatus("current")
_TmnxSysNetconfRequests_Type = Counter32
_TmnxSysNetconfRequests_Object = MibScalar
tmnxSysNetconfRequests = _TmnxSysNetconfRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 3),
    _TmnxSysNetconfRequests_Type()
)
tmnxSysNetconfRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysNetconfRequests.setStatus("current")
_TmnxSysNetconfGetRequests_Type = Counter32
_TmnxSysNetconfGetRequests_Object = MibScalar
tmnxSysNetconfGetRequests = _TmnxSysNetconfGetRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 4),
    _TmnxSysNetconfGetRequests_Type()
)
tmnxSysNetconfGetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysNetconfGetRequests.setStatus("current")
_TmnxSysNetconfGetConfigRequests_Type = Counter32
_TmnxSysNetconfGetConfigRequests_Object = MibScalar
tmnxSysNetconfGetConfigRequests = _TmnxSysNetconfGetConfigRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 5),
    _TmnxSysNetconfGetConfigRequests_Type()
)
tmnxSysNetconfGetConfigRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysNetconfGetConfigRequests.setStatus("current")
_TmnxSysNetconfEditConfigRequests_Type = Counter32
_TmnxSysNetconfEditConfigRequests_Object = MibScalar
tmnxSysNetconfEditConfigRequests = _TmnxSysNetconfEditConfigRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 6),
    _TmnxSysNetconfEditConfigRequests_Type()
)
tmnxSysNetconfEditConfigRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysNetconfEditConfigRequests.setStatus("current")
_TmnxSysNetconfCloseRequests_Type = Counter32
_TmnxSysNetconfCloseRequests_Object = MibScalar
tmnxSysNetconfCloseRequests = _TmnxSysNetconfCloseRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 7),
    _TmnxSysNetconfCloseRequests_Type()
)
tmnxSysNetconfCloseRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysNetconfCloseRequests.setStatus("current")
_TmnxSysNetconfKillRequests_Type = Counter32
_TmnxSysNetconfKillRequests_Object = MibScalar
tmnxSysNetconfKillRequests = _TmnxSysNetconfKillRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 8),
    _TmnxSysNetconfKillRequests_Type()
)
tmnxSysNetconfKillRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysNetconfKillRequests.setStatus("current")
_TmnxSysNetconfResponses_Type = Counter32
_TmnxSysNetconfResponses_Object = MibScalar
tmnxSysNetconfResponses = _TmnxSysNetconfResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 9),
    _TmnxSysNetconfResponses_Type()
)
tmnxSysNetconfResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysNetconfResponses.setStatus("current")
_TmnxSysNetconfErrorResponses_Type = Counter32
_TmnxSysNetconfErrorResponses_Object = MibScalar
tmnxSysNetconfErrorResponses = _TmnxSysNetconfErrorResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 10),
    _TmnxSysNetconfErrorResponses_Type()
)
tmnxSysNetconfErrorResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysNetconfErrorResponses.setStatus("current")
_TmnxSysNetconfCopyConfigRequests_Type = Counter32
_TmnxSysNetconfCopyConfigRequests_Object = MibScalar
tmnxSysNetconfCopyConfigRequests = _TmnxSysNetconfCopyConfigRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 11),
    _TmnxSysNetconfCopyConfigRequests_Type()
)
tmnxSysNetconfCopyConfigRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysNetconfCopyConfigRequests.setStatus("current")
_TmnxSysNetconfDelConfigRequests_Type = Counter32
_TmnxSysNetconfDelConfigRequests_Object = MibScalar
tmnxSysNetconfDelConfigRequests = _TmnxSysNetconfDelConfigRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 12),
    _TmnxSysNetconfDelConfigRequests_Type()
)
tmnxSysNetconfDelConfigRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysNetconfDelConfigRequests.setStatus("current")
_TmnxSysNetconfValidateRequests_Type = Counter32
_TmnxSysNetconfValidateRequests_Object = MibScalar
tmnxSysNetconfValidateRequests = _TmnxSysNetconfValidateRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 13),
    _TmnxSysNetconfValidateRequests_Type()
)
tmnxSysNetconfValidateRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysNetconfValidateRequests.setStatus("current")
_TmnxSysNetconfFailedEditCfgReqs_Type = Counter32
_TmnxSysNetconfFailedEditCfgReqs_Object = MibScalar
tmnxSysNetconfFailedEditCfgReqs = _TmnxSysNetconfFailedEditCfgReqs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 14),
    _TmnxSysNetconfFailedEditCfgReqs_Type()
)
tmnxSysNetconfFailedEditCfgReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysNetconfFailedEditCfgReqs.setStatus("current")
_TmnxSysNetconfFailedLockReqs_Type = Counter32
_TmnxSysNetconfFailedLockReqs_Object = MibScalar
tmnxSysNetconfFailedLockReqs = _TmnxSysNetconfFailedLockReqs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 15),
    _TmnxSysNetconfFailedLockReqs_Type()
)
tmnxSysNetconfFailedLockReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysNetconfFailedLockReqs.setStatus("current")
_TmnxSysNetconfLockRequests_Type = Counter32
_TmnxSysNetconfLockRequests_Object = MibScalar
tmnxSysNetconfLockRequests = _TmnxSysNetconfLockRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 16),
    _TmnxSysNetconfLockRequests_Type()
)
tmnxSysNetconfLockRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysNetconfLockRequests.setStatus("current")
_TmnxSysNetconfUnlockRequests_Type = Counter32
_TmnxSysNetconfUnlockRequests_Object = MibScalar
tmnxSysNetconfUnlockRequests = _TmnxSysNetconfUnlockRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 17),
    _TmnxSysNetconfUnlockRequests_Type()
)
tmnxSysNetconfUnlockRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysNetconfUnlockRequests.setStatus("current")
_TmnxSysNetconfCommitRequests_Type = Counter32
_TmnxSysNetconfCommitRequests_Object = MibScalar
tmnxSysNetconfCommitRequests = _TmnxSysNetconfCommitRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 18),
    _TmnxSysNetconfCommitRequests_Type()
)
tmnxSysNetconfCommitRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysNetconfCommitRequests.setStatus("current")
_TmnxSysNetconfDiscardRequests_Type = Counter32
_TmnxSysNetconfDiscardRequests_Object = MibScalar
tmnxSysNetconfDiscardRequests = _TmnxSysNetconfDiscardRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 19),
    _TmnxSysNetconfDiscardRequests_Type()
)
tmnxSysNetconfDiscardRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysNetconfDiscardRequests.setStatus("current")


class _TmnxSysNetconfCapCandidateCfg_Type(TruthValue):
    """Custom type tmnxSysNetconfCapCandidateCfg based on TruthValue"""
    defaultValue = 1


_TmnxSysNetconfCapCandidateCfg_Type.__name__ = "TruthValue"
_TmnxSysNetconfCapCandidateCfg_Object = MibScalar
tmnxSysNetconfCapCandidateCfg = _TmnxSysNetconfCapCandidateCfg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 20),
    _TmnxSysNetconfCapCandidateCfg_Type()
)
tmnxSysNetconfCapCandidateCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysNetconfCapCandidateCfg.setStatus("current")


class _TmnxSysNetconfCapRunningCfg_Type(TruthValue):
    """Custom type tmnxSysNetconfCapRunningCfg based on TruthValue"""
    defaultValue = 2


_TmnxSysNetconfCapRunningCfg_Type.__name__ = "TruthValue"
_TmnxSysNetconfCapRunningCfg_Object = MibScalar
tmnxSysNetconfCapRunningCfg = _TmnxSysNetconfCapRunningCfg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 21),
    _TmnxSysNetconfCapRunningCfg_Type()
)
tmnxSysNetconfCapRunningCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysNetconfCapRunningCfg.setStatus("current")


class _TmnxSysNetconfYangBaseR13_Type(TruthValue):
    """Custom type tmnxSysNetconfYangBaseR13 based on TruthValue"""
    defaultValue = 1


_TmnxSysNetconfYangBaseR13_Type.__name__ = "TruthValue"
_TmnxSysNetconfYangBaseR13_Object = MibScalar
tmnxSysNetconfYangBaseR13 = _TmnxSysNetconfYangBaseR13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 22),
    _TmnxSysNetconfYangBaseR13_Type()
)
tmnxSysNetconfYangBaseR13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysNetconfYangBaseR13.setStatus("obsolete")


class _TmnxSysNetconfYangNokia_Type(TruthValue):
    """Custom type tmnxSysNetconfYangNokia based on TruthValue"""
    defaultValue = 1


_TmnxSysNetconfYangNokia_Type.__name__ = "TruthValue"
_TmnxSysNetconfYangNokia_Object = MibScalar
tmnxSysNetconfYangNokia = _TmnxSysNetconfYangNokia_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 23),
    _TmnxSysNetconfYangNokia_Type()
)
tmnxSysNetconfYangNokia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysNetconfYangNokia.setStatus("obsolete")
_TmnxSysNetconfCreateSubRequests_Type = Counter32
_TmnxSysNetconfCreateSubRequests_Object = MibScalar
tmnxSysNetconfCreateSubRequests = _TmnxSysNetconfCreateSubRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 24),
    _TmnxSysNetconfCreateSubRequests_Type()
)
tmnxSysNetconfCreateSubRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysNetconfCreateSubRequests.setStatus("current")


class _TmnxSysNetconfAutoCfgSave_Type(TruthValue):
    """Custom type tmnxSysNetconfAutoCfgSave based on TruthValue"""
    defaultValue = 2


_TmnxSysNetconfAutoCfgSave_Type.__name__ = "TruthValue"
_TmnxSysNetconfAutoCfgSave_Object = MibScalar
tmnxSysNetconfAutoCfgSave = _TmnxSysNetconfAutoCfgSave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 25),
    _TmnxSysNetconfAutoCfgSave_Type()
)
tmnxSysNetconfAutoCfgSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysNetconfAutoCfgSave.setStatus("current")


class _TmnxSysNetconfPort_Type(Unsigned32):
    """Custom type tmnxSysNetconfPort based on Unsigned32"""
    defaultValue = 830

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(22, 22),
        ValueRangeConstraint(830, 830),
    )


_TmnxSysNetconfPort_Type.__name__ = "Unsigned32"
_TmnxSysNetconfPort_Object = MibScalar
tmnxSysNetconfPort = _TmnxSysNetconfPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 26),
    _TmnxSysNetconfPort_Type()
)
tmnxSysNetconfPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysNetconfPort.setStatus("current")
_TmnxSysNetconfGetSchemaRequests_Type = Counter32
_TmnxSysNetconfGetSchemaRequests_Object = MibScalar
tmnxSysNetconfGetSchemaRequests = _TmnxSysNetconfGetSchemaRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 27),
    _TmnxSysNetconfGetSchemaRequests_Type()
)
tmnxSysNetconfGetSchemaRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysNetconfGetSchemaRequests.setStatus("current")
_TmnxSysNetconfGetDataRequests_Type = Counter32
_TmnxSysNetconfGetDataRequests_Object = MibScalar
tmnxSysNetconfGetDataRequests = _TmnxSysNetconfGetDataRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 28),
    _TmnxSysNetconfGetDataRequests_Type()
)
tmnxSysNetconfGetDataRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysNetconfGetDataRequests.setStatus("current")
_TmnxSysNetconfActionRequests_Type = Counter32
_TmnxSysNetconfActionRequests_Object = MibScalar
tmnxSysNetconfActionRequests = _TmnxSysNetconfActionRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 23, 29),
    _TmnxSysNetconfActionRequests_Type()
)
tmnxSysNetconfActionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysNetconfActionRequests.setStatus("current")
_TmnxDCSysObjs_ObjectIdentity = ObjectIdentity
tmnxDCSysObjs = _TmnxDCSysObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 24)
)
_TmnxSysStrmInfo_ObjectIdentity = ObjectIdentity
tmnxSysStrmInfo = _TmnxSysStrmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 25)
)


class _TmnxSysStrmAdminStatus_Type(TmnxAdminState):
    """Custom type tmnxSysStrmAdminStatus based on TmnxAdminState"""
    defaultValue = 3


_TmnxSysStrmAdminStatus_Type.__name__ = "TmnxAdminState"
_TmnxSysStrmAdminStatus_Object = MibScalar
tmnxSysStrmAdminStatus = _TmnxSysStrmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 25, 1),
    _TmnxSysStrmAdminStatus_Type()
)
tmnxSysStrmAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysStrmAdminStatus.setStatus("current")
_TmnxSysStrmDumpSnmpRequests_Type = Counter32
_TmnxSysStrmDumpSnmpRequests_Object = MibScalar
tmnxSysStrmDumpSnmpRequests = _TmnxSysStrmDumpSnmpRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 25, 2),
    _TmnxSysStrmDumpSnmpRequests_Type()
)
tmnxSysStrmDumpSnmpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysStrmDumpSnmpRequests.setStatus("current")
_TmnxSysStrmGetManyRequests_Type = Counter32
_TmnxSysStrmGetManyRequests_Object = MibScalar
tmnxSysStrmGetManyRequests = _TmnxSysStrmGetManyRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 25, 3),
    _TmnxSysStrmGetManyRequests_Type()
)
tmnxSysStrmGetManyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysStrmGetManyRequests.setStatus("current")
_TmnxSysStrmResponses_Type = Counter32
_TmnxSysStrmResponses_Object = MibScalar
tmnxSysStrmResponses = _TmnxSysStrmResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 25, 4),
    _TmnxSysStrmResponses_Type()
)
tmnxSysStrmResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysStrmResponses.setStatus("current")
_TmnxSysXmppInfo_ObjectIdentity = ObjectIdentity
tmnxSysXmppInfo = _TmnxSysXmppInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26)
)
_TmnxSysXmppServerTable_Object = MibTable
tmnxSysXmppServerTable = _TmnxSysXmppServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1)
)
if mibBuilder.loadTexts:
    tmnxSysXmppServerTable.setStatus("current")
_TmnxSysXmppServerEntry_Object = MibTableRow
tmnxSysXmppServerEntry = _TmnxSysXmppServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1)
)
tmnxSysXmppServerEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysXmppServName"),
)
if mibBuilder.loadTexts:
    tmnxSysXmppServerEntry.setStatus("current")


class _TmnxSysXmppServName_Type(DisplayString):
    """Custom type tmnxSysXmppServName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxSysXmppServName_Type.__name__ = "DisplayString"
_TmnxSysXmppServName_Object = MibTableColumn
tmnxSysXmppServName = _TmnxSysXmppServName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 1),
    _TmnxSysXmppServName_Type()
)
tmnxSysXmppServName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysXmppServName.setStatus("current")


class _TmnxSysXmppServFQDN_Type(DisplayString):
    """Custom type tmnxSysXmppServFQDN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxSysXmppServFQDN_Type.__name__ = "DisplayString"
_TmnxSysXmppServFQDN_Object = MibTableColumn
tmnxSysXmppServFQDN = _TmnxSysXmppServFQDN_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 2),
    _TmnxSysXmppServFQDN_Type()
)
tmnxSysXmppServFQDN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysXmppServFQDN.setStatus("current")
_TmnxSysXmppServRowStatus_Type = RowStatus
_TmnxSysXmppServRowStatus_Object = MibTableColumn
tmnxSysXmppServRowStatus = _TmnxSysXmppServRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 3),
    _TmnxSysXmppServRowStatus_Type()
)
tmnxSysXmppServRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysXmppServRowStatus.setStatus("current")
_TmnxSysXmppServUserName_Type = TNamedItemOrEmpty
_TmnxSysXmppServUserName_Object = MibTableColumn
tmnxSysXmppServUserName = _TmnxSysXmppServUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 4),
    _TmnxSysXmppServUserName_Type()
)
tmnxSysXmppServUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysXmppServUserName.setStatus("current")


class _TmnxSysXmppServPassword_Type(DisplayString):
    """Custom type tmnxSysXmppServPassword based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxSysXmppServPassword_Type.__name__ = "DisplayString"
_TmnxSysXmppServPassword_Object = MibTableColumn
tmnxSysXmppServPassword = _TmnxSysXmppServPassword_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 5),
    _TmnxSysXmppServPassword_Type()
)
tmnxSysXmppServPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysXmppServPassword.setStatus("current")
_TmnxSysXmppServLastChanged_Type = TimeStamp
_TmnxSysXmppServLastChanged_Object = MibTableColumn
tmnxSysXmppServLastChanged = _TmnxSysXmppServLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 6),
    _TmnxSysXmppServLastChanged_Type()
)
tmnxSysXmppServLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysXmppServLastChanged.setStatus("current")
_TmnxSysXmppServUptime_Type = TimeStamp
_TmnxSysXmppServUptime_Object = MibTableColumn
tmnxSysXmppServUptime = _TmnxSysXmppServUptime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 7),
    _TmnxSysXmppServUptime_Type()
)
tmnxSysXmppServUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysXmppServUptime.setStatus("current")
_TmnxSysXmppServIQSent_Type = Counter64
_TmnxSysXmppServIQSent_Object = MibTableColumn
tmnxSysXmppServIQSent = _TmnxSysXmppServIQSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 8),
    _TmnxSysXmppServIQSent_Type()
)
tmnxSysXmppServIQSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysXmppServIQSent.setStatus("current")
_TmnxSysXmppServIQRcvd_Type = Counter64
_TmnxSysXmppServIQRcvd_Object = MibTableColumn
tmnxSysXmppServIQRcvd = _TmnxSysXmppServIQRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 9),
    _TmnxSysXmppServIQRcvd_Type()
)
tmnxSysXmppServIQRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysXmppServIQRcvd.setStatus("current")
_TmnxSysXmppServIQError_Type = Counter64
_TmnxSysXmppServIQError_Object = MibTableColumn
tmnxSysXmppServIQError = _TmnxSysXmppServIQError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 10),
    _TmnxSysXmppServIQError_Type()
)
tmnxSysXmppServIQError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysXmppServIQError.setStatus("current")
_TmnxSysXmppServIQTimedOut_Type = Counter64
_TmnxSysXmppServIQTimedOut_Object = MibTableColumn
tmnxSysXmppServIQTimedOut = _TmnxSysXmppServIQTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 11),
    _TmnxSysXmppServIQTimedOut_Type()
)
tmnxSysXmppServIQTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysXmppServIQTimedOut.setStatus("current")
_TmnxSysXmppServIQAckRcvd_Type = Counter64
_TmnxSysXmppServIQAckRcvd_Object = MibTableColumn
tmnxSysXmppServIQAckRcvd = _TmnxSysXmppServIQAckRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 12),
    _TmnxSysXmppServIQAckRcvd_Type()
)
tmnxSysXmppServIQAckRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysXmppServIQAckRcvd.setStatus("current")
_TmnxSysXmppServIQMinRtt_Type = Counter64
_TmnxSysXmppServIQMinRtt_Object = MibTableColumn
tmnxSysXmppServIQMinRtt = _TmnxSysXmppServIQMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 13),
    _TmnxSysXmppServIQMinRtt_Type()
)
tmnxSysXmppServIQMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysXmppServIQMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSysXmppServIQMinRtt.setUnits("milliseconds")
_TmnxSysXmppServIQMaxRtt_Type = Counter64
_TmnxSysXmppServIQMaxRtt_Object = MibTableColumn
tmnxSysXmppServIQMaxRtt = _TmnxSysXmppServIQMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 14),
    _TmnxSysXmppServIQMaxRtt_Type()
)
tmnxSysXmppServIQMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysXmppServIQMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSysXmppServIQMaxRtt.setUnits("milliseconds")
_TmnxSysXmppServVsdUpdatesRcvd_Type = Counter64
_TmnxSysXmppServVsdUpdatesRcvd_Object = MibTableColumn
tmnxSysXmppServVsdUpdatesRcvd = _TmnxSysXmppServVsdUpdatesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 15),
    _TmnxSysXmppServVsdUpdatesRcvd_Type()
)
tmnxSysXmppServVsdUpdatesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysXmppServVsdUpdatesRcvd.setStatus("current")
_TmnxSysXmppServUpdatesRcvd_Type = Counter64
_TmnxSysXmppServUpdatesRcvd_Object = MibTableColumn
tmnxSysXmppServUpdatesRcvd = _TmnxSysXmppServUpdatesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 16),
    _TmnxSysXmppServUpdatesRcvd_Type()
)
tmnxSysXmppServUpdatesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysXmppServUpdatesRcvd.setStatus("current")
_TmnxSysXmppServMsgSent_Type = Counter64
_TmnxSysXmppServMsgSent_Object = MibTableColumn
tmnxSysXmppServMsgSent = _TmnxSysXmppServMsgSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 17),
    _TmnxSysXmppServMsgSent_Type()
)
tmnxSysXmppServMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysXmppServMsgSent.setStatus("current")
_TmnxSysXmppServMsgRcvd_Type = Counter64
_TmnxSysXmppServMsgRcvd_Object = MibTableColumn
tmnxSysXmppServMsgRcvd = _TmnxSysXmppServMsgRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 18),
    _TmnxSysXmppServMsgRcvd_Type()
)
tmnxSysXmppServMsgRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysXmppServMsgRcvd.setStatus("current")
_TmnxSysXmppServMsgAckRcvd_Type = Counter64
_TmnxSysXmppServMsgAckRcvd_Object = MibTableColumn
tmnxSysXmppServMsgAckRcvd = _TmnxSysXmppServMsgAckRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 19),
    _TmnxSysXmppServMsgAckRcvd_Type()
)
tmnxSysXmppServMsgAckRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysXmppServMsgAckRcvd.setStatus("current")
_TmnxSysXmppServMsgError_Type = Counter64
_TmnxSysXmppServMsgError_Object = MibTableColumn
tmnxSysXmppServMsgError = _TmnxSysXmppServMsgError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 20),
    _TmnxSysXmppServMsgError_Type()
)
tmnxSysXmppServMsgError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysXmppServMsgError.setStatus("current")
_TmnxSysXmppServMsgTimedOut_Type = Counter64
_TmnxSysXmppServMsgTimedOut_Object = MibTableColumn
tmnxSysXmppServMsgTimedOut = _TmnxSysXmppServMsgTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 21),
    _TmnxSysXmppServMsgTimedOut_Type()
)
tmnxSysXmppServMsgTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysXmppServMsgTimedOut.setStatus("current")
_TmnxSysXmppServMsgMinRtt_Type = Counter64
_TmnxSysXmppServMsgMinRtt_Object = MibTableColumn
tmnxSysXmppServMsgMinRtt = _TmnxSysXmppServMsgMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 22),
    _TmnxSysXmppServMsgMinRtt_Type()
)
tmnxSysXmppServMsgMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysXmppServMsgMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSysXmppServMsgMinRtt.setUnits("milliseconds")
_TmnxSysXmppServMsgMaxRtt_Type = Counter64
_TmnxSysXmppServMsgMaxRtt_Object = MibTableColumn
tmnxSysXmppServMsgMaxRtt = _TmnxSysXmppServMsgMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 23),
    _TmnxSysXmppServMsgMaxRtt_Type()
)
tmnxSysXmppServMsgMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysXmppServMsgMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSysXmppServMsgMaxRtt.setUnits("milliseconds")
_TmnxSysXmppServSubSent_Type = Counter64
_TmnxSysXmppServSubSent_Object = MibTableColumn
tmnxSysXmppServSubSent = _TmnxSysXmppServSubSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 24),
    _TmnxSysXmppServSubSent_Type()
)
tmnxSysXmppServSubSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysXmppServSubSent.setStatus("current")
_TmnxSysXmppServUnSubSent_Type = Counter64
_TmnxSysXmppServUnSubSent_Object = MibTableColumn
tmnxSysXmppServUnSubSent = _TmnxSysXmppServUnSubSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 25),
    _TmnxSysXmppServUnSubSent_Type()
)
tmnxSysXmppServUnSubSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysXmppServUnSubSent.setStatus("current")


class _TmnxSysXmppServState_Type(DisplayString):
    """Custom type tmnxSysXmppServState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxSysXmppServState_Type.__name__ = "DisplayString"
_TmnxSysXmppServState_Object = MibTableColumn
tmnxSysXmppServState = _TmnxSysXmppServState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 26),
    _TmnxSysXmppServState_Type()
)
tmnxSysXmppServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysXmppServState.setStatus("current")


class _TmnxSysXmppServAdminState_Type(TmnxAdminState):
    """Custom type tmnxSysXmppServAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxSysXmppServAdminState_Type.__name__ = "TmnxAdminState"
_TmnxSysXmppServAdminState_Object = MibTableColumn
tmnxSysXmppServAdminState = _TmnxSysXmppServAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 27),
    _TmnxSysXmppServAdminState_Type()
)
tmnxSysXmppServAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysXmppServAdminState.setStatus("current")
_TmnxSysXmppServOperUserName_Type = TNamedItemOrEmpty
_TmnxSysXmppServOperUserName_Object = MibTableColumn
tmnxSysXmppServOperUserName = _TmnxSysXmppServOperUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 28),
    _TmnxSysXmppServOperUserName_Type()
)
tmnxSysXmppServOperUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysXmppServOperUserName.setStatus("current")
_TmnxSysXmppServAuthType_Type = TNamedItemOrEmpty
_TmnxSysXmppServAuthType_Object = MibTableColumn
tmnxSysXmppServAuthType = _TmnxSysXmppServAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 29),
    _TmnxSysXmppServAuthType_Type()
)
tmnxSysXmppServAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysXmppServAuthType.setStatus("current")


class _TmnxSysXmppServConnMode_Type(Integer32):
    """Custom type tmnxSysXmppServConnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inBand", 1),
          ("outOfBand", 2))
    )


_TmnxSysXmppServConnMode_Type.__name__ = "Integer32"
_TmnxSysXmppServConnMode_Object = MibTableColumn
tmnxSysXmppServConnMode = _TmnxSysXmppServConnMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 30),
    _TmnxSysXmppServConnMode_Type()
)
tmnxSysXmppServConnMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysXmppServConnMode.setStatus("current")


class _TmnxSysXmppServServiceId_Type(TmnxServId):
    """Custom type tmnxSysXmppServServiceId based on TmnxServId"""
    defaultValue = 0


_TmnxSysXmppServServiceId_Type.__name__ = "TmnxServId"
_TmnxSysXmppServServiceId_Object = MibTableColumn
tmnxSysXmppServServiceId = _TmnxSysXmppServServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 31),
    _TmnxSysXmppServServiceId_Type()
)
tmnxSysXmppServServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysXmppServServiceId.setStatus("current")


class _TmnxSysXmppServRouterId_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxSysXmppServRouterId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxSysXmppServRouterId_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxSysXmppServRouterId_Object = MibTableColumn
tmnxSysXmppServRouterId = _TmnxSysXmppServRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 1, 1, 32),
    _TmnxSysXmppServRouterId_Type()
)
tmnxSysXmppServRouterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysXmppServRouterId.setStatus("current")
_TmnxSysVsdServerTable_Object = MibTable
tmnxSysVsdServerTable = _TmnxSysVsdServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 2)
)
if mibBuilder.loadTexts:
    tmnxSysVsdServerTable.setStatus("current")
_TmnxSysVsdServerEntry_Object = MibTableRow
tmnxSysVsdServerEntry = _TmnxSysVsdServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 2, 1)
)
tmnxSysVsdServerEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysVsdServerInstance"),
)
if mibBuilder.loadTexts:
    tmnxSysVsdServerEntry.setStatus("current")
_TmnxSysVsdServerInstance_Type = Unsigned32
_TmnxSysVsdServerInstance_Object = MibTableColumn
tmnxSysVsdServerInstance = _TmnxSysVsdServerInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 2, 1, 1),
    _TmnxSysVsdServerInstance_Type()
)
tmnxSysVsdServerInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysVsdServerInstance.setStatus("current")
_TmnxSysVsdServUptime_Type = TimeStamp
_TmnxSysVsdServUptime_Object = MibTableColumn
tmnxSysVsdServUptime = _TmnxSysVsdServUptime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 2, 1, 2),
    _TmnxSysVsdServUptime_Type()
)
tmnxSysVsdServUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysVsdServUptime.setStatus("current")
_TmnxSysVsdServUserName_Type = TLDisplayString
_TmnxSysVsdServUserName_Object = MibTableColumn
tmnxSysVsdServUserName = _TmnxSysVsdServUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 2, 1, 3),
    _TmnxSysVsdServUserName_Type()
)
tmnxSysVsdServUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysVsdServUserName.setStatus("current")


class _TmnxSysVsdServerStatus_Type(DisplayString):
    """Custom type tmnxSysVsdServerStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxSysVsdServerStatus_Type.__name__ = "DisplayString"
_TmnxSysVsdServerStatus_Object = MibTableColumn
tmnxSysVsdServerStatus = _TmnxSysVsdServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 2, 1, 4),
    _TmnxSysVsdServerStatus_Type()
)
tmnxSysVsdServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysVsdServerStatus.setStatus("current")
_TmnxSysVsdServMsgSent_Type = Counter64
_TmnxSysVsdServMsgSent_Object = MibTableColumn
tmnxSysVsdServMsgSent = _TmnxSysVsdServMsgSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 2, 1, 5),
    _TmnxSysVsdServMsgSent_Type()
)
tmnxSysVsdServMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysVsdServMsgSent.setStatus("current")
_TmnxSysVsdServMsgRcvd_Type = Counter64
_TmnxSysVsdServMsgRcvd_Object = MibTableColumn
tmnxSysVsdServMsgRcvd = _TmnxSysVsdServMsgRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 2, 1, 6),
    _TmnxSysVsdServMsgRcvd_Type()
)
tmnxSysVsdServMsgRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysVsdServMsgRcvd.setStatus("current")
_TmnxSysVsdServMsgAckRcvd_Type = Counter64
_TmnxSysVsdServMsgAckRcvd_Object = MibTableColumn
tmnxSysVsdServMsgAckRcvd = _TmnxSysVsdServMsgAckRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 2, 1, 7),
    _TmnxSysVsdServMsgAckRcvd_Type()
)
tmnxSysVsdServMsgAckRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysVsdServMsgAckRcvd.setStatus("current")
_TmnxSysVsdServMsgError_Type = Counter64
_TmnxSysVsdServMsgError_Object = MibTableColumn
tmnxSysVsdServMsgError = _TmnxSysVsdServMsgError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 2, 1, 8),
    _TmnxSysVsdServMsgError_Type()
)
tmnxSysVsdServMsgError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysVsdServMsgError.setStatus("current")
_TmnxSysVsdServMsgTimedOut_Type = Counter64
_TmnxSysVsdServMsgTimedOut_Object = MibTableColumn
tmnxSysVsdServMsgTimedOut = _TmnxSysVsdServMsgTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 2, 1, 9),
    _TmnxSysVsdServMsgTimedOut_Type()
)
tmnxSysVsdServMsgTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysVsdServMsgTimedOut.setStatus("current")
_TmnxSysVsdServMsgMinRtt_Type = Counter64
_TmnxSysVsdServMsgMinRtt_Object = MibTableColumn
tmnxSysVsdServMsgMinRtt = _TmnxSysVsdServMsgMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 2, 1, 10),
    _TmnxSysVsdServMsgMinRtt_Type()
)
tmnxSysVsdServMsgMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysVsdServMsgMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSysVsdServMsgMinRtt.setUnits("milliseconds")
_TmnxSysVsdServMsgMaxRtt_Type = Counter64
_TmnxSysVsdServMsgMaxRtt_Object = MibTableColumn
tmnxSysVsdServMsgMaxRtt = _TmnxSysVsdServMsgMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 26, 2, 1, 11),
    _TmnxSysVsdServMsgMaxRtt_Type()
)
tmnxSysVsdServMsgMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysVsdServMsgMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSysVsdServMsgMaxRtt.setUnits("milliseconds")
_TmnxSysResInfo_ObjectIdentity = ObjectIdentity
tmnxSysResInfo = _TmnxSysResInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27)
)
_TmnxSysResCardInfo_ObjectIdentity = ObjectIdentity
tmnxSysResCardInfo = _TmnxSysResCardInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 1)
)
_TmnxCardCpuResMonitorTable_Object = MibTable
tmnxCardCpuResMonitorTable = _TmnxCardCpuResMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxCardCpuResMonitorTable.setStatus("current")
_TmnxCardCpuResMonitorEntry_Object = MibTableRow
tmnxCardCpuResMonitorEntry = _TmnxCardCpuResMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 1, 1, 1)
)
tmnxCardCpuResMonitorEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-SYSTEM-MIB", "tmnxCardResourceSlotNum"),
    (0, "TIMETRA-SYSTEM-MIB", "tmnxCardCpuResSampleTime"),
)
if mibBuilder.loadTexts:
    tmnxCardCpuResMonitorEntry.setStatus("current")
_TmnxCardResourceSlotNum_Type = TmnxSlotNum
_TmnxCardResourceSlotNum_Object = MibTableColumn
tmnxCardResourceSlotNum = _TmnxCardResourceSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 1, 1, 1, 1),
    _TmnxCardResourceSlotNum_Type()
)
tmnxCardResourceSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCardResourceSlotNum.setStatus("current")
_TmnxCardCpuResSampleTime_Type = TmnxSysMonSampleTime
_TmnxCardCpuResSampleTime_Object = MibTableColumn
tmnxCardCpuResSampleTime = _TmnxCardCpuResSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 1, 1, 1, 2),
    _TmnxCardCpuResSampleTime_Type()
)
tmnxCardCpuResSampleTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCardCpuResSampleTime.setStatus("current")
_TmnxCardCpuResMonCpuIdle_Type = TmnxSysMonUtilization
_TmnxCardCpuResMonCpuIdle_Object = MibTableColumn
tmnxCardCpuResMonCpuIdle = _TmnxCardCpuResMonCpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 1, 1, 1, 3),
    _TmnxCardCpuResMonCpuIdle_Type()
)
tmnxCardCpuResMonCpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardCpuResMonCpuIdle.setStatus("current")
_TmnxCardCpuResMonBusyCoreUtil_Type = TmnxSysMonUtilization
_TmnxCardCpuResMonBusyCoreUtil_Object = MibTableColumn
tmnxCardCpuResMonBusyCoreUtil = _TmnxCardCpuResMonBusyCoreUtil_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 1, 1, 1, 4),
    _TmnxCardCpuResMonBusyCoreUtil_Type()
)
tmnxCardCpuResMonBusyCoreUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardCpuResMonBusyCoreUtil.setStatus("current")


class _TmnxCardCpuResMonBusyGroupName_Type(OctetString):
    """Custom type tmnxCardCpuResMonBusyGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxCardCpuResMonBusyGroupName_Type.__name__ = "OctetString"
_TmnxCardCpuResMonBusyGroupName_Object = MibTableColumn
tmnxCardCpuResMonBusyGroupName = _TmnxCardCpuResMonBusyGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 1, 1, 1, 5),
    _TmnxCardCpuResMonBusyGroupName_Type()
)
tmnxCardCpuResMonBusyGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardCpuResMonBusyGroupName.setStatus("current")
_TmnxCardCpuResMonBusyGroupUtil_Type = TmnxSysMonUtilization
_TmnxCardCpuResMonBusyGroupUtil_Object = MibTableColumn
tmnxCardCpuResMonBusyGroupUtil = _TmnxCardCpuResMonBusyGroupUtil_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 1, 1, 1, 6),
    _TmnxCardCpuResMonBusyGroupUtil_Type()
)
tmnxCardCpuResMonBusyGroupUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardCpuResMonBusyGroupUtil.setStatus("current")
_TmnxCardMemResMonitorTable_Object = MibTable
tmnxCardMemResMonitorTable = _TmnxCardMemResMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxCardMemResMonitorTable.setStatus("current")
_TmnxCardMemResMonitorEntry_Object = MibTableRow
tmnxCardMemResMonitorEntry = _TmnxCardMemResMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 1, 2, 1)
)
tmnxCardMemResMonitorEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-SYSTEM-MIB", "tmnxCardResourceSlotNum"),
)
if mibBuilder.loadTexts:
    tmnxCardMemResMonitorEntry.setStatus("current")
_TmnxCardMemResMemoryUsed_Type = Gauge32
_TmnxCardMemResMemoryUsed_Object = MibTableColumn
tmnxCardMemResMemoryUsed = _TmnxCardMemResMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 1, 2, 1, 1),
    _TmnxCardMemResMemoryUsed_Type()
)
tmnxCardMemResMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardMemResMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCardMemResMemoryUsed.setUnits("kilobytes")
_TmnxCardMemResMemoryAvailable_Type = Gauge32
_TmnxCardMemResMemoryAvailable_Object = MibTableColumn
tmnxCardMemResMemoryAvailable = _TmnxCardMemResMemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 1, 2, 1, 2),
    _TmnxCardMemResMemoryAvailable_Type()
)
tmnxCardMemResMemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardMemResMemoryAvailable.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCardMemResMemoryAvailable.setUnits("kilobytes")
_TmnxCardMemResPoolsAllocated_Type = Gauge32
_TmnxCardMemResPoolsAllocated_Object = MibTableColumn
tmnxCardMemResPoolsAllocated = _TmnxCardMemResPoolsAllocated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 1, 2, 1, 3),
    _TmnxCardMemResPoolsAllocated_Type()
)
tmnxCardMemResPoolsAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardMemResPoolsAllocated.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCardMemResPoolsAllocated.setUnits("kilobytes")
_TmnxSysResEcmpProfInfo_ObjectIdentity = ObjectIdentity
tmnxSysResEcmpProfInfo = _TmnxSysResEcmpProfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 2)
)
_TmnxSysResEcmpProfTable_Object = MibTable
tmnxSysResEcmpProfTable = _TmnxSysResEcmpProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxSysResEcmpProfTable.setStatus("current")
_TmnxSysResEcmpProfEntry_Object = MibTableRow
tmnxSysResEcmpProfEntry = _TmnxSysResEcmpProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 2, 1, 1)
)
tmnxSysResEcmpProfEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysResEcmpProfId"),
)
if mibBuilder.loadTexts:
    tmnxSysResEcmpProfEntry.setStatus("current")


class _TmnxSysResEcmpProfId_Type(Unsigned32):
    """Custom type tmnxSysResEcmpProfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TmnxSysResEcmpProfId_Type.__name__ = "Unsigned32"
_TmnxSysResEcmpProfId_Object = MibTableColumn
tmnxSysResEcmpProfId = _TmnxSysResEcmpProfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 2, 1, 1, 1),
    _TmnxSysResEcmpProfId_Type()
)
tmnxSysResEcmpProfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysResEcmpProfId.setStatus("current")
_TmnxSysResEcmpProfRowStatus_Type = RowStatus
_TmnxSysResEcmpProfRowStatus_Object = MibTableColumn
tmnxSysResEcmpProfRowStatus = _TmnxSysResEcmpProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 2, 1, 1, 2),
    _TmnxSysResEcmpProfRowStatus_Type()
)
tmnxSysResEcmpProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysResEcmpProfRowStatus.setStatus("current")


class _TmnxSysResEcmpProfType_Type(Integer32):
    """Custom type tmnxSysResEcmpProfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mpls", 1),
          ("ip", 2))
    )


_TmnxSysResEcmpProfType_Type.__name__ = "Integer32"
_TmnxSysResEcmpProfType_Object = MibTableColumn
tmnxSysResEcmpProfType = _TmnxSysResEcmpProfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 2, 1, 1, 3),
    _TmnxSysResEcmpProfType_Type()
)
tmnxSysResEcmpProfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysResEcmpProfType.setStatus("current")


class _TmnxSysResEcmpProfLinksPerGrp_Type(Unsigned32):
    """Custom type tmnxSysResEcmpProfLinksPerGrp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TmnxSysResEcmpProfLinksPerGrp_Type.__name__ = "Unsigned32"
_TmnxSysResEcmpProfLinksPerGrp_Object = MibTableColumn
tmnxSysResEcmpProfLinksPerGrp = _TmnxSysResEcmpProfLinksPerGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 2, 1, 1, 4),
    _TmnxSysResEcmpProfLinksPerGrp_Type()
)
tmnxSysResEcmpProfLinksPerGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysResEcmpProfLinksPerGrp.setStatus("current")


class _TmnxSysResEcmpProfNumGrps_Type(Unsigned32):
    """Custom type tmnxSysResEcmpProfNumGrps based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_TmnxSysResEcmpProfNumGrps_Type.__name__ = "Unsigned32"
_TmnxSysResEcmpProfNumGrps_Object = MibTableColumn
tmnxSysResEcmpProfNumGrps = _TmnxSysResEcmpProfNumGrps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 2, 1, 1, 5),
    _TmnxSysResEcmpProfNumGrps_Type()
)
tmnxSysResEcmpProfNumGrps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysResEcmpProfNumGrps.setStatus("current")
_TmnxSysResItCam_ObjectIdentity = ObjectIdentity
tmnxSysResItCam = _TmnxSysResItCam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 3)
)
_TmnxSysResItCamBank_ObjectIdentity = ObjectIdentity
tmnxSysResItCamBank = _TmnxSysResItCamBank_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 3, 1)
)


class _TmnxSysResItCamBankV6Multicast_Type(Unsigned32):
    """Custom type tmnxSysResItCamBankV6Multicast based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_TmnxSysResItCamBankV6Multicast_Type.__name__ = "Unsigned32"
_TmnxSysResItCamBankV6Multicast_Object = MibScalar
tmnxSysResItCamBankV6Multicast = _TmnxSysResItCamBankV6Multicast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 3, 1, 1),
    _TmnxSysResItCamBankV6Multicast_Type()
)
tmnxSysResItCamBankV6Multicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysResItCamBankV6Multicast.setStatus("current")
_TmnxSysFpCam_ObjectIdentity = ObjectIdentity
tmnxSysFpCam = _TmnxSysFpCam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 4)
)
_TmnxSysFpCamAllocation_ObjectIdentity = ObjectIdentity
tmnxSysFpCamAllocation = _TmnxSysFpCamAllocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 4, 1)
)


class _TmnxSysFpCamAllocAdmnV6Multicast_Type(Unsigned32):
    """Custom type tmnxSysFpCamAllocAdmnV6Multicast based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10240),
    )


_TmnxSysFpCamAllocAdmnV6Multicast_Type.__name__ = "Unsigned32"
_TmnxSysFpCamAllocAdmnV6Multicast_Object = MibScalar
tmnxSysFpCamAllocAdmnV6Multicast = _TmnxSysFpCamAllocAdmnV6Multicast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 4, 1, 1),
    _TmnxSysFpCamAllocAdmnV6Multicast_Type()
)
tmnxSysFpCamAllocAdmnV6Multicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpCamAllocAdmnV6Multicast.setStatus("current")


class _TmnxSysFpCamAllocOperV6Multicast_Type(Unsigned32):
    """Custom type tmnxSysFpCamAllocOperV6Multicast based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10240),
    )


_TmnxSysFpCamAllocOperV6Multicast_Type.__name__ = "Unsigned32"
_TmnxSysFpCamAllocOperV6Multicast_Object = MibScalar
tmnxSysFpCamAllocOperV6Multicast = _TmnxSysFpCamAllocOperV6Multicast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 4, 1, 2),
    _TmnxSysFpCamAllocOperV6Multicast_Type()
)
tmnxSysFpCamAllocOperV6Multicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpCamAllocOperV6Multicast.setStatus("current")
_TmnxSysFpResAlloc_ObjectIdentity = ObjectIdentity
tmnxSysFpResAlloc = _TmnxSysFpResAlloc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 5)
)
_TmnxSysFpResAllocation_ObjectIdentity = ObjectIdentity
tmnxSysFpResAllocation = _TmnxSysFpResAllocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 5, 1)
)


class _TmnxSysFpResAllocG8032Sap_Type(Unsigned32):
    """Custom type tmnxSysFpResAllocG8032Sap based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TmnxSysFpResAllocG8032Sap_Type.__name__ = "Unsigned32"
_TmnxSysFpResAllocG8032Sap_Object = MibScalar
tmnxSysFpResAllocG8032Sap = _TmnxSysFpResAllocG8032Sap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 5, 1, 1),
    _TmnxSysFpResAllocG8032Sap_Type()
)
tmnxSysFpResAllocG8032Sap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpResAllocG8032Sap.setStatus("deprecated")


class _TmnxSysFpResAllocOperG8032Sap_Type(Unsigned32):
    """Custom type tmnxSysFpResAllocOperG8032Sap based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TmnxSysFpResAllocOperG8032Sap_Type.__name__ = "Unsigned32"
_TmnxSysFpResAllocOperG8032Sap_Object = MibScalar
tmnxSysFpResAllocOperG8032Sap = _TmnxSysFpResAllocOperG8032Sap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 5, 1, 2),
    _TmnxSysFpResAllocOperG8032Sap_Type()
)
tmnxSysFpResAllocOperG8032Sap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpResAllocOperG8032Sap.setStatus("deprecated")


class _TmnxSysFpResAllocFilterIpv6_Type(Unsigned32):
    """Custom type tmnxSysFpResAllocFilterIpv6 based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(6, 6),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(10, 10),
    )


_TmnxSysFpResAllocFilterIpv6_Type.__name__ = "Unsigned32"
_TmnxSysFpResAllocFilterIpv6_Object = MibScalar
tmnxSysFpResAllocFilterIpv6 = _TmnxSysFpResAllocFilterIpv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 5, 1, 3),
    _TmnxSysFpResAllocFilterIpv6_Type()
)
tmnxSysFpResAllocFilterIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpResAllocFilterIpv6.setStatus("current")


class _TmnxSysFpResAllocOperFilterIpv6_Type(Unsigned32):
    """Custom type tmnxSysFpResAllocOperFilterIpv6 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(6, 6),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(10, 10),
    )


_TmnxSysFpResAllocOperFilterIpv6_Type.__name__ = "Unsigned32"
_TmnxSysFpResAllocOperFilterIpv6_Object = MibScalar
tmnxSysFpResAllocOperFilterIpv6 = _TmnxSysFpResAllocOperFilterIpv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 5, 1, 4),
    _TmnxSysFpResAllocOperFilterIpv6_Type()
)
tmnxSysFpResAllocOperFilterIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpResAllocOperFilterIpv6.setStatus("current")


class _TmnxSysFpResAllocFecSysWdUnpd_Type(Unsigned32):
    """Custom type tmnxSysFpResAllocFecSysWdUnpd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 8192),
    )


_TmnxSysFpResAllocFecSysWdUnpd_Type.__name__ = "Unsigned32"
_TmnxSysFpResAllocFecSysWdUnpd_Object = MibScalar
tmnxSysFpResAllocFecSysWdUnpd = _TmnxSysFpResAllocFecSysWdUnpd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 5, 1, 5),
    _TmnxSysFpResAllocFecSysWdUnpd_Type()
)
tmnxSysFpResAllocFecSysWdUnpd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpResAllocFecSysWdUnpd.setStatus("current")
_TmnxSysFpResAllocFecOprSysWdUnpd_Type = Unsigned32
_TmnxSysFpResAllocFecOprSysWdUnpd_Object = MibScalar
tmnxSysFpResAllocFecOprSysWdUnpd = _TmnxSysFpResAllocFecOprSysWdUnpd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 5, 1, 6),
    _TmnxSysFpResAllocFecOprSysWdUnpd_Type()
)
tmnxSysFpResAllocFecOprSysWdUnpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpResAllocFecOprSysWdUnpd.setStatus("current")


class _TmnxSysFpResAllocFecSysWdPd_Type(Unsigned32):
    """Custom type tmnxSysFpResAllocFecSysWdPd based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_TmnxSysFpResAllocFecSysWdPd_Type.__name__ = "Unsigned32"
_TmnxSysFpResAllocFecSysWdPd_Object = MibScalar
tmnxSysFpResAllocFecSysWdPd = _TmnxSysFpResAllocFecSysWdPd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 5, 1, 7),
    _TmnxSysFpResAllocFecSysWdPd_Type()
)
tmnxSysFpResAllocFecSysWdPd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpResAllocFecSysWdPd.setStatus("current")
_TmnxSysFpResAllocFecOprSysWdPd_Type = Unsigned32
_TmnxSysFpResAllocFecOprSysWdPd_Object = MibScalar
tmnxSysFpResAllocFecOprSysWdPd = _TmnxSysFpResAllocFecOprSysWdPd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 5, 1, 8),
    _TmnxSysFpResAllocFecOprSysWdPd_Type()
)
tmnxSysFpResAllocFecOprSysWdPd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpResAllocFecOprSysWdPd.setStatus("current")
_TmnxSysFpResAllocPoolTable_Object = MibTable
tmnxSysFpResAllocPoolTable = _TmnxSysFpResAllocPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 5, 2)
)
if mibBuilder.loadTexts:
    tmnxSysFpResAllocPoolTable.setStatus("current")
_TmnxSysFpResAllocPoolEntry_Object = MibTableRow
tmnxSysFpResAllocPoolEntry = _TmnxSysFpResAllocPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 5, 2, 1)
)
tmnxSysFpResAllocPoolEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysFpRAPoolId"),
)
if mibBuilder.loadTexts:
    tmnxSysFpResAllocPoolEntry.setStatus("current")


class _TmnxSysFpRAPoolId_Type(Unsigned32):
    """Custom type tmnxSysFpRAPoolId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TmnxSysFpRAPoolId_Type.__name__ = "Unsigned32"
_TmnxSysFpRAPoolId_Object = MibTableColumn
tmnxSysFpRAPoolId = _TmnxSysFpRAPoolId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 5, 2, 1, 1),
    _TmnxSysFpRAPoolId_Type()
)
tmnxSysFpRAPoolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysFpRAPoolId.setStatus("current")


class _TmnxSysFpRAPoolLgBndRsvMemCnt_Type(Unsigned32):
    """Custom type tmnxSysFpRAPoolLgBndRsvMemCnt based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(64, 64),
    )


_TmnxSysFpRAPoolLgBndRsvMemCnt_Type.__name__ = "Unsigned32"
_TmnxSysFpRAPoolLgBndRsvMemCnt_Object = MibTableColumn
tmnxSysFpRAPoolLgBndRsvMemCnt = _TmnxSysFpRAPoolLgBndRsvMemCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 5, 2, 1, 2),
    _TmnxSysFpRAPoolLgBndRsvMemCnt_Type()
)
tmnxSysFpRAPoolLgBndRsvMemCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpRAPoolLgBndRsvMemCnt.setStatus("current")
_TmnxSysFpRAPoolOprLgBndRsvMemCnt_Type = Unsigned32
_TmnxSysFpRAPoolOprLgBndRsvMemCnt_Object = MibTableColumn
tmnxSysFpRAPoolOprLgBndRsvMemCnt = _TmnxSysFpRAPoolOprLgBndRsvMemCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 27, 5, 2, 1, 3),
    _TmnxSysFpRAPoolOprLgBndRsvMemCnt_Type()
)
tmnxSysFpRAPoolOprLgBndRsvMemCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpRAPoolOprLgBndRsvMemCnt.setStatus("current")
_TmnxSysDhcp_ObjectIdentity = ObjectIdentity
tmnxSysDhcp = _TmnxSysDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 28)
)


class _TmnxSysDhcp6AdvNoaddrsGlobal_Type(Bits):
    """Custom type tmnxSysDhcp6AdvNoaddrsGlobal based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("esmProxy", 0),
          ("esmRelay", 1),
          ("relay", 2),
          ("server", 3))
    )

_TmnxSysDhcp6AdvNoaddrsGlobal_Type.__name__ = "Bits"
_TmnxSysDhcp6AdvNoaddrsGlobal_Object = MibScalar
tmnxSysDhcp6AdvNoaddrsGlobal = _TmnxSysDhcp6AdvNoaddrsGlobal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 28, 1),
    _TmnxSysDhcp6AdvNoaddrsGlobal_Type()
)
tmnxSysDhcp6AdvNoaddrsGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysDhcp6AdvNoaddrsGlobal.setStatus("current")
_TmnxSysVsdInfo_ObjectIdentity = ObjectIdentity
tmnxSysVsdInfo = _TmnxSysVsdInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 29)
)


class _TmnxSysVsdSystemId_Type(TNamedItemOrEmpty):
    """Custom type tmnxSysVsdSystemId based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxSysVsdSystemId_Type.__name__ = "TNamedItemOrEmpty"
_TmnxSysVsdSystemId_Object = MibScalar
tmnxSysVsdSystemId = _TmnxSysVsdSystemId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 29, 1),
    _TmnxSysVsdSystemId_Type()
)
tmnxSysVsdSystemId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysVsdSystemId.setStatus("current")
_TmnxSysVsdGwPubSubIsSubscrd_Type = TruthValue
_TmnxSysVsdGwPubSubIsSubscrd_Object = MibScalar
tmnxSysVsdGwPubSubIsSubscrd = _TmnxSysVsdGwPubSubIsSubscrd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 29, 2),
    _TmnxSysVsdGwPubSubIsSubscrd_Type()
)
tmnxSysVsdGwPubSubIsSubscrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysVsdGwPubSubIsSubscrd.setStatus("current")
_TmnxSysVsdGwPubSubNodeName_Type = DisplayString
_TmnxSysVsdGwPubSubNodeName_Object = MibScalar
tmnxSysVsdGwPubSubNodeName = _TmnxSysVsdGwPubSubNodeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 29, 3),
    _TmnxSysVsdGwPubSubNodeName_Type()
)
tmnxSysVsdGwPubSubNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysVsdGwPubSubNodeName.setStatus("current")
_TmnxSysVsdGwPubSubLstSubscrdTime_Type = TimeStamp
_TmnxSysVsdGwPubSubLstSubscrdTime_Object = MibScalar
tmnxSysVsdGwPubSubLstSubscrdTime = _TmnxSysVsdGwPubSubLstSubscrdTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 29, 4),
    _TmnxSysVsdGwPubSubLstSubscrdTime_Type()
)
tmnxSysVsdGwPubSubLstSubscrdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysVsdGwPubSubLstSubscrdTime.setStatus("current")
_TmnxSysVsdGwLastAuditTxTime_Type = TimeStamp
_TmnxSysVsdGwLastAuditTxTime_Object = MibScalar
tmnxSysVsdGwLastAuditTxTime = _TmnxSysVsdGwLastAuditTxTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 29, 5),
    _TmnxSysVsdGwLastAuditTxTime_Type()
)
tmnxSysVsdGwLastAuditTxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysVsdGwLastAuditTxTime.setStatus("current")
_TmnxSysLicense_ObjectIdentity = ObjectIdentity
tmnxSysLicense = _TmnxSysLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30)
)
_TmnxSysLicenseStatus_Type = TItemDescription
_TmnxSysLicenseStatus_Object = MibScalar
tmnxSysLicenseStatus = _TmnxSysLicenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 1),
    _TmnxSysLicenseStatus_Type()
)
tmnxSysLicenseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysLicenseStatus.setStatus("current")
_TmnxSysLicenseName_Type = TItemDescription
_TmnxSysLicenseName_Object = MibScalar
tmnxSysLicenseName = _TmnxSysLicenseName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 2),
    _TmnxSysLicenseName_Type()
)
tmnxSysLicenseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysLicenseName.setStatus("current")
_TmnxSysLicenseUuid_Type = TmnxUuid
_TmnxSysLicenseUuid_Object = MibScalar
tmnxSysLicenseUuid = _TmnxSysLicenseUuid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 3),
    _TmnxSysLicenseUuid_Type()
)
tmnxSysLicenseUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysLicenseUuid.setStatus("current")
_TmnxSysLicenseDescription_Type = TItemDescription
_TmnxSysLicenseDescription_Object = MibScalar
tmnxSysLicenseDescription = _TmnxSysLicenseDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 4),
    _TmnxSysLicenseDescription_Type()
)
tmnxSysLicenseDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysLicenseDescription.setStatus("current")
_TmnxSysLicenseProduct_Type = TItemDescription
_TmnxSysLicenseProduct_Object = MibScalar
tmnxSysLicenseProduct = _TmnxSysLicenseProduct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 5),
    _TmnxSysLicenseProduct_Type()
)
tmnxSysLicenseProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysLicenseProduct.setStatus("current")
_TmnxSysLicenseSwVersion_Type = TItemDescription
_TmnxSysLicenseSwVersion_Object = MibScalar
tmnxSysLicenseSwVersion = _TmnxSysLicenseSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 6),
    _TmnxSysLicenseSwVersion_Type()
)
tmnxSysLicenseSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysLicenseSwVersion.setStatus("current")
_TmnxSysLicenseIssueDateAndTime_Type = DateAndTime
_TmnxSysLicenseIssueDateAndTime_Object = MibScalar
tmnxSysLicenseIssueDateAndTime = _TmnxSysLicenseIssueDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 7),
    _TmnxSysLicenseIssueDateAndTime_Type()
)
tmnxSysLicenseIssueDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysLicenseIssueDateAndTime.setStatus("current")
_TmnxSysLicenseStartDateAndTime_Type = DateAndTime
_TmnxSysLicenseStartDateAndTime_Object = MibScalar
tmnxSysLicenseStartDateAndTime = _TmnxSysLicenseStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 8),
    _TmnxSysLicenseStartDateAndTime_Type()
)
tmnxSysLicenseStartDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysLicenseStartDateAndTime.setStatus("current")
_TmnxSysLicenseEndDateAndTime_Type = DateAndTime
_TmnxSysLicenseEndDateAndTime_Object = MibScalar
tmnxSysLicenseEndDateAndTime = _TmnxSysLicenseEndDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 9),
    _TmnxSysLicenseEndDateAndTime_Type()
)
tmnxSysLicenseEndDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysLicenseEndDateAndTime.setStatus("current")
_TmnxSysLicenseVChassisType_Type = TNamedItemOrEmpty
_TmnxSysLicenseVChassisType_Object = MibScalar
tmnxSysLicenseVChassisType = _TmnxSysLicenseVChassisType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 10),
    _TmnxSysLicenseVChassisType_Type()
)
tmnxSysLicenseVChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysLicenseVChassisType.setStatus("current")
_TmnxSysLicenseMaxNumCPMs_Type = Unsigned32
_TmnxSysLicenseMaxNumCPMs_Object = MibScalar
tmnxSysLicenseMaxNumCPMs = _TmnxSysLicenseMaxNumCPMs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 11),
    _TmnxSysLicenseMaxNumCPMs_Type()
)
tmnxSysLicenseMaxNumCPMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysLicenseMaxNumCPMs.setStatus("current")
_TmnxSysLicenseMaxNumIOMs_Type = Unsigned32
_TmnxSysLicenseMaxNumIOMs_Object = MibScalar
tmnxSysLicenseMaxNumIOMs = _TmnxSysLicenseMaxNumIOMs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 12),
    _TmnxSysLicenseMaxNumIOMs_Type()
)
tmnxSysLicenseMaxNumIOMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysLicenseMaxNumIOMs.setStatus("current")
_TmnxSysCpmCardLicenseTable_Object = MibTable
tmnxSysCpmCardLicenseTable = _TmnxSysCpmCardLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 13)
)
if mibBuilder.loadTexts:
    tmnxSysCpmCardLicenseTable.setStatus("current")
_TmnxSysCpmCardLicenseEntry_Object = MibTableRow
tmnxSysCpmCardLicenseEntry = _TmnxSysCpmCardLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 13, 1)
)
tmnxSysCpmCardLicenseEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCpmCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCpmCardNum"),
)
if mibBuilder.loadTexts:
    tmnxSysCpmCardLicenseEntry.setStatus("current")
_TmnxSysCpmCardLicStatus_Type = TItemDescription
_TmnxSysCpmCardLicStatus_Object = MibTableColumn
tmnxSysCpmCardLicStatus = _TmnxSysCpmCardLicStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 13, 1, 1),
    _TmnxSysCpmCardLicStatus_Type()
)
tmnxSysCpmCardLicStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCpmCardLicStatus.setStatus("current")
_TmnxSysCpmCardLicName_Type = TItemDescription
_TmnxSysCpmCardLicName_Object = MibTableColumn
tmnxSysCpmCardLicName = _TmnxSysCpmCardLicName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 13, 1, 2),
    _TmnxSysCpmCardLicName_Type()
)
tmnxSysCpmCardLicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCpmCardLicName.setStatus("current")
_TmnxSysCpmCardLicUuid_Type = TmnxUuid
_TmnxSysCpmCardLicUuid_Object = MibTableColumn
tmnxSysCpmCardLicUuid = _TmnxSysCpmCardLicUuid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 13, 1, 3),
    _TmnxSysCpmCardLicUuid_Type()
)
tmnxSysCpmCardLicUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCpmCardLicUuid.setStatus("current")
_TmnxSysCpmCardLicDescription_Type = TItemDescription
_TmnxSysCpmCardLicDescription_Object = MibTableColumn
tmnxSysCpmCardLicDescription = _TmnxSysCpmCardLicDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 13, 1, 4),
    _TmnxSysCpmCardLicDescription_Type()
)
tmnxSysCpmCardLicDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCpmCardLicDescription.setStatus("current")
_TmnxSysCpmCardLicProduct_Type = TItemDescription
_TmnxSysCpmCardLicProduct_Object = MibTableColumn
tmnxSysCpmCardLicProduct = _TmnxSysCpmCardLicProduct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 13, 1, 5),
    _TmnxSysCpmCardLicProduct_Type()
)
tmnxSysCpmCardLicProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCpmCardLicProduct.setStatus("current")
_TmnxSysCpmCardLicSwVersion_Type = TItemDescription
_TmnxSysCpmCardLicSwVersion_Object = MibTableColumn
tmnxSysCpmCardLicSwVersion = _TmnxSysCpmCardLicSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 13, 1, 6),
    _TmnxSysCpmCardLicSwVersion_Type()
)
tmnxSysCpmCardLicSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCpmCardLicSwVersion.setStatus("current")
_TmnxSysCpmCardLicIssueDateTime_Type = DateAndTime
_TmnxSysCpmCardLicIssueDateTime_Object = MibTableColumn
tmnxSysCpmCardLicIssueDateTime = _TmnxSysCpmCardLicIssueDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 13, 1, 7),
    _TmnxSysCpmCardLicIssueDateTime_Type()
)
tmnxSysCpmCardLicIssueDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCpmCardLicIssueDateTime.setStatus("current")
_TmnxSysCpmCardLicStartDateTime_Type = DateAndTime
_TmnxSysCpmCardLicStartDateTime_Object = MibTableColumn
tmnxSysCpmCardLicStartDateTime = _TmnxSysCpmCardLicStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 13, 1, 8),
    _TmnxSysCpmCardLicStartDateTime_Type()
)
tmnxSysCpmCardLicStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCpmCardLicStartDateTime.setStatus("current")
_TmnxSysCpmCardLicEndDateTime_Type = DateAndTime
_TmnxSysCpmCardLicEndDateTime_Object = MibTableColumn
tmnxSysCpmCardLicEndDateTime = _TmnxSysCpmCardLicEndDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 13, 1, 9),
    _TmnxSysCpmCardLicEndDateTime_Type()
)
tmnxSysCpmCardLicEndDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCpmCardLicEndDateTime.setStatus("current")
_TmnxSysCpmCardLicVChassisType_Type = TNamedItemOrEmpty
_TmnxSysCpmCardLicVChassisType_Object = MibTableColumn
tmnxSysCpmCardLicVChassisType = _TmnxSysCpmCardLicVChassisType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 13, 1, 10),
    _TmnxSysCpmCardLicVChassisType_Type()
)
tmnxSysCpmCardLicVChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCpmCardLicVChassisType.setStatus("current")
_TmnxSysCpmCardLicMaxNumCPMs_Type = Unsigned32
_TmnxSysCpmCardLicMaxNumCPMs_Object = MibTableColumn
tmnxSysCpmCardLicMaxNumCPMs = _TmnxSysCpmCardLicMaxNumCPMs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 13, 1, 11),
    _TmnxSysCpmCardLicMaxNumCPMs_Type()
)
tmnxSysCpmCardLicMaxNumCPMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCpmCardLicMaxNumCPMs.setStatus("current")
_TmnxSysCpmCardLicMaxNumIOMs_Type = Unsigned32
_TmnxSysCpmCardLicMaxNumIOMs_Object = MibTableColumn
tmnxSysCpmCardLicMaxNumIOMs = _TmnxSysCpmCardLicMaxNumIOMs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 13, 1, 12),
    _TmnxSysCpmCardLicMaxNumIOMs_Type()
)
tmnxSysCpmCardLicMaxNumIOMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCpmCardLicMaxNumIOMs.setStatus("current")
_TmnxSysCpmCardLicFeatureTable_Object = MibTable
tmnxSysCpmCardLicFeatureTable = _TmnxSysCpmCardLicFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 14)
)
if mibBuilder.loadTexts:
    tmnxSysCpmCardLicFeatureTable.setStatus("current")
_TmnxSysCpmCardLicFeatureEntry_Object = MibTableRow
tmnxSysCpmCardLicFeatureEntry = _TmnxSysCpmCardLicFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 14, 1)
)
tmnxSysCpmCardLicFeatureEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCpmCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCpmCardNum"),
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysCpmCardLicFeatApplication"),
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysCpmCardLicFeatNumber"),
)
if mibBuilder.loadTexts:
    tmnxSysCpmCardLicFeatureEntry.setStatus("current")
_TmnxSysCpmCardLicFeatApplication_Type = TNamedItem
_TmnxSysCpmCardLicFeatApplication_Object = MibTableColumn
tmnxSysCpmCardLicFeatApplication = _TmnxSysCpmCardLicFeatApplication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 14, 1, 1),
    _TmnxSysCpmCardLicFeatApplication_Type()
)
tmnxSysCpmCardLicFeatApplication.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysCpmCardLicFeatApplication.setStatus("current")


class _TmnxSysCpmCardLicFeatNumber_Type(Unsigned32):
    """Custom type tmnxSysCpmCardLicFeatNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxSysCpmCardLicFeatNumber_Type.__name__ = "Unsigned32"
_TmnxSysCpmCardLicFeatNumber_Object = MibTableColumn
tmnxSysCpmCardLicFeatNumber = _TmnxSysCpmCardLicFeatNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 14, 1, 2),
    _TmnxSysCpmCardLicFeatNumber_Type()
)
tmnxSysCpmCardLicFeatNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysCpmCardLicFeatNumber.setStatus("current")
_TmnxSysCpmCardLicFeatDescription_Type = TItemDescription
_TmnxSysCpmCardLicFeatDescription_Object = MibTableColumn
tmnxSysCpmCardLicFeatDescription = _TmnxSysCpmCardLicFeatDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 14, 1, 3),
    _TmnxSysCpmCardLicFeatDescription_Type()
)
tmnxSysCpmCardLicFeatDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysCpmCardLicFeatDescription.setStatus("current")
_TmnxSysLicensingTable_Object = MibTable
tmnxSysLicensingTable = _TmnxSysLicensingTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 16)
)
if mibBuilder.loadTexts:
    tmnxSysLicensingTable.setStatus("current")
_TmnxSysLicensingEntry_Object = MibTableRow
tmnxSysLicensingEntry = _TmnxSysLicensingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 16, 1)
)
tmnxSysLicensingEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysLicensingGroup"),
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysLicensedAppName"),
)
if mibBuilder.loadTexts:
    tmnxSysLicensingEntry.setStatus("current")
_TmnxSysLicensingGroup_Type = TmnxSysLicensingGroup
_TmnxSysLicensingGroup_Object = MibTableColumn
tmnxSysLicensingGroup = _TmnxSysLicensingGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 16, 1, 1),
    _TmnxSysLicensingGroup_Type()
)
tmnxSysLicensingGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysLicensingGroup.setStatus("current")
_TmnxSysLicensedAppName_Type = TNamedItem
_TmnxSysLicensedAppName_Object = MibTableColumn
tmnxSysLicensedAppName = _TmnxSysLicensedAppName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 16, 1, 2),
    _TmnxSysLicensedAppName_Type()
)
tmnxSysLicensedAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysLicensedAppName.setStatus("current")


class _TmnxSysAppLicenseDescription_Type(DisplayString):
    """Custom type tmnxSysAppLicenseDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxSysAppLicenseDescription_Type.__name__ = "DisplayString"
_TmnxSysAppLicenseDescription_Object = MibTableColumn
tmnxSysAppLicenseDescription = _TmnxSysAppLicenseDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 16, 1, 3),
    _TmnxSysAppLicenseDescription_Type()
)
tmnxSysAppLicenseDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAppLicenseDescription.setStatus("current")


class _TmnxSysAppLicenseType_Type(Integer32):
    """Custom type tmnxSysAppLicenseType based on Integer32"""
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
        *(("unknown", 0),
          ("pool", 1),
          ("rtu", 2),
          ("monitored", 3))
    )


_TmnxSysAppLicenseType_Type.__name__ = "Integer32"
_TmnxSysAppLicenseType_Object = MibTableColumn
tmnxSysAppLicenseType = _TmnxSysAppLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 16, 1, 4),
    _TmnxSysAppLicenseType_Type()
)
tmnxSysAppLicenseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAppLicenseType.setStatus("current")
_TmnxSysAppLicensePoolSize_Type = Integer32
_TmnxSysAppLicensePoolSize_Object = MibTableColumn
tmnxSysAppLicensePoolSize = _TmnxSysAppLicensePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 16, 1, 5),
    _TmnxSysAppLicensePoolSize_Type()
)
tmnxSysAppLicensePoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAppLicensePoolSize.setStatus("current")
_TmnxSysAppLicenseAllocated_Type = Unsigned32
_TmnxSysAppLicenseAllocated_Object = MibTableColumn
tmnxSysAppLicenseAllocated = _TmnxSysAppLicenseAllocated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 16, 1, 6),
    _TmnxSysAppLicenseAllocated_Type()
)
tmnxSysAppLicenseAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAppLicenseAllocated.setStatus("current")
_TmnxSysAppLicensePresent_Type = TruthValue
_TmnxSysAppLicensePresent_Object = MibTableColumn
tmnxSysAppLicensePresent = _TmnxSysAppLicensePresent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 16, 1, 7),
    _TmnxSysAppLicensePresent_Type()
)
tmnxSysAppLicensePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAppLicensePresent.setStatus("current")


class _TmnxSysAppLicenseState_Type(Integer32):
    """Custom type tmnxSysAppLicenseState based on Integer32"""
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
        *(("unknown", 0),
          ("valid", 1),
          ("error", 2),
          ("violation", 3))
    )


_TmnxSysAppLicenseState_Type.__name__ = "Integer32"
_TmnxSysAppLicenseState_Object = MibTableColumn
tmnxSysAppLicenseState = _TmnxSysAppLicenseState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 16, 1, 8),
    _TmnxSysAppLicenseState_Type()
)
tmnxSysAppLicenseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAppLicenseState.setStatus("current")
_TmnxSysAppLicense24HrDateTime_Type = DateAndTime
_TmnxSysAppLicense24HrDateTime_Object = MibTableColumn
tmnxSysAppLicense24HrDateTime = _TmnxSysAppLicense24HrDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 16, 1, 9),
    _TmnxSysAppLicense24HrDateTime_Type()
)
tmnxSysAppLicense24HrDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAppLicense24HrDateTime.setStatus("current")
_TmnxSysAppLicense24HrMax_Type = Unsigned32
_TmnxSysAppLicense24HrMax_Object = MibTableColumn
tmnxSysAppLicense24HrMax = _TmnxSysAppLicense24HrMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 16, 1, 10),
    _TmnxSysAppLicense24HrMax_Type()
)
tmnxSysAppLicense24HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAppLicense24HrMax.setStatus("current")
_TmnxSysAppLicenseCurrentMax_Type = Unsigned32
_TmnxSysAppLicenseCurrentMax_Object = MibTableColumn
tmnxSysAppLicenseCurrentMax = _TmnxSysAppLicenseCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 16, 1, 11),
    _TmnxSysAppLicenseCurrentMax_Type()
)
tmnxSysAppLicenseCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAppLicenseCurrentMax.setStatus("current")
_TmnxSysAvailableLicensesTable_Object = MibTable
tmnxSysAvailableLicensesTable = _TmnxSysAvailableLicensesTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 17)
)
if mibBuilder.loadTexts:
    tmnxSysAvailableLicensesTable.setStatus("current")
_TmnxSysAvailableLicensesEntry_Object = MibTableRow
tmnxSysAvailableLicensesEntry = _TmnxSysAvailableLicensesEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 17, 1)
)
tmnxSysAvailableLicensesEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysAvailLicenseIndex"),
)
if mibBuilder.loadTexts:
    tmnxSysAvailableLicensesEntry.setStatus("current")
_TmnxSysAvailLicenseIndex_Type = Unsigned32
_TmnxSysAvailLicenseIndex_Object = MibTableColumn
tmnxSysAvailLicenseIndex = _TmnxSysAvailLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 17, 1, 1),
    _TmnxSysAvailLicenseIndex_Type()
)
tmnxSysAvailLicenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysAvailLicenseIndex.setStatus("current")
_TmnxSysAvailLicenseName_Type = TItemDescription
_TmnxSysAvailLicenseName_Object = MibTableColumn
tmnxSysAvailLicenseName = _TmnxSysAvailLicenseName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 17, 1, 2),
    _TmnxSysAvailLicenseName_Type()
)
tmnxSysAvailLicenseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAvailLicenseName.setStatus("current")
_TmnxSysAvailLicenseUuid_Type = TmnxUuid
_TmnxSysAvailLicenseUuid_Object = MibTableColumn
tmnxSysAvailLicenseUuid = _TmnxSysAvailLicenseUuid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 17, 1, 3),
    _TmnxSysAvailLicenseUuid_Type()
)
tmnxSysAvailLicenseUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAvailLicenseUuid.setStatus("current")
_TmnxSysAvailLicenseDescription_Type = TItemDescription
_TmnxSysAvailLicenseDescription_Object = MibTableColumn
tmnxSysAvailLicenseDescription = _TmnxSysAvailLicenseDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 17, 1, 4),
    _TmnxSysAvailLicenseDescription_Type()
)
tmnxSysAvailLicenseDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAvailLicenseDescription.setStatus("current")
_TmnxSysAvailLicenseSwVersion_Type = TItemDescription
_TmnxSysAvailLicenseSwVersion_Object = MibTableColumn
tmnxSysAvailLicenseSwVersion = _TmnxSysAvailLicenseSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 17, 1, 5),
    _TmnxSysAvailLicenseSwVersion_Type()
)
tmnxSysAvailLicenseSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAvailLicenseSwVersion.setStatus("current")
_TmnxSysAvailLicIssueDateTime_Type = DateAndTime
_TmnxSysAvailLicIssueDateTime_Object = MibTableColumn
tmnxSysAvailLicIssueDateTime = _TmnxSysAvailLicIssueDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 17, 1, 6),
    _TmnxSysAvailLicIssueDateTime_Type()
)
tmnxSysAvailLicIssueDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAvailLicIssueDateTime.setStatus("current")
_TmnxSysAvailLicStartDateTime_Type = DateAndTime
_TmnxSysAvailLicStartDateTime_Object = MibTableColumn
tmnxSysAvailLicStartDateTime = _TmnxSysAvailLicStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 17, 1, 7),
    _TmnxSysAvailLicStartDateTime_Type()
)
tmnxSysAvailLicStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAvailLicStartDateTime.setStatus("current")
_TmnxSysAvailLicEndDateTime_Type = DateAndTime
_TmnxSysAvailLicEndDateTime_Object = MibTableColumn
tmnxSysAvailLicEndDateTime = _TmnxSysAvailLicEndDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 17, 1, 8),
    _TmnxSysAvailLicEndDateTime_Type()
)
tmnxSysAvailLicEndDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAvailLicEndDateTime.setStatus("current")
_TmnxSysAvailLicenseProduct_Type = TItemDescription
_TmnxSysAvailLicenseProduct_Object = MibTableColumn
tmnxSysAvailLicenseProduct = _TmnxSysAvailLicenseProduct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 17, 1, 9),
    _TmnxSysAvailLicenseProduct_Type()
)
tmnxSysAvailLicenseProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAvailLicenseProduct.setStatus("current")


class _TmnxSysLicensingState_Type(Integer32):
    """Custom type tmnxSysLicensingState based on Integer32"""
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
        *(("unlicensed", 0),
          ("licensed", 1),
          ("invalid-license", 2),
          ("expired-license", 3))
    )


_TmnxSysLicensingState_Type.__name__ = "Integer32"
_TmnxSysLicensingState_Object = MibScalar
tmnxSysLicensingState = _TmnxSysLicensingState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 18),
    _TmnxSysLicensingState_Type()
)
tmnxSysLicensingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysLicensingState.setStatus("current")
_TmnxSysLicensingRebootPending_Type = TruthValue
_TmnxSysLicensingRebootPending_Object = MibScalar
tmnxSysLicensingRebootPending = _TmnxSysLicensingRebootPending_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 19),
    _TmnxSysLicensingRebootPending_Type()
)
tmnxSysLicensingRebootPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysLicensingRebootPending.setStatus("current")
_TmnxSysLicenseStatistics_ObjectIdentity = ObjectIdentity
tmnxSysLicenseStatistics = _TmnxSysLicenseStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20)
)
_TmnxSysAppStats24HrsTable_Object = MibTable
tmnxSysAppStats24HrsTable = _TmnxSysAppStats24HrsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 1)
)
if mibBuilder.loadTexts:
    tmnxSysAppStats24HrsTable.setStatus("current")
_TmnxSysAppStats24HrsEntry_Object = MibTableRow
tmnxSysAppStats24HrsEntry = _TmnxSysAppStats24HrsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 1, 1)
)
tmnxSysAppStats24HrsEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysAppStats24HrsApplication"),
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysAppStats24HrsType"),
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysAppStats24HrsIndex"),
)
if mibBuilder.loadTexts:
    tmnxSysAppStats24HrsEntry.setStatus("current")
_TmnxSysAppStats24HrsApplication_Type = TmnxSysLicenseApplication
_TmnxSysAppStats24HrsApplication_Object = MibTableColumn
tmnxSysAppStats24HrsApplication = _TmnxSysAppStats24HrsApplication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 1, 1, 1),
    _TmnxSysAppStats24HrsApplication_Type()
)
tmnxSysAppStats24HrsApplication.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysAppStats24HrsApplication.setStatus("current")
_TmnxSysAppStats24HrsType_Type = TmnxSysLicenseAppStatsType
_TmnxSysAppStats24HrsType_Object = MibTableColumn
tmnxSysAppStats24HrsType = _TmnxSysAppStats24HrsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 1, 1, 2),
    _TmnxSysAppStats24HrsType_Type()
)
tmnxSysAppStats24HrsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysAppStats24HrsType.setStatus("current")
_TmnxSysAppStats24HrsIndex_Type = Unsigned32
_TmnxSysAppStats24HrsIndex_Object = MibTableColumn
tmnxSysAppStats24HrsIndex = _TmnxSysAppStats24HrsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 1, 1, 3),
    _TmnxSysAppStats24HrsIndex_Type()
)
tmnxSysAppStats24HrsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysAppStats24HrsIndex.setStatus("current")


class _TmnxSysAppStats24HrsName_Type(DisplayString):
    """Custom type tmnxSysAppStats24HrsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxSysAppStats24HrsName_Type.__name__ = "DisplayString"
_TmnxSysAppStats24HrsName_Object = MibTableColumn
tmnxSysAppStats24HrsName = _TmnxSysAppStats24HrsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 1, 1, 4),
    _TmnxSysAppStats24HrsName_Type()
)
tmnxSysAppStats24HrsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAppStats24HrsName.setStatus("current")
_TmnxSysAppStats24HrsValue_Type = CounterBasedGauge64
_TmnxSysAppStats24HrsValue_Object = MibTableColumn
tmnxSysAppStats24HrsValue = _TmnxSysAppStats24HrsValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 1, 1, 5),
    _TmnxSysAppStats24HrsValue_Type()
)
tmnxSysAppStats24HrsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAppStats24HrsValue.setStatus("current")


class _TmnxSysAppStats24HrsTime_Type(DateAndTime):
    """Custom type tmnxSysAppStats24HrsTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxSysAppStats24HrsTime_Type.__name__ = "DateAndTime"
_TmnxSysAppStats24HrsTime_Object = MibTableColumn
tmnxSysAppStats24HrsTime = _TmnxSysAppStats24HrsTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 1, 1, 6),
    _TmnxSysAppStats24HrsTime_Type()
)
tmnxSysAppStats24HrsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAppStats24HrsTime.setStatus("current")
_TmnxSysAppStatsWeekTable_Object = MibTable
tmnxSysAppStatsWeekTable = _TmnxSysAppStatsWeekTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 2)
)
if mibBuilder.loadTexts:
    tmnxSysAppStatsWeekTable.setStatus("current")
_TmnxSysAppStatsWeekEntry_Object = MibTableRow
tmnxSysAppStatsWeekEntry = _TmnxSysAppStatsWeekEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 2, 1)
)
tmnxSysAppStatsWeekEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysAppStatsWeekApplication"),
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysAppStatsWeekType"),
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysAppStatsWeekIndex"),
)
if mibBuilder.loadTexts:
    tmnxSysAppStatsWeekEntry.setStatus("current")
_TmnxSysAppStatsWeekApplication_Type = TmnxSysLicenseApplication
_TmnxSysAppStatsWeekApplication_Object = MibTableColumn
tmnxSysAppStatsWeekApplication = _TmnxSysAppStatsWeekApplication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 2, 1, 1),
    _TmnxSysAppStatsWeekApplication_Type()
)
tmnxSysAppStatsWeekApplication.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysAppStatsWeekApplication.setStatus("current")
_TmnxSysAppStatsWeekType_Type = TmnxSysLicenseAppStatsType
_TmnxSysAppStatsWeekType_Object = MibTableColumn
tmnxSysAppStatsWeekType = _TmnxSysAppStatsWeekType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 2, 1, 2),
    _TmnxSysAppStatsWeekType_Type()
)
tmnxSysAppStatsWeekType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysAppStatsWeekType.setStatus("current")
_TmnxSysAppStatsWeekIndex_Type = Unsigned32
_TmnxSysAppStatsWeekIndex_Object = MibTableColumn
tmnxSysAppStatsWeekIndex = _TmnxSysAppStatsWeekIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 2, 1, 3),
    _TmnxSysAppStatsWeekIndex_Type()
)
tmnxSysAppStatsWeekIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysAppStatsWeekIndex.setStatus("current")


class _TmnxSysAppStatsWeekName_Type(DisplayString):
    """Custom type tmnxSysAppStatsWeekName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxSysAppStatsWeekName_Type.__name__ = "DisplayString"
_TmnxSysAppStatsWeekName_Object = MibTableColumn
tmnxSysAppStatsWeekName = _TmnxSysAppStatsWeekName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 2, 1, 4),
    _TmnxSysAppStatsWeekName_Type()
)
tmnxSysAppStatsWeekName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAppStatsWeekName.setStatus("current")
_TmnxSysAppStatsWeekAverage_Type = CounterBasedGauge64
_TmnxSysAppStatsWeekAverage_Object = MibTableColumn
tmnxSysAppStatsWeekAverage = _TmnxSysAppStatsWeekAverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 2, 1, 5),
    _TmnxSysAppStatsWeekAverage_Type()
)
tmnxSysAppStatsWeekAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAppStatsWeekAverage.setStatus("current")
_TmnxSysAppStatsWeekPeak_Type = CounterBasedGauge64
_TmnxSysAppStatsWeekPeak_Object = MibTableColumn
tmnxSysAppStatsWeekPeak = _TmnxSysAppStatsWeekPeak_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 2, 1, 6),
    _TmnxSysAppStatsWeekPeak_Type()
)
tmnxSysAppStatsWeekPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAppStatsWeekPeak.setStatus("current")


class _TmnxSysAppStatsWeekTime_Type(DateAndTime):
    """Custom type tmnxSysAppStatsWeekTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxSysAppStatsWeekTime_Type.__name__ = "DateAndTime"
_TmnxSysAppStatsWeekTime_Object = MibTableColumn
tmnxSysAppStatsWeekTime = _TmnxSysAppStatsWeekTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 2, 1, 7),
    _TmnxSysAppStatsWeekTime_Type()
)
tmnxSysAppStatsWeekTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAppStatsWeekTime.setStatus("current")
_TmnxSysAppStatsPeakTable_Object = MibTable
tmnxSysAppStatsPeakTable = _TmnxSysAppStatsPeakTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 3)
)
if mibBuilder.loadTexts:
    tmnxSysAppStatsPeakTable.setStatus("current")
_TmnxSysAppStatsPeakEntry_Object = MibTableRow
tmnxSysAppStatsPeakEntry = _TmnxSysAppStatsPeakEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 3, 1)
)
tmnxSysAppStatsPeakEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysAppStatsPeakApplication"),
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysAppStatsPeakType"),
)
if mibBuilder.loadTexts:
    tmnxSysAppStatsPeakEntry.setStatus("current")
_TmnxSysAppStatsPeakApplication_Type = TmnxSysLicenseApplication
_TmnxSysAppStatsPeakApplication_Object = MibTableColumn
tmnxSysAppStatsPeakApplication = _TmnxSysAppStatsPeakApplication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 3, 1, 1),
    _TmnxSysAppStatsPeakApplication_Type()
)
tmnxSysAppStatsPeakApplication.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysAppStatsPeakApplication.setStatus("current")
_TmnxSysAppStatsPeakType_Type = TmnxSysLicenseAppStatsType
_TmnxSysAppStatsPeakType_Object = MibTableColumn
tmnxSysAppStatsPeakType = _TmnxSysAppStatsPeakType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 3, 1, 2),
    _TmnxSysAppStatsPeakType_Type()
)
tmnxSysAppStatsPeakType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysAppStatsPeakType.setStatus("current")


class _TmnxSysAppStatsPeakName_Type(DisplayString):
    """Custom type tmnxSysAppStatsPeakName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxSysAppStatsPeakName_Type.__name__ = "DisplayString"
_TmnxSysAppStatsPeakName_Object = MibTableColumn
tmnxSysAppStatsPeakName = _TmnxSysAppStatsPeakName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 3, 1, 3),
    _TmnxSysAppStatsPeakName_Type()
)
tmnxSysAppStatsPeakName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAppStatsPeakName.setStatus("current")
_TmnxSysAppStatsPeakValue_Type = CounterBasedGauge64
_TmnxSysAppStatsPeakValue_Object = MibTableColumn
tmnxSysAppStatsPeakValue = _TmnxSysAppStatsPeakValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 3, 1, 4),
    _TmnxSysAppStatsPeakValue_Type()
)
tmnxSysAppStatsPeakValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAppStatsPeakValue.setStatus("current")


class _TmnxSysAppStatsPeakTime_Type(DateAndTime):
    """Custom type tmnxSysAppStatsPeakTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxSysAppStatsPeakTime_Type.__name__ = "DateAndTime"
_TmnxSysAppStatsPeakTime_Object = MibTableColumn
tmnxSysAppStatsPeakTime = _TmnxSysAppStatsPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 3, 1, 5),
    _TmnxSysAppStatsPeakTime_Type()
)
tmnxSysAppStatsPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAppStatsPeakTime.setStatus("current")
_TmnxSysAppStats48HrsTable_Object = MibTable
tmnxSysAppStats48HrsTable = _TmnxSysAppStats48HrsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 4)
)
if mibBuilder.loadTexts:
    tmnxSysAppStats48HrsTable.setStatus("current")
_TmnxSysAppStats48HrsEntry_Object = MibTableRow
tmnxSysAppStats48HrsEntry = _TmnxSysAppStats48HrsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 4, 1)
)
tmnxSysAppStats48HrsEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysAppStats48HrsApplication"),
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysAppStats48HrsType"),
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysAppStats48HrsIndex"),
)
if mibBuilder.loadTexts:
    tmnxSysAppStats48HrsEntry.setStatus("current")
_TmnxSysAppStats48HrsApplication_Type = TmnxSysLicenseApplication
_TmnxSysAppStats48HrsApplication_Object = MibTableColumn
tmnxSysAppStats48HrsApplication = _TmnxSysAppStats48HrsApplication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 4, 1, 1),
    _TmnxSysAppStats48HrsApplication_Type()
)
tmnxSysAppStats48HrsApplication.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysAppStats48HrsApplication.setStatus("current")
_TmnxSysAppStats48HrsType_Type = TmnxSysLicenseAppStatsType
_TmnxSysAppStats48HrsType_Object = MibTableColumn
tmnxSysAppStats48HrsType = _TmnxSysAppStats48HrsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 4, 1, 2),
    _TmnxSysAppStats48HrsType_Type()
)
tmnxSysAppStats48HrsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysAppStats48HrsType.setStatus("current")
_TmnxSysAppStats48HrsIndex_Type = Unsigned32
_TmnxSysAppStats48HrsIndex_Object = MibTableColumn
tmnxSysAppStats48HrsIndex = _TmnxSysAppStats48HrsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 4, 1, 3),
    _TmnxSysAppStats48HrsIndex_Type()
)
tmnxSysAppStats48HrsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysAppStats48HrsIndex.setStatus("current")


class _TmnxSysAppStats48HrsName_Type(DisplayString):
    """Custom type tmnxSysAppStats48HrsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxSysAppStats48HrsName_Type.__name__ = "DisplayString"
_TmnxSysAppStats48HrsName_Object = MibTableColumn
tmnxSysAppStats48HrsName = _TmnxSysAppStats48HrsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 4, 1, 4),
    _TmnxSysAppStats48HrsName_Type()
)
tmnxSysAppStats48HrsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAppStats48HrsName.setStatus("current")
_TmnxSysAppStats48HrsValue_Type = CounterBasedGauge64
_TmnxSysAppStats48HrsValue_Object = MibTableColumn
tmnxSysAppStats48HrsValue = _TmnxSysAppStats48HrsValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 4, 1, 5),
    _TmnxSysAppStats48HrsValue_Type()
)
tmnxSysAppStats48HrsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAppStats48HrsValue.setStatus("current")


class _TmnxSysAppStats48HrsTime_Type(DateAndTime):
    """Custom type tmnxSysAppStats48HrsTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxSysAppStats48HrsTime_Type.__name__ = "DateAndTime"
_TmnxSysAppStats48HrsTime_Object = MibTableColumn
tmnxSysAppStats48HrsTime = _TmnxSysAppStats48HrsTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 20, 4, 1, 6),
    _TmnxSysAppStats48HrsTime_Type()
)
tmnxSysAppStats48HrsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysAppStats48HrsTime.setStatus("current")
_TmnxSysLicensingProduct_Type = TItemDescription
_TmnxSysLicensingProduct_Object = MibScalar
tmnxSysLicensingProduct = _TmnxSysLicensingProduct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 21),
    _TmnxSysLicensingProduct_Type()
)
tmnxSysLicensingProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysLicensingProduct.setStatus("current")
_TmnxSysLicensingUuid_Type = TmnxUuid
_TmnxSysLicensingUuid_Object = MibScalar
tmnxSysLicensingUuid = _TmnxSysLicensingUuid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 30, 22),
    _TmnxSysLicensingUuid_Type()
)
tmnxSysLicensingUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysLicensingUuid.setStatus("current")
_TmnxSysFibInfo_ObjectIdentity = ObjectIdentity
tmnxSysFibInfo = _TmnxSysFibInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 31)
)


class _TmnxSysFibSelective_Type(TruthValue):
    """Custom type tmnxSysFibSelective based on TruthValue"""
    defaultValue = 2


_TmnxSysFibSelective_Type.__name__ = "TruthValue"
_TmnxSysFibSelective_Object = MibScalar
tmnxSysFibSelective = _TmnxSysFibSelective_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 31, 1),
    _TmnxSysFibSelective_Type()
)
tmnxSysFibSelective.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFibSelective.setStatus("current")
_TmnxSysSnmpSrcAccessObjs_ObjectIdentity = ObjectIdentity
tmnxSysSnmpSrcAccessObjs = _TmnxSysSnmpSrcAccessObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 32)
)
_TmnxSysSnmpConfigObjs_ObjectIdentity = ObjectIdentity
tmnxSysSnmpConfigObjs = _TmnxSysSnmpConfigObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 32, 1)
)
_TmnxSysSnmpSrcAccessTblLstChgd_Type = TimeStamp
_TmnxSysSnmpSrcAccessTblLstChgd_Object = MibScalar
tmnxSysSnmpSrcAccessTblLstChgd = _TmnxSysSnmpSrcAccessTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 32, 1, 1),
    _TmnxSysSnmpSrcAccessTblLstChgd_Type()
)
tmnxSysSnmpSrcAccessTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysSnmpSrcAccessTblLstChgd.setStatus("current")
_TmnxSysSnmpSrcAccessLstTable_Object = MibTable
tmnxSysSnmpSrcAccessLstTable = _TmnxSysSnmpSrcAccessLstTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 32, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxSysSnmpSrcAccessLstTable.setStatus("current")
_TmnxSysSnmpSrcAccessLstEntry_Object = MibTableRow
tmnxSysSnmpSrcAccessLstEntry = _TmnxSysSnmpSrcAccessLstEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 32, 1, 2, 1)
)
tmnxSysSnmpSrcAccessLstEntry.setIndexNames(
    (1, "TIMETRA-SYSTEM-MIB", "tmnxSysSnmpSrcAccessLstName"),
)
if mibBuilder.loadTexts:
    tmnxSysSnmpSrcAccessLstEntry.setStatus("current")
_TmnxSysSnmpSrcAccessLstName_Type = TNamedItem
_TmnxSysSnmpSrcAccessLstName_Object = MibTableColumn
tmnxSysSnmpSrcAccessLstName = _TmnxSysSnmpSrcAccessLstName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 32, 1, 2, 1, 1),
    _TmnxSysSnmpSrcAccessLstName_Type()
)
tmnxSysSnmpSrcAccessLstName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysSnmpSrcAccessLstName.setStatus("current")
_TmnxSysSnmpSrcAccessLstRowStatus_Type = RowStatus
_TmnxSysSnmpSrcAccessLstRowStatus_Object = MibTableColumn
tmnxSysSnmpSrcAccessLstRowStatus = _TmnxSysSnmpSrcAccessLstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 32, 1, 2, 1, 2),
    _TmnxSysSnmpSrcAccessLstRowStatus_Type()
)
tmnxSysSnmpSrcAccessLstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysSnmpSrcAccessLstRowStatus.setStatus("current")
_TmnxSysSnmpSrcAccessLstLastChg_Type = TimeStamp
_TmnxSysSnmpSrcAccessLstLastChg_Object = MibTableColumn
tmnxSysSnmpSrcAccessLstLastChg = _TmnxSysSnmpSrcAccessLstLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 32, 1, 2, 1, 3),
    _TmnxSysSnmpSrcAccessLstLastChg_Type()
)
tmnxSysSnmpSrcAccessLstLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysSnmpSrcAccessLstLastChg.setStatus("current")
_TmnxSysSnmpStatsObjs_ObjectIdentity = ObjectIdentity
tmnxSysSnmpStatsObjs = _TmnxSysSnmpStatsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 32, 2)
)
_TmnxSysSnmpCommunityStatsTable_Object = MibTable
tmnxSysSnmpCommunityStatsTable = _TmnxSysSnmpCommunityStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 32, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxSysSnmpCommunityStatsTable.setStatus("current")
_TmnxSysSnmpCommunityStatsEntry_Object = MibTableRow
tmnxSysSnmpCommunityStatsEntry = _TmnxSysSnmpCommunityStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 32, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxSysSnmpCommunityStatsEntry.setStatus("current")
_TmnxSysSnmpCommunityPktDropped_Type = Gauge32
_TmnxSysSnmpCommunityPktDropped_Object = MibTableColumn
tmnxSysSnmpCommunityPktDropped = _TmnxSysSnmpCommunityPktDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 32, 2, 1, 1, 1),
    _TmnxSysSnmpCommunityPktDropped_Type()
)
tmnxSysSnmpCommunityPktDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysSnmpCommunityPktDropped.setStatus("current")
_TmnxSysMgmtProtocolObjs_ObjectIdentity = ObjectIdentity
tmnxSysMgmtProtocolObjs = _TmnxSysMgmtProtocolObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 33)
)
_TmnxSysMgmtProtocolTblLstChng_Type = TimeStamp
_TmnxSysMgmtProtocolTblLstChng_Object = MibScalar
tmnxSysMgmtProtocolTblLstChng = _TmnxSysMgmtProtocolTblLstChng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 33, 1),
    _TmnxSysMgmtProtocolTblLstChng_Type()
)
tmnxSysMgmtProtocolTblLstChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtProtocolTblLstChng.setStatus("current")
_TmnxSysMgmtProtocolTable_Object = MibTable
tmnxSysMgmtProtocolTable = _TmnxSysMgmtProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 33, 2)
)
if mibBuilder.loadTexts:
    tmnxSysMgmtProtocolTable.setStatus("current")
_TmnxSysMgmtProtocolEntry_Object = MibTableRow
tmnxSysMgmtProtocolEntry = _TmnxSysMgmtProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 33, 2, 1)
)
tmnxSysMgmtProtocolEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysMgmtProtocol"),
)
if mibBuilder.loadTexts:
    tmnxSysMgmtProtocolEntry.setStatus("current")


class _TmnxSysMgmtProtocol_Type(Integer32):
    """Custom type tmnxSysMgmtProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("cli", 0)
    )


_TmnxSysMgmtProtocol_Type.__name__ = "Integer32"
_TmnxSysMgmtProtocol_Object = MibTableColumn
tmnxSysMgmtProtocol = _TmnxSysMgmtProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 33, 2, 1, 1),
    _TmnxSysMgmtProtocol_Type()
)
tmnxSysMgmtProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysMgmtProtocol.setStatus("current")
_TmnxSysMgmtProtLastChange_Type = TimeStamp
_TmnxSysMgmtProtLastChange_Object = MibTableColumn
tmnxSysMgmtProtLastChange = _TmnxSysMgmtProtLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 33, 2, 1, 2),
    _TmnxSysMgmtProtLastChange_Type()
)
tmnxSysMgmtProtLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtProtLastChange.setStatus("current")


class _TmnxSysMgmtAllowImmediateChange_Type(TruthValue):
    """Custom type tmnxSysMgmtAllowImmediateChange based on TruthValue"""
    defaultValue = 1


_TmnxSysMgmtAllowImmediateChange_Type.__name__ = "TruthValue"
_TmnxSysMgmtAllowImmediateChange_Object = MibTableColumn
tmnxSysMgmtAllowImmediateChange = _TmnxSysMgmtAllowImmediateChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 33, 2, 1, 3),
    _TmnxSysMgmtAllowImmediateChange_Type()
)
tmnxSysMgmtAllowImmediateChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysMgmtAllowImmediateChange.setStatus("current")


class _TmnxSysMgmtCliEngine1_Type(TmnxCliEngine):
    """Custom type tmnxSysMgmtCliEngine1 based on TmnxCliEngine"""
    defaultValue = 3


_TmnxSysMgmtCliEngine1_Type.__name__ = "TmnxCliEngine"
_TmnxSysMgmtCliEngine1_Object = MibTableColumn
tmnxSysMgmtCliEngine1 = _TmnxSysMgmtCliEngine1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 33, 2, 1, 4),
    _TmnxSysMgmtCliEngine1_Type()
)
tmnxSysMgmtCliEngine1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysMgmtCliEngine1.setStatus("current")


class _TmnxSysMgmtCliEngine2_Type(TmnxCliEngine):
    """Custom type tmnxSysMgmtCliEngine2 based on TmnxCliEngine"""
    defaultValue = 3


_TmnxSysMgmtCliEngine2_Type.__name__ = "TmnxCliEngine"
_TmnxSysMgmtCliEngine2_Object = MibTableColumn
tmnxSysMgmtCliEngine2 = _TmnxSysMgmtCliEngine2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 33, 2, 1, 5),
    _TmnxSysMgmtCliEngine2_Type()
)
tmnxSysMgmtCliEngine2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysMgmtCliEngine2.setStatus("current")
_TmnxSysFileTransProfObjs_ObjectIdentity = ObjectIdentity
tmnxSysFileTransProfObjs = _TmnxSysFileTransProfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 34)
)
_TmnxSysFileTransProfTableLstChgd_Type = TimeStamp
_TmnxSysFileTransProfTableLstChgd_Object = MibScalar
tmnxSysFileTransProfTableLstChgd = _TmnxSysFileTransProfTableLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 34, 1),
    _TmnxSysFileTransProfTableLstChgd_Type()
)
tmnxSysFileTransProfTableLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFileTransProfTableLstChgd.setStatus("current")
_TmnxSysFileTransProfTable_Object = MibTable
tmnxSysFileTransProfTable = _TmnxSysFileTransProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 34, 2)
)
if mibBuilder.loadTexts:
    tmnxSysFileTransProfTable.setStatus("current")
_TmnxSysFileTransProfEntry_Object = MibTableRow
tmnxSysFileTransProfEntry = _TmnxSysFileTransProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 34, 2, 1)
)
tmnxSysFileTransProfEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysFileTransProfName"),
)
if mibBuilder.loadTexts:
    tmnxSysFileTransProfEntry.setStatus("current")
_TmnxSysFileTransProfName_Type = TNamedItem
_TmnxSysFileTransProfName_Object = MibTableColumn
tmnxSysFileTransProfName = _TmnxSysFileTransProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 34, 2, 1, 1),
    _TmnxSysFileTransProfName_Type()
)
tmnxSysFileTransProfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysFileTransProfName.setStatus("current")
_TmnxSysFileTransProfRowStatus_Type = RowStatus
_TmnxSysFileTransProfRowStatus_Object = MibTableColumn
tmnxSysFileTransProfRowStatus = _TmnxSysFileTransProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 34, 2, 1, 2),
    _TmnxSysFileTransProfRowStatus_Type()
)
tmnxSysFileTransProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysFileTransProfRowStatus.setStatus("current")
_TmnxSysFileTransProfLastChanged_Type = TimeStamp
_TmnxSysFileTransProfLastChanged_Object = MibTableColumn
tmnxSysFileTransProfLastChanged = _TmnxSysFileTransProfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 34, 2, 1, 3),
    _TmnxSysFileTransProfLastChanged_Type()
)
tmnxSysFileTransProfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFileTransProfLastChanged.setStatus("current")


class _TmnxSysFileTransProfRtrId_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxSysFileTransProfRtrId based on TmnxVRtrIDOrZero"""
    defaultValue = 1


_TmnxSysFileTransProfRtrId_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxSysFileTransProfRtrId_Object = MibTableColumn
tmnxSysFileTransProfRtrId = _TmnxSysFileTransProfRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 34, 2, 1, 4),
    _TmnxSysFileTransProfRtrId_Type()
)
tmnxSysFileTransProfRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysFileTransProfRtrId.setStatus("current")


class _TmnxSysFileTransProfSvcId_Type(TmnxServId):
    """Custom type tmnxSysFileTransProfSvcId based on TmnxServId"""
    defaultValue = 0

    subtypeSpec = TmnxServId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxSysFileTransProfSvcId_Type.__name__ = "TmnxServId"
_TmnxSysFileTransProfSvcId_Object = MibTableColumn
tmnxSysFileTransProfSvcId = _TmnxSysFileTransProfSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 34, 2, 1, 5),
    _TmnxSysFileTransProfSvcId_Type()
)
tmnxSysFileTransProfSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysFileTransProfSvcId.setStatus("current")


class _TmnxSysFileTransProfSrcAddrV4T_Type(InetAddressType):
    """Custom type tmnxSysFileTransProfSrcAddrV4T based on InetAddressType"""
    defaultValue = 0


_TmnxSysFileTransProfSrcAddrV4T_Type.__name__ = "InetAddressType"
_TmnxSysFileTransProfSrcAddrV4T_Object = MibTableColumn
tmnxSysFileTransProfSrcAddrV4T = _TmnxSysFileTransProfSrcAddrV4T_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 34, 2, 1, 6),
    _TmnxSysFileTransProfSrcAddrV4T_Type()
)
tmnxSysFileTransProfSrcAddrV4T.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysFileTransProfSrcAddrV4T.setStatus("current")


class _TmnxSysFileTransProfSrcAddrV4_Type(InetAddress):
    """Custom type tmnxSysFileTransProfSrcAddrV4 based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxSysFileTransProfSrcAddrV4_Type.__name__ = "InetAddress"
_TmnxSysFileTransProfSrcAddrV4_Object = MibTableColumn
tmnxSysFileTransProfSrcAddrV4 = _TmnxSysFileTransProfSrcAddrV4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 34, 2, 1, 7),
    _TmnxSysFileTransProfSrcAddrV4_Type()
)
tmnxSysFileTransProfSrcAddrV4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysFileTransProfSrcAddrV4.setStatus("current")


class _TmnxSysFileTransProfSrcAddrV6T_Type(InetAddressType):
    """Custom type tmnxSysFileTransProfSrcAddrV6T based on InetAddressType"""
    defaultValue = 0


_TmnxSysFileTransProfSrcAddrV6T_Type.__name__ = "InetAddressType"
_TmnxSysFileTransProfSrcAddrV6T_Object = MibTableColumn
tmnxSysFileTransProfSrcAddrV6T = _TmnxSysFileTransProfSrcAddrV6T_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 34, 2, 1, 8),
    _TmnxSysFileTransProfSrcAddrV6T_Type()
)
tmnxSysFileTransProfSrcAddrV6T.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysFileTransProfSrcAddrV6T.setStatus("current")


class _TmnxSysFileTransProfSrcAddrV6_Type(InetAddress):
    """Custom type tmnxSysFileTransProfSrcAddrV6 based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxSysFileTransProfSrcAddrV6_Type.__name__ = "InetAddress"
_TmnxSysFileTransProfSrcAddrV6_Object = MibTableColumn
tmnxSysFileTransProfSrcAddrV6 = _TmnxSysFileTransProfSrcAddrV6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 34, 2, 1, 9),
    _TmnxSysFileTransProfSrcAddrV6_Type()
)
tmnxSysFileTransProfSrcAddrV6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysFileTransProfSrcAddrV6.setStatus("current")


class _TmnxSysFileTransProfTimeout_Type(Unsigned32):
    """Custom type tmnxSysFileTransProfTimeout based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_TmnxSysFileTransProfTimeout_Type.__name__ = "Unsigned32"
_TmnxSysFileTransProfTimeout_Object = MibTableColumn
tmnxSysFileTransProfTimeout = _TmnxSysFileTransProfTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 34, 2, 1, 10),
    _TmnxSysFileTransProfTimeout_Type()
)
tmnxSysFileTransProfTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysFileTransProfTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSysFileTransProfTimeout.setUnits("seconds")


class _TmnxSysFileTransProfRetry_Type(Unsigned32):
    """Custom type tmnxSysFileTransProfRetry based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_TmnxSysFileTransProfRetry_Type.__name__ = "Unsigned32"
_TmnxSysFileTransProfRetry_Object = MibTableColumn
tmnxSysFileTransProfRetry = _TmnxSysFileTransProfRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 34, 2, 1, 11),
    _TmnxSysFileTransProfRetry_Type()
)
tmnxSysFileTransProfRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysFileTransProfRetry.setStatus("current")


class _TmnxSysFileTransProfRedirection_Type(Unsigned32):
    """Custom type tmnxSysFileTransProfRedirection based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_TmnxSysFileTransProfRedirection_Type.__name__ = "Unsigned32"
_TmnxSysFileTransProfRedirection_Object = MibTableColumn
tmnxSysFileTransProfRedirection = _TmnxSysFileTransProfRedirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 34, 2, 1, 12),
    _TmnxSysFileTransProfRedirection_Type()
)
tmnxSysFileTransProfRedirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysFileTransProfRedirection.setStatus("current")


class _TmnxSysFileTransProfSvcName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxSysFileTransProfSvcName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxSysFileTransProfSvcName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxSysFileTransProfSvcName_Object = MibTableColumn
tmnxSysFileTransProfSvcName = _TmnxSysFileTransProfSvcName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 34, 2, 1, 13),
    _TmnxSysFileTransProfSvcName_Type()
)
tmnxSysFileTransProfSvcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysFileTransProfSvcName.setStatus("current")
_TmnxEhsExtObjs_ObjectIdentity = ObjectIdentity
tmnxEhsExtObjs = _TmnxEhsExtObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 35)
)
_TmnxSmLaunchExtTable_Object = MibTable
tmnxSmLaunchExtTable = _TmnxSmLaunchExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 35, 1)
)
if mibBuilder.loadTexts:
    tmnxSmLaunchExtTable.setStatus("current")
_TmnxSmLaunchExtEntry_Object = MibTableRow
tmnxSmLaunchExtEntry = _TmnxSmLaunchExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 35, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxSmLaunchExtEntry.setStatus("current")
_TmnxSmLaunchExtAuthType_Type = TmnxScriptAuthType
_TmnxSmLaunchExtAuthType_Object = MibTableColumn
tmnxSmLaunchExtAuthType = _TmnxSmLaunchExtAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 35, 1, 1, 1),
    _TmnxSmLaunchExtAuthType_Type()
)
tmnxSmLaunchExtAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSmLaunchExtAuthType.setStatus("current")


class _TmnxSmLaunchExtLockOverride_Type(TruthValue):
    """Custom type tmnxSmLaunchExtLockOverride based on TruthValue"""
    defaultValue = 2


_TmnxSmLaunchExtLockOverride_Type.__name__ = "TruthValue"
_TmnxSmLaunchExtLockOverride_Object = MibTableColumn
tmnxSmLaunchExtLockOverride = _TmnxSmLaunchExtLockOverride_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 35, 1, 1, 2),
    _TmnxSmLaunchExtLockOverride_Type()
)
tmnxSmLaunchExtLockOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSmLaunchExtLockOverride.setStatus("current")
_TmnxSmRunExtTable_Object = MibTable
tmnxSmRunExtTable = _TmnxSmRunExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 35, 2)
)
if mibBuilder.loadTexts:
    tmnxSmRunExtTable.setStatus("current")
_TmnxSmRunExtEntry_Object = MibTableRow
tmnxSmRunExtEntry = _TmnxSmRunExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 35, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxSmRunExtEntry.setStatus("current")
_TmnxSmRunExtAuthType_Type = TmnxScriptAuthType
_TmnxSmRunExtAuthType_Object = MibTableColumn
tmnxSmRunExtAuthType = _TmnxSmRunExtAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 35, 2, 1, 1),
    _TmnxSmRunExtAuthType_Type()
)
tmnxSmRunExtAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSmRunExtAuthType.setStatus("current")
_TmnxSmRunExtUserName_Type = TNamedItemOrEmpty
_TmnxSmRunExtUserName_Object = MibTableColumn
tmnxSmRunExtUserName = _TmnxSmRunExtUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 35, 2, 1, 2),
    _TmnxSmRunExtUserName_Type()
)
tmnxSmRunExtUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSmRunExtUserName.setStatus("current")
_TmnxSmRunArgsTable_Object = MibTable
tmnxSmRunArgsTable = _TmnxSmRunArgsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 35, 3)
)
if mibBuilder.loadTexts:
    tmnxSmRunArgsTable.setStatus("current")
_TmnxSmRunArgsEntry_Object = MibTableRow
tmnxSmRunArgsEntry = _TmnxSmRunArgsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 35, 3, 1)
)
tmnxSmRunArgsEntry.setIndexNames(
    (0, "DISMAN-SCRIPT-MIB", "smLaunchOwner"),
    (0, "DISMAN-SCRIPT-MIB", "smLaunchName"),
    (0, "DISMAN-SCRIPT-MIB", "smRunIndex"),
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSmRunEventArgIndex"),
)
if mibBuilder.loadTexts:
    tmnxSmRunArgsEntry.setStatus("current")
_TmnxSmRunEventArgIndex_Type = Unsigned32
_TmnxSmRunEventArgIndex_Object = MibTableColumn
tmnxSmRunEventArgIndex = _TmnxSmRunEventArgIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 35, 3, 1, 1),
    _TmnxSmRunEventArgIndex_Type()
)
tmnxSmRunEventArgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSmRunEventArgIndex.setStatus("current")
_TmnxSmRunEventArgName_Type = TLNamedItem
_TmnxSmRunEventArgName_Object = MibTableColumn
tmnxSmRunEventArgName = _TmnxSmRunEventArgName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 35, 3, 1, 2),
    _TmnxSmRunEventArgName_Type()
)
tmnxSmRunEventArgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSmRunEventArgName.setStatus("current")


class _TmnxSmRunEventArgValue_Type(DisplayString):
    """Custom type tmnxSmRunEventArgValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxSmRunEventArgValue_Type.__name__ = "DisplayString"
_TmnxSmRunEventArgValue_Object = MibTableColumn
tmnxSmRunEventArgValue = _TmnxSmRunEventArgValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 35, 3, 1, 3),
    _TmnxSmRunEventArgValue_Type()
)
tmnxSmRunEventArgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSmRunEventArgValue.setStatus("current")
_TmnxSysSwReposObjs_ObjectIdentity = ObjectIdentity
tmnxSysSwReposObjs = _TmnxSysSwReposObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 36)
)
_TmnxSysSwReposTableLastChanged_Type = TimeStamp
_TmnxSysSwReposTableLastChanged_Object = MibScalar
tmnxSysSwReposTableLastChanged = _TmnxSysSwReposTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 36, 1),
    _TmnxSysSwReposTableLastChanged_Type()
)
tmnxSysSwReposTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysSwReposTableLastChanged.setStatus("current")
_TmnxSysSoftwareRepositoryTable_Object = MibTable
tmnxSysSoftwareRepositoryTable = _TmnxSysSoftwareRepositoryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 36, 2)
)
if mibBuilder.loadTexts:
    tmnxSysSoftwareRepositoryTable.setStatus("current")
_TmnxSysSoftwareRepositoryEntry_Object = MibTableRow
tmnxSysSoftwareRepositoryEntry = _TmnxSysSoftwareRepositoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 36, 2, 1)
)
tmnxSysSoftwareRepositoryEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysSwReposName"),
)
if mibBuilder.loadTexts:
    tmnxSysSoftwareRepositoryEntry.setStatus("current")
_TmnxSysSwReposName_Type = TNamedItem
_TmnxSysSwReposName_Object = MibTableColumn
tmnxSysSwReposName = _TmnxSysSwReposName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 36, 2, 1, 1),
    _TmnxSysSwReposName_Type()
)
tmnxSysSwReposName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysSwReposName.setStatus("current")
_TmnxSysSwReposRowStatus_Type = RowStatus
_TmnxSysSwReposRowStatus_Object = MibTableColumn
tmnxSysSwReposRowStatus = _TmnxSysSwReposRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 36, 2, 1, 2),
    _TmnxSysSwReposRowStatus_Type()
)
tmnxSysSwReposRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysSwReposRowStatus.setStatus("current")
_TmnxSysSwReposLastChanged_Type = TimeStamp
_TmnxSysSwReposLastChanged_Object = MibTableColumn
tmnxSysSwReposLastChanged = _TmnxSysSwReposLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 36, 2, 1, 3),
    _TmnxSysSwReposLastChanged_Type()
)
tmnxSysSwReposLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysSwReposLastChanged.setStatus("current")


class _TmnxSysSwReposDescription_Type(TItemDescription):
    """Custom type tmnxSysSwReposDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxSysSwReposDescription_Type.__name__ = "TItemDescription"
_TmnxSysSwReposDescription_Object = MibTableColumn
tmnxSysSwReposDescription = _TmnxSysSwReposDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 36, 2, 1, 4),
    _TmnxSysSwReposDescription_Type()
)
tmnxSysSwReposDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysSwReposDescription.setStatus("current")


class _TmnxSysSwReposPrimaryLocation_Type(TmnxDisplayStringURL):
    """Custom type tmnxSysSwReposPrimaryLocation based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_TmnxSysSwReposPrimaryLocation_Type.__name__ = "TmnxDisplayStringURL"
_TmnxSysSwReposPrimaryLocation_Object = MibTableColumn
tmnxSysSwReposPrimaryLocation = _TmnxSysSwReposPrimaryLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 36, 2, 1, 5),
    _TmnxSysSwReposPrimaryLocation_Type()
)
tmnxSysSwReposPrimaryLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysSwReposPrimaryLocation.setStatus("current")


class _TmnxSysSwReposSecondaryLocation_Type(TmnxDisplayStringURL):
    """Custom type tmnxSysSwReposSecondaryLocation based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_TmnxSysSwReposSecondaryLocation_Type.__name__ = "TmnxDisplayStringURL"
_TmnxSysSwReposSecondaryLocation_Object = MibTableColumn
tmnxSysSwReposSecondaryLocation = _TmnxSysSwReposSecondaryLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 36, 2, 1, 6),
    _TmnxSysSwReposSecondaryLocation_Type()
)
tmnxSysSwReposSecondaryLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysSwReposSecondaryLocation.setStatus("current")


class _TmnxSysSwReposTertiaryLocation_Type(TmnxDisplayStringURL):
    """Custom type tmnxSysSwReposTertiaryLocation based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_TmnxSysSwReposTertiaryLocation_Type.__name__ = "TmnxDisplayStringURL"
_TmnxSysSwReposTertiaryLocation_Object = MibTableColumn
tmnxSysSwReposTertiaryLocation = _TmnxSysSwReposTertiaryLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 36, 2, 1, 7),
    _TmnxSysSwReposTertiaryLocation_Type()
)
tmnxSysSwReposTertiaryLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysSwReposTertiaryLocation.setStatus("current")
_TmnxSysNspProxyInfo_ObjectIdentity = ObjectIdentity
tmnxSysNspProxyInfo = _TmnxSysNspProxyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 37)
)
_TmnxSysGrpcInfo_ObjectIdentity = ObjectIdentity
tmnxSysGrpcInfo = _TmnxSysGrpcInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 39)
)


class _TmnxSysGrpcAdminState_Type(TmnxAdminState):
    """Custom type tmnxSysGrpcAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxSysGrpcAdminState_Type.__name__ = "TmnxAdminState"
_TmnxSysGrpcAdminState_Object = MibScalar
tmnxSysGrpcAdminState = _TmnxSysGrpcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 39, 1),
    _TmnxSysGrpcAdminState_Type()
)
tmnxSysGrpcAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysGrpcAdminState.setStatus("current")
_TmnxSysGrpcOperState_Type = TmnxOperState
_TmnxSysGrpcOperState_Object = MibScalar
tmnxSysGrpcOperState = _TmnxSysGrpcOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 39, 2),
    _TmnxSysGrpcOperState_Type()
)
tmnxSysGrpcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcOperState.setStatus("current")


class _TmnxSysGrpcTlsServerProfile_Type(TNamedItemOrEmpty):
    """Custom type tmnxSysGrpcTlsServerProfile based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxSysGrpcTlsServerProfile_Type.__name__ = "TNamedItemOrEmpty"
_TmnxSysGrpcTlsServerProfile_Object = MibScalar
tmnxSysGrpcTlsServerProfile = _TmnxSysGrpcTlsServerProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 39, 3),
    _TmnxSysGrpcTlsServerProfile_Type()
)
tmnxSysGrpcTlsServerProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysGrpcTlsServerProfile.setStatus("current")


class _TmnxSysGrpcMaxMsgSize_Type(Unsigned32):
    """Custom type tmnxSysGrpcMaxMsgSize based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_TmnxSysGrpcMaxMsgSize_Type.__name__ = "Unsigned32"
_TmnxSysGrpcMaxMsgSize_Object = MibScalar
tmnxSysGrpcMaxMsgSize = _TmnxSysGrpcMaxMsgSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 39, 4),
    _TmnxSysGrpcMaxMsgSize_Type()
)
tmnxSysGrpcMaxMsgSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysGrpcMaxMsgSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSysGrpcMaxMsgSize.setUnits("megabytes")


class _TmnxSysGrpcAutoCfgSave_Type(TruthValue):
    """Custom type tmnxSysGrpcAutoCfgSave based on TruthValue"""
    defaultValue = 2


_TmnxSysGrpcAutoCfgSave_Type.__name__ = "TruthValue"
_TmnxSysGrpcAutoCfgSave_Object = MibScalar
tmnxSysGrpcAutoCfgSave = _TmnxSysGrpcAutoCfgSave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 39, 5),
    _TmnxSysGrpcAutoCfgSave_Type()
)
tmnxSysGrpcAutoCfgSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysGrpcAutoCfgSave.setStatus("current")


class _TmnxSysGrpcGnmiVersion_Type(DisplayString):
    """Custom type tmnxSysGrpcGnmiVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_TmnxSysGrpcGnmiVersion_Type.__name__ = "DisplayString"
_TmnxSysGrpcGnmiVersion_Object = MibScalar
tmnxSysGrpcGnmiVersion = _TmnxSysGrpcGnmiVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 39, 6),
    _TmnxSysGrpcGnmiVersion_Type()
)
tmnxSysGrpcGnmiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcGnmiVersion.setStatus("current")


class _TmnxSysGrpcAllowUnsecure_Type(TruthValue):
    """Custom type tmnxSysGrpcAllowUnsecure based on TruthValue"""
    defaultValue = 2


_TmnxSysGrpcAllowUnsecure_Type.__name__ = "TruthValue"
_TmnxSysGrpcAllowUnsecure_Object = MibScalar
tmnxSysGrpcAllowUnsecure = _TmnxSysGrpcAllowUnsecure_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 39, 7),
    _TmnxSysGrpcAllowUnsecure_Type()
)
tmnxSysGrpcAllowUnsecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysGrpcAllowUnsecure.setStatus("current")


class _TmnxSysGrpcGnmiAdminState_Type(TmnxAdminState):
    """Custom type tmnxSysGrpcGnmiAdminState based on TmnxAdminState"""
    defaultValue = 2


_TmnxSysGrpcGnmiAdminState_Type.__name__ = "TmnxAdminState"
_TmnxSysGrpcGnmiAdminState_Object = MibScalar
tmnxSysGrpcGnmiAdminState = _TmnxSysGrpcGnmiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 39, 8),
    _TmnxSysGrpcGnmiAdminState_Type()
)
tmnxSysGrpcGnmiAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysGrpcGnmiAdminState.setStatus("current")


class _TmnxSysGrpcTcpKaAdminState_Type(TmnxAdminState):
    """Custom type tmnxSysGrpcTcpKaAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxSysGrpcTcpKaAdminState_Type.__name__ = "TmnxAdminState"
_TmnxSysGrpcTcpKaAdminState_Object = MibScalar
tmnxSysGrpcTcpKaAdminState = _TmnxSysGrpcTcpKaAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 39, 9),
    _TmnxSysGrpcTcpKaAdminState_Type()
)
tmnxSysGrpcTcpKaAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysGrpcTcpKaAdminState.setStatus("current")


class _TmnxSysGrpcTcpKaIdle_Type(Unsigned32):
    """Custom type tmnxSysGrpcTcpKaIdle based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_TmnxSysGrpcTcpKaIdle_Type.__name__ = "Unsigned32"
_TmnxSysGrpcTcpKaIdle_Object = MibScalar
tmnxSysGrpcTcpKaIdle = _TmnxSysGrpcTcpKaIdle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 39, 10),
    _TmnxSysGrpcTcpKaIdle_Type()
)
tmnxSysGrpcTcpKaIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysGrpcTcpKaIdle.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSysGrpcTcpKaIdle.setUnits("seconds")


class _TmnxSysGrpcTcpKaInterval_Type(Unsigned32):
    """Custom type tmnxSysGrpcTcpKaInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_TmnxSysGrpcTcpKaInterval_Type.__name__ = "Unsigned32"
_TmnxSysGrpcTcpKaInterval_Object = MibScalar
tmnxSysGrpcTcpKaInterval = _TmnxSysGrpcTcpKaInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 39, 11),
    _TmnxSysGrpcTcpKaInterval_Type()
)
tmnxSysGrpcTcpKaInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysGrpcTcpKaInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSysGrpcTcpKaInterval.setUnits("seconds")


class _TmnxSysGrpcTcpKaCount_Type(Unsigned32):
    """Custom type tmnxSysGrpcTcpKaCount based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 100),
    )


_TmnxSysGrpcTcpKaCount_Type.__name__ = "Unsigned32"
_TmnxSysGrpcTcpKaCount_Object = MibScalar
tmnxSysGrpcTcpKaCount = _TmnxSysGrpcTcpKaCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 39, 12),
    _TmnxSysGrpcTcpKaCount_Type()
)
tmnxSysGrpcTcpKaCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysGrpcTcpKaCount.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSysGrpcTcpKaCount.setUnits("seconds")


class _TmnxSysGrpcRibApiAdminState_Type(TmnxAdminState):
    """Custom type tmnxSysGrpcRibApiAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxSysGrpcRibApiAdminState_Type.__name__ = "TmnxAdminState"
_TmnxSysGrpcRibApiAdminState_Object = MibScalar
tmnxSysGrpcRibApiAdminState = _TmnxSysGrpcRibApiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 39, 13),
    _TmnxSysGrpcRibApiAdminState_Type()
)
tmnxSysGrpcRibApiAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysGrpcRibApiAdminState.setStatus("current")


class _TmnxSysGrpcRibApiPurgeTimeout_Type(Unsigned32):
    """Custom type tmnxSysGrpcRibApiPurgeTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxSysGrpcRibApiPurgeTimeout_Type.__name__ = "Unsigned32"
_TmnxSysGrpcRibApiPurgeTimeout_Object = MibScalar
tmnxSysGrpcRibApiPurgeTimeout = _TmnxSysGrpcRibApiPurgeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 39, 14),
    _TmnxSysGrpcRibApiPurgeTimeout_Type()
)
tmnxSysGrpcRibApiPurgeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysGrpcRibApiPurgeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSysGrpcRibApiPurgeTimeout.setUnits("seconds")


class _TmnxSysGrpcRibApiVersion_Type(DisplayString):
    """Custom type tmnxSysGrpcRibApiVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_TmnxSysGrpcRibApiVersion_Type.__name__ = "DisplayString"
_TmnxSysGrpcRibApiVersion_Object = MibScalar
tmnxSysGrpcRibApiVersion = _TmnxSysGrpcRibApiVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 39, 15),
    _TmnxSysGrpcRibApiVersion_Type()
)
tmnxSysGrpcRibApiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcRibApiVersion.setStatus("current")


class _TmnxSysGrpcGnoiCertMgmtAdmnState_Type(TmnxAdminState):
    """Custom type tmnxSysGrpcGnoiCertMgmtAdmnState based on TmnxAdminState"""
    defaultValue = 3


_TmnxSysGrpcGnoiCertMgmtAdmnState_Type.__name__ = "TmnxAdminState"
_TmnxSysGrpcGnoiCertMgmtAdmnState_Object = MibScalar
tmnxSysGrpcGnoiCertMgmtAdmnState = _TmnxSysGrpcGnoiCertMgmtAdmnState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 39, 16),
    _TmnxSysGrpcGnoiCertMgmtAdmnState_Type()
)
tmnxSysGrpcGnoiCertMgmtAdmnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysGrpcGnoiCertMgmtAdmnState.setStatus("current")


class _TmnxSysGrpcGnoiCertMgmtVersion_Type(DisplayString):
    """Custom type tmnxSysGrpcGnoiCertMgmtVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_TmnxSysGrpcGnoiCertMgmtVersion_Type.__name__ = "DisplayString"
_TmnxSysGrpcGnoiCertMgmtVersion_Object = MibScalar
tmnxSysGrpcGnoiCertMgmtVersion = _TmnxSysGrpcGnoiCertMgmtVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 39, 17),
    _TmnxSysGrpcGnoiCertMgmtVersion_Type()
)
tmnxSysGrpcGnoiCertMgmtVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcGnoiCertMgmtVersion.setStatus("current")


class _TmnxSysGrpcMdCliAdminState_Type(TmnxAdminState):
    """Custom type tmnxSysGrpcMdCliAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxSysGrpcMdCliAdminState_Type.__name__ = "TmnxAdminState"
_TmnxSysGrpcMdCliAdminState_Object = MibScalar
tmnxSysGrpcMdCliAdminState = _TmnxSysGrpcMdCliAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 39, 18),
    _TmnxSysGrpcMdCliAdminState_Type()
)
tmnxSysGrpcMdCliAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysGrpcMdCliAdminState.setStatus("current")


class _TmnxSysGrpcMdCliVersion_Type(DisplayString):
    """Custom type tmnxSysGrpcMdCliVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_TmnxSysGrpcMdCliVersion_Type.__name__ = "DisplayString"
_TmnxSysGrpcMdCliVersion_Object = MibScalar
tmnxSysGrpcMdCliVersion = _TmnxSysGrpcMdCliVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 39, 19),
    _TmnxSysGrpcMdCliVersion_Type()
)
tmnxSysGrpcMdCliVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcMdCliVersion.setStatus("current")


class _TmnxSysGrpcGnoiFileAdminState_Type(TmnxAdminState):
    """Custom type tmnxSysGrpcGnoiFileAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxSysGrpcGnoiFileAdminState_Type.__name__ = "TmnxAdminState"
_TmnxSysGrpcGnoiFileAdminState_Object = MibScalar
tmnxSysGrpcGnoiFileAdminState = _TmnxSysGrpcGnoiFileAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 39, 20),
    _TmnxSysGrpcGnoiFileAdminState_Type()
)
tmnxSysGrpcGnoiFileAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysGrpcGnoiFileAdminState.setStatus("current")


class _TmnxSysGrpcGnoiFileVersion_Type(DisplayString):
    """Custom type tmnxSysGrpcGnoiFileVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_TmnxSysGrpcGnoiFileVersion_Type.__name__ = "DisplayString"
_TmnxSysGrpcGnoiFileVersion_Object = MibScalar
tmnxSysGrpcGnoiFileVersion = _TmnxSysGrpcGnoiFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 39, 21),
    _TmnxSysGrpcGnoiFileVersion_Type()
)
tmnxSysGrpcGnoiFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcGnoiFileVersion.setStatus("current")


class _TmnxSysGrpcGnoiSystemAdminState_Type(TmnxAdminState):
    """Custom type tmnxSysGrpcGnoiSystemAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxSysGrpcGnoiSystemAdminState_Type.__name__ = "TmnxAdminState"
_TmnxSysGrpcGnoiSystemAdminState_Object = MibScalar
tmnxSysGrpcGnoiSystemAdminState = _TmnxSysGrpcGnoiSystemAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 39, 22),
    _TmnxSysGrpcGnoiSystemAdminState_Type()
)
tmnxSysGrpcGnoiSystemAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysGrpcGnoiSystemAdminState.setStatus("current")


class _TmnxSysGrpcGnoiSystemVersion_Type(DisplayString):
    """Custom type tmnxSysGrpcGnoiSystemVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_TmnxSysGrpcGnoiSystemVersion_Type.__name__ = "DisplayString"
_TmnxSysGrpcGnoiSystemVersion_Object = MibScalar
tmnxSysGrpcGnoiSystemVersion = _TmnxSysGrpcGnoiSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 39, 23),
    _TmnxSysGrpcGnoiSystemVersion_Type()
)
tmnxSysGrpcGnoiSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcGnoiSystemVersion.setStatus("current")
_TmnxSysMgmtInterfaceMDCli_ObjectIdentity = ObjectIdentity
tmnxSysMgmtInterfaceMDCli = _TmnxSysMgmtInterfaceMDCli_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 40)
)


class _TmnxSysMgmtIfMDCliAutoCfgSave_Type(TruthValue):
    """Custom type tmnxSysMgmtIfMDCliAutoCfgSave based on TruthValue"""
    defaultValue = 2


_TmnxSysMgmtIfMDCliAutoCfgSave_Type.__name__ = "TruthValue"
_TmnxSysMgmtIfMDCliAutoCfgSave_Object = MibScalar
tmnxSysMgmtIfMDCliAutoCfgSave = _TmnxSysMgmtIfMDCliAutoCfgSave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 40, 1),
    _TmnxSysMgmtIfMDCliAutoCfgSave_Type()
)
tmnxSysMgmtIfMDCliAutoCfgSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfMDCliAutoCfgSave.setStatus("current")


class _TmnxSysMgmtIfMDEnvComplEnter_Type(TruthValue):
    """Custom type tmnxSysMgmtIfMDEnvComplEnter based on TruthValue"""
    defaultValue = 1


_TmnxSysMgmtIfMDEnvComplEnter_Type.__name__ = "TruthValue"
_TmnxSysMgmtIfMDEnvComplEnter_Object = MibScalar
tmnxSysMgmtIfMDEnvComplEnter = _TmnxSysMgmtIfMDEnvComplEnter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 40, 2),
    _TmnxSysMgmtIfMDEnvComplEnter_Type()
)
tmnxSysMgmtIfMDEnvComplEnter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfMDEnvComplEnter.setStatus("current")


class _TmnxSysMgmtIfMDEnvComplSpace_Type(TruthValue):
    """Custom type tmnxSysMgmtIfMDEnvComplSpace based on TruthValue"""
    defaultValue = 1


_TmnxSysMgmtIfMDEnvComplSpace_Type.__name__ = "TruthValue"
_TmnxSysMgmtIfMDEnvComplSpace_Object = MibScalar
tmnxSysMgmtIfMDEnvComplSpace = _TmnxSysMgmtIfMDEnvComplSpace_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 40, 3),
    _TmnxSysMgmtIfMDEnvComplSpace_Type()
)
tmnxSysMgmtIfMDEnvComplSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfMDEnvComplSpace.setStatus("current")


class _TmnxSysMgmtIfMDEnvComplTab_Type(TruthValue):
    """Custom type tmnxSysMgmtIfMDEnvComplTab based on TruthValue"""
    defaultValue = 1


_TmnxSysMgmtIfMDEnvComplTab_Type.__name__ = "TruthValue"
_TmnxSysMgmtIfMDEnvComplTab_Object = MibScalar
tmnxSysMgmtIfMDEnvComplTab = _TmnxSysMgmtIfMDEnvComplTab_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 40, 4),
    _TmnxSysMgmtIfMDEnvComplTab_Type()
)
tmnxSysMgmtIfMDEnvComplTab.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfMDEnvComplTab.setStatus("current")


class _TmnxSysMgmtIfMDEnvConsLength_Type(Unsigned32):
    """Custom type tmnxSysMgmtIfMDEnvConsLength based on Unsigned32"""
    defaultValue = 24

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(24, 512),
    )


_TmnxSysMgmtIfMDEnvConsLength_Type.__name__ = "Unsigned32"
_TmnxSysMgmtIfMDEnvConsLength_Object = MibScalar
tmnxSysMgmtIfMDEnvConsLength = _TmnxSysMgmtIfMDEnvConsLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 40, 5),
    _TmnxSysMgmtIfMDEnvConsLength_Type()
)
tmnxSysMgmtIfMDEnvConsLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfMDEnvConsLength.setStatus("current")


class _TmnxSysMgmtIfMDEnvConsWidth_Type(Unsigned32):
    """Custom type tmnxSysMgmtIfMDEnvConsWidth based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 512),
    )


_TmnxSysMgmtIfMDEnvConsWidth_Type.__name__ = "Unsigned32"
_TmnxSysMgmtIfMDEnvConsWidth_Object = MibScalar
tmnxSysMgmtIfMDEnvConsWidth = _TmnxSysMgmtIfMDEnvConsWidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 40, 6),
    _TmnxSysMgmtIfMDEnvConsWidth_Type()
)
tmnxSysMgmtIfMDEnvConsWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfMDEnvConsWidth.setStatus("current")


class _TmnxSysMgmtIfMDEnvMore_Type(TruthValue):
    """Custom type tmnxSysMgmtIfMDEnvMore based on TruthValue"""
    defaultValue = 1


_TmnxSysMgmtIfMDEnvMore_Type.__name__ = "TruthValue"
_TmnxSysMgmtIfMDEnvMore_Object = MibScalar
tmnxSysMgmtIfMDEnvMore = _TmnxSysMgmtIfMDEnvMore_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 40, 8),
    _TmnxSysMgmtIfMDEnvMore_Type()
)
tmnxSysMgmtIfMDEnvMore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfMDEnvMore.setStatus("current")


class _TmnxSysMgmtIfMDEnvPromptCtx_Type(TruthValue):
    """Custom type tmnxSysMgmtIfMDEnvPromptCtx based on TruthValue"""
    defaultValue = 1


_TmnxSysMgmtIfMDEnvPromptCtx_Type.__name__ = "TruthValue"
_TmnxSysMgmtIfMDEnvPromptCtx_Object = MibScalar
tmnxSysMgmtIfMDEnvPromptCtx = _TmnxSysMgmtIfMDEnvPromptCtx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 40, 9),
    _TmnxSysMgmtIfMDEnvPromptCtx_Type()
)
tmnxSysMgmtIfMDEnvPromptCtx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfMDEnvPromptCtx.setStatus("current")


class _TmnxSysMgmtIfMDEnvPromptNewline_Type(TruthValue):
    """Custom type tmnxSysMgmtIfMDEnvPromptNewline based on TruthValue"""
    defaultValue = 1


_TmnxSysMgmtIfMDEnvPromptNewline_Type.__name__ = "TruthValue"
_TmnxSysMgmtIfMDEnvPromptNewline_Object = MibScalar
tmnxSysMgmtIfMDEnvPromptNewline = _TmnxSysMgmtIfMDEnvPromptNewline_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 40, 10),
    _TmnxSysMgmtIfMDEnvPromptNewline_Type()
)
tmnxSysMgmtIfMDEnvPromptNewline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfMDEnvPromptNewline.setStatus("current")


class _TmnxSysMgmtIfMDEnvPromptTime_Type(TruthValue):
    """Custom type tmnxSysMgmtIfMDEnvPromptTime based on TruthValue"""
    defaultValue = 2


_TmnxSysMgmtIfMDEnvPromptTime_Type.__name__ = "TruthValue"
_TmnxSysMgmtIfMDEnvPromptTime_Object = MibScalar
tmnxSysMgmtIfMDEnvPromptTime = _TmnxSysMgmtIfMDEnvPromptTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 40, 11),
    _TmnxSysMgmtIfMDEnvPromptTime_Type()
)
tmnxSysMgmtIfMDEnvPromptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfMDEnvPromptTime.setStatus("current")


class _TmnxSysMgmtIfMDEnvPromptIndic_Type(TruthValue):
    """Custom type tmnxSysMgmtIfMDEnvPromptIndic based on TruthValue"""
    defaultValue = 1


_TmnxSysMgmtIfMDEnvPromptIndic_Type.__name__ = "TruthValue"
_TmnxSysMgmtIfMDEnvPromptIndic_Object = MibScalar
tmnxSysMgmtIfMDEnvPromptIndic = _TmnxSysMgmtIfMDEnvPromptIndic_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 40, 12),
    _TmnxSysMgmtIfMDEnvPromptIndic_Type()
)
tmnxSysMgmtIfMDEnvPromptIndic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfMDEnvPromptIndic.setStatus("current")


class _TmnxSysMgmtIfMDEnvTimeDisplay_Type(Integer32):
    """Custom type tmnxSysMgmtIfMDEnvTimeDisplay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("utc", 2))
    )


_TmnxSysMgmtIfMDEnvTimeDisplay_Type.__name__ = "Integer32"
_TmnxSysMgmtIfMDEnvTimeDisplay_Object = MibScalar
tmnxSysMgmtIfMDEnvTimeDisplay = _TmnxSysMgmtIfMDEnvTimeDisplay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 40, 13),
    _TmnxSysMgmtIfMDEnvTimeDisplay_Type()
)
tmnxSysMgmtIfMDEnvTimeDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfMDEnvTimeDisplay.setStatus("current")


class _TmnxSysMgmtIfMDEnvMsgCliSvrt_Type(Integer32):
    """Custom type tmnxSysMgmtIfMDEnvMsgCliSvrt based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("warning", 6),
          ("info", 7))
    )


_TmnxSysMgmtIfMDEnvMsgCliSvrt_Type.__name__ = "Integer32"
_TmnxSysMgmtIfMDEnvMsgCliSvrt_Object = MibScalar
tmnxSysMgmtIfMDEnvMsgCliSvrt = _TmnxSysMgmtIfMDEnvMsgCliSvrt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 40, 14),
    _TmnxSysMgmtIfMDEnvMsgCliSvrt_Type()
)
tmnxSysMgmtIfMDEnvMsgCliSvrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfMDEnvMsgCliSvrt.setStatus("current")


class _TmnxSysMgmtIfMDEnvProIndAdminSt_Type(TmnxAdminStateTruthValue):
    """Custom type tmnxSysMgmtIfMDEnvProIndAdminSt based on TmnxAdminStateTruthValue"""
    defaultValue = 1


_TmnxSysMgmtIfMDEnvProIndAdminSt_Type.__name__ = "TmnxAdminStateTruthValue"
_TmnxSysMgmtIfMDEnvProIndAdminSt_Object = MibScalar
tmnxSysMgmtIfMDEnvProIndAdminSt = _TmnxSysMgmtIfMDEnvProIndAdminSt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 40, 15),
    _TmnxSysMgmtIfMDEnvProIndAdminSt_Type()
)
tmnxSysMgmtIfMDEnvProIndAdminSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfMDEnvProIndAdminSt.setStatus("current")


class _TmnxSysMgmtIfMDEnvProIndType_Type(Integer32):
    """Custom type tmnxSysMgmtIfMDEnvProIndType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("dots", 1)
    )


_TmnxSysMgmtIfMDEnvProIndType_Type.__name__ = "Integer32"
_TmnxSysMgmtIfMDEnvProIndType_Object = MibScalar
tmnxSysMgmtIfMDEnvProIndType = _TmnxSysMgmtIfMDEnvProIndType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 40, 16),
    _TmnxSysMgmtIfMDEnvProIndType_Type()
)
tmnxSysMgmtIfMDEnvProIndType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfMDEnvProIndType.setStatus("current")


class _TmnxSysMgmtIfMDEnvProIndDelay_Type(Unsigned32):
    """Custom type tmnxSysMgmtIfMDEnvProIndDelay based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TmnxSysMgmtIfMDEnvProIndDelay_Type.__name__ = "Unsigned32"
_TmnxSysMgmtIfMDEnvProIndDelay_Object = MibScalar
tmnxSysMgmtIfMDEnvProIndDelay = _TmnxSysMgmtIfMDEnvProIndDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 40, 17),
    _TmnxSysMgmtIfMDEnvProIndDelay_Type()
)
tmnxSysMgmtIfMDEnvProIndDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfMDEnvProIndDelay.setStatus("current")


class _TmnxSysMgmtIfMDCliCmdAccntLoad_Type(TruthValue):
    """Custom type tmnxSysMgmtIfMDCliCmdAccntLoad based on TruthValue"""
    defaultValue = 1


_TmnxSysMgmtIfMDCliCmdAccntLoad_Type.__name__ = "TruthValue"
_TmnxSysMgmtIfMDCliCmdAccntLoad_Object = MibScalar
tmnxSysMgmtIfMDCliCmdAccntLoad = _TmnxSysMgmtIfMDCliCmdAccntLoad_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 40, 18),
    _TmnxSysMgmtIfMDCliCmdAccntLoad_Type()
)
tmnxSysMgmtIfMDCliCmdAccntLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfMDCliCmdAccntLoad.setStatus("obsolete")


class _TmnxSysMgmtIfMDEnvTimeFormat_Type(Integer32):
    """Custom type tmnxSysMgmtIfMDEnvTimeFormat based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iso-8601", 1),
          ("rfc-1123", 2),
          ("rfc-3339", 3))
    )


_TmnxSysMgmtIfMDEnvTimeFormat_Type.__name__ = "Integer32"
_TmnxSysMgmtIfMDEnvTimeFormat_Object = MibScalar
tmnxSysMgmtIfMDEnvTimeFormat = _TmnxSysMgmtIfMDEnvTimeFormat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 40, 19),
    _TmnxSysMgmtIfMDEnvTimeFormat_Type()
)
tmnxSysMgmtIfMDEnvTimeFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfMDEnvTimeFormat.setStatus("current")
_TmnxMGSysObjs_ObjectIdentity = ObjectIdentity
tmnxMGSysObjs = _TmnxMGSysObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 41)
)
_TmnxSysMgmtInterfaceYangModules_ObjectIdentity = ObjectIdentity
tmnxSysMgmtInterfaceYangModules = _TmnxSysMgmtInterfaceYangModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 42)
)


class _TmnxSysMgmtIfYangBaseR13_Type(TruthValue):
    """Custom type tmnxSysMgmtIfYangBaseR13 based on TruthValue"""
    defaultValue = 2


_TmnxSysMgmtIfYangBaseR13_Type.__name__ = "TruthValue"
_TmnxSysMgmtIfYangBaseR13_Object = MibScalar
tmnxSysMgmtIfYangBaseR13 = _TmnxSysMgmtIfYangBaseR13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 42, 1),
    _TmnxSysMgmtIfYangBaseR13_Type()
)
tmnxSysMgmtIfYangBaseR13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfYangBaseR13.setStatus("current")
_TmnxSysMgmtIfYangNokia_Type = TruthValue
_TmnxSysMgmtIfYangNokia_Object = MibScalar
tmnxSysMgmtIfYangNokia = _TmnxSysMgmtIfYangNokia_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 42, 2),
    _TmnxSysMgmtIfYangNokia_Type()
)
tmnxSysMgmtIfYangNokia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfYangNokia.setStatus("current")


class _TmnxSysMgmtIfYangOpenConfig_Type(TruthValue):
    """Custom type tmnxSysMgmtIfYangOpenConfig based on TruthValue"""
    defaultValue = 2


_TmnxSysMgmtIfYangOpenConfig_Type.__name__ = "TruthValue"
_TmnxSysMgmtIfYangOpenConfig_Object = MibScalar
tmnxSysMgmtIfYangOpenConfig = _TmnxSysMgmtIfYangOpenConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 42, 3),
    _TmnxSysMgmtIfYangOpenConfig_Type()
)
tmnxSysMgmtIfYangOpenConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfYangOpenConfig.setStatus("current")
_TmnxSysMgmtIfYangNokiaCombined_Type = TruthValue
_TmnxSysMgmtIfYangNokiaCombined_Object = MibScalar
tmnxSysMgmtIfYangNokiaCombined = _TmnxSysMgmtIfYangNokiaCombined_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 42, 4),
    _TmnxSysMgmtIfYangNokiaCombined_Type()
)
tmnxSysMgmtIfYangNokiaCombined.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfYangNokiaCombined.setStatus("current")


class _TmnxSysMgmtIfYangNmdaSupport_Type(TruthValue):
    """Custom type tmnxSysMgmtIfYangNmdaSupport based on TruthValue"""
    defaultValue = 2


_TmnxSysMgmtIfYangNmdaSupport_Type.__name__ = "TruthValue"
_TmnxSysMgmtIfYangNmdaSupport_Object = MibScalar
tmnxSysMgmtIfYangNmdaSupport = _TmnxSysMgmtIfYangNmdaSupport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 42, 5),
    _TmnxSysMgmtIfYangNmdaSupport_Type()
)
tmnxSysMgmtIfYangNmdaSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfYangNmdaSupport.setStatus("current")
_TmnxSysMgmtInterfaces_ObjectIdentity = ObjectIdentity
tmnxSysMgmtInterfaces = _TmnxSysMgmtInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43)
)


class _TmnxSysMgmtIfWriteMode_Type(Integer32):
    """Custom type tmnxSysMgmtIfWriteMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("classic", 1),
          ("modelDriven", 2),
          ("mixed", 3))
    )


_TmnxSysMgmtIfWriteMode_Type.__name__ = "Integer32"
_TmnxSysMgmtIfWriteMode_Object = MibScalar
tmnxSysMgmtIfWriteMode = _TmnxSysMgmtIfWriteMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 1),
    _TmnxSysMgmtIfWriteMode_Type()
)
tmnxSysMgmtIfWriteMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfWriteMode.setStatus("current")


class _TmnxSysMgmtIfWriteOperMode_Type(Integer32):
    """Custom type tmnxSysMgmtIfWriteOperMode based on Integer32"""
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
        *(("syncing", 0),
          ("classic", 1),
          ("modelDriven", 2),
          ("mixed", 3))
    )


_TmnxSysMgmtIfWriteOperMode_Type.__name__ = "Integer32"
_TmnxSysMgmtIfWriteOperMode_Object = MibScalar
tmnxSysMgmtIfWriteOperMode = _TmnxSysMgmtIfWriteOperMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 2),
    _TmnxSysMgmtIfWriteOperMode_Type()
)
tmnxSysMgmtIfWriteOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfWriteOperMode.setStatus("current")


class _TmnxSysMgmtIfModeLastSwitchTime_Type(DateAndTime):
    """Custom type tmnxSysMgmtIfModeLastSwitchTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxSysMgmtIfModeLastSwitchTime_Type.__name__ = "DateAndTime"
_TmnxSysMgmtIfModeLastSwitchTime_Object = MibScalar
tmnxSysMgmtIfModeLastSwitchTime = _TmnxSysMgmtIfModeLastSwitchTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 3),
    _TmnxSysMgmtIfModeLastSwitchTime_Type()
)
tmnxSysMgmtIfModeLastSwitchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfModeLastSwitchTime.setStatus("current")
_TmnxSysMgmtIfModeSwitchDuration_Type = Counter32
_TmnxSysMgmtIfModeSwitchDuration_Object = MibScalar
tmnxSysMgmtIfModeSwitchDuration = _TmnxSysMgmtIfModeSwitchDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 4),
    _TmnxSysMgmtIfModeSwitchDuration_Type()
)
tmnxSysMgmtIfModeSwitchDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfModeSwitchDuration.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfModeSwitchDuration.setUnits("milliseconds")
_TmnxSysMgmtIfDstoreLocksTable_Object = MibTable
tmnxSysMgmtIfDstoreLocksTable = _TmnxSysMgmtIfDstoreLocksTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 5)
)
if mibBuilder.loadTexts:
    tmnxSysMgmtIfDstoreLocksTable.setStatus("current")
_TmnxSysMgmtIfDstoreLocksEntry_Object = MibTableRow
tmnxSysMgmtIfDstoreLocksEntry = _TmnxSysMgmtIfDstoreLocksEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 5, 1)
)
tmnxSysMgmtIfDstoreLocksEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfDsLocksSessionId"),
)
if mibBuilder.loadTexts:
    tmnxSysMgmtIfDstoreLocksEntry.setStatus("current")
_TmnxSysMgmtIfDsLocksSessionId_Type = Unsigned32
_TmnxSysMgmtIfDsLocksSessionId_Object = MibTableColumn
tmnxSysMgmtIfDsLocksSessionId = _TmnxSysMgmtIfDsLocksSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 5, 1, 1),
    _TmnxSysMgmtIfDsLocksSessionId_Type()
)
tmnxSysMgmtIfDsLocksSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfDsLocksSessionId.setStatus("current")


class _TmnxSysMgmtIfDsLocksRmtIpAddress_Type(InetAddress):
    """Custom type tmnxSysMgmtIfDsLocksRmtIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxSysMgmtIfDsLocksRmtIpAddress_Type.__name__ = "InetAddress"
_TmnxSysMgmtIfDsLocksRmtIpAddress_Object = MibTableColumn
tmnxSysMgmtIfDsLocksRmtIpAddress = _TmnxSysMgmtIfDsLocksRmtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 5, 1, 2),
    _TmnxSysMgmtIfDsLocksRmtIpAddress_Type()
)
tmnxSysMgmtIfDsLocksRmtIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfDsLocksRmtIpAddress.setStatus("current")


class _TmnxSysMgmtIfDsLocksConsole_Type(TruthValue):
    """Custom type tmnxSysMgmtIfDsLocksConsole based on TruthValue"""
    defaultValue = 2


_TmnxSysMgmtIfDsLocksConsole_Type.__name__ = "TruthValue"
_TmnxSysMgmtIfDsLocksConsole_Object = MibTableColumn
tmnxSysMgmtIfDsLocksConsole = _TmnxSysMgmtIfDsLocksConsole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 5, 1, 3),
    _TmnxSysMgmtIfDsLocksConsole_Type()
)
tmnxSysMgmtIfDsLocksConsole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfDsLocksConsole.setStatus("current")
_TmnxSysMgmtIfDsLocksUserName_Type = TNamedItemOrEmpty
_TmnxSysMgmtIfDsLocksUserName_Object = MibTableColumn
tmnxSysMgmtIfDsLocksUserName = _TmnxSysMgmtIfDsLocksUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 5, 1, 4),
    _TmnxSysMgmtIfDsLocksUserName_Type()
)
tmnxSysMgmtIfDsLocksUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfDsLocksUserName.setStatus("current")


class _TmnxSysMgmtIfDsLocksSessionMode_Type(Integer32):
    """Custom type tmnxSysMgmtIfDsLocksSessionMode based on Integer32"""
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
        *(("global", 1),
          ("exclusive", 2),
          ("private", 3),
          ("privateExclusive", 4),
          ("readOnly", 5))
    )


_TmnxSysMgmtIfDsLocksSessionMode_Type.__name__ = "Integer32"
_TmnxSysMgmtIfDsLocksSessionMode_Object = MibTableColumn
tmnxSysMgmtIfDsLocksSessionMode = _TmnxSysMgmtIfDsLocksSessionMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 5, 1, 5),
    _TmnxSysMgmtIfDsLocksSessionMode_Type()
)
tmnxSysMgmtIfDsLocksSessionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfDsLocksSessionMode.setStatus("current")


class _TmnxSysMgmtIfDsLocksSessionType_Type(Integer32):
    """Custom type tmnxSysMgmtIfDsLocksSessionType based on Integer32"""
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
        *(("classicCli", 1),
          ("grpc", 2),
          ("mdCli", 3),
          ("netconf", 4),
          ("snmp", 5),
          ("system", 6))
    )


_TmnxSysMgmtIfDsLocksSessionType_Type.__name__ = "Integer32"
_TmnxSysMgmtIfDsLocksSessionType_Object = MibTableColumn
tmnxSysMgmtIfDsLocksSessionType = _TmnxSysMgmtIfDsLocksSessionType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 5, 1, 6),
    _TmnxSysMgmtIfDsLocksSessionType_Type()
)
tmnxSysMgmtIfDsLocksSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfDsLocksSessionType.setStatus("current")
_TmnxSysMgmtIfDsLocksRegion_Type = TNamedItem
_TmnxSysMgmtIfDsLocksRegion_Object = MibTableColumn
tmnxSysMgmtIfDsLocksRegion = _TmnxSysMgmtIfDsLocksRegion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 5, 1, 7),
    _TmnxSysMgmtIfDsLocksRegion_Type()
)
tmnxSysMgmtIfDsLocksRegion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfDsLocksRegion.setStatus("current")
_TmnxSysMgmtIfDsLocksRunLock_Type = TmnxSysMgmtIfDstoreLockState
_TmnxSysMgmtIfDsLocksRunLock_Object = MibTableColumn
tmnxSysMgmtIfDsLocksRunLock = _TmnxSysMgmtIfDsLocksRunLock_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 5, 1, 8),
    _TmnxSysMgmtIfDsLocksRunLock_Type()
)
tmnxSysMgmtIfDsLocksRunLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfDsLocksRunLock.setStatus("current")
_TmnxSysMgmtIfDsLocksCndLock_Type = TmnxSysMgmtIfDstoreLockState
_TmnxSysMgmtIfDsLocksCndLock_Object = MibTableColumn
tmnxSysMgmtIfDsLocksCndLock = _TmnxSysMgmtIfDsLocksCndLock_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 5, 1, 9),
    _TmnxSysMgmtIfDsLocksCndLock_Type()
)
tmnxSysMgmtIfDsLocksCndLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfDsLocksCndLock.setStatus("current")
_TmnxSysMgmtIfDsLocksIdleTime_Type = Unsigned32
_TmnxSysMgmtIfDsLocksIdleTime_Object = MibTableColumn
tmnxSysMgmtIfDsLocksIdleTime = _TmnxSysMgmtIfDsLocksIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 5, 1, 10),
    _TmnxSysMgmtIfDsLocksIdleTime_Type()
)
tmnxSysMgmtIfDsLocksIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfDsLocksIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfDsLocksIdleTime.setUnits("seconds")
_TmnxSysMgmtIfDsLocksScratchCnt_Type = Unsigned32
_TmnxSysMgmtIfDsLocksScratchCnt_Object = MibTableColumn
tmnxSysMgmtIfDsLocksScratchCnt = _TmnxSysMgmtIfDsLocksScratchCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 5, 1, 11),
    _TmnxSysMgmtIfDsLocksScratchCnt_Type()
)
tmnxSysMgmtIfDsLocksScratchCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfDsLocksScratchCnt.setStatus("current")


class _TmnxSysMgmtIfDsLocksCronEhs_Type(TruthValue):
    """Custom type tmnxSysMgmtIfDsLocksCronEhs based on TruthValue"""
    defaultValue = 2


_TmnxSysMgmtIfDsLocksCronEhs_Type.__name__ = "TruthValue"
_TmnxSysMgmtIfDsLocksCronEhs_Object = MibTableColumn
tmnxSysMgmtIfDsLocksCronEhs = _TmnxSysMgmtIfDsLocksCronEhs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 5, 1, 12),
    _TmnxSysMgmtIfDsLocksCronEhs_Type()
)
tmnxSysMgmtIfDsLocksCronEhs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfDsLocksCronEhs.setStatus("current")


class _TmnxSysMgmtIfSchemaPath_Type(TmnxDisplayStringURL):
    """Custom type tmnxSysMgmtIfSchemaPath based on TmnxDisplayStringURL"""
    defaultValue = OctetString("")


_TmnxSysMgmtIfSchemaPath_Type.__name__ = "TmnxDisplayStringURL"
_TmnxSysMgmtIfSchemaPath_Object = MibScalar
tmnxSysMgmtIfSchemaPath = _TmnxSysMgmtIfSchemaPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 6),
    _TmnxSysMgmtIfSchemaPath_Type()
)
tmnxSysMgmtIfSchemaPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfSchemaPath.setStatus("current")


class _TmnxSysMgmtIfWriteSwitchReason_Type(Integer32):
    """Custom type tmnxSysMgmtIfWriteSwitchReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boot", 0),
          ("manual", 1),
          ("validation", 2))
    )


_TmnxSysMgmtIfWriteSwitchReason_Type.__name__ = "Integer32"
_TmnxSysMgmtIfWriteSwitchReason_Object = MibScalar
tmnxSysMgmtIfWriteSwitchReason = _TmnxSysMgmtIfWriteSwitchReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 7),
    _TmnxSysMgmtIfWriteSwitchReason_Type()
)
tmnxSysMgmtIfWriteSwitchReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfWriteSwitchReason.setStatus("current")
_TmnxSysMgmtIfPriSchemaPathState_Type = TmnxSchemaPathState
_TmnxSysMgmtIfPriSchemaPathState_Object = MibScalar
tmnxSysMgmtIfPriSchemaPathState = _TmnxSysMgmtIfPriSchemaPathState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 8),
    _TmnxSysMgmtIfPriSchemaPathState_Type()
)
tmnxSysMgmtIfPriSchemaPathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfPriSchemaPathState.setStatus("current")
_TmnxSysMgmtIfPriSchemaPathValue_Type = TmnxDisplayStringURL
_TmnxSysMgmtIfPriSchemaPathValue_Object = MibScalar
tmnxSysMgmtIfPriSchemaPathValue = _TmnxSysMgmtIfPriSchemaPathValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 9),
    _TmnxSysMgmtIfPriSchemaPathValue_Type()
)
tmnxSysMgmtIfPriSchemaPathValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfPriSchemaPathValue.setStatus("current")
_TmnxSysMgmtIfSecSchemaPathState_Type = TmnxSchemaPathState
_TmnxSysMgmtIfSecSchemaPathState_Object = MibScalar
tmnxSysMgmtIfSecSchemaPathState = _TmnxSysMgmtIfSecSchemaPathState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 10),
    _TmnxSysMgmtIfSecSchemaPathState_Type()
)
tmnxSysMgmtIfSecSchemaPathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfSecSchemaPathState.setStatus("current")
_TmnxSysMgmtIfSecSchemaPathValue_Type = TmnxDisplayStringURL
_TmnxSysMgmtIfSecSchemaPathValue_Object = MibScalar
tmnxSysMgmtIfSecSchemaPathValue = _TmnxSysMgmtIfSecSchemaPathValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 11),
    _TmnxSysMgmtIfSecSchemaPathValue_Type()
)
tmnxSysMgmtIfSecSchemaPathValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfSecSchemaPathValue.setStatus("current")
_TmnxSysMgmtIfTerSchemaPathState_Type = TmnxSchemaPathState
_TmnxSysMgmtIfTerSchemaPathState_Object = MibScalar
tmnxSysMgmtIfTerSchemaPathState = _TmnxSysMgmtIfTerSchemaPathState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 12),
    _TmnxSysMgmtIfTerSchemaPathState_Type()
)
tmnxSysMgmtIfTerSchemaPathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfTerSchemaPathState.setStatus("current")
_TmnxSysMgmtIfTerSchemaPathValue_Type = TmnxDisplayStringURL
_TmnxSysMgmtIfTerSchemaPathValue_Object = MibScalar
tmnxSysMgmtIfTerSchemaPathValue = _TmnxSysMgmtIfTerSchemaPathValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 13),
    _TmnxSysMgmtIfTerSchemaPathValue_Type()
)
tmnxSysMgmtIfTerSchemaPathValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfTerSchemaPathValue.setStatus("current")
_TmnxSysMgmtIfOperSchemaPathState_Type = TmnxSchemaPathState
_TmnxSysMgmtIfOperSchemaPathState_Object = MibScalar
tmnxSysMgmtIfOperSchemaPathState = _TmnxSysMgmtIfOperSchemaPathState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 14),
    _TmnxSysMgmtIfOperSchemaPathState_Type()
)
tmnxSysMgmtIfOperSchemaPathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfOperSchemaPathState.setStatus("current")
_TmnxSysMgmtIfOperSchemaPathValue_Type = TmnxDisplayStringURL
_TmnxSysMgmtIfOperSchemaPathValue_Object = MibScalar
tmnxSysMgmtIfOperSchemaPathValue = _TmnxSysMgmtIfOperSchemaPathValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 15),
    _TmnxSysMgmtIfOperSchemaPathValue_Type()
)
tmnxSysMgmtIfOperSchemaPathValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfOperSchemaPathValue.setStatus("current")


class _TmnxSysMgmtIfCommitHistory_Type(Unsigned32):
    """Custom type tmnxSysMgmtIfCommitHistory based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_TmnxSysMgmtIfCommitHistory_Type.__name__ = "Unsigned32"
_TmnxSysMgmtIfCommitHistory_Object = MibScalar
tmnxSysMgmtIfCommitHistory = _TmnxSysMgmtIfCommitHistory_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 43, 16),
    _TmnxSysMgmtIfCommitHistory_Type()
)
tmnxSysMgmtIfCommitHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfCommitHistory.setStatus("current")
_TmnxSysGrpcConnTable_Object = MibTable
tmnxSysGrpcConnTable = _TmnxSysGrpcConnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 44)
)
if mibBuilder.loadTexts:
    tmnxSysGrpcConnTable.setStatus("current")
_TmnxSysGrpcConnEntry_Object = MibTableRow
tmnxSysGrpcConnEntry = _TmnxSysGrpcConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 44, 1)
)
tmnxSysGrpcConnEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysGrpcConnSrcIpAddType"),
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysGrpcConnSrcIpAddress"),
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysGrpcConnSrcPort"),
)
if mibBuilder.loadTexts:
    tmnxSysGrpcConnEntry.setStatus("current")
_TmnxSysGrpcConnSrcIpAddType_Type = InetAddressType
_TmnxSysGrpcConnSrcIpAddType_Object = MibTableColumn
tmnxSysGrpcConnSrcIpAddType = _TmnxSysGrpcConnSrcIpAddType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 44, 1, 1),
    _TmnxSysGrpcConnSrcIpAddType_Type()
)
tmnxSysGrpcConnSrcIpAddType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysGrpcConnSrcIpAddType.setStatus("current")


class _TmnxSysGrpcConnSrcIpAddress_Type(InetAddress):
    """Custom type tmnxSysGrpcConnSrcIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxSysGrpcConnSrcIpAddress_Type.__name__ = "InetAddress"
_TmnxSysGrpcConnSrcIpAddress_Object = MibTableColumn
tmnxSysGrpcConnSrcIpAddress = _TmnxSysGrpcConnSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 44, 1, 2),
    _TmnxSysGrpcConnSrcIpAddress_Type()
)
tmnxSysGrpcConnSrcIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysGrpcConnSrcIpAddress.setStatus("current")
_TmnxSysGrpcConnSrcPort_Type = InetPortNumber
_TmnxSysGrpcConnSrcPort_Object = MibTableColumn
tmnxSysGrpcConnSrcPort = _TmnxSysGrpcConnSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 44, 1, 3),
    _TmnxSysGrpcConnSrcPort_Type()
)
tmnxSysGrpcConnSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysGrpcConnSrcPort.setStatus("current")
_TmnxSysGrpcConnStartTime_Type = DateAndTime
_TmnxSysGrpcConnStartTime_Object = MibTableColumn
tmnxSysGrpcConnStartTime = _TmnxSysGrpcConnStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 44, 1, 4),
    _TmnxSysGrpcConnStartTime_Type()
)
tmnxSysGrpcConnStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcConnStartTime.setStatus("current")
_TmnxSysGrpcConnActRpcCnt_Type = CounterBasedGauge64
_TmnxSysGrpcConnActRpcCnt_Object = MibTableColumn
tmnxSysGrpcConnActRpcCnt = _TmnxSysGrpcConnActRpcCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 44, 1, 5),
    _TmnxSysGrpcConnActRpcCnt_Type()
)
tmnxSysGrpcConnActRpcCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcConnActRpcCnt.setStatus("current")
_TmnxSysGrpcConnTotRpcCnt_Type = Counter64
_TmnxSysGrpcConnTotRpcCnt_Object = MibTableColumn
tmnxSysGrpcConnTotRpcCnt = _TmnxSysGrpcConnTotRpcCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 44, 1, 6),
    _TmnxSysGrpcConnTotRpcCnt_Type()
)
tmnxSysGrpcConnTotRpcCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcConnTotRpcCnt.setStatus("current")
_TmnxSysGrpcConnRxBytes_Type = Counter64
_TmnxSysGrpcConnRxBytes_Object = MibTableColumn
tmnxSysGrpcConnRxBytes = _TmnxSysGrpcConnRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 44, 1, 7),
    _TmnxSysGrpcConnRxBytes_Type()
)
tmnxSysGrpcConnRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcConnRxBytes.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSysGrpcConnRxBytes.setUnits("bytes")
_TmnxSysGrpcConnTxBytes_Type = Counter64
_TmnxSysGrpcConnTxBytes_Object = MibTableColumn
tmnxSysGrpcConnTxBytes = _TmnxSysGrpcConnTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 44, 1, 8),
    _TmnxSysGrpcConnTxBytes_Type()
)
tmnxSysGrpcConnTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcConnTxBytes.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSysGrpcConnTxBytes.setUnits("bytes")
_TmnxSysGrpcConnQos_Type = TDSCPNameOrEmpty
_TmnxSysGrpcConnQos_Object = MibTableColumn
tmnxSysGrpcConnQos = _TmnxSysGrpcConnQos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 44, 1, 9),
    _TmnxSysGrpcConnQos_Type()
)
tmnxSysGrpcConnQos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcConnQos.setStatus("current")
_TmnxSysGrpcConnSrcVRtrId_Type = TmnxVRtrID
_TmnxSysGrpcConnSrcVRtrId_Object = MibTableColumn
tmnxSysGrpcConnSrcVRtrId = _TmnxSysGrpcConnSrcVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 44, 1, 10),
    _TmnxSysGrpcConnSrcVRtrId_Type()
)
tmnxSysGrpcConnSrcVRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcConnSrcVRtrId.setStatus("current")
_TmnxSysGrpcConnGrpcTunnel_Type = TNamedItemOrEmpty
_TmnxSysGrpcConnGrpcTunnel_Object = MibTableColumn
tmnxSysGrpcConnGrpcTunnel = _TmnxSysGrpcConnGrpcTunnel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 44, 1, 11),
    _TmnxSysGrpcConnGrpcTunnel_Type()
)
tmnxSysGrpcConnGrpcTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcConnGrpcTunnel.setStatus("current")
_TmnxSysHttpRdr_ObjectIdentity = ObjectIdentity
tmnxSysHttpRdr = _TmnxSysHttpRdr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 45)
)


class _TmnxSysHttpRdrCpmOptimizedMode_Type(TruthValue):
    """Custom type tmnxSysHttpRdrCpmOptimizedMode based on TruthValue"""
    defaultValue = 1


_TmnxSysHttpRdrCpmOptimizedMode_Type.__name__ = "TruthValue"
_TmnxSysHttpRdrCpmOptimizedMode_Object = MibScalar
tmnxSysHttpRdrCpmOptimizedMode = _TmnxSysHttpRdrCpmOptimizedMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 45, 1),
    _TmnxSysHttpRdrCpmOptimizedMode_Type()
)
tmnxSysHttpRdrCpmOptimizedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysHttpRdrCpmOptimizedMode.setStatus("current")
_TmnxSysGrpcRpcTable_Object = MibTable
tmnxSysGrpcRpcTable = _TmnxSysGrpcRpcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 46)
)
if mibBuilder.loadTexts:
    tmnxSysGrpcRpcTable.setStatus("current")
_TmnxSysGrpcRpcEntry_Object = MibTableRow
tmnxSysGrpcRpcEntry = _TmnxSysGrpcRpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 46, 1)
)
tmnxSysGrpcRpcEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysGrpcRpcId"),
)
if mibBuilder.loadTexts:
    tmnxSysGrpcRpcEntry.setStatus("current")
_TmnxSysGrpcRpcId_Type = Unsigned32
_TmnxSysGrpcRpcId_Object = MibTableColumn
tmnxSysGrpcRpcId = _TmnxSysGrpcRpcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 46, 1, 1),
    _TmnxSysGrpcRpcId_Type()
)
tmnxSysGrpcRpcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysGrpcRpcId.setStatus("current")
_TmnxSysGrpcRpcName_Type = TNamedItem
_TmnxSysGrpcRpcName_Object = MibTableColumn
tmnxSysGrpcRpcName = _TmnxSysGrpcRpcName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 46, 1, 2),
    _TmnxSysGrpcRpcName_Type()
)
tmnxSysGrpcRpcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcRpcName.setStatus("current")
_TmnxSysGrpcRpcServiceName_Type = TNamedItem
_TmnxSysGrpcRpcServiceName_Object = MibTableColumn
tmnxSysGrpcRpcServiceName = _TmnxSysGrpcRpcServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 46, 1, 3),
    _TmnxSysGrpcRpcServiceName_Type()
)
tmnxSysGrpcRpcServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcRpcServiceName.setStatus("current")
_TmnxSysGrpcRpcStartTime_Type = DateAndTime
_TmnxSysGrpcRpcStartTime_Object = MibTableColumn
tmnxSysGrpcRpcStartTime = _TmnxSysGrpcRpcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 46, 1, 4),
    _TmnxSysGrpcRpcStartTime_Type()
)
tmnxSysGrpcRpcStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcRpcStartTime.setStatus("current")
_TmnxSysGrpcRpcSrcIpAddType_Type = InetAddressType
_TmnxSysGrpcRpcSrcIpAddType_Object = MibTableColumn
tmnxSysGrpcRpcSrcIpAddType = _TmnxSysGrpcRpcSrcIpAddType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 46, 1, 5),
    _TmnxSysGrpcRpcSrcIpAddType_Type()
)
tmnxSysGrpcRpcSrcIpAddType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcRpcSrcIpAddType.setStatus("current")


class _TmnxSysGrpcRpcSrcIpAddress_Type(InetAddress):
    """Custom type tmnxSysGrpcRpcSrcIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxSysGrpcRpcSrcIpAddress_Type.__name__ = "InetAddress"
_TmnxSysGrpcRpcSrcIpAddress_Object = MibTableColumn
tmnxSysGrpcRpcSrcIpAddress = _TmnxSysGrpcRpcSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 46, 1, 6),
    _TmnxSysGrpcRpcSrcIpAddress_Type()
)
tmnxSysGrpcRpcSrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcRpcSrcIpAddress.setStatus("current")
_TmnxSysGrpcRpcSrcPort_Type = InetPortNumber
_TmnxSysGrpcRpcSrcPort_Object = MibTableColumn
tmnxSysGrpcRpcSrcPort = _TmnxSysGrpcRpcSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 46, 1, 7),
    _TmnxSysGrpcRpcSrcPort_Type()
)
tmnxSysGrpcRpcSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcRpcSrcPort.setStatus("current")
_TmnxSysGrpcRpcUserName_Type = TNamedItemOrEmpty
_TmnxSysGrpcRpcUserName_Object = MibTableColumn
tmnxSysGrpcRpcUserName = _TmnxSysGrpcRpcUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 46, 1, 8),
    _TmnxSysGrpcRpcUserName_Type()
)
tmnxSysGrpcRpcUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcRpcUserName.setStatus("current")
_TmnxSysGrpcRpcSessionId_Type = Unsigned32
_TmnxSysGrpcRpcSessionId_Object = MibTableColumn
tmnxSysGrpcRpcSessionId = _TmnxSysGrpcRpcSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 46, 1, 9),
    _TmnxSysGrpcRpcSessionId_Type()
)
tmnxSysGrpcRpcSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcRpcSessionId.setStatus("current")
_TmnxSysGrpcRpcGrpcTunnel_Type = TNamedItemOrEmpty
_TmnxSysGrpcRpcGrpcTunnel_Object = MibTableColumn
tmnxSysGrpcRpcGrpcTunnel = _TmnxSysGrpcRpcGrpcTunnel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 46, 1, 10),
    _TmnxSysGrpcRpcGrpcTunnel_Type()
)
tmnxSysGrpcRpcGrpcTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcRpcGrpcTunnel.setStatus("current")
_TmnxSysNetworkElementObjs_ObjectIdentity = ObjectIdentity
tmnxSysNetworkElementObjs = _TmnxSysNetworkElementObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 47)
)
_TmnxSysNEProfTableLstChgd_Type = TimeStamp
_TmnxSysNEProfTableLstChgd_Object = MibScalar
tmnxSysNEProfTableLstChgd = _TmnxSysNEProfTableLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 47, 1),
    _TmnxSysNEProfTableLstChgd_Type()
)
tmnxSysNEProfTableLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysNEProfTableLstChgd.setStatus("current")
_TmnxSysNEProfTable_Object = MibTable
tmnxSysNEProfTable = _TmnxSysNEProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 47, 2)
)
if mibBuilder.loadTexts:
    tmnxSysNEProfTable.setStatus("current")
_TmnxSysNEProfEntry_Object = MibTableRow
tmnxSysNEProfEntry = _TmnxSysNEProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 47, 2, 1)
)
tmnxSysNEProfEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysNEProfName"),
)
if mibBuilder.loadTexts:
    tmnxSysNEProfEntry.setStatus("current")
_TmnxSysNEProfName_Type = TNamedItem
_TmnxSysNEProfName_Object = MibTableColumn
tmnxSysNEProfName = _TmnxSysNEProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 47, 2, 1, 1),
    _TmnxSysNEProfName_Type()
)
tmnxSysNEProfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysNEProfName.setStatus("current")
_TmnxSysNEProfRowStatus_Type = RowStatus
_TmnxSysNEProfRowStatus_Object = MibTableColumn
tmnxSysNEProfRowStatus = _TmnxSysNEProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 47, 2, 1, 2),
    _TmnxSysNEProfRowStatus_Type()
)
tmnxSysNEProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysNEProfRowStatus.setStatus("current")
_TmnxSysNEProfLastChanged_Type = TimeStamp
_TmnxSysNEProfLastChanged_Object = MibTableColumn
tmnxSysNEProfLastChanged = _TmnxSysNEProfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 47, 2, 1, 3),
    _TmnxSysNEProfLastChanged_Type()
)
tmnxSysNEProfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysNEProfLastChanged.setStatus("current")


class _TmnxSysNEProfNeid_Type(TmnxSysNeid):
    """Custom type tmnxSysNEProfNeid based on TmnxSysNeid"""
    defaultHexValue = ""


_TmnxSysNEProfNeid_Type.__name__ = "TmnxSysNeid"
_TmnxSysNEProfNeid_Object = MibTableColumn
tmnxSysNEProfNeid = _TmnxSysNEProfNeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 47, 2, 1, 4),
    _TmnxSysNEProfNeid_Type()
)
tmnxSysNEProfNeid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysNEProfNeid.setStatus("current")


class _TmnxSysNEProfNeipV4Type_Type(InetAddressType):
    """Custom type tmnxSysNEProfNeipV4Type based on InetAddressType"""
    defaultValue = 0


_TmnxSysNEProfNeipV4Type_Type.__name__ = "InetAddressType"
_TmnxSysNEProfNeipV4Type_Object = MibTableColumn
tmnxSysNEProfNeipV4Type = _TmnxSysNEProfNeipV4Type_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 47, 2, 1, 5),
    _TmnxSysNEProfNeipV4Type_Type()
)
tmnxSysNEProfNeipV4Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysNEProfNeipV4Type.setStatus("current")


class _TmnxSysNEProfNeipV4_Type(InetAddress):
    """Custom type tmnxSysNEProfNeipV4 based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxSysNEProfNeipV4_Type.__name__ = "InetAddress"
_TmnxSysNEProfNeipV4_Object = MibTableColumn
tmnxSysNEProfNeipV4 = _TmnxSysNEProfNeipV4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 47, 2, 1, 6),
    _TmnxSysNEProfNeipV4_Type()
)
tmnxSysNEProfNeipV4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysNEProfNeipV4.setStatus("current")


class _TmnxSysNEProfNeipV6Type_Type(InetAddressType):
    """Custom type tmnxSysNEProfNeipV6Type based on InetAddressType"""
    defaultValue = 0


_TmnxSysNEProfNeipV6Type_Type.__name__ = "InetAddressType"
_TmnxSysNEProfNeipV6Type_Object = MibTableColumn
tmnxSysNEProfNeipV6Type = _TmnxSysNEProfNeipV6Type_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 47, 2, 1, 7),
    _TmnxSysNEProfNeipV6Type_Type()
)
tmnxSysNEProfNeipV6Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysNEProfNeipV6Type.setStatus("current")


class _TmnxSysNEProfNeipV6_Type(InetAddress):
    """Custom type tmnxSysNEProfNeipV6 based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxSysNEProfNeipV6_Type.__name__ = "InetAddress"
_TmnxSysNEProfNeipV6_Object = MibTableColumn
tmnxSysNEProfNeipV6 = _TmnxSysNEProfNeipV6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 47, 2, 1, 8),
    _TmnxSysNEProfNeipV6_Type()
)
tmnxSysNEProfNeipV6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysNEProfNeipV6.setStatus("current")


class _TmnxSysNEProfSystemMac_Type(MacAddress):
    """Custom type tmnxSysNEProfSystemMac based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxSysNEProfSystemMac_Type.__name__ = "MacAddress"
_TmnxSysNEProfSystemMac_Object = MibTableColumn
tmnxSysNEProfSystemMac = _TmnxSysNEProfSystemMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 47, 2, 1, 9),
    _TmnxSysNEProfSystemMac_Type()
)
tmnxSysNEProfSystemMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysNEProfSystemMac.setStatus("current")


class _TmnxSysNEProfPlatformType_Type(DisplayString):
    """Custom type tmnxSysNEProfPlatformType based on DisplayString"""
    defaultHexValue = ""


_TmnxSysNEProfPlatformType_Type.__name__ = "DisplayString"
_TmnxSysNEProfPlatformType_Object = MibTableColumn
tmnxSysNEProfPlatformType = _TmnxSysNEProfPlatformType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 47, 2, 1, 10),
    _TmnxSysNEProfPlatformType_Type()
)
tmnxSysNEProfPlatformType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysNEProfPlatformType.setStatus("current")


class _TmnxSysNEProfVendorId_Type(DisplayString):
    """Custom type tmnxSysNEProfVendorId based on DisplayString"""
    defaultValue = OctetString("Nokia")


_TmnxSysNEProfVendorId_Type.__name__ = "DisplayString"
_TmnxSysNEProfVendorId_Object = MibTableColumn
tmnxSysNEProfVendorId = _TmnxSysNEProfVendorId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 47, 2, 1, 11),
    _TmnxSysNEProfVendorId_Type()
)
tmnxSysNEProfVendorId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysNEProfVendorId.setStatus("current")


class _TmnxSysNEProfNeipV4AutoGenerate_Type(TruthValue):
    """Custom type tmnxSysNEProfNeipV4AutoGenerate based on TruthValue"""
    defaultValue = 2


_TmnxSysNEProfNeipV4AutoGenerate_Type.__name__ = "TruthValue"
_TmnxSysNEProfNeipV4AutoGenerate_Object = MibTableColumn
tmnxSysNEProfNeipV4AutoGenerate = _TmnxSysNEProfNeipV4AutoGenerate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 47, 2, 1, 12),
    _TmnxSysNEProfNeipV4AutoGenerate_Type()
)
tmnxSysNEProfNeipV4AutoGenerate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysNEProfNeipV4AutoGenerate.setStatus("current")


class _TmnxSysNEProfNeipV4NeidVendorId_Type(Unsigned32):
    """Custom type tmnxSysNEProfNeipV4NeidVendorId based on Unsigned32"""
    defaultValue = 140

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxSysNEProfNeipV4NeidVendorId_Type.__name__ = "Unsigned32"
_TmnxSysNEProfNeipV4NeidVendorId_Object = MibTableColumn
tmnxSysNEProfNeipV4NeidVendorId = _TmnxSysNEProfNeipV4NeidVendorId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 47, 2, 1, 13),
    _TmnxSysNEProfNeipV4NeidVendorId_Type()
)
tmnxSysNEProfNeipV4NeidVendorId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysNEProfNeipV4NeidVendorId.setStatus("current")


class _TmnxSysNEProfNeipV6AutoGenerate_Type(TruthValue):
    """Custom type tmnxSysNEProfNeipV6AutoGenerate based on TruthValue"""
    defaultValue = 2


_TmnxSysNEProfNeipV6AutoGenerate_Type.__name__ = "TruthValue"
_TmnxSysNEProfNeipV6AutoGenerate_Object = MibTableColumn
tmnxSysNEProfNeipV6AutoGenerate = _TmnxSysNEProfNeipV6AutoGenerate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 47, 2, 1, 14),
    _TmnxSysNEProfNeipV6AutoGenerate_Type()
)
tmnxSysNEProfNeipV6AutoGenerate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysNEProfNeipV6AutoGenerate.setStatus("current")


class _TmnxSysNEProfNeipV6NeidVendorId_Type(Unsigned32):
    """Custom type tmnxSysNEProfNeipV6NeidVendorId based on Unsigned32"""
    defaultValue = 140

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxSysNEProfNeipV6NeidVendorId_Type.__name__ = "Unsigned32"
_TmnxSysNEProfNeipV6NeidVendorId_Object = MibTableColumn
tmnxSysNEProfNeipV6NeidVendorId = _TmnxSysNEProfNeipV6NeidVendorId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 47, 2, 1, 15),
    _TmnxSysNEProfNeipV6NeidVendorId_Type()
)
tmnxSysNEProfNeipV6NeidVendorId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysNEProfNeipV6NeidVendorId.setStatus("current")


class _TmnxSysNEDiscoveryGenerateTraps_Type(TruthValue):
    """Custom type tmnxSysNEDiscoveryGenerateTraps based on TruthValue"""
    defaultValue = 2


_TmnxSysNEDiscoveryGenerateTraps_Type.__name__ = "TruthValue"
_TmnxSysNEDiscoveryGenerateTraps_Object = MibScalar
tmnxSysNEDiscoveryGenerateTraps = _TmnxSysNEDiscoveryGenerateTraps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 47, 3),
    _TmnxSysNEDiscoveryGenerateTraps_Type()
)
tmnxSysNEDiscoveryGenerateTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysNEDiscoveryGenerateTraps.setStatus("current")
_TmnxSysFwdPathOptsObjs_ObjectIdentity = ObjectIdentity
tmnxSysFwdPathOptsObjs = _TmnxSysFwdPathOptsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48)
)


class _TmnxSysFpoDscpTransAdminState_Type(TmnxAdminState):
    """Custom type tmnxSysFpoDscpTransAdminState based on TmnxAdminState"""
    defaultValue = 2


_TmnxSysFpoDscpTransAdminState_Type.__name__ = "TmnxAdminState"
_TmnxSysFpoDscpTransAdminState_Object = MibScalar
tmnxSysFpoDscpTransAdminState = _TmnxSysFpoDscpTransAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 1),
    _TmnxSysFpoDscpTransAdminState_Type()
)
tmnxSysFpoDscpTransAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpoDscpTransAdminState.setStatus("current")
_TmnxSysFpoDscpTransOperState_Type = TmnxOperState
_TmnxSysFpoDscpTransOperState_Object = MibScalar
tmnxSysFpoDscpTransOperState = _TmnxSysFpoDscpTransOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 2),
    _TmnxSysFpoDscpTransOperState_Type()
)
tmnxSysFpoDscpTransOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpoDscpTransOperState.setStatus("current")


class _TmnxSysFpoEntropyLabelAdminState_Type(TmnxAdminState):
    """Custom type tmnxSysFpoEntropyLabelAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxSysFpoEntropyLabelAdminState_Type.__name__ = "TmnxAdminState"
_TmnxSysFpoEntropyLabelAdminState_Object = MibScalar
tmnxSysFpoEntropyLabelAdminState = _TmnxSysFpoEntropyLabelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 3),
    _TmnxSysFpoEntropyLabelAdminState_Type()
)
tmnxSysFpoEntropyLabelAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpoEntropyLabelAdminState.setStatus("current")
_TmnxSysFpoEntropyLabelOperState_Type = TmnxOperState
_TmnxSysFpoEntropyLabelOperState_Object = MibScalar
tmnxSysFpoEntropyLabelOperState = _TmnxSysFpoEntropyLabelOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 4),
    _TmnxSysFpoEntropyLabelOperState_Type()
)
tmnxSysFpoEntropyLabelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpoEntropyLabelOperState.setStatus("current")


class _TmnxSysFpoMacFltOutVlanPrioAdmSt_Type(TmnxAdminState):
    """Custom type tmnxSysFpoMacFltOutVlanPrioAdmSt based on TmnxAdminState"""
    defaultValue = 3


_TmnxSysFpoMacFltOutVlanPrioAdmSt_Type.__name__ = "TmnxAdminState"
_TmnxSysFpoMacFltOutVlanPrioAdmSt_Object = MibScalar
tmnxSysFpoMacFltOutVlanPrioAdmSt = _TmnxSysFpoMacFltOutVlanPrioAdmSt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 5),
    _TmnxSysFpoMacFltOutVlanPrioAdmSt_Type()
)
tmnxSysFpoMacFltOutVlanPrioAdmSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpoMacFltOutVlanPrioAdmSt.setStatus("obsolete")
_TmnxSysFpoMacFltOutVlanPrioOprSt_Type = TmnxOperState
_TmnxSysFpoMacFltOutVlanPrioOprSt_Object = MibScalar
tmnxSysFpoMacFltOutVlanPrioOprSt = _TmnxSysFpoMacFltOutVlanPrioOprSt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 6),
    _TmnxSysFpoMacFltOutVlanPrioOprSt_Type()
)
tmnxSysFpoMacFltOutVlanPrioOprSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpoMacFltOutVlanPrioOprSt.setStatus("obsolete")


class _TmnxSysFpoVplsEvpnMplsAdminState_Type(TmnxAdminState):
    """Custom type tmnxSysFpoVplsEvpnMplsAdminState based on TmnxAdminState"""
    defaultValue = 2


_TmnxSysFpoVplsEvpnMplsAdminState_Type.__name__ = "TmnxAdminState"
_TmnxSysFpoVplsEvpnMplsAdminState_Object = MibScalar
tmnxSysFpoVplsEvpnMplsAdminState = _TmnxSysFpoVplsEvpnMplsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 7),
    _TmnxSysFpoVplsEvpnMplsAdminState_Type()
)
tmnxSysFpoVplsEvpnMplsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpoVplsEvpnMplsAdminState.setStatus("current")
_TmnxSysFpoVplsEvpnMplsOperState_Type = TmnxOperState
_TmnxSysFpoVplsEvpnMplsOperState_Object = MibScalar
tmnxSysFpoVplsEvpnMplsOperState = _TmnxSysFpoVplsEvpnMplsOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 8),
    _TmnxSysFpoVplsEvpnMplsOperState_Type()
)
tmnxSysFpoVplsEvpnMplsOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpoVplsEvpnMplsOperState.setStatus("current")


class _TmnxSysFpoQosFc4ProfAdminState_Type(TmnxAdminState):
    """Custom type tmnxSysFpoQosFc4ProfAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxSysFpoQosFc4ProfAdminState_Type.__name__ = "TmnxAdminState"
_TmnxSysFpoQosFc4ProfAdminState_Object = MibScalar
tmnxSysFpoQosFc4ProfAdminState = _TmnxSysFpoQosFc4ProfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 9),
    _TmnxSysFpoQosFc4ProfAdminState_Type()
)
tmnxSysFpoQosFc4ProfAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpoQosFc4ProfAdminState.setStatus("current")
_TmnxSysFpoQosFc4ProfOperState_Type = TmnxOperState
_TmnxSysFpoQosFc4ProfOperState_Object = MibScalar
tmnxSysFpoQosFc4ProfOperState = _TmnxSysFpoQosFc4ProfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 10),
    _TmnxSysFpoQosFc4ProfOperState_Type()
)
tmnxSysFpoQosFc4ProfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpoQosFc4ProfOperState.setStatus("current")


class _TmnxSysFpoMplsFastSwOvAdminState_Type(TmnxAdminState):
    """Custom type tmnxSysFpoMplsFastSwOvAdminState based on TmnxAdminState"""
    defaultValue = 2


_TmnxSysFpoMplsFastSwOvAdminState_Type.__name__ = "TmnxAdminState"
_TmnxSysFpoMplsFastSwOvAdminState_Object = MibScalar
tmnxSysFpoMplsFastSwOvAdminState = _TmnxSysFpoMplsFastSwOvAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 11),
    _TmnxSysFpoMplsFastSwOvAdminState_Type()
)
tmnxSysFpoMplsFastSwOvAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpoMplsFastSwOvAdminState.setStatus("current")
_TmnxSysFpoMplsFastSwOvOperState_Type = TmnxOperState
_TmnxSysFpoMplsFastSwOvOperState_Object = MibScalar
tmnxSysFpoMplsFastSwOvOperState = _TmnxSysFpoMplsFastSwOvOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 12),
    _TmnxSysFpoMplsFastSwOvOperState_Type()
)
tmnxSysFpoMplsFastSwOvOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpoMplsFastSwOvOperState.setStatus("current")


class _TmnxSysFpoRouterEcmpAdminState_Type(TmnxAdminState):
    """Custom type tmnxSysFpoRouterEcmpAdminState based on TmnxAdminState"""
    defaultValue = 2


_TmnxSysFpoRouterEcmpAdminState_Type.__name__ = "TmnxAdminState"
_TmnxSysFpoRouterEcmpAdminState_Object = MibScalar
tmnxSysFpoRouterEcmpAdminState = _TmnxSysFpoRouterEcmpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 13),
    _TmnxSysFpoRouterEcmpAdminState_Type()
)
tmnxSysFpoRouterEcmpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpoRouterEcmpAdminState.setStatus("current")
_TmnxSysFpoRouterEcmpOperState_Type = TmnxOperState
_TmnxSysFpoRouterEcmpOperState_Object = MibScalar
tmnxSysFpoRouterEcmpOperState = _TmnxSysFpoRouterEcmpOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 14),
    _TmnxSysFpoRouterEcmpOperState_Type()
)
tmnxSysFpoRouterEcmpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpoRouterEcmpOperState.setStatus("current")


class _TmnxSysFpoQosMacCritAdminState_Type(TmnxAdminState):
    """Custom type tmnxSysFpoQosMacCritAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxSysFpoQosMacCritAdminState_Type.__name__ = "TmnxAdminState"
_TmnxSysFpoQosMacCritAdminState_Object = MibScalar
tmnxSysFpoQosMacCritAdminState = _TmnxSysFpoQosMacCritAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 15),
    _TmnxSysFpoQosMacCritAdminState_Type()
)
tmnxSysFpoQosMacCritAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpoQosMacCritAdminState.setStatus("current")
_TmnxSysFpoQosMacCritOperState_Type = TmnxOperState
_TmnxSysFpoQosMacCritOperState_Object = MibScalar
tmnxSysFpoQosMacCritOperState = _TmnxSysFpoQosMacCritOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 16),
    _TmnxSysFpoQosMacCritOperState_Type()
)
tmnxSysFpoQosMacCritOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpoQosMacCritOperState.setStatus("current")


class _TmnxSysFpoQosIpv6CritAdminState_Type(TmnxAdminState):
    """Custom type tmnxSysFpoQosIpv6CritAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxSysFpoQosIpv6CritAdminState_Type.__name__ = "TmnxAdminState"
_TmnxSysFpoQosIpv6CritAdminState_Object = MibScalar
tmnxSysFpoQosIpv6CritAdminState = _TmnxSysFpoQosIpv6CritAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 17),
    _TmnxSysFpoQosIpv6CritAdminState_Type()
)
tmnxSysFpoQosIpv6CritAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpoQosIpv6CritAdminState.setStatus("current")
_TmnxSysFpoQosIpv6CritOperState_Type = TmnxOperState
_TmnxSysFpoQosIpv6CritOperState_Object = MibScalar
tmnxSysFpoQosIpv6CritOperState = _TmnxSysFpoQosIpv6CritOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 18),
    _TmnxSysFpoQosIpv6CritOperState_Type()
)
tmnxSysFpoQosIpv6CritOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpoQosIpv6CritOperState.setStatus("current")


class _TmnxSysFpoQosBumPolAdminState_Type(TmnxAdminState):
    """Custom type tmnxSysFpoQosBumPolAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxSysFpoQosBumPolAdminState_Type.__name__ = "TmnxAdminState"
_TmnxSysFpoQosBumPolAdminState_Object = MibScalar
tmnxSysFpoQosBumPolAdminState = _TmnxSysFpoQosBumPolAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 19),
    _TmnxSysFpoQosBumPolAdminState_Type()
)
tmnxSysFpoQosBumPolAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpoQosBumPolAdminState.setStatus("current")
_TmnxSysFpoQosBumPolOperState_Type = TmnxOperState
_TmnxSysFpoQosBumPolOperState_Object = MibScalar
tmnxSysFpoQosBumPolOperState = _TmnxSysFpoQosBumPolOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 20),
    _TmnxSysFpoQosBumPolOperState_Type()
)
tmnxSysFpoQosBumPolOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpoQosBumPolOperState.setStatus("current")


class _TmnxSysFpoLpmAlcnScl1AdminState_Type(TmnxAdminState):
    """Custom type tmnxSysFpoLpmAlcnScl1AdminState based on TmnxAdminState"""
    defaultValue = 2


_TmnxSysFpoLpmAlcnScl1AdminState_Type.__name__ = "TmnxAdminState"
_TmnxSysFpoLpmAlcnScl1AdminState_Object = MibScalar
tmnxSysFpoLpmAlcnScl1AdminState = _TmnxSysFpoLpmAlcnScl1AdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 21),
    _TmnxSysFpoLpmAlcnScl1AdminState_Type()
)
tmnxSysFpoLpmAlcnScl1AdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpoLpmAlcnScl1AdminState.setStatus("obsolete")
_TmnxSysFpoLpmAlcnScl1OperState_Type = TmnxOperState
_TmnxSysFpoLpmAlcnScl1OperState_Object = MibScalar
tmnxSysFpoLpmAlcnScl1OperState = _TmnxSysFpoLpmAlcnScl1OperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 22),
    _TmnxSysFpoLpmAlcnScl1OperState_Type()
)
tmnxSysFpoLpmAlcnScl1OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpoLpmAlcnScl1OperState.setStatus("obsolete")


class _TmnxSysFpoLpmAlcnScl2AdminState_Type(TmnxAdminState):
    """Custom type tmnxSysFpoLpmAlcnScl2AdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxSysFpoLpmAlcnScl2AdminState_Type.__name__ = "TmnxAdminState"
_TmnxSysFpoLpmAlcnScl2AdminState_Object = MibScalar
tmnxSysFpoLpmAlcnScl2AdminState = _TmnxSysFpoLpmAlcnScl2AdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 23),
    _TmnxSysFpoLpmAlcnScl2AdminState_Type()
)
tmnxSysFpoLpmAlcnScl2AdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpoLpmAlcnScl2AdminState.setStatus("obsolete")
_TmnxSysFpoLpmAlcnScl2OperState_Type = TmnxOperState
_TmnxSysFpoLpmAlcnScl2OperState_Object = MibScalar
tmnxSysFpoLpmAlcnScl2OperState = _TmnxSysFpoLpmAlcnScl2OperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 24),
    _TmnxSysFpoLpmAlcnScl2OperState_Type()
)
tmnxSysFpoLpmAlcnScl2OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpoLpmAlcnScl2OperState.setStatus("obsolete")


class _TmnxSysFpoLpmAlcnScl3AdminState_Type(TmnxAdminState):
    """Custom type tmnxSysFpoLpmAlcnScl3AdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxSysFpoLpmAlcnScl3AdminState_Type.__name__ = "TmnxAdminState"
_TmnxSysFpoLpmAlcnScl3AdminState_Object = MibScalar
tmnxSysFpoLpmAlcnScl3AdminState = _TmnxSysFpoLpmAlcnScl3AdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 25),
    _TmnxSysFpoLpmAlcnScl3AdminState_Type()
)
tmnxSysFpoLpmAlcnScl3AdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpoLpmAlcnScl3AdminState.setStatus("obsolete")
_TmnxSysFpoLpmAlcnScl3OperState_Type = TmnxOperState
_TmnxSysFpoLpmAlcnScl3OperState_Object = MibScalar
tmnxSysFpoLpmAlcnScl3OperState = _TmnxSysFpoLpmAlcnScl3OperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 26),
    _TmnxSysFpoLpmAlcnScl3OperState_Type()
)
tmnxSysFpoLpmAlcnScl3OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpoLpmAlcnScl3OperState.setStatus("obsolete")


class _TmnxSysFpoDot1xHostAuthAdmState_Type(TmnxAdminState):
    """Custom type tmnxSysFpoDot1xHostAuthAdmState based on TmnxAdminState"""
    defaultValue = 3


_TmnxSysFpoDot1xHostAuthAdmState_Type.__name__ = "TmnxAdminState"
_TmnxSysFpoDot1xHostAuthAdmState_Object = MibScalar
tmnxSysFpoDot1xHostAuthAdmState = _TmnxSysFpoDot1xHostAuthAdmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 27),
    _TmnxSysFpoDot1xHostAuthAdmState_Type()
)
tmnxSysFpoDot1xHostAuthAdmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpoDot1xHostAuthAdmState.setStatus("current")
_TmnxSysFpoDot1xHostAuthOperState_Type = TmnxOperState
_TmnxSysFpoDot1xHostAuthOperState_Object = MibScalar
tmnxSysFpoDot1xHostAuthOperState = _TmnxSysFpoDot1xHostAuthOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 28),
    _TmnxSysFpoDot1xHostAuthOperState_Type()
)
tmnxSysFpoDot1xHostAuthOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpoDot1xHostAuthOperState.setStatus("current")


class _TmnxSysFpoIpv6FltrEgrAdminState_Type(TmnxAdminState):
    """Custom type tmnxSysFpoIpv6FltrEgrAdminState based on TmnxAdminState"""
    defaultValue = 2


_TmnxSysFpoIpv6FltrEgrAdminState_Type.__name__ = "TmnxAdminState"
_TmnxSysFpoIpv6FltrEgrAdminState_Object = MibScalar
tmnxSysFpoIpv6FltrEgrAdminState = _TmnxSysFpoIpv6FltrEgrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 29),
    _TmnxSysFpoIpv6FltrEgrAdminState_Type()
)
tmnxSysFpoIpv6FltrEgrAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpoIpv6FltrEgrAdminState.setStatus("current")
_TmnxSysFpoIpv6FltrEgrOperState_Type = TmnxOperState
_TmnxSysFpoIpv6FltrEgrOperState_Object = MibScalar
tmnxSysFpoIpv6FltrEgrOperState = _TmnxSysFpoIpv6FltrEgrOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 30),
    _TmnxSysFpoIpv6FltrEgrOperState_Type()
)
tmnxSysFpoIpv6FltrEgrOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpoIpv6FltrEgrOperState.setStatus("current")


class _TmnxSysFpoIpv6FltrNxtHdrAdmState_Type(TmnxAdminState):
    """Custom type tmnxSysFpoIpv6FltrNxtHdrAdmState based on TmnxAdminState"""
    defaultValue = 2


_TmnxSysFpoIpv6FltrNxtHdrAdmState_Type.__name__ = "TmnxAdminState"
_TmnxSysFpoIpv6FltrNxtHdrAdmState_Object = MibScalar
tmnxSysFpoIpv6FltrNxtHdrAdmState = _TmnxSysFpoIpv6FltrNxtHdrAdmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 31),
    _TmnxSysFpoIpv6FltrNxtHdrAdmState_Type()
)
tmnxSysFpoIpv6FltrNxtHdrAdmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpoIpv6FltrNxtHdrAdmState.setStatus("current")
_TmnxSysFpoIpv6FltrNxtHdrOprState_Type = TmnxOperState
_TmnxSysFpoIpv6FltrNxtHdrOprState_Object = MibScalar
tmnxSysFpoIpv6FltrNxtHdrOprState = _TmnxSysFpoIpv6FltrNxtHdrOprState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 32),
    _TmnxSysFpoIpv6FltrNxtHdrOprState_Type()
)
tmnxSysFpoIpv6FltrNxtHdrOprState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpoIpv6FltrNxtHdrOprState.setStatus("current")


class _TmnxSysFpoIpv6FltrDstPrtAdmState_Type(TmnxAdminState):
    """Custom type tmnxSysFpoIpv6FltrDstPrtAdmState based on TmnxAdminState"""
    defaultValue = 2


_TmnxSysFpoIpv6FltrDstPrtAdmState_Type.__name__ = "TmnxAdminState"
_TmnxSysFpoIpv6FltrDstPrtAdmState_Object = MibScalar
tmnxSysFpoIpv6FltrDstPrtAdmState = _TmnxSysFpoIpv6FltrDstPrtAdmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 33),
    _TmnxSysFpoIpv6FltrDstPrtAdmState_Type()
)
tmnxSysFpoIpv6FltrDstPrtAdmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpoIpv6FltrDstPrtAdmState.setStatus("current")
_TmnxSysFpoIpv6FltrDstPrtOprState_Type = TmnxOperState
_TmnxSysFpoIpv6FltrDstPrtOprState_Object = MibScalar
tmnxSysFpoIpv6FltrDstPrtOprState = _TmnxSysFpoIpv6FltrDstPrtOprState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 34),
    _TmnxSysFpoIpv6FltrDstPrtOprState_Type()
)
tmnxSysFpoIpv6FltrDstPrtOprState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpoIpv6FltrDstPrtOprState.setStatus("current")


class _TmnxSysFpoIpv6FltrSrcPrtAdmState_Type(TmnxAdminState):
    """Custom type tmnxSysFpoIpv6FltrSrcPrtAdmState based on TmnxAdminState"""
    defaultValue = 2


_TmnxSysFpoIpv6FltrSrcPrtAdmState_Type.__name__ = "TmnxAdminState"
_TmnxSysFpoIpv6FltrSrcPrtAdmState_Object = MibScalar
tmnxSysFpoIpv6FltrSrcPrtAdmState = _TmnxSysFpoIpv6FltrSrcPrtAdmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 35),
    _TmnxSysFpoIpv6FltrSrcPrtAdmState_Type()
)
tmnxSysFpoIpv6FltrSrcPrtAdmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpoIpv6FltrSrcPrtAdmState.setStatus("current")
_TmnxSysFpoIpv6FltrSrcPrtOprState_Type = TmnxOperState
_TmnxSysFpoIpv6FltrSrcPrtOprState_Object = MibScalar
tmnxSysFpoIpv6FltrSrcPrtOprState = _TmnxSysFpoIpv6FltrSrcPrtOprState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 36),
    _TmnxSysFpoIpv6FltrSrcPrtOprState_Type()
)
tmnxSysFpoIpv6FltrSrcPrtOprState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpoIpv6FltrSrcPrtOprState.setStatus("current")


class _TmnxSysFpoIpv6FltrDstIpLsbAdmSt_Type(TmnxAdminState):
    """Custom type tmnxSysFpoIpv6FltrDstIpLsbAdmSt based on TmnxAdminState"""
    defaultValue = 3


_TmnxSysFpoIpv6FltrDstIpLsbAdmSt_Type.__name__ = "TmnxAdminState"
_TmnxSysFpoIpv6FltrDstIpLsbAdmSt_Object = MibScalar
tmnxSysFpoIpv6FltrDstIpLsbAdmSt = _TmnxSysFpoIpv6FltrDstIpLsbAdmSt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 37),
    _TmnxSysFpoIpv6FltrDstIpLsbAdmSt_Type()
)
tmnxSysFpoIpv6FltrDstIpLsbAdmSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpoIpv6FltrDstIpLsbAdmSt.setStatus("current")
_TmnxSysFpoIpv6FltrDstIpLsbOprSt_Type = TmnxOperState
_TmnxSysFpoIpv6FltrDstIpLsbOprSt_Object = MibScalar
tmnxSysFpoIpv6FltrDstIpLsbOprSt = _TmnxSysFpoIpv6FltrDstIpLsbOprSt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 38),
    _TmnxSysFpoIpv6FltrDstIpLsbOprSt_Type()
)
tmnxSysFpoIpv6FltrDstIpLsbOprSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpoIpv6FltrDstIpLsbOprSt.setStatus("current")


class _TmnxSysFpoIpv6FltrTcpFlgAdmState_Type(TmnxAdminState):
    """Custom type tmnxSysFpoIpv6FltrTcpFlgAdmState based on TmnxAdminState"""
    defaultValue = 2


_TmnxSysFpoIpv6FltrTcpFlgAdmState_Type.__name__ = "TmnxAdminState"
_TmnxSysFpoIpv6FltrTcpFlgAdmState_Object = MibScalar
tmnxSysFpoIpv6FltrTcpFlgAdmState = _TmnxSysFpoIpv6FltrTcpFlgAdmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 39),
    _TmnxSysFpoIpv6FltrTcpFlgAdmState_Type()
)
tmnxSysFpoIpv6FltrTcpFlgAdmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpoIpv6FltrTcpFlgAdmState.setStatus("current")
_TmnxSysFpoIpv6FltrTcpFlgOprState_Type = TmnxOperState
_TmnxSysFpoIpv6FltrTcpFlgOprState_Object = MibScalar
tmnxSysFpoIpv6FltrTcpFlgOprState = _TmnxSysFpoIpv6FltrTcpFlgOprState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 40),
    _TmnxSysFpoIpv6FltrTcpFlgOprState_Type()
)
tmnxSysFpoIpv6FltrTcpFlgOprState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpoIpv6FltrTcpFlgOprState.setStatus("current")


class _TmnxSysFpoIpv6FltStatColAdmState_Type(TmnxAdminState):
    """Custom type tmnxSysFpoIpv6FltStatColAdmState based on TmnxAdminState"""
    defaultValue = 2


_TmnxSysFpoIpv6FltStatColAdmState_Type.__name__ = "TmnxAdminState"
_TmnxSysFpoIpv6FltStatColAdmState_Object = MibScalar
tmnxSysFpoIpv6FltStatColAdmState = _TmnxSysFpoIpv6FltStatColAdmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 41),
    _TmnxSysFpoIpv6FltStatColAdmState_Type()
)
tmnxSysFpoIpv6FltStatColAdmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpoIpv6FltStatColAdmState.setStatus("current")
_TmnxSysFpoIpv6FltStatColOprState_Type = TmnxOperState
_TmnxSysFpoIpv6FltStatColOprState_Object = MibScalar
tmnxSysFpoIpv6FltStatColOprState = _TmnxSysFpoIpv6FltStatColOprState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 42),
    _TmnxSysFpoIpv6FltStatColOprState_Type()
)
tmnxSysFpoIpv6FltStatColOprState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpoIpv6FltStatColOprState.setStatus("current")


class _TmnxSysFpoIpv4FltStatColAdmState_Type(TmnxAdminState):
    """Custom type tmnxSysFpoIpv4FltStatColAdmState based on TmnxAdminState"""
    defaultValue = 2


_TmnxSysFpoIpv4FltStatColAdmState_Type.__name__ = "TmnxAdminState"
_TmnxSysFpoIpv4FltStatColAdmState_Object = MibScalar
tmnxSysFpoIpv4FltStatColAdmState = _TmnxSysFpoIpv4FltStatColAdmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 43),
    _TmnxSysFpoIpv4FltStatColAdmState_Type()
)
tmnxSysFpoIpv4FltStatColAdmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpoIpv4FltStatColAdmState.setStatus("current")
_TmnxSysFpoIpv4FltStatColOprState_Type = TmnxOperState
_TmnxSysFpoIpv4FltStatColOprState_Object = MibScalar
tmnxSysFpoIpv4FltStatColOprState = _TmnxSysFpoIpv4FltStatColOprState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 44),
    _TmnxSysFpoIpv4FltStatColOprState_Type()
)
tmnxSysFpoIpv4FltStatColOprState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpoIpv4FltStatColOprState.setStatus("current")


class _TmnxSysFpoIpv4FltPbrRdrtAdmState_Type(TmnxAdminState):
    """Custom type tmnxSysFpoIpv4FltPbrRdrtAdmState based on TmnxAdminState"""
    defaultValue = 3


_TmnxSysFpoIpv4FltPbrRdrtAdmState_Type.__name__ = "TmnxAdminState"
_TmnxSysFpoIpv4FltPbrRdrtAdmState_Object = MibScalar
tmnxSysFpoIpv4FltPbrRdrtAdmState = _TmnxSysFpoIpv4FltPbrRdrtAdmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 45),
    _TmnxSysFpoIpv4FltPbrRdrtAdmState_Type()
)
tmnxSysFpoIpv4FltPbrRdrtAdmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpoIpv4FltPbrRdrtAdmState.setStatus("current")
_TmnxSysFpoIpv4FltPbrRdrtOprState_Type = TmnxOperState
_TmnxSysFpoIpv4FltPbrRdrtOprState_Object = MibScalar
tmnxSysFpoIpv4FltPbrRdrtOprState = _TmnxSysFpoIpv4FltPbrRdrtOprState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 46),
    _TmnxSysFpoIpv4FltPbrRdrtOprState_Type()
)
tmnxSysFpoIpv4FltPbrRdrtOprState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpoIpv4FltPbrRdrtOprState.setStatus("current")


class _TmnxSysFpoIpv6FltPbrRdrtAdmState_Type(TmnxAdminState):
    """Custom type tmnxSysFpoIpv6FltPbrRdrtAdmState based on TmnxAdminState"""
    defaultValue = 3


_TmnxSysFpoIpv6FltPbrRdrtAdmState_Type.__name__ = "TmnxAdminState"
_TmnxSysFpoIpv6FltPbrRdrtAdmState_Object = MibScalar
tmnxSysFpoIpv6FltPbrRdrtAdmState = _TmnxSysFpoIpv6FltPbrRdrtAdmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 47),
    _TmnxSysFpoIpv6FltPbrRdrtAdmState_Type()
)
tmnxSysFpoIpv6FltPbrRdrtAdmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpoIpv6FltPbrRdrtAdmState.setStatus("current")
_TmnxSysFpoIpv6FltPbrRdrtOprState_Type = TmnxOperState
_TmnxSysFpoIpv6FltPbrRdrtOprState_Object = MibScalar
tmnxSysFpoIpv6FltPbrRdrtOprState = _TmnxSysFpoIpv6FltPbrRdrtOprState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 48),
    _TmnxSysFpoIpv6FltPbrRdrtOprState_Type()
)
tmnxSysFpoIpv6FltPbrRdrtOprState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpoIpv6FltPbrRdrtOprState.setStatus("current")


class _TmnxSysFpoRingApsAdminState_Type(TmnxAdminState):
    """Custom type tmnxSysFpoRingApsAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxSysFpoRingApsAdminState_Type.__name__ = "TmnxAdminState"
_TmnxSysFpoRingApsAdminState_Object = MibScalar
tmnxSysFpoRingApsAdminState = _TmnxSysFpoRingApsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 49),
    _TmnxSysFpoRingApsAdminState_Type()
)
tmnxSysFpoRingApsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpoRingApsAdminState.setStatus("current")
_TmnxSysFpoRingApsOperState_Type = TmnxOperState
_TmnxSysFpoRingApsOperState_Object = MibScalar
tmnxSysFpoRingApsOperState = _TmnxSysFpoRingApsOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 48, 50),
    _TmnxSysFpoRingApsOperState_Type()
)
tmnxSysFpoRingApsOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpoRingApsOperState.setStatus("current")
_TmnxSysSwitchFabricObjs_ObjectIdentity = ObjectIdentity
tmnxSysSwitchFabricObjs = _TmnxSysSwitchFabricObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 49)
)


class _TmnxSysSwFabSfmLossThresh_Type(Unsigned32):
    """Custom type tmnxSysSwFabSfmLossThresh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TmnxSysSwFabSfmLossThresh_Type.__name__ = "Unsigned32"
_TmnxSysSwFabSfmLossThresh_Object = MibScalar
tmnxSysSwFabSfmLossThresh = _TmnxSysSwFabSfmLossThresh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 49, 1),
    _TmnxSysSwFabSfmLossThresh_Type()
)
tmnxSysSwFabSfmLossThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysSwFabSfmLossThresh.setStatus("current")


class _TmnxSysSwFabFailRecAdminState_Type(TmnxEnabledDisabledAdminState):
    """Custom type tmnxSysSwFabFailRecAdminState based on TmnxEnabledDisabledAdminState"""
    defaultValue = 2


_TmnxSysSwFabFailRecAdminState_Type.__name__ = "TmnxEnabledDisabledAdminState"
_TmnxSysSwFabFailRecAdminState_Object = MibScalar
tmnxSysSwFabFailRecAdminState = _TmnxSysSwFabFailRecAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 49, 2),
    _TmnxSysSwFabFailRecAdminState_Type()
)
tmnxSysSwFabFailRecAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysSwFabFailRecAdminState.setStatus("current")


class _TmnxSysSwFabFailRecOperState_Type(Integer32):
    """Custom type tmnxSysSwFabFailRecOperState based on Integer32"""
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
        *(("disabled", 0),
          ("holdDown", 1),
          ("ready", 2),
          ("recoveryInProgress", 3),
          ("detectedDisabled", 4),
          ("detectedHoldDown", 5),
          ("detectedXRS40Migration", 6),
          ("detectedSFMUpgradePending", 7))
    )


_TmnxSysSwFabFailRecOperState_Type.__name__ = "Integer32"
_TmnxSysSwFabFailRecOperState_Object = MibScalar
tmnxSysSwFabFailRecOperState = _TmnxSysSwFabFailRecOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 49, 3),
    _TmnxSysSwFabFailRecOperState_Type()
)
tmnxSysSwFabFailRecOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysSwFabFailRecOperState.setStatus("current")
_TmnxSysUsbTable_Object = MibTable
tmnxSysUsbTable = _TmnxSysUsbTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 50)
)
if mibBuilder.loadTexts:
    tmnxSysUsbTable.setStatus("current")
_TmnxSysUsbEntry_Object = MibTableRow
tmnxSysUsbEntry = _TmnxSysUsbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 50, 1)
)
tmnxSysUsbEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysUsbCFlashId"),
)
if mibBuilder.loadTexts:
    tmnxSysUsbEntry.setStatus("current")


class _TmnxSysUsbCFlashId_Type(Integer32):
    """Custom type tmnxSysUsbCFlashId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("cf2", 2)
    )


_TmnxSysUsbCFlashId_Type.__name__ = "Integer32"
_TmnxSysUsbCFlashId_Object = MibTableColumn
tmnxSysUsbCFlashId = _TmnxSysUsbCFlashId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 50, 1, 1),
    _TmnxSysUsbCFlashId_Type()
)
tmnxSysUsbCFlashId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysUsbCFlashId.setStatus("current")
_TmnxSysUsbLastChgd_Type = TimeStamp
_TmnxSysUsbLastChgd_Object = MibTableColumn
tmnxSysUsbLastChgd = _TmnxSysUsbLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 50, 1, 2),
    _TmnxSysUsbLastChgd_Type()
)
tmnxSysUsbLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysUsbLastChgd.setStatus("current")


class _TmnxSysUsbAdminState_Type(TmnxEnabledDisabledAdminState):
    """Custom type tmnxSysUsbAdminState based on TmnxEnabledDisabledAdminState"""
    defaultValue = 2


_TmnxSysUsbAdminState_Type.__name__ = "TmnxEnabledDisabledAdminState"
_TmnxSysUsbAdminState_Object = MibTableColumn
tmnxSysUsbAdminState = _TmnxSysUsbAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 50, 1, 3),
    _TmnxSysUsbAdminState_Type()
)
tmnxSysUsbAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysUsbAdminState.setStatus("current")
_TmnxSysRemoteMgmt_ObjectIdentity = ObjectIdentity
tmnxSysRemoteMgmt = _TmnxSysRemoteMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52)
)


class _TmnxSysRmtMgmtAdminState_Type(TmnxAdminState):
    """Custom type tmnxSysRmtMgmtAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxSysRmtMgmtAdminState_Type.__name__ = "TmnxAdminState"
_TmnxSysRmtMgmtAdminState_Object = MibScalar
tmnxSysRmtMgmtAdminState = _TmnxSysRmtMgmtAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 1),
    _TmnxSysRmtMgmtAdminState_Type()
)
tmnxSysRmtMgmtAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtAdminState.setStatus("current")
_TmnxSysRmtMgmtOperState_Type = TmnxOperState
_TmnxSysRmtMgmtOperState_Object = MibScalar
tmnxSysRmtMgmtOperState = _TmnxSysRmtMgmtOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 2),
    _TmnxSysRmtMgmtOperState_Type()
)
tmnxSysRmtMgmtOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtOperState.setStatus("current")


class _TmnxSysRmtMgmtOperDownReason_Type(Integer32):
    """Custom type tmnxSysRmtMgmtOperDownReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("adminDown", 1),
          ("noManager", 2))
    )


_TmnxSysRmtMgmtOperDownReason_Type.__name__ = "Integer32"
_TmnxSysRmtMgmtOperDownReason_Object = MibScalar
tmnxSysRmtMgmtOperDownReason = _TmnxSysRmtMgmtOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 3),
    _TmnxSysRmtMgmtOperDownReason_Type()
)
tmnxSysRmtMgmtOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtOperDownReason.setStatus("current")


class _TmnxSysRmtMgmtAllowUnsecure_Type(TruthValue):
    """Custom type tmnxSysRmtMgmtAllowUnsecure based on TruthValue"""
    defaultValue = 2


_TmnxSysRmtMgmtAllowUnsecure_Type.__name__ = "TruthValue"
_TmnxSysRmtMgmtAllowUnsecure_Object = MibScalar
tmnxSysRmtMgmtAllowUnsecure = _TmnxSysRmtMgmtAllowUnsecure_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 4),
    _TmnxSysRmtMgmtAllowUnsecure_Type()
)
tmnxSysRmtMgmtAllowUnsecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtAllowUnsecure.setStatus("current")


class _TmnxSysRmtMgmtTlsClientProf_Type(TNamedItemOrEmpty):
    """Custom type tmnxSysRmtMgmtTlsClientProf based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxSysRmtMgmtTlsClientProf_Type.__name__ = "TNamedItemOrEmpty"
_TmnxSysRmtMgmtTlsClientProf_Object = MibScalar
tmnxSysRmtMgmtTlsClientProf = _TmnxSysRmtMgmtTlsClientProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 5),
    _TmnxSysRmtMgmtTlsClientProf_Type()
)
tmnxSysRmtMgmtTlsClientProf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtTlsClientProf.setStatus("current")


class _TmnxSysRmtMgmtTimeout_Type(Unsigned32):
    """Custom type tmnxSysRmtMgmtTimeout based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_TmnxSysRmtMgmtTimeout_Type.__name__ = "Unsigned32"
_TmnxSysRmtMgmtTimeout_Object = MibScalar
tmnxSysRmtMgmtTimeout = _TmnxSysRmtMgmtTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 6),
    _TmnxSysRmtMgmtTimeout_Type()
)
tmnxSysRmtMgmtTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtTimeout.setUnits("seconds")


class _TmnxSysRmtMgmtVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxSysRmtMgmtVRtrId based on TmnxVRtrID"""
    defaultValue = 4095


_TmnxSysRmtMgmtVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxSysRmtMgmtVRtrId_Object = MibScalar
tmnxSysRmtMgmtVRtrId = _TmnxSysRmtMgmtVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 7),
    _TmnxSysRmtMgmtVRtrId_Type()
)
tmnxSysRmtMgmtVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtVRtrId.setStatus("current")
_TmnxSysRmtMgmtSrcIpAddType_Type = InetAddressType
_TmnxSysRmtMgmtSrcIpAddType_Object = MibScalar
tmnxSysRmtMgmtSrcIpAddType = _TmnxSysRmtMgmtSrcIpAddType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 8),
    _TmnxSysRmtMgmtSrcIpAddType_Type()
)
tmnxSysRmtMgmtSrcIpAddType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtSrcIpAddType.setStatus("current")


class _TmnxSysRmtMgmtSrcIpAddress_Type(InetAddress):
    """Custom type tmnxSysRmtMgmtSrcIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxSysRmtMgmtSrcIpAddress_Type.__name__ = "InetAddress"
_TmnxSysRmtMgmtSrcIpAddress_Object = MibScalar
tmnxSysRmtMgmtSrcIpAddress = _TmnxSysRmtMgmtSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 9),
    _TmnxSysRmtMgmtSrcIpAddress_Type()
)
tmnxSysRmtMgmtSrcIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtSrcIpAddress.setStatus("current")


class _TmnxSysRmtMgmtSrcPort_Type(InetPortNumber):
    """Custom type tmnxSysRmtMgmtSrcPort based on InetPortNumber"""
    defaultValue = 0


_TmnxSysRmtMgmtSrcPort_Type.__name__ = "InetPortNumber"
_TmnxSysRmtMgmtSrcPort_Object = MibScalar
tmnxSysRmtMgmtSrcPort = _TmnxSysRmtMgmtSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 10),
    _TmnxSysRmtMgmtSrcPort_Type()
)
tmnxSysRmtMgmtSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtSrcPort.setStatus("current")


class _TmnxSysRmtMgmtSrcDefaultPort_Type(TmnxSysRmtMgmtSrcDefaultPort):
    """Custom type tmnxSysRmtMgmtSrcDefaultPort based on TmnxSysRmtMgmtSrcDefaultPort"""
    defaultValue = -1


_TmnxSysRmtMgmtSrcDefaultPort_Type.__name__ = "TmnxSysRmtMgmtSrcDefaultPort"
_TmnxSysRmtMgmtSrcDefaultPort_Object = MibScalar
tmnxSysRmtMgmtSrcDefaultPort = _TmnxSysRmtMgmtSrcDefaultPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 11),
    _TmnxSysRmtMgmtSrcDefaultPort_Type()
)
tmnxSysRmtMgmtSrcDefaultPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtSrcDefaultPort.setStatus("current")


class _TmnxSysRmtMgmtDeviceLabel_Type(TLNamedItemOrEmpty):
    """Custom type tmnxSysRmtMgmtDeviceLabel based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxSysRmtMgmtDeviceLabel_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxSysRmtMgmtDeviceLabel_Object = MibScalar
tmnxSysRmtMgmtDeviceLabel = _TmnxSysRmtMgmtDeviceLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 12),
    _TmnxSysRmtMgmtDeviceLabel_Type()
)
tmnxSysRmtMgmtDeviceLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtDeviceLabel.setStatus("current")


class _TmnxSysRmtMgmtDeviceName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxSysRmtMgmtDeviceName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxSysRmtMgmtDeviceName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxSysRmtMgmtDeviceName_Object = MibScalar
tmnxSysRmtMgmtDeviceName = _TmnxSysRmtMgmtDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 13),
    _TmnxSysRmtMgmtDeviceName_Type()
)
tmnxSysRmtMgmtDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtDeviceName.setStatus("current")
_TmnxSysRmtMgmtLastRegStatus_Type = TmnxSysRmtMgmtLastRegStatus
_TmnxSysRmtMgmtLastRegStatus_Object = MibScalar
tmnxSysRmtMgmtLastRegStatus = _TmnxSysRmtMgmtLastRegStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 14),
    _TmnxSysRmtMgmtLastRegStatus_Type()
)
tmnxSysRmtMgmtLastRegStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtLastRegStatus.setStatus("current")
_TmnxSysRmtMgmtLastRegTime_Type = DateAndTime
_TmnxSysRmtMgmtLastRegTime_Object = MibScalar
tmnxSysRmtMgmtLastRegTime = _TmnxSysRmtMgmtLastRegTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 15),
    _TmnxSysRmtMgmtLastRegTime_Type()
)
tmnxSysRmtMgmtLastRegTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtLastRegTime.setStatus("current")
_TmnxSysRmtMgmtRegsCancelled_Type = Counter64
_TmnxSysRmtMgmtRegsCancelled_Object = MibScalar
tmnxSysRmtMgmtRegsCancelled = _TmnxSysRmtMgmtRegsCancelled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 16),
    _TmnxSysRmtMgmtRegsCancelled_Type()
)
tmnxSysRmtMgmtRegsCancelled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtRegsCancelled.setStatus("current")
_TmnxSysRmtMgmtRegsFailed_Type = Counter64
_TmnxSysRmtMgmtRegsFailed_Object = MibScalar
tmnxSysRmtMgmtRegsFailed = _TmnxSysRmtMgmtRegsFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 17),
    _TmnxSysRmtMgmtRegsFailed_Type()
)
tmnxSysRmtMgmtRegsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtRegsFailed.setStatus("current")
_TmnxSysRmtMgmtRegsSent_Type = Counter64
_TmnxSysRmtMgmtRegsSent_Object = MibScalar
tmnxSysRmtMgmtRegsSent = _TmnxSysRmtMgmtRegsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 18),
    _TmnxSysRmtMgmtRegsSent_Type()
)
tmnxSysRmtMgmtRegsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtRegsSent.setStatus("current")


class _TmnxSysRmtMgmtHelloInterval_Type(Unsigned32):
    """Custom type tmnxSysRmtMgmtHelloInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_TmnxSysRmtMgmtHelloInterval_Type.__name__ = "Unsigned32"
_TmnxSysRmtMgmtHelloInterval_Object = MibScalar
tmnxSysRmtMgmtHelloInterval = _TmnxSysRmtMgmtHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 19),
    _TmnxSysRmtMgmtHelloInterval_Type()
)
tmnxSysRmtMgmtHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtHelloInterval.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtHelloInterval.setUnits("minutes")
_TmnxSysRmtMgmtLastHelloTime_Type = DateAndTime
_TmnxSysRmtMgmtLastHelloTime_Object = MibScalar
tmnxSysRmtMgmtLastHelloTime = _TmnxSysRmtMgmtLastHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 20),
    _TmnxSysRmtMgmtLastHelloTime_Type()
)
tmnxSysRmtMgmtLastHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtLastHelloTime.setStatus("current")
_TmnxSysRmtMgmtManagerTable_Object = MibTable
tmnxSysRmtMgmtManagerTable = _TmnxSysRmtMgmtManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21)
)
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtManagerTable.setStatus("current")
_TmnxSysRmtMgmtManagerEntry_Object = MibTableRow
tmnxSysRmtMgmtManagerEntry = _TmnxSysRmtMgmtManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1)
)
tmnxSysRmtMgmtManagerEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrName"),
)
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtManagerEntry.setStatus("current")
_TmnxSysRmtMgmtMgrName_Type = TLNamedItem
_TmnxSysRmtMgmtMgrName_Object = MibTableColumn
tmnxSysRmtMgmtMgrName = _TmnxSysRmtMgmtMgrName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 1),
    _TmnxSysRmtMgmtMgrName_Type()
)
tmnxSysRmtMgmtMgrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrName.setStatus("current")
_TmnxSysRmtMgmtMgrRowStatus_Type = RowStatus
_TmnxSysRmtMgmtMgrRowStatus_Object = MibTableColumn
tmnxSysRmtMgmtMgrRowStatus = _TmnxSysRmtMgmtMgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 2),
    _TmnxSysRmtMgmtMgrRowStatus_Type()
)
tmnxSysRmtMgmtMgrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrRowStatus.setStatus("current")


class _TmnxSysRmtMgmtMgrAdminState_Type(TmnxAdminState):
    """Custom type tmnxSysRmtMgmtMgrAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxSysRmtMgmtMgrAdminState_Type.__name__ = "TmnxAdminState"
_TmnxSysRmtMgmtMgrAdminState_Object = MibTableColumn
tmnxSysRmtMgmtMgrAdminState = _TmnxSysRmtMgmtMgrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 3),
    _TmnxSysRmtMgmtMgrAdminState_Type()
)
tmnxSysRmtMgmtMgrAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrAdminState.setStatus("current")
_TmnxSysRmtMgmtMgrOperState_Type = TmnxOperState
_TmnxSysRmtMgmtMgrOperState_Object = MibTableColumn
tmnxSysRmtMgmtMgrOperState = _TmnxSysRmtMgmtMgrOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 4),
    _TmnxSysRmtMgmtMgrOperState_Type()
)
tmnxSysRmtMgmtMgrOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrOperState.setStatus("current")


class _TmnxSysRmtMgmtMgrOperDownReason_Type(Integer32):
    """Custom type tmnxSysRmtMgmtMgrOperDownReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("adminDown", 1),
          ("noTransportType", 2),
          ("noSourceAddress", 3),
          ("invalidManagerAddress", 4),
          ("registration-failed", 5))
    )


_TmnxSysRmtMgmtMgrOperDownReason_Type.__name__ = "Integer32"
_TmnxSysRmtMgmtMgrOperDownReason_Object = MibTableColumn
tmnxSysRmtMgmtMgrOperDownReason = _TmnxSysRmtMgmtMgrOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 5),
    _TmnxSysRmtMgmtMgrOperDownReason_Type()
)
tmnxSysRmtMgmtMgrOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrOperDownReason.setStatus("current")


class _TmnxSysRmtMgmtMgrFQDN_Type(DisplayString):
    """Custom type tmnxSysRmtMgmtMgrFQDN based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxSysRmtMgmtMgrFQDN_Type.__name__ = "DisplayString"
_TmnxSysRmtMgmtMgrFQDN_Object = MibTableColumn
tmnxSysRmtMgmtMgrFQDN = _TmnxSysRmtMgmtMgrFQDN_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 6),
    _TmnxSysRmtMgmtMgrFQDN_Type()
)
tmnxSysRmtMgmtMgrFQDN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrFQDN.setStatus("current")
_TmnxSysRmtMgmtMgrIpAddType_Type = InetAddressType
_TmnxSysRmtMgmtMgrIpAddType_Object = MibTableColumn
tmnxSysRmtMgmtMgrIpAddType = _TmnxSysRmtMgmtMgrIpAddType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 7),
    _TmnxSysRmtMgmtMgrIpAddType_Type()
)
tmnxSysRmtMgmtMgrIpAddType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrIpAddType.setStatus("current")


class _TmnxSysRmtMgmtMgrIpAddress_Type(InetAddress):
    """Custom type tmnxSysRmtMgmtMgrIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxSysRmtMgmtMgrIpAddress_Type.__name__ = "InetAddress"
_TmnxSysRmtMgmtMgrIpAddress_Object = MibTableColumn
tmnxSysRmtMgmtMgrIpAddress = _TmnxSysRmtMgmtMgrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 8),
    _TmnxSysRmtMgmtMgrIpAddress_Type()
)
tmnxSysRmtMgmtMgrIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrIpAddress.setStatus("current")


class _TmnxSysRmtMgmtMgrPort_Type(InetPortNumber):
    """Custom type tmnxSysRmtMgmtMgrPort based on InetPortNumber"""
    defaultValue = 57400


_TmnxSysRmtMgmtMgrPort_Type.__name__ = "InetPortNumber"
_TmnxSysRmtMgmtMgrPort_Object = MibTableColumn
tmnxSysRmtMgmtMgrPort = _TmnxSysRmtMgmtMgrPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 9),
    _TmnxSysRmtMgmtMgrPort_Type()
)
tmnxSysRmtMgmtMgrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrPort.setStatus("current")


class _TmnxSysRmtMgmtMgrAllowUnsecure_Type(TruthValue):
    """Custom type tmnxSysRmtMgmtMgrAllowUnsecure based on TruthValue"""
    defaultValue = 2


_TmnxSysRmtMgmtMgrAllowUnsecure_Type.__name__ = "TruthValue"
_TmnxSysRmtMgmtMgrAllowUnsecure_Object = MibTableColumn
tmnxSysRmtMgmtMgrAllowUnsecure = _TmnxSysRmtMgmtMgrAllowUnsecure_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 10),
    _TmnxSysRmtMgmtMgrAllowUnsecure_Type()
)
tmnxSysRmtMgmtMgrAllowUnsecure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrAllowUnsecure.setStatus("current")


class _TmnxSysRmtMgmtMgrTlsClientProf_Type(TNamedItemOrEmpty):
    """Custom type tmnxSysRmtMgmtMgrTlsClientProf based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxSysRmtMgmtMgrTlsClientProf_Type.__name__ = "TNamedItemOrEmpty"
_TmnxSysRmtMgmtMgrTlsClientProf_Object = MibTableColumn
tmnxSysRmtMgmtMgrTlsClientProf = _TmnxSysRmtMgmtMgrTlsClientProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 11),
    _TmnxSysRmtMgmtMgrTlsClientProf_Type()
)
tmnxSysRmtMgmtMgrTlsClientProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrTlsClientProf.setStatus("current")


class _TmnxSysRmtMgmtMgrDescription_Type(TItemDescription):
    """Custom type tmnxSysRmtMgmtMgrDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxSysRmtMgmtMgrDescription_Type.__name__ = "TItemDescription"
_TmnxSysRmtMgmtMgrDescription_Object = MibTableColumn
tmnxSysRmtMgmtMgrDescription = _TmnxSysRmtMgmtMgrDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 12),
    _TmnxSysRmtMgmtMgrDescription_Type()
)
tmnxSysRmtMgmtMgrDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrDescription.setStatus("current")


class _TmnxSysRmtMgmtMgrTimeout_Type(Unsigned32):
    """Custom type tmnxSysRmtMgmtMgrTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 3600),
    )


_TmnxSysRmtMgmtMgrTimeout_Type.__name__ = "Unsigned32"
_TmnxSysRmtMgmtMgrTimeout_Object = MibTableColumn
tmnxSysRmtMgmtMgrTimeout = _TmnxSysRmtMgmtMgrTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 13),
    _TmnxSysRmtMgmtMgrTimeout_Type()
)
tmnxSysRmtMgmtMgrTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrTimeout.setUnits("seconds")


class _TmnxSysRmtMgmtMgrVRtrId_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxSysRmtMgmtMgrVRtrId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxSysRmtMgmtMgrVRtrId_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxSysRmtMgmtMgrVRtrId_Object = MibTableColumn
tmnxSysRmtMgmtMgrVRtrId = _TmnxSysRmtMgmtMgrVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 14),
    _TmnxSysRmtMgmtMgrVRtrId_Type()
)
tmnxSysRmtMgmtMgrVRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrVRtrId.setStatus("current")
_TmnxSysRmtMgmtMgrSrcIpAddType_Type = InetAddressType
_TmnxSysRmtMgmtMgrSrcIpAddType_Object = MibTableColumn
tmnxSysRmtMgmtMgrSrcIpAddType = _TmnxSysRmtMgmtMgrSrcIpAddType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 15),
    _TmnxSysRmtMgmtMgrSrcIpAddType_Type()
)
tmnxSysRmtMgmtMgrSrcIpAddType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrSrcIpAddType.setStatus("current")


class _TmnxSysRmtMgmtMgrSrcIpAddress_Type(InetAddress):
    """Custom type tmnxSysRmtMgmtMgrSrcIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxSysRmtMgmtMgrSrcIpAddress_Type.__name__ = "InetAddress"
_TmnxSysRmtMgmtMgrSrcIpAddress_Object = MibTableColumn
tmnxSysRmtMgmtMgrSrcIpAddress = _TmnxSysRmtMgmtMgrSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 16),
    _TmnxSysRmtMgmtMgrSrcIpAddress_Type()
)
tmnxSysRmtMgmtMgrSrcIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrSrcIpAddress.setStatus("current")


class _TmnxSysRmtMgmtMgrSrcPort_Type(InetPortNumber):
    """Custom type tmnxSysRmtMgmtMgrSrcPort based on InetPortNumber"""
    defaultValue = 0


_TmnxSysRmtMgmtMgrSrcPort_Type.__name__ = "InetPortNumber"
_TmnxSysRmtMgmtMgrSrcPort_Object = MibTableColumn
tmnxSysRmtMgmtMgrSrcPort = _TmnxSysRmtMgmtMgrSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 17),
    _TmnxSysRmtMgmtMgrSrcPort_Type()
)
tmnxSysRmtMgmtMgrSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrSrcPort.setStatus("current")


class _TmnxSysRmtMgmtMgrSrcDefaultPort_Type(TmnxSysRmtMgmtSrcDefaultPort):
    """Custom type tmnxSysRmtMgmtMgrSrcDefaultPort based on TmnxSysRmtMgmtSrcDefaultPort"""
    defaultValue = 0


_TmnxSysRmtMgmtMgrSrcDefaultPort_Type.__name__ = "TmnxSysRmtMgmtSrcDefaultPort"
_TmnxSysRmtMgmtMgrSrcDefaultPort_Object = MibTableColumn
tmnxSysRmtMgmtMgrSrcDefaultPort = _TmnxSysRmtMgmtMgrSrcDefaultPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 18),
    _TmnxSysRmtMgmtMgrSrcDefaultPort_Type()
)
tmnxSysRmtMgmtMgrSrcDefaultPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrSrcDefaultPort.setStatus("current")


class _TmnxSysRmtMgmtMgrDeviceLabel_Type(TLNamedItemOrEmpty):
    """Custom type tmnxSysRmtMgmtMgrDeviceLabel based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxSysRmtMgmtMgrDeviceLabel_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxSysRmtMgmtMgrDeviceLabel_Object = MibTableColumn
tmnxSysRmtMgmtMgrDeviceLabel = _TmnxSysRmtMgmtMgrDeviceLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 19),
    _TmnxSysRmtMgmtMgrDeviceLabel_Type()
)
tmnxSysRmtMgmtMgrDeviceLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrDeviceLabel.setStatus("current")


class _TmnxSysRmtMgmtMgrDeviceName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxSysRmtMgmtMgrDeviceName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxSysRmtMgmtMgrDeviceName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxSysRmtMgmtMgrDeviceName_Object = MibTableColumn
tmnxSysRmtMgmtMgrDeviceName = _TmnxSysRmtMgmtMgrDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 20),
    _TmnxSysRmtMgmtMgrDeviceName_Type()
)
tmnxSysRmtMgmtMgrDeviceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrDeviceName.setStatus("current")
_TmnxSysRmtMgmtMgrLastRegStatus_Type = TmnxSysRmtMgmtLastRegStatus
_TmnxSysRmtMgmtMgrLastRegStatus_Object = MibTableColumn
tmnxSysRmtMgmtMgrLastRegStatus = _TmnxSysRmtMgmtMgrLastRegStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 21),
    _TmnxSysRmtMgmtMgrLastRegStatus_Type()
)
tmnxSysRmtMgmtMgrLastRegStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrLastRegStatus.setStatus("current")
_TmnxSysRmtMgmtMgrLastRegTime_Type = DateAndTime
_TmnxSysRmtMgmtMgrLastRegTime_Object = MibTableColumn
tmnxSysRmtMgmtMgrLastRegTime = _TmnxSysRmtMgmtMgrLastRegTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 22),
    _TmnxSysRmtMgmtMgrLastRegTime_Type()
)
tmnxSysRmtMgmtMgrLastRegTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrLastRegTime.setStatus("current")
_TmnxSysRmtMgmtMgrRegsCancelled_Type = Counter64
_TmnxSysRmtMgmtMgrRegsCancelled_Object = MibTableColumn
tmnxSysRmtMgmtMgrRegsCancelled = _TmnxSysRmtMgmtMgrRegsCancelled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 23),
    _TmnxSysRmtMgmtMgrRegsCancelled_Type()
)
tmnxSysRmtMgmtMgrRegsCancelled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrRegsCancelled.setStatus("current")
_TmnxSysRmtMgmtMgrRegsFailed_Type = Counter64
_TmnxSysRmtMgmtMgrRegsFailed_Object = MibTableColumn
tmnxSysRmtMgmtMgrRegsFailed = _TmnxSysRmtMgmtMgrRegsFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 24),
    _TmnxSysRmtMgmtMgrRegsFailed_Type()
)
tmnxSysRmtMgmtMgrRegsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrRegsFailed.setStatus("current")
_TmnxSysRmtMgmtMgrRegsSent_Type = Counter64
_TmnxSysRmtMgmtMgrRegsSent_Object = MibTableColumn
tmnxSysRmtMgmtMgrRegsSent = _TmnxSysRmtMgmtMgrRegsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 25),
    _TmnxSysRmtMgmtMgrRegsSent_Type()
)
tmnxSysRmtMgmtMgrRegsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrRegsSent.setStatus("current")
_TmnxSysRmtMgmtMgrOperTlsProf_Type = TNamedItemOrEmpty
_TmnxSysRmtMgmtMgrOperTlsProf_Object = MibTableColumn
tmnxSysRmtMgmtMgrOperTlsProf = _TmnxSysRmtMgmtMgrOperTlsProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 26),
    _TmnxSysRmtMgmtMgrOperTlsProf_Type()
)
tmnxSysRmtMgmtMgrOperTlsProf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrOperTlsProf.setStatus("current")


class _TmnxSysRmtMgmtMgrOperTranspType_Type(Integer32):
    """Custom type tmnxSysRmtMgmtMgrOperTranspType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tls", 1),
          ("unsecured", 2))
    )


_TmnxSysRmtMgmtMgrOperTranspType_Type.__name__ = "Integer32"
_TmnxSysRmtMgmtMgrOperTranspType_Object = MibTableColumn
tmnxSysRmtMgmtMgrOperTranspType = _TmnxSysRmtMgmtMgrOperTranspType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 27),
    _TmnxSysRmtMgmtMgrOperTranspType_Type()
)
tmnxSysRmtMgmtMgrOperTranspType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrOperTranspType.setStatus("current")
_TmnxSysRmtMgmtMgrOperTimeout_Type = Unsigned32
_TmnxSysRmtMgmtMgrOperTimeout_Object = MibTableColumn
tmnxSysRmtMgmtMgrOperTimeout = _TmnxSysRmtMgmtMgrOperTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 28),
    _TmnxSysRmtMgmtMgrOperTimeout_Type()
)
tmnxSysRmtMgmtMgrOperTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrOperTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrOperTimeout.setUnits("seconds")
_TmnxSysRmtMgmtMgrOperVRtrId_Type = TmnxVRtrIDOrZero
_TmnxSysRmtMgmtMgrOperVRtrId_Object = MibTableColumn
tmnxSysRmtMgmtMgrOperVRtrId = _TmnxSysRmtMgmtMgrOperVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 29),
    _TmnxSysRmtMgmtMgrOperVRtrId_Type()
)
tmnxSysRmtMgmtMgrOperVRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrOperVRtrId.setStatus("current")
_TmnxSysRmtMgmtMgrOperDevName_Type = TLNamedItemOrEmpty
_TmnxSysRmtMgmtMgrOperDevName_Object = MibTableColumn
tmnxSysRmtMgmtMgrOperDevName = _TmnxSysRmtMgmtMgrOperDevName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 30),
    _TmnxSysRmtMgmtMgrOperDevName_Type()
)
tmnxSysRmtMgmtMgrOperDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrOperDevName.setStatus("current")
_TmnxSysRmtMgmtMgrOperDevLabel_Type = TLNamedItemOrEmpty
_TmnxSysRmtMgmtMgrOperDevLabel_Object = MibTableColumn
tmnxSysRmtMgmtMgrOperDevLabel = _TmnxSysRmtMgmtMgrOperDevLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 31),
    _TmnxSysRmtMgmtMgrOperDevLabel_Type()
)
tmnxSysRmtMgmtMgrOperDevLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrOperDevLabel.setStatus("current")
_TmnxSysRmtMgmtMgrOperSrcIpAdType_Type = InetAddressType
_TmnxSysRmtMgmtMgrOperSrcIpAdType_Object = MibTableColumn
tmnxSysRmtMgmtMgrOperSrcIpAdType = _TmnxSysRmtMgmtMgrOperSrcIpAdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 32),
    _TmnxSysRmtMgmtMgrOperSrcIpAdType_Type()
)
tmnxSysRmtMgmtMgrOperSrcIpAdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrOperSrcIpAdType.setStatus("current")


class _TmnxSysRmtMgmtMgrOperSrcIpAddr_Type(InetAddress):
    """Custom type tmnxSysRmtMgmtMgrOperSrcIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxSysRmtMgmtMgrOperSrcIpAddr_Type.__name__ = "InetAddress"
_TmnxSysRmtMgmtMgrOperSrcIpAddr_Object = MibTableColumn
tmnxSysRmtMgmtMgrOperSrcIpAddr = _TmnxSysRmtMgmtMgrOperSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 33),
    _TmnxSysRmtMgmtMgrOperSrcIpAddr_Type()
)
tmnxSysRmtMgmtMgrOperSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrOperSrcIpAddr.setStatus("current")
_TmnxSysRmtMgmtMgrOperSrcPort_Type = InetPortNumber
_TmnxSysRmtMgmtMgrOperSrcPort_Object = MibTableColumn
tmnxSysRmtMgmtMgrOperSrcPort = _TmnxSysRmtMgmtMgrOperSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 21, 1, 34),
    _TmnxSysRmtMgmtMgrOperSrcPort_Type()
)
tmnxSysRmtMgmtMgrOperSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtMgrOperSrcPort.setStatus("current")


class _TmnxSysRmtMgmtHelloIntervalSec_Type(Unsigned32):
    """Custom type tmnxSysRmtMgmtHelloIntervalSec based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 216000),
    )


_TmnxSysRmtMgmtHelloIntervalSec_Type.__name__ = "Unsigned32"
_TmnxSysRmtMgmtHelloIntervalSec_Object = MibScalar
tmnxSysRmtMgmtHelloIntervalSec = _TmnxSysRmtMgmtHelloIntervalSec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 52, 22),
    _TmnxSysRmtMgmtHelloIntervalSec_Type()
)
tmnxSysRmtMgmtHelloIntervalSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtHelloIntervalSec.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSysRmtMgmtHelloIntervalSec.setUnits("seconds")
_TmnxSysMgmtInterfaceOperations_ObjectIdentity = ObjectIdentity
tmnxSysMgmtInterfaceOperations = _TmnxSysMgmtInterfaceOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 53)
)


class _TmnxSysMgmtIfOpsAsyncExecTimeout_Type(Unsigned32):
    """Custom type tmnxSysMgmtIfOpsAsyncExecTimeout based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_TmnxSysMgmtIfOpsAsyncExecTimeout_Type.__name__ = "Unsigned32"
_TmnxSysMgmtIfOpsAsyncExecTimeout_Object = MibScalar
tmnxSysMgmtIfOpsAsyncExecTimeout = _TmnxSysMgmtIfOpsAsyncExecTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 53, 1),
    _TmnxSysMgmtIfOpsAsyncExecTimeout_Type()
)
tmnxSysMgmtIfOpsAsyncExecTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfOpsAsyncExecTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfOpsAsyncExecTimeout.setUnits("seconds")


class _TmnxSysMgmtIfOpsAsyncRetTimeout_Type(Unsigned32):
    """Custom type tmnxSysMgmtIfOpsAsyncRetTimeout based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_TmnxSysMgmtIfOpsAsyncRetTimeout_Type.__name__ = "Unsigned32"
_TmnxSysMgmtIfOpsAsyncRetTimeout_Object = MibScalar
tmnxSysMgmtIfOpsAsyncRetTimeout = _TmnxSysMgmtIfOpsAsyncRetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 53, 2),
    _TmnxSysMgmtIfOpsAsyncRetTimeout_Type()
)
tmnxSysMgmtIfOpsAsyncRetTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfOpsAsyncRetTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfOpsAsyncRetTimeout.setUnits("seconds")


class _TmnxSysMgmtIfOpsSyncExecTimeout_Type(Unsigned32):
    """Custom type tmnxSysMgmtIfOpsSyncExecTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_TmnxSysMgmtIfOpsSyncExecTimeout_Type.__name__ = "Unsigned32"
_TmnxSysMgmtIfOpsSyncExecTimeout_Object = MibScalar
tmnxSysMgmtIfOpsSyncExecTimeout = _TmnxSysMgmtIfOpsSyncExecTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 53, 3),
    _TmnxSysMgmtIfOpsSyncExecTimeout_Type()
)
tmnxSysMgmtIfOpsSyncExecTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfOpsSyncExecTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSysMgmtIfOpsSyncExecTimeout.setUnits("seconds")
_TmnxSysSwFabFailRecSfmStatsTable_Object = MibTable
tmnxSysSwFabFailRecSfmStatsTable = _TmnxSysSwFabFailRecSfmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 54)
)
if mibBuilder.loadTexts:
    tmnxSysSwFabFailRecSfmStatsTable.setStatus("current")
_TmnxSysSwFabFailRecSfmStatsEntry_Object = MibTableRow
tmnxSysSwFabFailRecSfmStatsEntry = _TmnxSysSwFabFailRecSfmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 54, 1)
)
tmnxSysSwFabFailRecSfmStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFabricSlotNum"),
)
if mibBuilder.loadTexts:
    tmnxSysSwFabFailRecSfmStatsEntry.setStatus("current")


class _TmnxSysSwFabFailRecSfmState_Type(Integer32):
    """Custom type tmnxSysSwFabFailRecSfmState based on Integer32"""
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
        *(("complete", 0),
          ("inProgress", 1),
          ("pending", 2),
          ("aborted", 3),
          ("failed", 4))
    )


_TmnxSysSwFabFailRecSfmState_Type.__name__ = "Integer32"
_TmnxSysSwFabFailRecSfmState_Object = MibTableColumn
tmnxSysSwFabFailRecSfmState = _TmnxSysSwFabFailRecSfmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 54, 1, 1),
    _TmnxSysSwFabFailRecSfmState_Type()
)
tmnxSysSwFabFailRecSfmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysSwFabFailRecSfmState.setStatus("current")
_TmnxSysSwFabFailRecSfmStateTime_Type = TimeStamp
_TmnxSysSwFabFailRecSfmStateTime_Object = MibTableColumn
tmnxSysSwFabFailRecSfmStateTime = _TmnxSysSwFabFailRecSfmStateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 54, 1, 2),
    _TmnxSysSwFabFailRecSfmStateTime_Type()
)
tmnxSysSwFabFailRecSfmStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysSwFabFailRecSfmStateTime.setStatus("current")
_SysBofInfoExt_ObjectIdentity = ObjectIdentity
sysBofInfoExt = _SysBofInfoExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 55)
)


class _SbiEncryptConfig_Type(TruthValue):
    """Custom type sbiEncryptConfig based on TruthValue"""
    defaultValue = 2


_SbiEncryptConfig_Type.__name__ = "TruthValue"
_SbiEncryptConfig_Object = MibScalar
sbiEncryptConfig = _SbiEncryptConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 55, 1),
    _SbiEncryptConfig_Type()
)
sbiEncryptConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiEncryptConfig.setStatus("current")


class _SbiPassword_Type(DisplayString):
    """Custom type sbiPassword based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SbiPassword_Type.__name__ = "DisplayString"
_SbiPassword_Object = MibScalar
sbiPassword = _SbiPassword_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 55, 2),
    _SbiPassword_Type()
)
sbiPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiPassword.setStatus("current")


class _SbiEncryptKey_Type(DisplayString):
    """Custom type sbiEncryptKey based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SbiEncryptKey_Type.__name__ = "DisplayString"
_SbiEncryptKey_Object = MibScalar
sbiEncryptKey = _SbiEncryptKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 55, 3),
    _SbiEncryptKey_Type()
)
sbiEncryptKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbiEncryptKey.setStatus("current")
_TmnxSysGrpcPendRebTable_Object = MibTable
tmnxSysGrpcPendRebTable = _TmnxSysGrpcPendRebTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 56)
)
if mibBuilder.loadTexts:
    tmnxSysGrpcPendRebTable.setStatus("current")
_TmnxSysGrpcPendRebEntry_Object = MibTableRow
tmnxSysGrpcPendRebEntry = _TmnxSysGrpcPendRebEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 56, 1)
)
tmnxSysGrpcPendRebEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysGrpcPendRebComp"),
)
if mibBuilder.loadTexts:
    tmnxSysGrpcPendRebEntry.setStatus("current")
_TmnxSysGrpcPendRebComp_Type = TLNamedItem
_TmnxSysGrpcPendRebComp_Object = MibTableColumn
tmnxSysGrpcPendRebComp = _TmnxSysGrpcPendRebComp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 56, 1, 1),
    _TmnxSysGrpcPendRebComp_Type()
)
tmnxSysGrpcPendRebComp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysGrpcPendRebComp.setStatus("current")
_TmnxSysGrpcPendRebOperState_Type = TmnxOperState
_TmnxSysGrpcPendRebOperState_Object = MibTableColumn
tmnxSysGrpcPendRebOperState = _TmnxSysGrpcPendRebOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 56, 1, 2),
    _TmnxSysGrpcPendRebOperState_Type()
)
tmnxSysGrpcPendRebOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcPendRebOperState.setStatus("current")
_TmnxSysGrpcPendRebDelay_Type = Unsigned32
_TmnxSysGrpcPendRebDelay_Object = MibTableColumn
tmnxSysGrpcPendRebDelay = _TmnxSysGrpcPendRebDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 56, 1, 3),
    _TmnxSysGrpcPendRebDelay_Type()
)
tmnxSysGrpcPendRebDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcPendRebDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSysGrpcPendRebDelay.setUnits("seconds")


class _TmnxSysGrpcPendRebMsg_Type(OctetString):
    """Custom type tmnxSysGrpcPendRebMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TmnxSysGrpcPendRebMsg_Type.__name__ = "OctetString"
_TmnxSysGrpcPendRebMsg_Object = MibTableColumn
tmnxSysGrpcPendRebMsg = _TmnxSysGrpcPendRebMsg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 56, 1, 4),
    _TmnxSysGrpcPendRebMsg_Type()
)
tmnxSysGrpcPendRebMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcPendRebMsg.setStatus("current")
_TmnxSysGrpcPendRebCount_Type = Unsigned32
_TmnxSysGrpcPendRebCount_Object = MibTableColumn
tmnxSysGrpcPendRebCount = _TmnxSysGrpcPendRebCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 56, 1, 5),
    _TmnxSysGrpcPendRebCount_Type()
)
tmnxSysGrpcPendRebCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysGrpcPendRebCount.setStatus("current")
_TmnxSysGrpcTunnelObjs_ObjectIdentity = ObjectIdentity
tmnxSysGrpcTunnelObjs = _TmnxSysGrpcTunnelObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57)
)
_TmnxSysGrpcTunnelLastChangedObjs_ObjectIdentity = ObjectIdentity
tmnxSysGrpcTunnelLastChangedObjs = _TmnxSysGrpcTunnelLastChangedObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 1)
)
_TmnxGTnlDestGrpTblLastChgd_Type = TimeStamp
_TmnxGTnlDestGrpTblLastChgd_Object = MibScalar
tmnxGTnlDestGrpTblLastChgd = _TmnxGTnlDestGrpTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 1, 1),
    _TmnxGTnlDestGrpTblLastChgd_Type()
)
tmnxGTnlDestGrpTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGTnlDestGrpTblLastChgd.setStatus("current")
_TmnxGTnlDestGrpDestTblLastChgd_Type = TimeStamp
_TmnxGTnlDestGrpDestTblLastChgd_Object = MibScalar
tmnxGTnlDestGrpDestTblLastChgd = _TmnxGTnlDestGrpDestTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 1, 2),
    _TmnxGTnlDestGrpDestTblLastChgd_Type()
)
tmnxGTnlDestGrpDestTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGTnlDestGrpDestTblLastChgd.setStatus("current")
_TmnxGTnlTunnelTblLastChgd_Type = TimeStamp
_TmnxGTnlTunnelTblLastChgd_Object = MibScalar
tmnxGTnlTunnelTblLastChgd = _TmnxGTnlTunnelTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 1, 3),
    _TmnxGTnlTunnelTblLastChgd_Type()
)
tmnxGTnlTunnelTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelTblLastChgd.setStatus("current")
_TmnxGTnlTunnelHandlerTblLastChgd_Type = TimeStamp
_TmnxGTnlTunnelHandlerTblLastChgd_Object = MibScalar
tmnxGTnlTunnelHandlerTblLastChgd = _TmnxGTnlTunnelHandlerTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 1, 4),
    _TmnxGTnlTunnelHandlerTblLastChgd_Type()
)
tmnxGTnlTunnelHandlerTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelHandlerTblLastChgd.setStatus("current")
_TmnxGrpcTunnelDestGroupTable_Object = MibTable
tmnxGrpcTunnelDestGroupTable = _TmnxGrpcTunnelDestGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 2)
)
if mibBuilder.loadTexts:
    tmnxGrpcTunnelDestGroupTable.setStatus("current")
_TmnxGrpcTunnelDestGroupEntry_Object = MibTableRow
tmnxGrpcTunnelDestGroupEntry = _TmnxGrpcTunnelDestGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 2, 1)
)
tmnxGrpcTunnelDestGroupEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxGTnlDestGrpName"),
)
if mibBuilder.loadTexts:
    tmnxGrpcTunnelDestGroupEntry.setStatus("current")
_TmnxGTnlDestGrpName_Type = TNamedItem
_TmnxGTnlDestGrpName_Object = MibTableColumn
tmnxGTnlDestGrpName = _TmnxGTnlDestGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 2, 1, 1),
    _TmnxGTnlDestGrpName_Type()
)
tmnxGTnlDestGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxGTnlDestGrpName.setStatus("current")
_TmnxGTnlDestGrpRowStatus_Type = RowStatus
_TmnxGTnlDestGrpRowStatus_Object = MibTableColumn
tmnxGTnlDestGrpRowStatus = _TmnxGTnlDestGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 2, 1, 2),
    _TmnxGTnlDestGrpRowStatus_Type()
)
tmnxGTnlDestGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlDestGrpRowStatus.setStatus("current")
_TmnxGTnlDestGrpLastChgd_Type = TimeStamp
_TmnxGTnlDestGrpLastChgd_Object = MibTableColumn
tmnxGTnlDestGrpLastChgd = _TmnxGTnlDestGrpLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 2, 1, 3),
    _TmnxGTnlDestGrpLastChgd_Type()
)
tmnxGTnlDestGrpLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGTnlDestGrpLastChgd.setStatus("current")


class _TmnxGTnlDestGrpDescription_Type(TItemDescription):
    """Custom type tmnxGTnlDestGrpDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxGTnlDestGrpDescription_Type.__name__ = "TItemDescription"
_TmnxGTnlDestGrpDescription_Object = MibTableColumn
tmnxGTnlDestGrpDescription = _TmnxGTnlDestGrpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 2, 1, 4),
    _TmnxGTnlDestGrpDescription_Type()
)
tmnxGTnlDestGrpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlDestGrpDescription.setStatus("current")


class _TmnxGTnlDestGrpTlsClientProf_Type(TNamedItemOrEmpty):
    """Custom type tmnxGTnlDestGrpTlsClientProf based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxGTnlDestGrpTlsClientProf_Type.__name__ = "TNamedItemOrEmpty"
_TmnxGTnlDestGrpTlsClientProf_Object = MibTableColumn
tmnxGTnlDestGrpTlsClientProf = _TmnxGTnlDestGrpTlsClientProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 2, 1, 5),
    _TmnxGTnlDestGrpTlsClientProf_Type()
)
tmnxGTnlDestGrpTlsClientProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlDestGrpTlsClientProf.setStatus("current")


class _TmnxGTnlDestGrpAllowUnsecConn_Type(TruthValue):
    """Custom type tmnxGTnlDestGrpAllowUnsecConn based on TruthValue"""
    defaultValue = 2


_TmnxGTnlDestGrpAllowUnsecConn_Type.__name__ = "TruthValue"
_TmnxGTnlDestGrpAllowUnsecConn_Object = MibTableColumn
tmnxGTnlDestGrpAllowUnsecConn = _TmnxGTnlDestGrpAllowUnsecConn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 2, 1, 6),
    _TmnxGTnlDestGrpAllowUnsecConn_Type()
)
tmnxGTnlDestGrpAllowUnsecConn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlDestGrpAllowUnsecConn.setStatus("current")


class _TmnxGTnlDestGrpTcpKaAdminState_Type(TmnxAdminState):
    """Custom type tmnxGTnlDestGrpTcpKaAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxGTnlDestGrpTcpKaAdminState_Type.__name__ = "TmnxAdminState"
_TmnxGTnlDestGrpTcpKaAdminState_Object = MibTableColumn
tmnxGTnlDestGrpTcpKaAdminState = _TmnxGTnlDestGrpTcpKaAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 2, 1, 7),
    _TmnxGTnlDestGrpTcpKaAdminState_Type()
)
tmnxGTnlDestGrpTcpKaAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlDestGrpTcpKaAdminState.setStatus("current")


class _TmnxGTnlDestGrpTcpKaIdle_Type(Unsigned32):
    """Custom type tmnxGTnlDestGrpTcpKaIdle based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_TmnxGTnlDestGrpTcpKaIdle_Type.__name__ = "Unsigned32"
_TmnxGTnlDestGrpTcpKaIdle_Object = MibTableColumn
tmnxGTnlDestGrpTcpKaIdle = _TmnxGTnlDestGrpTcpKaIdle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 2, 1, 8),
    _TmnxGTnlDestGrpTcpKaIdle_Type()
)
tmnxGTnlDestGrpTcpKaIdle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlDestGrpTcpKaIdle.setStatus("current")
if mibBuilder.loadTexts:
    tmnxGTnlDestGrpTcpKaIdle.setUnits("seconds")


class _TmnxGTnlDestGrpTcpKaInterval_Type(Unsigned32):
    """Custom type tmnxGTnlDestGrpTcpKaInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_TmnxGTnlDestGrpTcpKaInterval_Type.__name__ = "Unsigned32"
_TmnxGTnlDestGrpTcpKaInterval_Object = MibTableColumn
tmnxGTnlDestGrpTcpKaInterval = _TmnxGTnlDestGrpTcpKaInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 2, 1, 9),
    _TmnxGTnlDestGrpTcpKaInterval_Type()
)
tmnxGTnlDestGrpTcpKaInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlDestGrpTcpKaInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxGTnlDestGrpTcpKaInterval.setUnits("seconds")


class _TmnxGTnlDestGrpTcpKaCount_Type(Unsigned32):
    """Custom type tmnxGTnlDestGrpTcpKaCount based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 100),
    )


_TmnxGTnlDestGrpTcpKaCount_Type.__name__ = "Unsigned32"
_TmnxGTnlDestGrpTcpKaCount_Object = MibTableColumn
tmnxGTnlDestGrpTcpKaCount = _TmnxGTnlDestGrpTcpKaCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 2, 1, 10),
    _TmnxGTnlDestGrpTcpKaCount_Type()
)
tmnxGTnlDestGrpTcpKaCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlDestGrpTcpKaCount.setStatus("current")
_TmnxGrpcTunnelDestGroupDestTable_Object = MibTable
tmnxGrpcTunnelDestGroupDestTable = _TmnxGrpcTunnelDestGroupDestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 3)
)
if mibBuilder.loadTexts:
    tmnxGrpcTunnelDestGroupDestTable.setStatus("current")
_TmnxGrpcTunnelDestGroupDestEntry_Object = MibTableRow
tmnxGrpcTunnelDestGroupDestEntry = _TmnxGrpcTunnelDestGroupDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 3, 1)
)
tmnxGrpcTunnelDestGroupDestEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxGTnlDestGrpName"),
    (0, "TIMETRA-SYSTEM-MIB", "tmnxGTnlDestGrpDestIndex"),
)
if mibBuilder.loadTexts:
    tmnxGrpcTunnelDestGroupDestEntry.setStatus("current")


class _TmnxGTnlDestGrpDestIndex_Type(Unsigned32):
    """Custom type tmnxGTnlDestGrpDestIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TmnxGTnlDestGrpDestIndex_Type.__name__ = "Unsigned32"
_TmnxGTnlDestGrpDestIndex_Object = MibTableColumn
tmnxGTnlDestGrpDestIndex = _TmnxGTnlDestGrpDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 3, 1, 1),
    _TmnxGTnlDestGrpDestIndex_Type()
)
tmnxGTnlDestGrpDestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxGTnlDestGrpDestIndex.setStatus("current")
_TmnxGTnlDestGrpDestRowStatus_Type = RowStatus
_TmnxGTnlDestGrpDestRowStatus_Object = MibTableColumn
tmnxGTnlDestGrpDestRowStatus = _TmnxGTnlDestGrpDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 3, 1, 2),
    _TmnxGTnlDestGrpDestRowStatus_Type()
)
tmnxGTnlDestGrpDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlDestGrpDestRowStatus.setStatus("current")
_TmnxGTnlDestGrpDestLastChgd_Type = TimeStamp
_TmnxGTnlDestGrpDestLastChgd_Object = MibTableColumn
tmnxGTnlDestGrpDestLastChgd = _TmnxGTnlDestGrpDestLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 3, 1, 3),
    _TmnxGTnlDestGrpDestLastChgd_Type()
)
tmnxGTnlDestGrpDestLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGTnlDestGrpDestLastChgd.setStatus("current")
_TmnxGTnlDestGrpDestAddType_Type = InetAddressType
_TmnxGTnlDestGrpDestAddType_Object = MibTableColumn
tmnxGTnlDestGrpDestAddType = _TmnxGTnlDestGrpDestAddType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 3, 1, 4),
    _TmnxGTnlDestGrpDestAddType_Type()
)
tmnxGTnlDestGrpDestAddType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlDestGrpDestAddType.setStatus("current")


class _TmnxGTnlDestGrpDestAddress_Type(InetAddress):
    """Custom type tmnxGTnlDestGrpDestAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxGTnlDestGrpDestAddress_Type.__name__ = "InetAddress"
_TmnxGTnlDestGrpDestAddress_Object = MibTableColumn
tmnxGTnlDestGrpDestAddress = _TmnxGTnlDestGrpDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 3, 1, 5),
    _TmnxGTnlDestGrpDestAddress_Type()
)
tmnxGTnlDestGrpDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlDestGrpDestAddress.setStatus("current")
_TmnxGTnlDestGrpDestPort_Type = InetPortNumber
_TmnxGTnlDestGrpDestPort_Object = MibTableColumn
tmnxGTnlDestGrpDestPort = _TmnxGTnlDestGrpDestPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 3, 1, 6),
    _TmnxGTnlDestGrpDestPort_Type()
)
tmnxGTnlDestGrpDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlDestGrpDestPort.setStatus("current")


class _TmnxGTnlDestGrpDestVRtrId_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxGTnlDestGrpDestVRtrId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxGTnlDestGrpDestVRtrId_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxGTnlDestGrpDestVRtrId_Object = MibTableColumn
tmnxGTnlDestGrpDestVRtrId = _TmnxGTnlDestGrpDestVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 3, 1, 7),
    _TmnxGTnlDestGrpDestVRtrId_Type()
)
tmnxGTnlDestGrpDestVRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlDestGrpDestVRtrId.setStatus("current")


class _TmnxGTnlDestGrpDestLclSrcAddType_Type(InetAddressType):
    """Custom type tmnxGTnlDestGrpDestLclSrcAddType based on InetAddressType"""
    defaultValue = 0


_TmnxGTnlDestGrpDestLclSrcAddType_Type.__name__ = "InetAddressType"
_TmnxGTnlDestGrpDestLclSrcAddType_Object = MibTableColumn
tmnxGTnlDestGrpDestLclSrcAddType = _TmnxGTnlDestGrpDestLclSrcAddType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 3, 1, 8),
    _TmnxGTnlDestGrpDestLclSrcAddType_Type()
)
tmnxGTnlDestGrpDestLclSrcAddType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlDestGrpDestLclSrcAddType.setStatus("current")


class _TmnxGTnlDestGrpDestLclSrcAddress_Type(InetAddress):
    """Custom type tmnxGTnlDestGrpDestLclSrcAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxGTnlDestGrpDestLclSrcAddress_Type.__name__ = "InetAddress"
_TmnxGTnlDestGrpDestLclSrcAddress_Object = MibTableColumn
tmnxGTnlDestGrpDestLclSrcAddress = _TmnxGTnlDestGrpDestLclSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 3, 1, 9),
    _TmnxGTnlDestGrpDestLclSrcAddress_Type()
)
tmnxGTnlDestGrpDestLclSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlDestGrpDestLclSrcAddress.setStatus("current")


class _TmnxGTnlDestGrpDestOrigQosMark_Type(TDSCPNameOrEmpty):
    """Custom type tmnxGTnlDestGrpDestOrigQosMark based on TDSCPNameOrEmpty"""
    defaultHexValue = ""


_TmnxGTnlDestGrpDestOrigQosMark_Type.__name__ = "TDSCPNameOrEmpty"
_TmnxGTnlDestGrpDestOrigQosMark_Object = MibTableColumn
tmnxGTnlDestGrpDestOrigQosMark = _TmnxGTnlDestGrpDestOrigQosMark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 3, 1, 10),
    _TmnxGTnlDestGrpDestOrigQosMark_Type()
)
tmnxGTnlDestGrpDestOrigQosMark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlDestGrpDestOrigQosMark.setStatus("current")
_TmnxGTnlTunnelTable_Object = MibTable
tmnxGTnlTunnelTable = _TmnxGTnlTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 4)
)
if mibBuilder.loadTexts:
    tmnxGTnlTunnelTable.setStatus("current")
_TmnxGTnlTunnelEntry_Object = MibTableRow
tmnxGTnlTunnelEntry = _TmnxGTnlTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 4, 1)
)
tmnxGTnlTunnelEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelName"),
)
if mibBuilder.loadTexts:
    tmnxGTnlTunnelEntry.setStatus("current")
_TmnxGTnlTunnelName_Type = TNamedItem
_TmnxGTnlTunnelName_Object = MibTableColumn
tmnxGTnlTunnelName = _TmnxGTnlTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 4, 1, 1),
    _TmnxGTnlTunnelName_Type()
)
tmnxGTnlTunnelName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelName.setStatus("current")
_TmnxGTnlTunnelRowStatus_Type = RowStatus
_TmnxGTnlTunnelRowStatus_Object = MibTableColumn
tmnxGTnlTunnelRowStatus = _TmnxGTnlTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 4, 1, 2),
    _TmnxGTnlTunnelRowStatus_Type()
)
tmnxGTnlTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelRowStatus.setStatus("current")
_TmnxGTnlTunnelLastChgd_Type = TimeStamp
_TmnxGTnlTunnelLastChgd_Object = MibTableColumn
tmnxGTnlTunnelLastChgd = _TmnxGTnlTunnelLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 4, 1, 3),
    _TmnxGTnlTunnelLastChgd_Type()
)
tmnxGTnlTunnelLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelLastChgd.setStatus("current")


class _TmnxGTnlTunnelAdminState_Type(TmnxAdminState):
    """Custom type tmnxGTnlTunnelAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxGTnlTunnelAdminState_Type.__name__ = "TmnxAdminState"
_TmnxGTnlTunnelAdminState_Object = MibTableColumn
tmnxGTnlTunnelAdminState = _TmnxGTnlTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 4, 1, 4),
    _TmnxGTnlTunnelAdminState_Type()
)
tmnxGTnlTunnelAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelAdminState.setStatus("current")
_TmnxGTnlTunnelOperState_Type = TmnxOperState
_TmnxGTnlTunnelOperState_Object = MibTableColumn
tmnxGTnlTunnelOperState = _TmnxGTnlTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 4, 1, 5),
    _TmnxGTnlTunnelOperState_Type()
)
tmnxGTnlTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelOperState.setStatus("current")


class _TmnxGTnlTunnelOperDownReason_Type(OctetString):
    """Custom type tmnxGTnlTunnelOperDownReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TmnxGTnlTunnelOperDownReason_Type.__name__ = "OctetString"
_TmnxGTnlTunnelOperDownReason_Object = MibTableColumn
tmnxGTnlTunnelOperDownReason = _TmnxGTnlTunnelOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 4, 1, 6),
    _TmnxGTnlTunnelOperDownReason_Type()
)
tmnxGTnlTunnelOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelOperDownReason.setStatus("current")


class _TmnxGTnlTunnelDescription_Type(TItemDescription):
    """Custom type tmnxGTnlTunnelDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxGTnlTunnelDescription_Type.__name__ = "TItemDescription"
_TmnxGTnlTunnelDescription_Object = MibTableColumn
tmnxGTnlTunnelDescription = _TmnxGTnlTunnelDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 4, 1, 7),
    _TmnxGTnlTunnelDescription_Type()
)
tmnxGTnlTunnelDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelDescription.setStatus("current")


class _TmnxGTnlTunnelDestGrp_Type(TNamedItemOrEmpty):
    """Custom type tmnxGTnlTunnelDestGrp based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxGTnlTunnelDestGrp_Type.__name__ = "TNamedItemOrEmpty"
_TmnxGTnlTunnelDestGrp_Object = MibTableColumn
tmnxGTnlTunnelDestGrp = _TmnxGTnlTunnelDestGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 4, 1, 8),
    _TmnxGTnlTunnelDestGrp_Type()
)
tmnxGTnlTunnelDestGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelDestGrp.setStatus("current")


class _TmnxGTnlTunnelTgtNameCustomStr_Type(DisplayString):
    """Custom type tmnxGTnlTunnelTgtNameCustomStr based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxGTnlTunnelTgtNameCustomStr_Type.__name__ = "DisplayString"
_TmnxGTnlTunnelTgtNameCustomStr_Object = MibTableColumn
tmnxGTnlTunnelTgtNameCustomStr = _TmnxGTnlTunnelTgtNameCustomStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 4, 1, 9),
    _TmnxGTnlTunnelTgtNameCustomStr_Type()
)
tmnxGTnlTunnelTgtNameCustomStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelTgtNameCustomStr.setStatus("current")


class _TmnxGTnlTunnelTgtNameUserAgent_Type(TruthValue):
    """Custom type tmnxGTnlTunnelTgtNameUserAgent based on TruthValue"""
    defaultValue = 2


_TmnxGTnlTunnelTgtNameUserAgent_Type.__name__ = "TruthValue"
_TmnxGTnlTunnelTgtNameUserAgent_Object = MibTableColumn
tmnxGTnlTunnelTgtNameUserAgent = _TmnxGTnlTunnelTgtNameUserAgent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 4, 1, 10),
    _TmnxGTnlTunnelTgtNameUserAgent_Type()
)
tmnxGTnlTunnelTgtNameUserAgent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelTgtNameUserAgent.setStatus("current")


class _TmnxGTnlTunnelTgtNameNodeName_Type(TruthValue):
    """Custom type tmnxGTnlTunnelTgtNameNodeName based on TruthValue"""
    defaultValue = 2


_TmnxGTnlTunnelTgtNameNodeName_Type.__name__ = "TruthValue"
_TmnxGTnlTunnelTgtNameNodeName_Object = MibTableColumn
tmnxGTnlTunnelTgtNameNodeName = _TmnxGTnlTunnelTgtNameNodeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 4, 1, 11),
    _TmnxGTnlTunnelTgtNameNodeName_Type()
)
tmnxGTnlTunnelTgtNameNodeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelTgtNameNodeName.setStatus("current")


class _TmnxGTnlTunnelOperTargetName_Type(OctetString):
    """Custom type tmnxGTnlTunnelOperTargetName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 422),
    )


_TmnxGTnlTunnelOperTargetName_Type.__name__ = "OctetString"
_TmnxGTnlTunnelOperTargetName_Object = MibTableColumn
tmnxGTnlTunnelOperTargetName = _TmnxGTnlTunnelOperTargetName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 4, 1, 12),
    _TmnxGTnlTunnelOperTargetName_Type()
)
tmnxGTnlTunnelOperTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelOperTargetName.setStatus("current")
_TmnxGTnlTunnelHandlerTable_Object = MibTable
tmnxGTnlTunnelHandlerTable = _TmnxGTnlTunnelHandlerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 5)
)
if mibBuilder.loadTexts:
    tmnxGTnlTunnelHandlerTable.setStatus("current")
_TmnxGTnlTunnelHandlerEntry_Object = MibTableRow
tmnxGTnlTunnelHandlerEntry = _TmnxGTnlTunnelHandlerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 5, 1)
)
tmnxGTnlTunnelHandlerEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelName"),
    (0, "TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelHandlerName"),
)
if mibBuilder.loadTexts:
    tmnxGTnlTunnelHandlerEntry.setStatus("current")
_TmnxGTnlTunnelHandlerName_Type = TNamedItem
_TmnxGTnlTunnelHandlerName_Object = MibTableColumn
tmnxGTnlTunnelHandlerName = _TmnxGTnlTunnelHandlerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 5, 1, 1),
    _TmnxGTnlTunnelHandlerName_Type()
)
tmnxGTnlTunnelHandlerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelHandlerName.setStatus("current")
_TmnxGTnlTunnelHandlerRowStatus_Type = RowStatus
_TmnxGTnlTunnelHandlerRowStatus_Object = MibTableColumn
tmnxGTnlTunnelHandlerRowStatus = _TmnxGTnlTunnelHandlerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 5, 1, 2),
    _TmnxGTnlTunnelHandlerRowStatus_Type()
)
tmnxGTnlTunnelHandlerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelHandlerRowStatus.setStatus("current")
_TmnxGTnlTunnelHandlerLastChgd_Type = TimeStamp
_TmnxGTnlTunnelHandlerLastChgd_Object = MibTableColumn
tmnxGTnlTunnelHandlerLastChgd = _TmnxGTnlTunnelHandlerLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 5, 1, 3),
    _TmnxGTnlTunnelHandlerLastChgd_Type()
)
tmnxGTnlTunnelHandlerLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelHandlerLastChgd.setStatus("current")


class _TmnxGTnlTunnelHandlerAdminState_Type(TmnxAdminState):
    """Custom type tmnxGTnlTunnelHandlerAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxGTnlTunnelHandlerAdminState_Type.__name__ = "TmnxAdminState"
_TmnxGTnlTunnelHandlerAdminState_Object = MibTableColumn
tmnxGTnlTunnelHandlerAdminState = _TmnxGTnlTunnelHandlerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 5, 1, 4),
    _TmnxGTnlTunnelHandlerAdminState_Type()
)
tmnxGTnlTunnelHandlerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelHandlerAdminState.setStatus("current")


class _TmnxGTnlTunnelHandlerPort_Type(InetPortNumber):
    """Custom type tmnxGTnlTunnelHandlerPort based on InetPortNumber"""
    defaultValue = 0


_TmnxGTnlTunnelHandlerPort_Type.__name__ = "InetPortNumber"
_TmnxGTnlTunnelHandlerPort_Object = MibTableColumn
tmnxGTnlTunnelHandlerPort = _TmnxGTnlTunnelHandlerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 5, 1, 5),
    _TmnxGTnlTunnelHandlerPort_Type()
)
tmnxGTnlTunnelHandlerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelHandlerPort.setStatus("current")


class _TmnxGTnlTunnelHandlerCustomType_Type(DisplayString):
    """Custom type tmnxGTnlTunnelHandlerCustomType based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxGTnlTunnelHandlerCustomType_Type.__name__ = "DisplayString"
_TmnxGTnlTunnelHandlerCustomType_Object = MibTableColumn
tmnxGTnlTunnelHandlerCustomType = _TmnxGTnlTunnelHandlerCustomType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 5, 1, 6),
    _TmnxGTnlTunnelHandlerCustomType_Type()
)
tmnxGTnlTunnelHandlerCustomType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelHandlerCustomType.setStatus("current")


class _TmnxGTnlTunnelHandlerGrpcServer_Type(TruthValue):
    """Custom type tmnxGTnlTunnelHandlerGrpcServer based on TruthValue"""
    defaultValue = 2


_TmnxGTnlTunnelHandlerGrpcServer_Type.__name__ = "TruthValue"
_TmnxGTnlTunnelHandlerGrpcServer_Object = MibTableColumn
tmnxGTnlTunnelHandlerGrpcServer = _TmnxGTnlTunnelHandlerGrpcServer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 5, 1, 7),
    _TmnxGTnlTunnelHandlerGrpcServer_Type()
)
tmnxGTnlTunnelHandlerGrpcServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelHandlerGrpcServer.setStatus("current")


class _TmnxGTnlTunnelHandlerSshServer_Type(TruthValue):
    """Custom type tmnxGTnlTunnelHandlerSshServer based on TruthValue"""
    defaultValue = 2


_TmnxGTnlTunnelHandlerSshServer_Type.__name__ = "TruthValue"
_TmnxGTnlTunnelHandlerSshServer_Object = MibTableColumn
tmnxGTnlTunnelHandlerSshServer = _TmnxGTnlTunnelHandlerSshServer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 5, 1, 8),
    _TmnxGTnlTunnelHandlerSshServer_Type()
)
tmnxGTnlTunnelHandlerSshServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelHandlerSshServer.setStatus("current")
_TmnxGTnlTunnelDestTable_Object = MibTable
tmnxGTnlTunnelDestTable = _TmnxGTnlTunnelDestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 6)
)
if mibBuilder.loadTexts:
    tmnxGTnlTunnelDestTable.setStatus("current")
_TmnxGTnlTunnelDestEntry_Object = MibTableRow
tmnxGTnlTunnelDestEntry = _TmnxGTnlTunnelDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 6, 1)
)
tmnxGTnlTunnelDestEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelName"),
    (0, "TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelDestIndex"),
)
if mibBuilder.loadTexts:
    tmnxGTnlTunnelDestEntry.setStatus("current")


class _TmnxGTnlTunnelDestIndex_Type(Unsigned32):
    """Custom type tmnxGTnlTunnelDestIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TmnxGTnlTunnelDestIndex_Type.__name__ = "Unsigned32"
_TmnxGTnlTunnelDestIndex_Object = MibTableColumn
tmnxGTnlTunnelDestIndex = _TmnxGTnlTunnelDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 6, 1, 1),
    _TmnxGTnlTunnelDestIndex_Type()
)
tmnxGTnlTunnelDestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelDestIndex.setStatus("current")
_TmnxGTnlTunnelDestAddType_Type = InetAddressType
_TmnxGTnlTunnelDestAddType_Object = MibTableColumn
tmnxGTnlTunnelDestAddType = _TmnxGTnlTunnelDestAddType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 6, 1, 2),
    _TmnxGTnlTunnelDestAddType_Type()
)
tmnxGTnlTunnelDestAddType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelDestAddType.setStatus("current")


class _TmnxGTnlTunnelDestAddress_Type(InetAddress):
    """Custom type tmnxGTnlTunnelDestAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxGTnlTunnelDestAddress_Type.__name__ = "InetAddress"
_TmnxGTnlTunnelDestAddress_Object = MibTableColumn
tmnxGTnlTunnelDestAddress = _TmnxGTnlTunnelDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 6, 1, 3),
    _TmnxGTnlTunnelDestAddress_Type()
)
tmnxGTnlTunnelDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelDestAddress.setStatus("current")
_TmnxGTnlTunnelDestPort_Type = InetPortNumber
_TmnxGTnlTunnelDestPort_Object = MibTableColumn
tmnxGTnlTunnelDestPort = _TmnxGTnlTunnelDestPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 6, 1, 4),
    _TmnxGTnlTunnelDestPort_Type()
)
tmnxGTnlTunnelDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelDestPort.setStatus("current")
_TmnxGTnlTunnelDestOperState_Type = TmnxOperState
_TmnxGTnlTunnelDestOperState_Object = MibTableColumn
tmnxGTnlTunnelDestOperState = _TmnxGTnlTunnelDestOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 6, 1, 5),
    _TmnxGTnlTunnelDestOperState_Type()
)
tmnxGTnlTunnelDestOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelDestOperState.setStatus("current")


class _TmnxGTnlTunnelDestOperDownReason_Type(OctetString):
    """Custom type tmnxGTnlTunnelDestOperDownReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TmnxGTnlTunnelDestOperDownReason_Type.__name__ = "OctetString"
_TmnxGTnlTunnelDestOperDownReason_Object = MibTableColumn
tmnxGTnlTunnelDestOperDownReason = _TmnxGTnlTunnelDestOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 6, 1, 6),
    _TmnxGTnlTunnelDestOperDownReason_Type()
)
tmnxGTnlTunnelDestOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelDestOperDownReason.setStatus("current")
_TmnxGTnlTunnelDestOperVRtrId_Type = TmnxVRtrIDOrZero
_TmnxGTnlTunnelDestOperVRtrId_Object = MibTableColumn
tmnxGTnlTunnelDestOperVRtrId = _TmnxGTnlTunnelDestOperVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 6, 1, 7),
    _TmnxGTnlTunnelDestOperVRtrId_Type()
)
tmnxGTnlTunnelDestOperVRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelDestOperVRtrId.setStatus("current")
_TmnxGTnlTunnelDestLastOperChange_Type = DateAndTime
_TmnxGTnlTunnelDestLastOperChange_Object = MibTableColumn
tmnxGTnlTunnelDestLastOperChange = _TmnxGTnlTunnelDestLastOperChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 6, 1, 8),
    _TmnxGTnlTunnelDestLastOperChange_Type()
)
tmnxGTnlTunnelDestLastOperChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelDestLastOperChange.setStatus("current")
_TmnxGTnlTunnelDestConnAttempts_Type = Counter64
_TmnxGTnlTunnelDestConnAttempts_Object = MibTableColumn
tmnxGTnlTunnelDestConnAttempts = _TmnxGTnlTunnelDestConnAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 6, 1, 9),
    _TmnxGTnlTunnelDestConnAttempts_Type()
)
tmnxGTnlTunnelDestConnAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelDestConnAttempts.setStatus("current")
_TmnxGTnlTunnelSessionTable_Object = MibTable
tmnxGTnlTunnelSessionTable = _TmnxGTnlTunnelSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 7)
)
if mibBuilder.loadTexts:
    tmnxGTnlTunnelSessionTable.setStatus("current")
_TmnxGTnlTunnelSessionEntry_Object = MibTableRow
tmnxGTnlTunnelSessionEntry = _TmnxGTnlTunnelSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 7, 1)
)
tmnxGTnlTunnelSessionEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelName"),
    (0, "TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelSessionTag"),
)
if mibBuilder.loadTexts:
    tmnxGTnlTunnelSessionEntry.setStatus("current")
_TmnxGTnlTunnelSessionTag_Type = Integer32
_TmnxGTnlTunnelSessionTag_Object = MibTableColumn
tmnxGTnlTunnelSessionTag = _TmnxGTnlTunnelSessionTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 7, 1, 1),
    _TmnxGTnlTunnelSessionTag_Type()
)
tmnxGTnlTunnelSessionTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelSessionTag.setStatus("current")
_TmnxGTnlTunnelSessionStartTime_Type = DateAndTime
_TmnxGTnlTunnelSessionStartTime_Object = MibTableColumn
tmnxGTnlTunnelSessionStartTime = _TmnxGTnlTunnelSessionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 7, 1, 2),
    _TmnxGTnlTunnelSessionStartTime_Type()
)
tmnxGTnlTunnelSessionStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelSessionStartTime.setStatus("current")


class _TmnxGTnlTunnelSessionTargetType_Type(DisplayString):
    """Custom type tmnxGTnlTunnelSessionTargetType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxGTnlTunnelSessionTargetType_Type.__name__ = "DisplayString"
_TmnxGTnlTunnelSessionTargetType_Object = MibTableColumn
tmnxGTnlTunnelSessionTargetType = _TmnxGTnlTunnelSessionTargetType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 7, 1, 3),
    _TmnxGTnlTunnelSessionTargetType_Type()
)
tmnxGTnlTunnelSessionTargetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelSessionTargetType.setStatus("current")
_TmnxGTnlTunnelSessionLclSrcPort_Type = InetPortNumber
_TmnxGTnlTunnelSessionLclSrcPort_Object = MibTableColumn
tmnxGTnlTunnelSessionLclSrcPort = _TmnxGTnlTunnelSessionLclSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 7, 1, 4),
    _TmnxGTnlTunnelSessionLclSrcPort_Type()
)
tmnxGTnlTunnelSessionLclSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelSessionLclSrcPort.setStatus("current")
_TmnxGTnlTunnelSessionRxBytes_Type = Counter64
_TmnxGTnlTunnelSessionRxBytes_Object = MibTableColumn
tmnxGTnlTunnelSessionRxBytes = _TmnxGTnlTunnelSessionRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 7, 1, 5),
    _TmnxGTnlTunnelSessionRxBytes_Type()
)
tmnxGTnlTunnelSessionRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelSessionRxBytes.setStatus("current")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelSessionRxBytes.setUnits("bytes")
_TmnxGTnlTunnelSessionTxBytes_Type = Counter64
_TmnxGTnlTunnelSessionTxBytes_Object = MibTableColumn
tmnxGTnlTunnelSessionTxBytes = _TmnxGTnlTunnelSessionTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 57, 7, 1, 6),
    _TmnxGTnlTunnelSessionTxBytes_Type()
)
tmnxGTnlTunnelSessionTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelSessionTxBytes.setStatus("current")
if mibBuilder.loadTexts:
    tmnxGTnlTunnelSessionTxBytes.setUnits("bytes")
_TmnxSysFanControl_ObjectIdentity = ObjectIdentity
tmnxSysFanControl = _TmnxSysFanControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 58)
)


class _TmnxSysFanIncMinimumSpeed_Type(TruthValue):
    """Custom type tmnxSysFanIncMinimumSpeed based on TruthValue"""
    defaultValue = 2


_TmnxSysFanIncMinimumSpeed_Type.__name__ = "TruthValue"
_TmnxSysFanIncMinimumSpeed_Object = MibScalar
tmnxSysFanIncMinimumSpeed = _TmnxSysFanIncMinimumSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 58, 1),
    _TmnxSysFanIncMinimumSpeed_Type()
)
tmnxSysFanIncMinimumSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFanIncMinimumSpeed.setStatus("current")
_TmnxSysFpResourceAllocationObjs_ObjectIdentity = ObjectIdentity
tmnxSysFpResourceAllocationObjs = _TmnxSysFpResourceAllocationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 59)
)
_TmnxSysFpResAlcnLpmTblLastChg_Type = TimeStamp
_TmnxSysFpResAlcnLpmTblLastChg_Object = MibScalar
tmnxSysFpResAlcnLpmTblLastChg = _TmnxSysFpResAlcnLpmTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 59, 1),
    _TmnxSysFpResAlcnLpmTblLastChg_Type()
)
tmnxSysFpResAlcnLpmTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpResAlcnLpmTblLastChg.setStatus("current")
_TmnxSysFpResAlcnLpmTable_Object = MibTable
tmnxSysFpResAlcnLpmTable = _TmnxSysFpResAlcnLpmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 59, 2)
)
if mibBuilder.loadTexts:
    tmnxSysFpResAlcnLpmTable.setStatus("current")
_TmnxSysFpResAlcnLpmEntry_Object = MibTableRow
tmnxSysFpResAlcnLpmEntry = _TmnxSysFpResAlcnLpmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 59, 2, 1)
)
tmnxSysFpResAlcnLpmEntry.setIndexNames(
    (0, "TIMETRA-SYSTEM-MIB", "tmnxSysFpResAlcnLpmScaleOption"),
)
if mibBuilder.loadTexts:
    tmnxSysFpResAlcnLpmEntry.setStatus("current")


class _TmnxSysFpResAlcnLpmScaleOption_Type(Unsigned32):
    """Custom type tmnxSysFpResAlcnLpmScaleOption based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_TmnxSysFpResAlcnLpmScaleOption_Type.__name__ = "Unsigned32"
_TmnxSysFpResAlcnLpmScaleOption_Object = MibTableColumn
tmnxSysFpResAlcnLpmScaleOption = _TmnxSysFpResAlcnLpmScaleOption_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 59, 2, 1, 1),
    _TmnxSysFpResAlcnLpmScaleOption_Type()
)
tmnxSysFpResAlcnLpmScaleOption.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSysFpResAlcnLpmScaleOption.setStatus("current")
_TmnxSysFpResAlcnLpmLastChanged_Type = TimeStamp
_TmnxSysFpResAlcnLpmLastChanged_Object = MibTableColumn
tmnxSysFpResAlcnLpmLastChanged = _TmnxSysFpResAlcnLpmLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 59, 2, 1, 2),
    _TmnxSysFpResAlcnLpmLastChanged_Type()
)
tmnxSysFpResAlcnLpmLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpResAlcnLpmLastChanged.setStatus("current")
_TmnxSysFpResAlcnLpmAdminState_Type = TmnxAdminState
_TmnxSysFpResAlcnLpmAdminState_Object = MibTableColumn
tmnxSysFpResAlcnLpmAdminState = _TmnxSysFpResAlcnLpmAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 59, 2, 1, 3),
    _TmnxSysFpResAlcnLpmAdminState_Type()
)
tmnxSysFpResAlcnLpmAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSysFpResAlcnLpmAdminState.setStatus("current")
_TmnxSysFpResAlcnLpmOperState_Type = TmnxOperState
_TmnxSysFpResAlcnLpmOperState_Object = MibTableColumn
tmnxSysFpResAlcnLpmOperState = _TmnxSysFpResAlcnLpmOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 1, 59, 2, 1, 4),
    _TmnxSysFpResAlcnLpmOperState_Type()
)
tmnxSysFpResAlcnLpmOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSysFpResAlcnLpmOperState.setStatus("current")
_TmnxSysMIBNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxSysMIBNotifyPrefix = _TmnxSysMIBNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1)
)
_TmnxSysNotifications_ObjectIdentity = ObjectIdentity
tmnxSysNotifications = _TmnxSysNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0)
)
_TmnxSysMGNotifications_ObjectIdentity = ObjectIdentity
tmnxSysMGNotifications = _TmnxSysMGNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 1)
)
snmpCommunityEntry.registerAugmentions(
    ("TIMETRA-SYSTEM-MIB",
     "tmnxSysSnmpCommunityStatsEntry")
)
tmnxSysSnmpCommunityStatsEntry.setIndexNames(*snmpCommunityEntry.getIndexNames())
smLaunchEntry.registerAugmentions(
    ("TIMETRA-SYSTEM-MIB",
     "tmnxSmLaunchExtEntry")
)
tmnxSmLaunchExtEntry.setIndexNames(*smLaunchEntry.getIndexNames())
smRunEntry.registerAugmentions(
    ("TIMETRA-SYSTEM-MIB",
     "tmnxSmRunExtEntry")
)
tmnxSmRunExtEntry.setIndexNames(*smRunEntry.getIndexNames())

# Managed Objects groups

tmnxSysRadiusServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 4)
)
tmnxSysRadiusServerGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "radiusOperStatus"),
        ("TIMETRA-SYSTEM-MIB", "radiusServerAddress"),
        ("TIMETRA-SYSTEM-MIB", "radiusServerOperStatus"))
)
if mibBuilder.loadTexts:
    tmnxSysRadiusServerGroup.setStatus("obsolete")

tmnxSysTacPlusServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 5)
)
tmnxSysTacPlusServerGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tacplusOperStatus"),
        ("TIMETRA-SYSTEM-MIB", "tacplusServerAddress"),
        ("TIMETRA-SYSTEM-MIB", "tacplusServerOperStatus"))
)
if mibBuilder.loadTexts:
    tmnxSysTacPlusServerGroup.setStatus("obsolete")

tmnxSysBofGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 8)
)
tmnxSysBofGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sbiActiveIpAddr"),
        ("TIMETRA-SYSTEM-MIB", "sbiActiveIpMask"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyIpAddr"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyIpMask"),
        ("TIMETRA-SYSTEM-MIB", "sbiPrimaryImage"),
        ("TIMETRA-SYSTEM-MIB", "sbiSecondaryImage"),
        ("TIMETRA-SYSTEM-MIB", "sbiTertiaryImage"),
        ("TIMETRA-SYSTEM-MIB", "sbiPrimaryConfigFile"),
        ("TIMETRA-SYSTEM-MIB", "sbiSecondaryConfigFile"),
        ("TIMETRA-SYSTEM-MIB", "sbiTertiaryConfigFile"),
        ("TIMETRA-SYSTEM-MIB", "sbiPersist"),
        ("TIMETRA-SYSTEM-MIB", "sbiConsoleSpeed"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoNegotiate"),
        ("TIMETRA-SYSTEM-MIB", "sbiSpeed"),
        ("TIMETRA-SYSTEM-MIB", "sbiDuplex"),
        ("TIMETRA-SYSTEM-MIB", "sbiPrimaryDns"),
        ("TIMETRA-SYSTEM-MIB", "sbiSecondaryDns"),
        ("TIMETRA-SYSTEM-MIB", "sbiTertiaryDns"),
        ("TIMETRA-SYSTEM-MIB", "sbiDnsDomain"),
        ("TIMETRA-SYSTEM-MIB", "sbiWait"),
        ("TIMETRA-SYSTEM-MIB", "sbiStaticRouteNextHop"),
        ("TIMETRA-SYSTEM-MIB", "sbiStaticRouteRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxSysBofGroup.setStatus("obsolete")

tmnxSysConfigV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 12)
)
tmnxSysConfigV3v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "ssiSaveConfig"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncMode"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncForce"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncStatus"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncConfigLastTime"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncBootEnvLastTime"),
        ("TIMETRA-SYSTEM-MIB", "ssiConfigMaxBackupRevisions"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveConfigResult"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveBof"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveBofResult"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveConfigDest"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveConfigDetail"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedFailoverTime"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedFailoverReason"),
        ("TIMETRA-SYSTEM-MIB", "sbiConfigStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiPersistStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiPersistIndex"),
        ("TIMETRA-SYSTEM-MIB", "sbiSnmpdAdminStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiSnmpdOperStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiSnmpdMaxPktSize"),
        ("TIMETRA-SYSTEM-MIB", "sbiSnmpdPortNum"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootConfigOKScript"),
        ("TIMETRA-SYSTEM-MIB", "sbiConfigOKScriptStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootConfigFailScript"),
        ("TIMETRA-SYSTEM-MIB", "sbiConfigFailScriptStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiRedSwitchoverScript"),
        ("TIMETRA-SYSTEM-MIB", "sbiRedSwitchoverScriptStatus"),
        ("TIMETRA-SYSTEM-MIB", "slcFtpInboundMaxSessions"),
        ("TIMETRA-SYSTEM-MIB", "slcTelnetInboundMaxSessions"),
        ("TIMETRA-SYSTEM-MIB", "slcTelnetOutboundMaxSessions"),
        ("TIMETRA-SYSTEM-MIB", "slcPreLoginMessage"),
        ("TIMETRA-SYSTEM-MIB", "slcPreLoginMessageInclName"),
        ("TIMETRA-SYSTEM-MIB", "slcMessageOfTheDay"),
        ("TIMETRA-SYSTEM-MIB", "slcMessageOfTheDayType"),
        ("TIMETRA-SYSTEM-MIB", "slcLoginBanner"),
        ("TIMETRA-SYSTEM-MIB", "sysLACPSystemPriority"),
        ("TIMETRA-SYSTEM-MIB", "slcLoginExponentialBackOff"))
)
if mibBuilder.loadTexts:
    tmnxSysConfigV3v0Group.setStatus("obsolete")

tmnxSysGeneralV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 15)
)
tmnxSysGeneralV3v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sgiCpuUsage"),
        ("TIMETRA-SYSTEM-MIB", "sgiMemoryUsed"),
        ("TIMETRA-SYSTEM-MIB", "sgiMemoryAvailable"),
        ("TIMETRA-SYSTEM-MIB", "sgiMemoryPoolAllocated"),
        ("TIMETRA-SYSTEM-MIB", "sgiSwMajorVersion"),
        ("TIMETRA-SYSTEM-MIB", "sgiSwMinorVersion"),
        ("TIMETRA-SYSTEM-MIB", "sgiSwVersionModifier"))
)
if mibBuilder.loadTexts:
    tmnxSysGeneralV3v0Group.setStatus("current")

tmnxSysObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 17)
)
tmnxSysObsoleteGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "stiSummerZoneStartDate"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneEndDate"),
        ("TIMETRA-SYSTEM-MIB", "tacplusServerAddress"),
        ("TIMETRA-SYSTEM-MIB", "radiusServerAddress"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfMDCliCmdAccntLoad"))
)
if mibBuilder.loadTexts:
    tmnxSysObsoleteGroup.setStatus("obsolete")

tmnxPersistenceV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 18)
)
tmnxPersistenceV4v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "spiDhcpL2PersistenceFileLocation"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpL2PersistenceDescription"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpL3PersistenceFileLocation"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpL3PersistenceDescription"),
        ("TIMETRA-SYSTEM-MIB", "spiSubMgmtPersistenceFileLocation"),
        ("TIMETRA-SYSTEM-MIB", "spiSubMgmtPersistenceDescription"))
)
if mibBuilder.loadTexts:
    tmnxPersistenceV4v0Group.setStatus("obsolete")

tmnxSysTimeV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 19)
)
tmnxSysTimeV4v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "stiDateAndTime"),
        ("TIMETRA-SYSTEM-MIB", "stiActiveZone"),
        ("TIMETRA-SYSTEM-MIB", "stiHoursOffset"),
        ("TIMETRA-SYSTEM-MIB", "stiMinutesOffset"),
        ("TIMETRA-SYSTEM-MIB", "stiZoneType"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneRowStatus"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneOffset"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneStartDay"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneStartWeek"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneStartMonth"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneStartHour"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneStartMinute"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneEndDay"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneEndWeek"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneEndMonth"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneEndHour"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneEndMinute"),
        ("TIMETRA-SYSTEM-MIB", "sntpState"),
        ("TIMETRA-SYSTEM-MIB", "sntpServerRowStatus"),
        ("TIMETRA-SYSTEM-MIB", "sntpServerVersion"),
        ("TIMETRA-SYSTEM-MIB", "sntpServerPreference"),
        ("TIMETRA-SYSTEM-MIB", "sntpServerInterval"),
        ("TIMETRA-SYSTEM-MIB", "sntpAdminState"),
        ("TIMETRA-SYSTEM-MIB", "sntpOperStatus"))
)
if mibBuilder.loadTexts:
    tmnxSysTimeV4v0Group.setStatus("current")

tmnxSysNotifyObjsR4r0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 20)
)
tmnxSysNotifyObjsR4r0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxNotifyRow"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyRowAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyRowOperState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxMemoryModule"),
        ("TIMETRA-SYSTEM-MIB", "tmnxModuleMallocSize"),
        ("TIMETRA-SYSTEM-MIB", "tmnxDroppedTrapID"),
        ("TIMETRA-SYSTEM-MIB", "tmnxTrapDroppedReasonCode"),
        ("TIMETRA-SYSTEM-MIB", "tmnxTrapDroppedEntryID"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyEntryOID"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSnmpdErrorMsg"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTimeSetBy"))
)
if mibBuilder.loadTexts:
    tmnxSysNotifyObjsR4r0Group.setStatus("obsolete")

tmnxSysNotifyObjsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 22)
)
tmnxSysNotifyObjsV5v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxPersistencyClient"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyFileLocator"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyNotifyMsg"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistenceAffectedCpm"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyRow"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyRowAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyRowOperState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxMemoryModule"),
        ("TIMETRA-SYSTEM-MIB", "tmnxModuleMallocSize"),
        ("TIMETRA-SYSTEM-MIB", "tmnxDroppedTrapID"),
        ("TIMETRA-SYSTEM-MIB", "tmnxTrapDroppedReasonCode"),
        ("TIMETRA-SYSTEM-MIB", "tmnxTrapDroppedEntryID"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyEntryOID"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSnmpdErrorMsg"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTimeSetBy"),
        ("TIMETRA-SYSTEM-MIB", "tmnxFtpFailureMsg"),
        ("TIMETRA-SYSTEM-MIB", "tmnxFtpFailureDestAddressType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxFtpFailureDestAddress"))
)
if mibBuilder.loadTexts:
    tmnxSysNotifyObjsV5v0Group.setStatus("current")

tmnxSysTacPlusServerV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 25)
)
tmnxSysTacPlusServerV5v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tacplusOperStatus"),
        ("TIMETRA-SYSTEM-MIB", "tacplusServerOperStatus"),
        ("TIMETRA-SYSTEM-MIB", "tacPlusServerInetAddressType"),
        ("TIMETRA-SYSTEM-MIB", "tacPlusServerInetAddress"))
)
if mibBuilder.loadTexts:
    tmnxSysTacPlusServerV5v0Group.setStatus("current")

tmnxSysRadiusServerV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 26)
)
tmnxSysRadiusServerV5v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "radiusOperStatus"),
        ("TIMETRA-SYSTEM-MIB", "radiusServerOperStatus"),
        ("TIMETRA-SYSTEM-MIB", "radiusServerInetAddressType"),
        ("TIMETRA-SYSTEM-MIB", "radiusServerInetAddress"))
)
if mibBuilder.loadTexts:
    tmnxSysRadiusServerV5v0Group.setStatus("current")

tmnxSysObsoleteV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 27)
)
tmnxSysObsoleteV5v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "stiSummerZoneStartDate"),
        ("TIMETRA-SYSTEM-MIB", "stiSummerZoneEndDate"),
        ("TIMETRA-SYSTEM-MIB", "tacplusServerAddress"),
        ("TIMETRA-SYSTEM-MIB", "radiusServerAddress"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpL2PersistenceFileLocation"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpL2PersistenceDescription"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpL3PersistenceFileLocation"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpL3PersistenceDescription"))
)
if mibBuilder.loadTexts:
    tmnxSysObsoleteV5v0Group.setStatus("current")

tmnxPersistenceV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 28)
)
tmnxPersistenceV5v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "spiSubMgmtPersistenceFileLocation"),
        ("TIMETRA-SYSTEM-MIB", "spiSubMgmtPersistenceDescription"))
)
if mibBuilder.loadTexts:
    tmnxPersistenceV5v0Group.setStatus("obsolete")

tmnxSysIpv6MgmtItfV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 29)
)
tmnxSysIpv6MgmtItfV6v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sbiActiveIPv6Addr"),
        ("TIMETRA-SYSTEM-MIB", "sbiActiveIPv6PfxLen"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyIPv6Addr"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyIPv6PfxLen"),
        ("TIMETRA-SYSTEM-MIB", "sbiPrimaryDnsIPv6Addr"),
        ("TIMETRA-SYSTEM-MIB", "sbiSecondaryDnsIPv6Addr"),
        ("TIMETRA-SYSTEM-MIB", "sbiTertiaryDnsIPv6Addr"),
        ("TIMETRA-SYSTEM-MIB", "sbiStaticRouteIPv6NextHop"),
        ("TIMETRA-SYSTEM-MIB", "sbiStaticRouteIPv6RowStatus"),
        ("TIMETRA-SYSTEM-MIB", "sysDNSInfoLastChanged"),
        ("TIMETRA-SYSTEM-MIB", "sysDNSAddressResolvePref"))
)
if mibBuilder.loadTexts:
    tmnxSysIpv6MgmtItfV6v0Group.setStatus("current")

tmnxPersistenceV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 30)
)
tmnxPersistenceV6v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "spiSubMgmtPersistenceFileLocation"),
        ("TIMETRA-SYSTEM-MIB", "spiSubMgmtPersistenceDescription"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpSrvPersistenceFileLoc"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpSrvPersistenceDescr"))
)
if mibBuilder.loadTexts:
    tmnxPersistenceV6v0Group.setStatus("obsolete")

tmnxSysBofV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 31)
)
tmnxSysBofV6v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sbiActiveIpAddr"),
        ("TIMETRA-SYSTEM-MIB", "sbiActiveIpMask"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyIpAddr"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyIpMask"),
        ("TIMETRA-SYSTEM-MIB", "sbiPrimaryImage"),
        ("TIMETRA-SYSTEM-MIB", "sbiSecondaryImage"),
        ("TIMETRA-SYSTEM-MIB", "sbiTertiaryImage"),
        ("TIMETRA-SYSTEM-MIB", "sbiPrimaryConfigFile"),
        ("TIMETRA-SYSTEM-MIB", "sbiSecondaryConfigFile"),
        ("TIMETRA-SYSTEM-MIB", "sbiTertiaryConfigFile"),
        ("TIMETRA-SYSTEM-MIB", "sbiPersist"),
        ("TIMETRA-SYSTEM-MIB", "sbiConsoleSpeed"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoNegotiate"),
        ("TIMETRA-SYSTEM-MIB", "sbiSpeed"),
        ("TIMETRA-SYSTEM-MIB", "sbiDuplex"),
        ("TIMETRA-SYSTEM-MIB", "sbiPrimaryDns"),
        ("TIMETRA-SYSTEM-MIB", "sbiSecondaryDns"),
        ("TIMETRA-SYSTEM-MIB", "sbiTertiaryDns"),
        ("TIMETRA-SYSTEM-MIB", "sbiDnsDomain"),
        ("TIMETRA-SYSTEM-MIB", "sbiWait"),
        ("TIMETRA-SYSTEM-MIB", "sbiStaticRouteNextHop"),
        ("TIMETRA-SYSTEM-MIB", "sbiStaticRouteRowStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiLiSeparate"),
        ("TIMETRA-SYSTEM-MIB", "sbiLiLocalSave"))
)
if mibBuilder.loadTexts:
    tmnxSysBofV6v0Group.setStatus("current")

tmnxSysLiV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 33)
)
tmnxSysLiV6v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sliConfigStatus"),
        ("TIMETRA-SYSTEM-MIB", "sliSaveConfig"),
        ("TIMETRA-SYSTEM-MIB", "sliSaveConfigResult"),
        ("TIMETRA-SYSTEM-MIB", "sliConfigLastModified"),
        ("TIMETRA-SYSTEM-MIB", "sliConfigLastSaved"))
)
if mibBuilder.loadTexts:
    tmnxSysLiV6v0Group.setStatus("current")

tmnxSysNotifyObjsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 34)
)
tmnxSysNotifyObjsV6v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxNotifyObjectName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSyncFailureReason"))
)
if mibBuilder.loadTexts:
    tmnxSysNotifyObjsV6v0Group.setStatus("current")

tmnxSysGeneralV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 35)
)
tmnxSysGeneralV7v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sgiSnmpInGetBulks"),
        ("TIMETRA-SYSTEM-MIB", "sgiKbMemoryUsed"),
        ("TIMETRA-SYSTEM-MIB", "sgiKbMemoryAvailable"),
        ("TIMETRA-SYSTEM-MIB", "sgiKbMemoryPoolAllocated"))
)
if mibBuilder.loadTexts:
    tmnxSysGeneralV7v0Group.setStatus("current")

tmnxSysIcmpVSV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 36)
)
tmnxSysIcmpVSV6v1Group.setObjects(
    ("TIMETRA-SYSTEM-MIB", "sysIcmpVSEnhancement")
)
if mibBuilder.loadTexts:
    tmnxSysIcmpVSV6v1Group.setStatus("current")

tmnxSysConfigV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 37)
)
tmnxSysConfigV8v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "ssiSaveConfig"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncMode"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncForce"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncStatus"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncConfigLastTime"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncBootEnvLastTime"),
        ("TIMETRA-SYSTEM-MIB", "ssiConfigMaxBackupRevisions"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveConfigResult"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveBof"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveBofResult"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveConfigDest"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveConfigDetail"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedFailoverTime"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedFailoverReason"),
        ("TIMETRA-SYSTEM-MIB", "sbiConfigStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiPersistStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiPersistIndex"),
        ("TIMETRA-SYSTEM-MIB", "sbiSnmpdAdminStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiSnmpdOperStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiSnmpdMaxPktSize"),
        ("TIMETRA-SYSTEM-MIB", "sbiSnmpdPortNum"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootConfigOKScript"),
        ("TIMETRA-SYSTEM-MIB", "sbiConfigOKScriptStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootConfigFailScript"),
        ("TIMETRA-SYSTEM-MIB", "sbiConfigFailScriptStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiRedSwitchoverScript"),
        ("TIMETRA-SYSTEM-MIB", "sbiRedSwitchoverScriptStatus"),
        ("TIMETRA-SYSTEM-MIB", "sysLACPSystemPriority"))
)
if mibBuilder.loadTexts:
    tmnxSysConfigV8v0Group.setStatus("current")

tmnxSysLoginControlV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 38)
)
tmnxSysLoginControlV8v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "slcFtpInboundMaxSessions"),
        ("TIMETRA-SYSTEM-MIB", "slcTelnetInboundMaxSessions"),
        ("TIMETRA-SYSTEM-MIB", "slcTelnetOutboundMaxSessions"),
        ("TIMETRA-SYSTEM-MIB", "slcPreLoginMessage"),
        ("TIMETRA-SYSTEM-MIB", "slcPreLoginMessageInclName"),
        ("TIMETRA-SYSTEM-MIB", "slcMessageOfTheDay"),
        ("TIMETRA-SYSTEM-MIB", "slcMessageOfTheDayType"),
        ("TIMETRA-SYSTEM-MIB", "slcLoginBanner"),
        ("TIMETRA-SYSTEM-MIB", "slcLoginExponentialBackOff"),
        ("TIMETRA-SYSTEM-MIB", "slcTelnetGracefulShutdown"),
        ("TIMETRA-SYSTEM-MIB", "slcSSHGracefulShutdown"))
)
if mibBuilder.loadTexts:
    tmnxSysLoginControlV8v0Group.setStatus("current")

tmnxSysEthInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 39)
)
tmnxSysEthInfoGroup.setObjects(
    ("TIMETRA-SYSTEM-MIB", "sysNewQinqUntaggedSap")
)
if mibBuilder.loadTexts:
    tmnxSysEthInfoGroup.setStatus("current")

tmnxPersistenceV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 40)
)
tmnxPersistenceV9v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "spiSubMgmtPersistenceFileLocation"),
        ("TIMETRA-SYSTEM-MIB", "spiSubMgmtPersistenceDescription"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpSrvPersistenceFileLoc"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpSrvPersistenceDescr"),
        ("TIMETRA-SYSTEM-MIB", "spiNatFwdPersistenceFileLoc"),
        ("TIMETRA-SYSTEM-MIB", "spiNatFwdPersistenceDescr"),
        ("TIMETRA-SYSTEM-MIB", "spiAAPersistenceFileLoc"),
        ("TIMETRA-SYSTEM-MIB", "spiAAPersistenceDescr"))
)
if mibBuilder.loadTexts:
    tmnxPersistenceV9v0Group.setStatus("obsolete")

tmnxSysLoginControlSecGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 41)
)
tmnxSysLoginControlSecGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "slcTelnetMinTTLValue"),
        ("TIMETRA-SYSTEM-MIB", "slcSSHMinTTLValue"))
)
if mibBuilder.loadTexts:
    tmnxSysLoginControlSecGroup.setStatus("current")

tmnxSysLiFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 42)
)
tmnxSysLiFilterGroup.setObjects(
    ("TIMETRA-SYSTEM-MIB", "sliFilterLock")
)
if mibBuilder.loadTexts:
    tmnxSysLiFilterGroup.setStatus("current")

tmnxSysRollbackV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 44)
)
tmnxSysRollbackV9v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackIndex"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackStart"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackResult"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackSave"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackSaveResult"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackLocation"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRevertIndex"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRevertEndTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackTableLastChanged"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileCreationTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileComment"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileUserName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackSavedTime"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncRollbackLastTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRevertStartTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRevertUserName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRevertFilename"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackSaveComment"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackAbortRevert"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileVersion"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileDelete"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileDeleteResult"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncRollbackMode"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncRollbackForce"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncRollbackStatus"))
)
if mibBuilder.loadTexts:
    tmnxSysRollbackV9v0Group.setStatus("current")

tmnxSysLoginControlV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 45)
)
tmnxSysLoginControlV9v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "slcSSHInboundMaxSessions"),
        ("TIMETRA-SYSTEM-MIB", "slcSSHOutboundMaxSessions"))
)
if mibBuilder.loadTexts:
    tmnxSysLoginControlV9v0Group.setStatus("current")

tmnxSystemCpuMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 46)
)
tmnxSystemCpuMonitorGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysCpuMonCpuIdle"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCpuMonBusyCoreUtil"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCpuMonBusyGroupName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCpuMonBusyGroupUtil"))
)
if mibBuilder.loadTexts:
    tmnxSystemCpuMonitorGroup.setStatus("current")

tmnxSysCertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 47)
)
tmnxSysCertGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "ssiSyncCertForce"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncCertLastTime"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncCertMode"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncCertStatus"))
)
if mibBuilder.loadTexts:
    tmnxSysCertGroup.setStatus("current")

tmnxSysBootedBofGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 48)
)
tmnxSysBootedBofGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sbbiLiSeparate"),
        ("TIMETRA-SYSTEM-MIB", "sbbiLiLocalSave"))
)
if mibBuilder.loadTexts:
    tmnxSysBootedBofGroup.setStatus("current")

tmnxSysRollbackRescueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 49)
)
tmnxSysRollbackRescueGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueLocation"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueSave"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueRevert"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueDelete"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueSaveRes"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueRevertRes"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueDeleteRes"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueSavedTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueRevStTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueRevEdTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueRevUser"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueSaveComment"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueAbortRevert"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueFileExists"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackMaxLocalFiles"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackMaxRemoteFiles"))
)
if mibBuilder.loadTexts:
    tmnxSysRollbackRescueGroup.setStatus("current")

tmnxSysNotifyObjsV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 51)
)
tmnxSysNotifyObjsV10v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysExecScript"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysExecResult"))
)
if mibBuilder.loadTexts:
    tmnxSysNotifyObjsV10v0Group.setStatus("current")

tmnxSysNotifyObjsGenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 53)
)
tmnxSysNotifyObjsGenGroup.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysFileErrorType")
)
if mibBuilder.loadTexts:
    tmnxSysNotifyObjsGenGroup.setStatus("current")

tmnxSysGroupingSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 54)
)
tmnxSysGroupingSystemGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sgiSystemGroupID"),
        ("TIMETRA-SYSTEM-MIB", "sgiSystemSubGroupID"))
)
if mibBuilder.loadTexts:
    tmnxSysGroupingSystemGroup.setStatus("current")

tmnxSysCandidateCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 55)
)
tmnxSysCandidateCfgGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysCandidateCfgState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCandidateCfgEditors"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCandidateCfgCommitState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCandidateCfgCommitTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCandidateCfgRevertTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCandidateCfgChckptCreated"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCandidateCfgExclusiveUsr"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCandidateCfgUser"))
)
if mibBuilder.loadTexts:
    tmnxSysCandidateCfgGroup.setStatus("current")

tmnxPersistenceV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 56)
)
tmnxPersistenceV11v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "spiSubMgmtPersistenceFileLocation"),
        ("TIMETRA-SYSTEM-MIB", "spiSubMgmtPersistenceDescription"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpSrvPersistenceFileLoc"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpSrvPersistenceDescr"),
        ("TIMETRA-SYSTEM-MIB", "spiNatFwdPersistenceFileLoc"),
        ("TIMETRA-SYSTEM-MIB", "spiNatFwdPersistenceDescr"),
        ("TIMETRA-SYSTEM-MIB", "spiAAPersistenceFileLoc"),
        ("TIMETRA-SYSTEM-MIB", "spiAAPersistenceDescr"),
        ("TIMETRA-SYSTEM-MIB", "spiAncpPersistenceFileLoc"),
        ("TIMETRA-SYSTEM-MIB", "spiAncpPersistenceDescr"))
)
if mibBuilder.loadTexts:
    tmnxPersistenceV11v0Group.setStatus("obsolete")

tmnxSysNetconfV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 57)
)
tmnxSysNetconfV11v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfAdminStatus"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfOperStatus"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfRequests"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfGetRequests"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfGetConfigRequests"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfEditConfigRequests"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfCloseRequests"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfKillRequests"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfResponses"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfErrorResponses"))
)
if mibBuilder.loadTexts:
    tmnxSysNetconfV11v0Group.setStatus("current")

tmnxSysStrmV11v0R4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 58)
)
tmnxSysStrmV11v0R4Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysStrmAdminStatus"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysStrmDumpSnmpRequests"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysStrmGetManyRequests"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysStrmResponses"))
)
if mibBuilder.loadTexts:
    tmnxSysStrmV11v0R4Group.setStatus("current")

tmnxSysNotifyObjsV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 59)
)
tmnxSysNotifyObjsV11v0Group.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxTrapDroppedCount")
)
if mibBuilder.loadTexts:
    tmnxSysNotifyObjsV11v0Group.setStatus("current")

tmnxPersistenceV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 60, 1)
)
tmnxPersistenceV12v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "spiSubMgmtPersistenceFileLocation"),
        ("TIMETRA-SYSTEM-MIB", "spiSubMgmtPersistenceDescription"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpSrvPersistenceFileLoc"),
        ("TIMETRA-SYSTEM-MIB", "spiDhcpSrvPersistenceDescr"),
        ("TIMETRA-SYSTEM-MIB", "spiNatFwdPersistenceFileLoc"),
        ("TIMETRA-SYSTEM-MIB", "spiNatFwdPersistenceDescr"),
        ("TIMETRA-SYSTEM-MIB", "spiAAPersistenceFileLoc"),
        ("TIMETRA-SYSTEM-MIB", "spiAAPersistenceDescr"),
        ("TIMETRA-SYSTEM-MIB", "spiAncpPersistenceFileLoc"),
        ("TIMETRA-SYSTEM-MIB", "spiAncpPersistenceDescr"),
        ("TIMETRA-SYSTEM-MIB", "spiPythonPersistenceFileLoc"),
        ("TIMETRA-SYSTEM-MIB", "spiPythonPersistenceDescr"))
)
if mibBuilder.loadTexts:
    tmnxPersistenceV12v0Group.setStatus("current")

tmnxSysDNSSecV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 60, 2)
)
tmnxSysDNSSecV12v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sysDNSSecAdValidation"),
        ("TIMETRA-SYSTEM-MIB", "sysDNSSecRespCtrl"))
)
if mibBuilder.loadTexts:
    tmnxSysDNSSecV12v0Group.setStatus("current")

tmnxSysXmppV12v4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 60, 5)
)
tmnxSysXmppV12v4Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysVsdSystemId"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysVsdGwPubSubIsSubscrd"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysVsdGwPubSubNodeName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysVsdGwPubSubLstSubscrdTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysVsdGwLastAuditTxTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServFQDN"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServRowStatus"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServUserName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServPassword"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServLastChanged"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServUptime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServIQSent"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServIQRcvd"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServIQError"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServIQTimedOut"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServIQAckRcvd"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServIQMinRtt"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServIQMaxRtt"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServVsdUpdatesRcvd"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServUpdatesRcvd"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServMsgSent"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServMsgRcvd"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServMsgAckRcvd"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServMsgError"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServMsgTimedOut"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServMsgMinRtt"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServMsgMaxRtt"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServSubSent"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServUnSubSent"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysVsdServUptime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysVsdServUserName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysVsdServerStatus"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysVsdServMsgSent"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysVsdServMsgRcvd"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysVsdServMsgAckRcvd"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysVsdServMsgError"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysVsdServMsgTimedOut"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysVsdServMsgMinRtt"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysVsdServMsgMaxRtt"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServOperUserName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServAuthType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServConnMode"))
)
if mibBuilder.loadTexts:
    tmnxSysXmppV12v4Group.setStatus("current")

tmnxSysCardResourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 60, 6)
)
tmnxSysCardResourceGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxCardCpuResMonCpuIdle"),
        ("TIMETRA-SYSTEM-MIB", "tmnxCardCpuResMonBusyCoreUtil"),
        ("TIMETRA-SYSTEM-MIB", "tmnxCardCpuResMonBusyGroupName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxCardCpuResMonBusyGroupUtil"),
        ("TIMETRA-SYSTEM-MIB", "tmnxCardMemResMemoryUsed"),
        ("TIMETRA-SYSTEM-MIB", "tmnxCardMemResMemoryAvailable"),
        ("TIMETRA-SYSTEM-MIB", "tmnxCardMemResPoolsAllocated"))
)
if mibBuilder.loadTexts:
    tmnxSysCardResourceGroup.setStatus("current")

tmnxSysNotifyObjsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 60, 7)
)
tmnxSysNotifyObjsV12v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysDNSSecDomainName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotifVsdServerName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotifXmppServerName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseErrorReason"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseTimeLeft"))
)
if mibBuilder.loadTexts:
    tmnxSysNotifyObjsV12v0Group.setStatus("current")

tmnxSysBofV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 60, 8)
)
tmnxSysBofV12v0Group.setObjects(
    ("TIMETRA-SYSTEM-MIB", "sbiLicenseFile")
)
if mibBuilder.loadTexts:
    tmnxSysBofV12v0Group.setStatus("current")

tmnxSysLicenseV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 60, 9)
)
tmnxSysLicenseV12v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseStatus"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseUuid"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseDescription"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseProduct"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseSwVersion"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseIssueDateAndTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseStartDateAndTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseEndDateAndTime"))
)
if mibBuilder.loadTexts:
    tmnxSysLicenseV12v0Group.setStatus("current")

tmnxSysDhcpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 61)
)
tmnxSysDhcpGroup.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysDhcp6AdvNoaddrsGlobal")
)
if mibBuilder.loadTexts:
    tmnxSysDhcpGroup.setStatus("current")

tmnxSysFibV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 62)
)
tmnxSysFibV13v0Group.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysFibSelective")
)
if mibBuilder.loadTexts:
    tmnxSysFibV13v0Group.setStatus("current")

tmnxSysNetconfV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 63)
)
tmnxSysNetconfV13v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfCopyConfigRequests"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfDelConfigRequests"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfValidateRequests"))
)
if mibBuilder.loadTexts:
    tmnxSysNetconfV13v0Group.setStatus("current")

tmnxSysSnmpSrcAccesLstV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 64)
)
tmnxSysSnmpSrcAccesLstV13v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysSnmpSrcAccessTblLstChgd"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysSnmpSrcAccessLstRowStatus"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysSnmpSrcAccessLstLastChg"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysSnmpCommunityPktDropped"))
)
if mibBuilder.loadTexts:
    tmnxSysSnmpSrcAccesLstV13v0Group.setStatus("current")

tmnxSysMgmtProtocolV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 65)
)
tmnxSysMgmtProtocolV13v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtProtocolTblLstChng"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtProtLastChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtAllowImmediateChange"))
)
if mibBuilder.loadTexts:
    tmnxSysMgmtProtocolV13v0Group.setStatus("current")

tmnxSysFileTransProfV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 66)
)
tmnxSysFileTransProfV13v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysFileTransProfTableLstChgd"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFileTransProfRowStatus"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFileTransProfLastChanged"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFileTransProfRtrId"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFileTransProfSvcId"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFileTransProfSrcAddrV4T"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFileTransProfSrcAddrV4"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFileTransProfSrcAddrV6T"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFileTransProfSrcAddrV6"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFileTransProfTimeout"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFileTransProfRetry"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFileTransProfRedirection"))
)
if mibBuilder.loadTexts:
    tmnxSysFileTransProfV13v0Group.setStatus("current")

tmnxSysEhsV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 67)
)
tmnxSysEhsV13v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSmLaunchExtAuthType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSmRunExtAuthType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSmRunExtUserName"))
)
if mibBuilder.loadTexts:
    tmnxSysEhsV13v0Group.setStatus("current")

tmnxSysLicenseV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 68)
)
tmnxSysLicenseV13v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseVChassisType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseMaxNumCPMs"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseMaxNumIOMs"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCpmCardLicStatus"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCpmCardLicName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCpmCardLicUuid"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCpmCardLicDescription"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCpmCardLicProduct"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCpmCardLicSwVersion"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCpmCardLicIssueDateTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCpmCardLicStartDateTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCpmCardLicEndDateTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCpmCardLicVChassisType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCpmCardLicMaxNumCPMs"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCpmCardLicMaxNumIOMs"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCpmCardLicFeatDescription"))
)
if mibBuilder.loadTexts:
    tmnxSysLicenseV13v0Group.setStatus("current")

tmnxSysSwReposV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 70)
)
tmnxSysSwReposV13v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysSwReposTableLastChanged"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysSwReposRowStatus"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysSwReposLastChanged"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysSwReposDescription"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysSwReposPrimaryLocation"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysSwReposSecondaryLocation"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysSwReposTertiaryLocation"))
)
if mibBuilder.loadTexts:
    tmnxSysSwReposV13v0Group.setStatus("current")

tmnxSysBofV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 71)
)
tmnxSysBofV13v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sbiFips1402Level1"),
        ("TIMETRA-SYSTEM-MIB", "sbiEssSystemType"))
)
if mibBuilder.loadTexts:
    tmnxSysBofV13v0Group.setStatus("current")

tmnxSysBofV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 72, 1)
)
tmnxSysBofV14v0Group.setObjects(
    ("TIMETRA-SYSTEM-MIB", "sbiSystemBaseMacAddress")
)
if mibBuilder.loadTexts:
    tmnxSysBofV14v0Group.setStatus("current")

tmnxPersistenceV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 72, 3)
)
tmnxPersistenceV14v0Group.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxDhcpLeaseTimeModeThreshold")
)
if mibBuilder.loadTexts:
    tmnxPersistenceV14v0Group.setStatus("current")

tmnxSysNetconfV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 72, 4)
)
tmnxSysNetconfV14v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfFailedEditCfgReqs"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfFailedLockReqs"),
        ("TIMETRA-SYSTEM-MIB", "sgiSnmpFailedSets"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfLockRequests"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfUnlockRequests"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfCommitRequests"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfDiscardRequests"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfCapCandidateCfg"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfCapRunningCfg"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfYangBaseR13"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfYangNokia"))
)
if mibBuilder.loadTexts:
    tmnxSysNetconfV14v0Group.setStatus("obsolete")

tmnxSysEhsParameterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 72, 5)
)
tmnxSysEhsParameterGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSmRunEventArgName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSmRunEventArgValue"))
)
if mibBuilder.loadTexts:
    tmnxSysEhsParameterGroup.setStatus("current")

tmnxSysLicenseApplicationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 72, 6)
)
tmnxSysLicenseApplicationGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysAppStats24HrsName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAppStats24HrsValue"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAppStats24HrsTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAppStatsWeekName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAppStatsWeekAverage"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAppStatsWeekPeak"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAppStatsWeekTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAppStatsPeakName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAppStatsPeakValue"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAppStatsPeakTime"))
)
if mibBuilder.loadTexts:
    tmnxSysLicenseApplicationGroup.setStatus("current")

tmnxSysNotifyObjsV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 72, 7)
)
tmnxSysNotifyObjsV14v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseErrorAction"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotifAppStatsTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotifAppStatsApplication"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotifAppStatsType"))
)
if mibBuilder.loadTexts:
    tmnxSysNotifyObjsV14v0Group.setStatus("current")

tmnxSysTimeV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 72, 8)
)
tmnxSysTimeV14v0Group.setObjects(
    ("TIMETRA-SYSTEM-MIB", "stiPreferLocalTime")
)
if mibBuilder.loadTexts:
    tmnxSysTimeV14v0Group.setStatus("current")

tmnxSysLoginControlV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 73)
)
tmnxSysLoginControlV15v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "slcIdleTimeout"),
        ("TIMETRA-SYSTEM-MIB", "slcLoginScriptGlobal"),
        ("TIMETRA-SYSTEM-MIB", "slcLoginScriptPerUserDirectory"),
        ("TIMETRA-SYSTEM-MIB", "slcLoginScriptPerUserFilename"))
)
if mibBuilder.loadTexts:
    tmnxSysLoginControlV15v0Group.setStatus("current")

tmnxSysGrpcV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 74)
)
tmnxSysGrpcV15v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcOperState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcTlsServerProfile"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcMaxMsgSize"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcGnmiVersion"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcAllowUnsecure"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcGnmiAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcTcpKaAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcTcpKaIdle"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcTcpKaInterval"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcTcpKaCount"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcRibApiAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcRibApiPurgeTimeout"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcRibApiVersion"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcGnoiCertMgmtAdmnState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcGnoiCertMgmtVersion"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcMdCliAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcMdCliVersion"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcGnoiFileAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcGnoiFileVersion"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcGnoiSystemAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcGnoiSystemVersion"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcConnStartTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcConnActRpcCnt"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcConnTotRpcCnt"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcConnRxBytes"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcConnTxBytes"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcConnQos"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcConnSrcVRtrId"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcConnGrpcTunnel"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcRpcName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcRpcServiceName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcRpcStartTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcRpcSrcIpAddType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcRpcSrcIpAddress"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcRpcSrcPort"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcRpcUserName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcRpcSessionId"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcRpcGrpcTunnel"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcPendRebOperState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcPendRebDelay"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcPendRebMsg"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcPendRebCount"))
)
if mibBuilder.loadTexts:
    tmnxSysGrpcV15v0Group.setStatus("current")

tmnxSysXmppMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 75)
)
tmnxSysXmppMgmtGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServServiceId"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServRouterId"))
)
if mibBuilder.loadTexts:
    tmnxSysXmppMgmtGroup.setStatus("current")

tmnxSysLicenseApp48HrsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 76, 3)
)
tmnxSysLicenseApp48HrsGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysAppStats48HrsName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAppStats48HrsValue"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAppStats48HrsTime"))
)
if mibBuilder.loadTexts:
    tmnxSysLicenseApp48HrsGroup.setStatus("current")

tmnxSysNetconfV15v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 77, 1)
)
tmnxSysNetconfV15v1Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfFailedEditCfgReqs"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfFailedLockReqs"),
        ("TIMETRA-SYSTEM-MIB", "sgiSnmpFailedSets"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfLockRequests"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfUnlockRequests"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfCommitRequests"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfDiscardRequests"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfCapCandidateCfg"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfCapRunningCfg"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfCreateSubRequests"))
)
if mibBuilder.loadTexts:
    tmnxSysNetconfV15v1Group.setStatus("current")

tmnxSysMgmtProtocolV15v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 77, 2)
)
tmnxSysMgmtProtocolV15v1Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtCliEngine1"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtCliEngine2"))
)
if mibBuilder.loadTexts:
    tmnxSysMgmtProtocolV15v1Group.setStatus("current")

tmnxSysConfigSaveCtrlV15v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 77, 3)
)
tmnxSysConfigSaveCtrlV15v1Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfMDCliAutoCfgSave"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfAutoCfgSave"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcAutoCfgSave"))
)
if mibBuilder.loadTexts:
    tmnxSysConfigSaveCtrlV15v1Group.setStatus("current")

tmnxSysMgmtIfMdCliGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 77, 4)
)
tmnxSysMgmtIfMdCliGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfMDEnvComplEnter"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfMDEnvComplSpace"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfMDEnvComplTab"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfMDEnvConsLength"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfMDEnvConsWidth"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfMDEnvMore"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfMDEnvPromptCtx"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfMDEnvPromptNewline"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfMDEnvPromptTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfMDEnvPromptIndic"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfMDEnvTimeDisplay"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfMDEnvMsgCliSvrt"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfMDEnvProIndAdminSt"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfMDEnvProIndType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfMDEnvProIndDelay"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfWriteMode"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfWriteOperMode"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfModeLastSwitchTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfModeSwitchDuration"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfMDEnvTimeFormat"))
)
if mibBuilder.loadTexts:
    tmnxSysMgmtIfMdCliGroup.setStatus("current")

tmnxSysMgmtIfYangModulesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 77, 5)
)
tmnxSysMgmtIfYangModulesGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfYangBaseR13"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfYangNokia"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfYangOpenConfig"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfYangNokiaCombined"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfYangNmdaSupport"))
)
if mibBuilder.loadTexts:
    tmnxSysMgmtIfYangModulesGroup.setStatus("current")

tmnxSysNetconfV15v1ObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 77, 6)
)
tmnxSysNetconfV15v1ObsoleteGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfYangBaseR13"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfYangNokia"))
)
if mibBuilder.loadTexts:
    tmnxSysNetconfV15v1ObsoleteGroup.setStatus("current")

tmnxSysFileTransProfV15v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 77, 7)
)
tmnxSysFileTransProfV15v1Group.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysFileTransProfSvcName")
)
if mibBuilder.loadTexts:
    tmnxSysFileTransProfV15v1Group.setStatus("current")

tmnxSysBofV15v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 77, 8)
)
tmnxSysBofV15v1Group.setObjects(
    ("TIMETRA-SYSTEM-MIB", "sbiSystemProfile")
)
if mibBuilder.loadTexts:
    tmnxSysBofV15v1Group.setStatus("current")

tmnxSysHttpRdrV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 78, 1)
)
tmnxSysHttpRdrV16v0Group.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysHttpRdrCpmOptimizedMode")
)
if mibBuilder.loadTexts:
    tmnxSysHttpRdrV16v0Group.setStatus("current")

tmnxSysMgmtIfDsLocksV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 78, 3)
)
tmnxSysMgmtIfDsLocksV16v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfDsLocksSessionId"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfDsLocksRmtIpAddress"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfDsLocksConsole"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfDsLocksUserName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfDsLocksSessionMode"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfDsLocksSessionType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfDsLocksRegion"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfDsLocksRunLock"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfDsLocksCndLock"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfDsLocksIdleTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfDsLocksScratchCnt"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfDsLocksCronEhs"))
)
if mibBuilder.loadTexts:
    tmnxSysMgmtIfDsLocksV16v0Group.setStatus("current")

tmnxSysLicensingV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 78, 4)
)
tmnxSysLicensingV16v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysAppLicenseDescription"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAppLicenseType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAppLicensePoolSize"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAppLicenseAllocated"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAppLicensePresent"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAppLicenseState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAvailLicenseName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAvailLicenseUuid"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAvailLicenseDescription"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAvailLicenseSwVersion"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAvailLicIssueDateTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAvailLicStartDateTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAvailLicEndDateTime"),
        ("TIMETRA-SYSTEM-MIB", "sbiAllowBootLicenseViolations"))
)
if mibBuilder.loadTexts:
    tmnxSysLicensingV16v0Group.setStatus("current")

tmnxSysMgmtInterfaceV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 78, 5)
)
tmnxSysMgmtInterfaceV16v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfSchemaPath"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfWriteSwitchReason"))
)
if mibBuilder.loadTexts:
    tmnxSysMgmtInterfaceV16v0Group.setStatus("current")

tmnxSysMgmtIfNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 78, 6)
)
tmnxSysMgmtIfNotifyObjsGroup.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxNotifySysMgmtIfOriginalMode")
)
if mibBuilder.loadTexts:
    tmnxSysMgmtIfNotifyObjsGroup.setStatus("current")

tmnxSysNetworkElementV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 78, 7)
)
tmnxSysNetworkElementV16v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfTableLstChgd"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfRowStatus"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfLastChanged"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfNeid"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfNeipV4Type"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfNeipV4"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfNeipV6Type"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfNeipV6"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfSystemMac"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfPlatformType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfVendorId"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNEDiscoveryGenerateTraps"))
)
if mibBuilder.loadTexts:
    tmnxSysNetworkElementV16v0Group.setStatus("current")

tmnxSysSwitchFabricV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 78, 8)
)
tmnxSysSwitchFabricV16v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysSwFabFailRecAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysSwFabFailRecOperState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysSwFabFailRecSfmState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysSwFabFailRecSfmStateTime"))
)
if mibBuilder.loadTexts:
    tmnxSysSwitchFabricV16v0Group.setStatus("current")

tmnxSysLicNotifyObjsV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 79, 1)
)
tmnxSysLicNotifyObjsV19v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysLicensingNotifyGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicensedNotifyAppName"))
)
if mibBuilder.loadTexts:
    tmnxSysLicNotifyObjsV19v0Group.setStatus("current")

tmnxSysResInfoV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 79, 3)
)
tmnxSysResInfoV19v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysResEcmpProfRowStatus"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysResEcmpProfType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysResEcmpProfLinksPerGrp"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysResEcmpProfNumGrps"))
)
if mibBuilder.loadTexts:
    tmnxSysResInfoV19v0Group.setStatus("current")

tmnxSysBofV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 79, 4)
)
tmnxSysBofV19v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sbiAutoBoot"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoBootClientId"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoBootClientIdType"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoBootUsingMgmt"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoBootUsingInband"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoBootInbandVlan"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoBootUsingIpv4"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoBootUsingIpv6"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoBootIncludeUserClass"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoIpv4Dhcp"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoIpv4DhcpClientIdType"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoIpv4DhcpClientId"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoIpv4DhcpOptUserClass"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoIpv4DhcpTimeout"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoIpv6Dhcp"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoIpv6DhcpClientIdType"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoIpv6DhcpClientIdDuidType"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoIpv6DhcpClientIdDuid"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoIpv6DhcpOptUserClass"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoIpv6DhcpTimeout"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyAIpAddr"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyAIpMask"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyAIPv6Addr"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyAIPv6PfxLen"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyBIpAddr"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyBIpMask"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyBIPv6Addr"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyBIPv6PfxLen"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyCIpAddr"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyCIpMask"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyCIPv6Addr"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyCIPv6PfxLen"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyDIpAddr"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyDIpMask"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyDIPv6Addr"),
        ("TIMETRA-SYSTEM-MIB", "sbiStandbyDIPv6PfxLen"),
        ("TIMETRA-SYSTEM-MIB", "sbiMgmtIfIpMtu"))
)
if mibBuilder.loadTexts:
    tmnxSysBofV19v0Group.setStatus("current")

tmnxSysNetworkElementV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 79, 5)
)
tmnxSysNetworkElementV19v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfTableLstChgd"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfRowStatus"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfLastChanged"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfNeid"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfNeipV4Type"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfNeipV4"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfNeipV6Type"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfNeipV6"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfSystemMac"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfPlatformType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfVendorId"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNEDiscoveryGenerateTraps"))
)
if mibBuilder.loadTexts:
    tmnxSysNetworkElementV19v0Group.setStatus("current")

tmnxSysLicensingV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 79, 6)
)
tmnxSysLicensingV19v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysAvailLicenseProduct"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicensingState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicensingRebootPending"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicensingProduct"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicensingUuid"))
)
if mibBuilder.loadTexts:
    tmnxSysLicensingV19v0Group.setStatus("current")

tmnxSysNetconfV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 79, 7)
)
tmnxSysNetconfV19v0Group.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfPort")
)
if mibBuilder.loadTexts:
    tmnxSysNetconfV19v0Group.setStatus("current")

tmnxSysEhsV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 79, 8)
)
tmnxSysEhsV19v0Group.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSmLaunchExtLockOverride")
)
if mibBuilder.loadTexts:
    tmnxSysEhsV19v0Group.setStatus("current")

tmnxSysBootConfFmtNotifyObjsGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 79, 9)
)
tmnxSysBootConfFmtNotifyObjsGrp.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxPrimaryConfigFileFormatType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxLiConfigFileFormatType"))
)
if mibBuilder.loadTexts:
    tmnxSysBootConfFmtNotifyObjsGrp.setStatus("current")

tmnxSysFwdPathOptsV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 79, 11)
)
tmnxSysFwdPathOptsV19v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysFpoDscpTransAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoDscpTransOperState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoEntropyLabelAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoEntropyLabelOperState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoVplsEvpnMplsAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoVplsEvpnMplsOperState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoQosFc4ProfAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoQosFc4ProfOperState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoQosMacCritAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoQosMacCritOperState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoQosIpv6CritAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoQosIpv6CritOperState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoQosBumPolAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoQosBumPolOperState"))
)
if mibBuilder.loadTexts:
    tmnxSysFwdPathOptsV19v0Group.setStatus("current")

tmnxSysMgmtIfMdCliCmdAccntGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 79, 12)
)
tmnxSysMgmtIfMdCliCmdAccntGroup.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfMDCliCmdAccntLoad")
)
if mibBuilder.loadTexts:
    tmnxSysMgmtIfMdCliCmdAccntGroup.setStatus("obsolete")

tmnxSysResItCamV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 79, 13)
)
tmnxSysResItCamV19v0Group.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysResItCamBankV6Multicast")
)
if mibBuilder.loadTexts:
    tmnxSysResItCamV19v0Group.setStatus("current")

tmnxSysFpCamAllocV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 79, 14)
)
tmnxSysFpCamAllocV19v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysFpCamAllocAdmnV6Multicast"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpCamAllocOperV6Multicast"))
)
if mibBuilder.loadTexts:
    tmnxSysFpCamAllocV19v0Group.setStatus("current")

tmnxSysFwdPathOptsV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 80, 2)
)
tmnxSysFwdPathOptsV20v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysFpoMplsFastSwOvAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoMplsFastSwOvOperState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoRouterEcmpAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoRouterEcmpOperState"))
)
if mibBuilder.loadTexts:
    tmnxSysFwdPathOptsV20v0Group.setStatus("current")

tmnxSysAutoBootV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 80, 3)
)
tmnxSysAutoBootV20v0Group.setObjects(
    ("TIMETRA-SYSTEM-MIB", "sbiAutoBootVlanDiscovery")
)
if mibBuilder.loadTexts:
    tmnxSysAutoBootV20v0Group.setStatus("current")

tmnxSysSwitchFabricV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 80, 4)
)
tmnxSysSwitchFabricV20v0Group.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysSwFabSfmLossThresh")
)
if mibBuilder.loadTexts:
    tmnxSysSwitchFabricV20v0Group.setStatus("current")

tmnxSysUsbV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 80, 5)
)
tmnxSysUsbV20v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysUsbLastChgd"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysUsbAdminState"))
)
if mibBuilder.loadTexts:
    tmnxSysUsbV20v0Group.setStatus("current")

tmnxSysGeneralV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 80, 7)
)
tmnxSysGeneralV20v0Group.setObjects(
    ("TIMETRA-SYSTEM-MIB", "sgiCryptoModVersion")
)
if mibBuilder.loadTexts:
    tmnxSysGeneralV20v0Group.setStatus("current")

tmnxSysMgmtInterfaceV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 80, 9)
)
tmnxSysMgmtInterfaceV20v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfPriSchemaPathState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfPriSchemaPathValue"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfSecSchemaPathState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfSecSchemaPathValue"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfTerSchemaPathState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfTerSchemaPathValue"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfOperSchemaPathState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfOperSchemaPathValue"))
)
if mibBuilder.loadTexts:
    tmnxSysMgmtInterfaceV20v0Group.setStatus("current")

tmnxSysFpResAllocV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 80, 10)
)
tmnxSysFpResAllocV20v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysFpResAllocG8032Sap"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpResAllocOperG8032Sap"))
)
if mibBuilder.loadTexts:
    tmnxSysFpResAllocV20v0Group.setStatus("deprecated")

tmnxSysAutoNEDV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 80, 11)
)
tmnxSysAutoNEDV20v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfNeipV4AutoGenerate"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfNeipV4NeidVendorId"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfNeipV6AutoGenerate"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNEProfNeipV6NeidVendorId"))
)
if mibBuilder.loadTexts:
    tmnxSysAutoNEDV20v0Group.setStatus("current")

tmnxSysAutoBootOspfV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 80, 12)
)
tmnxSysAutoBootOspfV20v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sbiAutoBootPortMtu"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoBootMode"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoBootOspfNeid"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoBootOspfVendorId"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoBootOspfNeipV4Type"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoBootOspfNeipV4"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoBootOspfNeipV6Type"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoBootOspfNeipV6"),
        ("TIMETRA-SYSTEM-MIB", "sbiAutoBootOspfMtu"))
)
if mibBuilder.loadTexts:
    tmnxSysAutoBootOspfV20v0Group.setStatus("current")

tmnxSysRemoteMgmtV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 80, 13)
)
tmnxSysRemoteMgmtV20v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtOperState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtAllowUnsecure"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtDeviceLabel"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtDeviceName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtHelloInterval"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtLastHelloTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtLastRegStatus"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtLastRegTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtOperDownReason"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtRegsCancelled"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtRegsFailed"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtRegsSent"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtSrcIpAddType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtSrcIpAddress"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtSrcPort"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtSrcDefaultPort"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtTimeout"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtTlsClientProf"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtVRtrId"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrAllowUnsecure"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrDescription"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrDeviceLabel"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrDeviceName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrFQDN"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrIpAddType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrPort"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrIpAddress"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrLastRegStatus"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrLastRegTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrOperDownReason"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrOperState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrRegsCancelled"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrRegsFailed"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrRegsSent"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrRowStatus"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrSrcIpAddType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrSrcIpAddress"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrSrcPort"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrSrcDefaultPort"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrTimeout"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrTlsClientProf"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrVRtrId"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrOperDevLabel"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrOperDevName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrOperSrcIpAdType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrOperSrcIpAddr"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrOperSrcPort"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrOperTimeout"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrOperTlsProf"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrOperVRtrId"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtMgrOperTranspType"))
)
if mibBuilder.loadTexts:
    tmnxSysRemoteMgmtV20v0Group.setStatus("current")

tmnxSysNetconfCountersExtension = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 80, 14)
)
tmnxSysNetconfCountersExtension.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfGetSchemaRequests"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfGetDataRequests"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfActionRequests"))
)
if mibBuilder.loadTexts:
    tmnxSysNetconfCountersExtension.setStatus("current")

tmnxSysFpResAllocObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 80, 15)
)
tmnxSysFpResAllocObsoleteGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysFpResAllocG8032Sap"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpResAllocOperG8032Sap"))
)
if mibBuilder.loadTexts:
    tmnxSysFpResAllocObsoleteGroup.setStatus("current")

tmnxSysLicensingV21v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 81, 2)
)
tmnxSysLicensingV21v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysAppLicenseCurrentMax"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAppLicense24HrDateTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAppLicense24HrMax"))
)
if mibBuilder.loadTexts:
    tmnxSysLicensingV21v0Group.setStatus("current")

tmnxSysMgmtIfOpsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 81, 3)
)
tmnxSysMgmtIfOpsGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfOpsAsyncExecTimeout"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfOpsAsyncRetTimeout"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfOpsSyncExecTimeout"))
)
if mibBuilder.loadTexts:
    tmnxSysMgmtIfOpsGroup.setStatus("current")

tmnxSysMgmtIfObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 81, 4)
)
tmnxSysMgmtIfObsoleteGroup.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfMDCliCmdAccntLoad")
)
if mibBuilder.loadTexts:
    tmnxSysMgmtIfObsoleteGroup.setStatus("current")

tmnxSysFwdPathOptsV21v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 81, 5)
)
tmnxSysFwdPathOptsV21v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysFpoDot1xHostAuthAdmState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoDot1xHostAuthOperState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoIpv6FltrEgrAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoIpv6FltrEgrOperState"))
)
if mibBuilder.loadTexts:
    tmnxSysFwdPathOptsV21v0Group.setStatus("current")

tmnxSysBofV21v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 81, 6)
)
tmnxSysBofV21v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sbiEncryptConfig"),
        ("TIMETRA-SYSTEM-MIB", "sbiPassword"),
        ("TIMETRA-SYSTEM-MIB", "sbiEncryptKey"),
        ("TIMETRA-SYSTEM-MIB", "sbbiEncryptConfig"))
)
if mibBuilder.loadTexts:
    tmnxSysBofV21v0Group.setStatus("current")

tmnxSysFpResAllocV21v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 81, 7)
)
tmnxSysFpResAllocV21v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysFpResAllocFilterIpv6"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpResAllocOperFilterIpv6"))
)
if mibBuilder.loadTexts:
    tmnxSysFpResAllocV21v0Group.setStatus("current")

tmnxSysFpResAllocPoolV21v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 81, 8)
)
tmnxSysFpResAllocPoolV21v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysFpRAPoolLgBndRsvMemCnt"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpRAPoolOprLgBndRsvMemCnt"))
)
if mibBuilder.loadTexts:
    tmnxSysFpResAllocPoolV21v0Group.setStatus("current")

tmnxSysMgmtIfComHistoryV21v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 81, 9)
)
tmnxSysMgmtIfComHistoryV21v0Grp.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfCommitHistory")
)
if mibBuilder.loadTexts:
    tmnxSysMgmtIfComHistoryV21v0Grp.setStatus("current")

tmnxSysFpResAllocFecV21v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 81, 10)
)
tmnxSysFpResAllocFecV21v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysFpResAllocFecSysWdUnpd"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpResAllocFecOprSysWdUnpd"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpResAllocFecSysWdPd"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpResAllocFecOprSysWdPd"))
)
if mibBuilder.loadTexts:
    tmnxSysFpResAllocFecV21v0Group.setStatus("current")

tmnxSysGrpcTunnelV21v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 81, 11)
)
tmnxSysGrpcTunnelV21v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxGTnlDestGrpTblLastChgd"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlDestGrpDestTblLastChgd"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelTblLastChgd"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelHandlerTblLastChgd"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlDestGrpRowStatus"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlDestGrpLastChgd"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlDestGrpDescription"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlDestGrpTlsClientProf"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlDestGrpAllowUnsecConn"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlDestGrpTcpKaAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlDestGrpTcpKaIdle"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlDestGrpTcpKaInterval"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlDestGrpTcpKaCount"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlDestGrpDestRowStatus"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlDestGrpDestLastChgd"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlDestGrpDestAddType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlDestGrpDestAddress"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlDestGrpDestPort"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlDestGrpDestVRtrId"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlDestGrpDestLclSrcAddType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlDestGrpDestLclSrcAddress"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlDestGrpDestOrigQosMark"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelRowStatus"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelLastChgd"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelOperState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelOperDownReason"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelDescription"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelDestGrp"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelTgtNameCustomStr"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelTgtNameUserAgent"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelTgtNameNodeName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelOperTargetName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelHandlerRowStatus"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelHandlerLastChgd"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelHandlerAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelHandlerPort"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelHandlerCustomType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelHandlerGrpcServer"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelHandlerSshServer"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelDestAddType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelDestAddress"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelDestPort"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelDestOperState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelDestOperDownReason"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelDestOperVRtrId"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelDestLastOperChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelDestConnAttempts"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelSessionStartTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelSessionTargetType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelSessionLclSrcPort"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelSessionRxBytes"),
        ("TIMETRA-SYSTEM-MIB", "tmnxGTnlTunnelSessionTxBytes"))
)
if mibBuilder.loadTexts:
    tmnxSysGrpcTunnelV21v0Group.setStatus("current")

tmnxSysFwdPathOptsV22v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 82, 1)
)
tmnxSysFwdPathOptsV22v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysFpoIpv6FltrNxtHdrAdmState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoIpv6FltrNxtHdrOprState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoIpv6FltrDstPrtAdmState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoIpv6FltrDstPrtOprState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoIpv6FltrSrcPrtAdmState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoIpv6FltrSrcPrtOprState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoIpv6FltrDstIpLsbAdmSt"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoIpv6FltrDstIpLsbOprSt"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoIpv6FltrTcpFlgAdmState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoIpv6FltrTcpFlgOprState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoIpv6FltStatColAdmState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoIpv6FltStatColOprState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoIpv4FltStatColAdmState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoIpv4FltStatColOprState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoIpv4FltPbrRdrtAdmState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoIpv4FltPbrRdrtOprState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoIpv6FltPbrRdrtAdmState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoIpv6FltPbrRdrtOprState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoRingApsAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoRingApsOperState"))
)
if mibBuilder.loadTexts:
    tmnxSysFwdPathOptsV22v0Group.setStatus("current")

tmnxSysFpLpmResAlcnV22v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 82, 3)
)
tmnxSysFpLpmResAlcnV22v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysFpResAlcnLpmTblLastChg"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpResAlcnLpmLastChanged"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpResAlcnLpmAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpResAlcnLpmOperState"))
)
if mibBuilder.loadTexts:
    tmnxSysFpLpmResAlcnV22v0Group.setStatus("current")

tmnxSysFanControlV22v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 82, 4)
)
tmnxSysFanControlV22v0Group.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysFanIncMinimumSpeed")
)
if mibBuilder.loadTexts:
    tmnxSysFanControlV22v0Group.setStatus("current")

tmnxSysRemoteMgmtV22v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 82, 5)
)
tmnxSysRemoteMgmtV22v0Group.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtHelloIntervalSec")
)
if mibBuilder.loadTexts:
    tmnxSysRemoteMgmtV22v0Group.setStatus("current")

tmnxSysRemoteMgmtObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 82, 6)
)
tmnxSysRemoteMgmtObsoleteGroup.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysRmtMgmtHelloInterval")
)
if mibBuilder.loadTexts:
    tmnxSysRemoteMgmtObsoleteGroup.setStatus("current")

tmnxSysFpOptsV22v0ObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 82, 7)
)
tmnxSysFpOptsV22v0ObsoleteGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysFpoLpmAlcnScl1AdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoLpmAlcnScl1OperState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoLpmAlcnScl2AdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoLpmAlcnScl2OperState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoLpmAlcnScl3AdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoLpmAlcnScl3OperState"))
)
if mibBuilder.loadTexts:
    tmnxSysFpOptsV22v0ObsoleteGroup.setStatus("current")

tmnxSysFpResMacFltrObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 82, 8)
)
tmnxSysFpResMacFltrObsoleteGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysFpoMacFltOutVlanPrioAdmSt"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpoMacFltOutVlanPrioOprSt"))
)
if mibBuilder.loadTexts:
    tmnxSysFpResMacFltrObsoleteGroup.setStatus("current")


# Notification objects

stiDateAndTimeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 1)
)
stiDateAndTimeChanged.setObjects(
    ("TIMETRA-SYSTEM-MIB", "stiDateAndTime")
)
if mibBuilder.loadTexts:
    stiDateAndTimeChanged.setStatus(
        "current"
    )

ssiSaveConfigSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 2)
)
if mibBuilder.loadTexts:
    ssiSaveConfigSucceeded.setStatus(
        "current"
    )

ssiSaveConfigFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 3)
)
if mibBuilder.loadTexts:
    ssiSaveConfigFailed.setStatus(
        "current"
    )

sbiBootConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 4)
)
sbiBootConfig.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sbiConfigStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiPersistStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiPersistIndex"))
)
if mibBuilder.loadTexts:
    sbiBootConfig.setStatus(
        "current"
    )

sbiBootSnmpd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 5)
)
sbiBootSnmpd.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sbiPersistIndex"),
        ("TIMETRA-SYSTEM-MIB", "sbiSnmpdAdminStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiSnmpdOperStatus"))
)
if mibBuilder.loadTexts:
    sbiBootSnmpd.setStatus(
        "current"
    )

radiusServerOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 6)
)
radiusServerOperStatusChange.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "radiusServerAddress"),
        ("TIMETRA-SYSTEM-MIB", "radiusServerOperStatus"))
)
if mibBuilder.loadTexts:
    radiusServerOperStatusChange.setStatus(
        "obsolete"
    )

radiusOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 7)
)
radiusOperStatusChange.setObjects(
    ("TIMETRA-SYSTEM-MIB", "radiusOperStatus")
)
if mibBuilder.loadTexts:
    radiusOperStatusChange.setStatus(
        "current"
    )

tmnxConfigModify = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 8)
)
tmnxConfigModify.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxNotifyRow"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyEntryOID"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyObjectName"))
)
if mibBuilder.loadTexts:
    tmnxConfigModify.setStatus(
        "current"
    )

tmnxConfigCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 9)
)
tmnxConfigCreate.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxNotifyRow"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyEntryOID"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyObjectName"))
)
if mibBuilder.loadTexts:
    tmnxConfigCreate.setStatus(
        "current"
    )

tmnxConfigDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 10)
)
tmnxConfigDelete.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxNotifyRow"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyEntryOID"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyObjectName"))
)
if mibBuilder.loadTexts:
    tmnxConfigDelete.setStatus(
        "current"
    )

tmnxStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 11)
)
tmnxStateChange.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxNotifyRow"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyRowAdminState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyRowOperState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyEntryOID"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyObjectName"))
)
if mibBuilder.loadTexts:
    tmnxStateChange.setStatus(
        "current"
    )

tmnxModuleMallocFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 12)
)
tmnxModuleMallocFailed.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxMemoryModule"),
        ("TIMETRA-SYSTEM-MIB", "tmnxModuleMallocSize"))
)
if mibBuilder.loadTexts:
    tmnxModuleMallocFailed.setStatus(
        "current"
    )

tmnxTrapDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 13)
)
tmnxTrapDropped.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxDroppedTrapID"),
        ("TIMETRA-SYSTEM-MIB", "tmnxTrapDroppedReasonCode"),
        ("TIMETRA-SYSTEM-MIB", "tmnxTrapDroppedEntryID"),
        ("TIMETRA-SYSTEM-MIB", "tmnxTrapDroppedCount"))
)
if mibBuilder.loadTexts:
    tmnxTrapDropped.setStatus(
        "current"
    )

ssiSyncConfigOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 14)
)
if mibBuilder.loadTexts:
    ssiSyncConfigOK.setStatus(
        "current"
    )

ssiSyncConfigFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 15)
)
ssiSyncConfigFailed.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSyncFailureReason")
)
if mibBuilder.loadTexts:
    ssiSyncConfigFailed.setStatus(
        "current"
    )

ssiSyncBootEnvOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 16)
)
if mibBuilder.loadTexts:
    ssiSyncBootEnvOK.setStatus(
        "current"
    )

ssiSyncBootEnvFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 17)
)
ssiSyncBootEnvFailed.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSyncFailureReason")
)
if mibBuilder.loadTexts:
    ssiSyncBootEnvFailed.setStatus(
        "current"
    )

sntpTimeDiffExceedsThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 18)
)
sntpTimeDiffExceedsThreshold.setObjects(
    ("TIMETRA-SYSTEM-MIB", "sntpAdminState")
)
if mibBuilder.loadTexts:
    sntpTimeDiffExceedsThreshold.setStatus(
        "current"
    )

tacplusServerOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 19)
)
tacplusServerOperStatusChange.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tacplusServerAddress"),
        ("TIMETRA-SYSTEM-MIB", "tacplusServerOperStatus"))
)
if mibBuilder.loadTexts:
    tacplusServerOperStatusChange.setStatus(
        "obsolete"
    )

tacplusOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 20)
)
tacplusOperStatusChange.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tacplusOperStatus")
)
if mibBuilder.loadTexts:
    tacplusOperStatusChange.setStatus(
        "current"
    )

tmnxSnmpdError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 21)
)
tmnxSnmpdError.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSnmpdErrorMsg")
)
if mibBuilder.loadTexts:
    tmnxSnmpdError.setStatus(
        "current"
    )

tmnxSsiMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 22)
)
tmnxSsiMismatch.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "ssiSyncMode"),
        ("TIMETRA-SYSTEM-MIB", "sbiPersist"))
)
if mibBuilder.loadTexts:
    tmnxSsiMismatch.setStatus(
        "current"
    )

tmnxSnmpdStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 23)
)
tmnxSnmpdStateChange.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sbiSnmpdAdminStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiSnmpdOperStatus"))
)
if mibBuilder.loadTexts:
    tmnxSnmpdStateChange.setStatus(
        "current"
    )

ssiRedStandbySyncing = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 24)
)
ssiRedStandbySyncing.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    ssiRedStandbySyncing.setStatus(
        "current"
    )

ssiRedStandbyReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 25)
)
ssiRedStandbyReady.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    ssiRedStandbyReady.setStatus(
        "current"
    )

ssiRedStandbySyncLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 26)
)
ssiRedStandbySyncLost.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    ssiRedStandbySyncLost.setStatus(
        "current"
    )

ssiRedSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 27)
)
ssiRedSwitchover.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedFailoverTime"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedFailoverReason"))
)
if mibBuilder.loadTexts:
    ssiRedSwitchover.setStatus(
        "current"
    )

ssiRedCpmActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 28)
)
ssiRedCpmActive.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    ssiRedCpmActive.setStatus(
        "current"
    )

ssiRedSingleCpm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 29)
)
ssiRedSingleCpm.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    ssiRedSingleCpm.setStatus(
        "current"
    )

persistencyClosedAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 30)
)
persistencyClosedAlarmRaised.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxPersistenceAffectedCpm"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyClient"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyFileLocator"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyNotifyMsg"))
)
if mibBuilder.loadTexts:
    persistencyClosedAlarmRaised.setStatus(
        "current"
    )

persistencyClosedAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 31)
)
persistencyClosedAlarmCleared.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxPersistenceAffectedCpm"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyClient"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyFileLocator"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyNotifyMsg"))
)
if mibBuilder.loadTexts:
    persistencyClosedAlarmCleared.setStatus(
        "current"
    )

tmnxSntpOperChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 32)
)
tmnxSntpOperChange.setObjects(
    ("TIMETRA-SYSTEM-MIB", "sntpOperStatus")
)
if mibBuilder.loadTexts:
    tmnxSntpOperChange.setStatus(
        "current"
    )

tmnxSysTimeSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 33)
)
tmnxSysTimeSet.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "stiDateAndTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTimeSetBy"))
)
if mibBuilder.loadTexts:
    tmnxSysTimeSet.setStatus(
        "current"
    )

tmnxFtpClientFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 34)
)
tmnxFtpClientFailure.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxFtpFailureMsg"),
        ("TIMETRA-SYSTEM-MIB", "tmnxFtpFailureDestAddressType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxFtpFailureDestAddress"))
)
if mibBuilder.loadTexts:
    tmnxFtpClientFailure.setStatus(
        "current"
    )

tacplusInetSrvrOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 35)
)
tacplusInetSrvrOperStatusChange.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tacPlusServerInetAddressType"),
        ("TIMETRA-SYSTEM-MIB", "tacPlusServerInetAddress"),
        ("TIMETRA-SYSTEM-MIB", "tacplusServerOperStatus"))
)
if mibBuilder.loadTexts:
    tacplusInetSrvrOperStatusChange.setStatus(
        "current"
    )

radiusInetServerOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 36)
)
radiusInetServerOperStatusChange.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "radiusServerInetAddressType"),
        ("TIMETRA-SYSTEM-MIB", "radiusServerInetAddress"),
        ("TIMETRA-SYSTEM-MIB", "radiusServerOperStatus"))
)
if mibBuilder.loadTexts:
    radiusInetServerOperStatusChange.setStatus(
        "current"
    )

persistencyEventReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 37)
)
persistencyEventReport.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyNotifyMsg")
)
if mibBuilder.loadTexts:
    persistencyEventReport.setStatus(
        "current"
    )

sbiBootConfigFailFileError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 38)
)
sbiBootConfigFailFileError.setObjects(
    ("TIMETRA-SYSTEM-MIB", "sbiBootConfigFailScript")
)
if mibBuilder.loadTexts:
    sbiBootConfigFailFileError.setStatus(
        "current"
    )

sbiBootConfigOKFileError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 39)
)
sbiBootConfigOKFileError.setObjects(
    ("TIMETRA-SYSTEM-MIB", "sbiBootConfigOKScript")
)
if mibBuilder.loadTexts:
    sbiBootConfigOKFileError.setStatus(
        "current"
    )

sbiBootLiConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 40)
)
sbiBootLiConfig.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sliConfigStatus"),
        ("TIMETRA-SYSTEM-MIB", "sbiLiSeparate"),
        ("TIMETRA-SYSTEM-MIB", "sbiLiLocalSave"))
)
if mibBuilder.loadTexts:
    sbiBootLiConfig.setStatus(
        "current"
    )

persistenceRestoreProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 41)
)
persistenceRestoreProblem.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxPersistencyClient"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyNotifyMsg"))
)
if mibBuilder.loadTexts:
    persistenceRestoreProblem.setStatus(
        "current"
    )

tmnxSysRollbackStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 42)
)
tmnxSysRollbackStarted.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackIndex"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileType"),
        ("TIMETRA-LOG-MIB", "tmnxLogExecRollbackOpIndex"))
)
if mibBuilder.loadTexts:
    tmnxSysRollbackStarted.setStatus(
        "current"
    )

tmnxSysRollbackStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 43)
)
tmnxSysRollbackStatusChange.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackIndex"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackResult"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileType"),
        ("TIMETRA-LOG-MIB", "tmnxLogExecRollbackOpIndex"))
)
if mibBuilder.loadTexts:
    tmnxSysRollbackStatusChange.setStatus(
        "current"
    )

tmnxSysRollbackSaveStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 44)
)
tmnxSysRollbackSaveStatusChange.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackSaveResult"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileType"))
)
if mibBuilder.loadTexts:
    tmnxSysRollbackSaveStatusChange.setStatus(
        "current"
    )

tmnxSysRollbackFileDeleteStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 45)
)
tmnxSysRollbackFileDeleteStatus.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackIndex"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileDeleteResult"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileType"))
)
if mibBuilder.loadTexts:
    tmnxSysRollbackFileDeleteStatus.setStatus(
        "current"
    )

ssiSyncRollbackOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 46)
)
if mibBuilder.loadTexts:
    ssiSyncRollbackOK.setStatus(
        "current"
    )

ssiSyncRollbackFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 47)
)
ssiSyncRollbackFailed.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSyncFailureReason")
)
if mibBuilder.loadTexts:
    ssiSyncRollbackFailed.setStatus(
        "current"
    )

ssiSyncCertOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 48)
)
if mibBuilder.loadTexts:
    ssiSyncCertOK.setStatus(
        "current"
    )

ssiSyncCertFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 49)
)
ssiSyncCertFailed.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSyncFailureReason")
)
if mibBuilder.loadTexts:
    ssiSyncCertFailed.setStatus(
        "current"
    )

persistencyFileSysThresRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 50)
)
persistencyFileSysThresRaised.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxPersistenceAffectedCpm"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyClient"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyFileLocator"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyNotifyMsg"))
)
if mibBuilder.loadTexts:
    persistencyFileSysThresRaised.setStatus(
        "current"
    )

persistencyFileSysThresCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 51)
)
persistencyFileSysThresCleared.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxPersistenceAffectedCpm"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyClient"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyFileLocator"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistencyNotifyMsg"))
)
if mibBuilder.loadTexts:
    persistencyFileSysThresCleared.setStatus(
        "current"
    )

tmnxSysExecStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 52)
)
tmnxSysExecStarted.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysExecScript"),
        ("TIMETRA-LOG-MIB", "tmnxLogExecRollbackOpIndex"),
        ("TIMETRA-LOG-MIB", "tmnxLogExecRollbackOpType"))
)
if mibBuilder.loadTexts:
    tmnxSysExecStarted.setStatus(
        "current"
    )

tmnxSysExecFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 53)
)
tmnxSysExecFinished.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysExecScript"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysExecResult"),
        ("TIMETRA-LOG-MIB", "tmnxLogExecRollbackOpIndex"),
        ("TIMETRA-LOG-MIB", "tmnxLogExecRollbackOpType"))
)
if mibBuilder.loadTexts:
    tmnxSysExecFinished.setStatus(
        "current"
    )

tmnxSysRollbackSaveStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 54)
)
tmnxSysRollbackSaveStarted.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileType")
)
if mibBuilder.loadTexts:
    tmnxSysRollbackSaveStarted.setStatus(
        "current"
    )

tmnxSysRollbackDeleteStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 55)
)
tmnxSysRollbackDeleteStarted.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackIndex"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileType"))
)
if mibBuilder.loadTexts:
    tmnxSysRollbackDeleteStarted.setStatus(
        "current"
    )

tmnxSysNvsysFileError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 56)
)
tmnxSysNvsysFileError.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysFileErrorType")
)
if mibBuilder.loadTexts:
    tmnxSysNvsysFileError.setStatus(
        "current"
    )

sysDNSSecFailedAuthentication = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 57)
)
sysDNSSecFailedAuthentication.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "sysDNSSecRespCtrl"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysDNSSecDomainName"))
)
if mibBuilder.loadTexts:
    sysDNSSecFailedAuthentication.setStatus(
        "current"
    )

tmnxConfigConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 58)
)
tmnxConfigConflict.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxNotifyRow"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyEntryOID"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyObjectName"))
)
if mibBuilder.loadTexts:
    tmnxConfigConflict.setStatus(
        "current"
    )

tmnxSysLicenseInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 59)
)
tmnxSysLicenseInvalid.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseErrorReason"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseTimeLeft"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseErrorAction"))
)
if mibBuilder.loadTexts:
    tmnxSysLicenseInvalid.setStatus(
        "current"
    )

tmnxSysLicenseExpiresSoon = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 60)
)
tmnxSysLicenseExpiresSoon.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseTimeLeft"))
)
if mibBuilder.loadTexts:
    tmnxSysLicenseExpiresSoon.setStatus(
        "current"
    )

tmnxSysVsdServerAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 63)
)
tmnxSysVsdServerAvailable.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysNotifVsdServerName")
)
if mibBuilder.loadTexts:
    tmnxSysVsdServerAvailable.setStatus(
        "current"
    )

tmnxSysVsdServerUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 64)
)
tmnxSysVsdServerUnavailable.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysNotifVsdServerName")
)
if mibBuilder.loadTexts:
    tmnxSysVsdServerUnavailable.setStatus(
        "current"
    )

tmnxSysXmppServerFunctional = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 65)
)
tmnxSysXmppServerFunctional.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysNotifXmppServerName")
)
if mibBuilder.loadTexts:
    tmnxSysXmppServerFunctional.setStatus(
        "current"
    )

tmnxSysXmppServerNotFunctional = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 66)
)
tmnxSysXmppServerNotFunctional.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysNotifXmppServerName")
)
if mibBuilder.loadTexts:
    tmnxSysXmppServerNotFunctional.setStatus(
        "current"
    )

tmnxSysLicenseValid = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 67)
)
tmnxSysLicenseValid.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxSysLicenseValid.setStatus(
        "current"
    )

tmnxSysBaseMacAddressNotSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 68)
)
tmnxSysBaseMacAddressNotSet.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxChassisBaseMacAddress")
)
if mibBuilder.loadTexts:
    tmnxSysBaseMacAddressNotSet.setStatus(
        "current"
    )

tmnxSmLaunchStartFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 69)
)
tmnxSmLaunchStartFailed.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxEhsHEntryScriptPlcyOwner"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHEntryScriptPlcyName"),
        ("DISMAN-SCRIPT-MIB", "smLaunchScriptOwner"),
        ("DISMAN-SCRIPT-MIB", "smLaunchScriptName"),
        ("DISMAN-SCRIPT-MIB", "smLaunchError"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSmLaunchExtAuthType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSmRunExtAuthType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSmRunExtUserName"))
)
if mibBuilder.loadTexts:
    tmnxSmLaunchStartFailed.setStatus(
        "current"
    )

tmnxEhsHandlerInvoked = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 70)
)
tmnxEhsHandlerInvoked.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxEhsHandlerDescription"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSmRunExtAuthType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSmRunExtUserName"))
)
if mibBuilder.loadTexts:
    tmnxEhsHandlerInvoked.setStatus(
        "current"
    )

tmnxEhsDroppedByMinDelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 71)
)
tmnxEhsDroppedByMinDelay.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxEhsHEntryScriptPlcyOwner"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHEntryScriptPlcyName"),
        ("DISMAN-SCRIPT-MIB", "smLaunchScriptOwner"),
        ("DISMAN-SCRIPT-MIB", "smLaunchScriptName"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHEntryMinDelay"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHEntryMinDelayInterval"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSmRunExtAuthType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSmRunExtUserName"))
)
if mibBuilder.loadTexts:
    tmnxEhsDroppedByMinDelay.setStatus(
        "current"
    )

tmnxSysAppStats24HrsAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 72)
)
tmnxSysAppStats24HrsAvailable.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysNotifAppStatsTime"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotifAppStatsApplication"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotifAppStatsType"))
)
if mibBuilder.loadTexts:
    tmnxSysAppStats24HrsAvailable.setStatus(
        "current"
    )

tmnxSysAppStatsWeekAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 73)
)
tmnxSysAppStatsWeekAvailable.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysNotifAppStatsTime")
)
if mibBuilder.loadTexts:
    tmnxSysAppStatsWeekAvailable.setStatus(
        "current"
    )

tmnxSysLicenseActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 75)
)
tmnxSysLicenseActivated.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxSysLicenseActivated.setStatus(
        "current"
    )

tmnxSysStandbyLicensingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 76)
)
tmnxSysStandbyLicensingError.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseErrorReason"))
)
if mibBuilder.loadTexts:
    tmnxSysStandbyLicensingError.setStatus(
        "current"
    )

tmnxSysStandbyLicensingReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 77)
)
tmnxSysStandbyLicensingReady.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxSysStandbyLicensingReady.setStatus(
        "current"
    )

tmnxSysMgmtIfModeChangeStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 78)
)
tmnxSysMgmtIfModeChangeStart.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxNotifySysMgmtIfOriginalMode"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfWriteMode"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfWriteSwitchReason"))
)
if mibBuilder.loadTexts:
    tmnxSysMgmtIfModeChangeStart.setStatus(
        "current"
    )

tmnxSysMgmtIfModeChangeComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 79)
)
tmnxSysMgmtIfModeChangeComplete.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfWriteMode")
)
if mibBuilder.loadTexts:
    tmnxSysMgmtIfModeChangeComplete.setStatus(
        "current"
    )

tmnxSysMgmtIfModeChangeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 80)
)
tmnxSysMgmtIfModeChangeFailure.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfWriteMode")
)
if mibBuilder.loadTexts:
    tmnxSysMgmtIfModeChangeFailure.setStatus(
        "current"
    )

tmnxSysAppLicenseInsufficient = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 81)
)
tmnxSysAppLicenseInsufficient.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysLicensingNotifyGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicensedNotifyAppName"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAppLicenseState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseErrorReason"))
)
if mibBuilder.loadTexts:
    tmnxSysAppLicenseInsufficient.setStatus(
        "current"
    )

tmnxSysMgmtIfLiIncorrectFormat = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 82)
)
tmnxSysMgmtIfLiIncorrectFormat.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxPrimaryConfigFileFormatType"),
        ("TIMETRA-SYSTEM-MIB", "tmnxLiConfigFileFormatType"))
)
if mibBuilder.loadTexts:
    tmnxSysMgmtIfLiIncorrectFormat.setStatus(
        "current"
    )

tmnxSysMgmtIfLiCfgNotEncrypted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 83)
)
if mibBuilder.loadTexts:
    tmnxSysMgmtIfLiCfgNotEncrypted.setStatus(
        "current"
    )

tmnxSysLicenseUpdateRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 84)
)
tmnxSysLicenseUpdateRequired.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxSysLicenseUpdateRequired.setStatus(
        "current"
    )

tmnxEqOperStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 85)
)
tmnxEqOperStateChange.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxNotifyRow"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyRowOperState"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyEntryOID"),
        ("TIMETRA-SYSTEM-MIB", "tmnxNotifyObjectName"))
)
if mibBuilder.loadTexts:
    tmnxEqOperStateChange.setStatus(
        "current"
    )

stiDateAndTimeChanging = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 86)
)
stiDateAndTimeChanging.setObjects(
    ("TIMETRA-SYSTEM-MIB", "stiDateAndTime")
)
if mibBuilder.loadTexts:
    stiDateAndTimeChanging.setStatus(
        "current"
    )

tmnxSysSwFabFailRecStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 87)
)
if mibBuilder.loadTexts:
    tmnxSysSwFabFailRecStarted.setStatus(
        "current"
    )

tmnxSysSwFabFailRecCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 88)
)
if mibBuilder.loadTexts:
    tmnxSysSwFabFailRecCompleted.setStatus(
        "current"
    )

tmnxSysSwFabFailRecAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 89)
)
if mibBuilder.loadTexts:
    tmnxSysSwFabFailRecAborted.setStatus(
        "current"
    )

tmnxSysSwFabFailRecDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 90)
)
if mibBuilder.loadTexts:
    tmnxSysSwFabFailRecDetected.setStatus(
        "current"
    )

mdSaveCommitHistoryFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 91)
)
if mibBuilder.loadTexts:
    mdSaveCommitHistoryFailed.setStatus(
        "current"
    )

sbiBootMdReadCommitHistoryFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 92)
)
if mibBuilder.loadTexts:
    sbiBootMdReadCommitHistoryFailed.setStatus(
        "current"
    )

tmnxSysDyingGasp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 1, 0, 93)
)
if mibBuilder.loadTexts:
    tmnxSysDyingGasp.setStatus(
        "current"
    )


# Notifications groups

tmnxSysNotificationV4v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 21)
)
tmnxSysNotificationV4v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "stiDateAndTimeChanged"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveConfigSucceeded"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveConfigFailed"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootConfig"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootSnmpd"),
        ("TIMETRA-SYSTEM-MIB", "radiusServerOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "radiusOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxConfigModify"),
        ("TIMETRA-SYSTEM-MIB", "tmnxConfigCreate"),
        ("TIMETRA-SYSTEM-MIB", "tmnxConfigDelete"),
        ("TIMETRA-SYSTEM-MIB", "tmnxStateChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxModuleMallocFailed"),
        ("TIMETRA-SYSTEM-MIB", "tmnxTrapDropped"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncConfigOK"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncConfigFailed"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncBootEnvOK"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncBootEnvFailed"),
        ("TIMETRA-SYSTEM-MIB", "sntpTimeDiffExceedsThreshold"),
        ("TIMETRA-SYSTEM-MIB", "tacplusServerOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "tacplusOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSnmpdError"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSsiMismatch"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSnmpdStateChange"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedStandbySyncing"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedStandbyReady"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedStandbySyncLost"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedSwitchover"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedCpmActive"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedSingleCpm"),
        ("TIMETRA-SYSTEM-MIB", "persistencyClosedAlarmRaised"),
        ("TIMETRA-SYSTEM-MIB", "persistencyClosedAlarmCleared"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSntpOperChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTimeSet"))
)
if mibBuilder.loadTexts:
    tmnxSysNotificationV4v0Group.setStatus(
        "obsolete"
    )

tmnxSysNotificationV5v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 23)
)
tmnxSysNotificationV5v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "stiDateAndTimeChanged"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveConfigSucceeded"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveConfigFailed"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootConfig"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootSnmpd"),
        ("TIMETRA-SYSTEM-MIB", "radiusOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxConfigModify"),
        ("TIMETRA-SYSTEM-MIB", "tmnxConfigCreate"),
        ("TIMETRA-SYSTEM-MIB", "tmnxConfigDelete"),
        ("TIMETRA-SYSTEM-MIB", "tmnxStateChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxModuleMallocFailed"),
        ("TIMETRA-SYSTEM-MIB", "tmnxTrapDropped"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncConfigOK"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncConfigFailed"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncBootEnvOK"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncBootEnvFailed"),
        ("TIMETRA-SYSTEM-MIB", "sntpTimeDiffExceedsThreshold"),
        ("TIMETRA-SYSTEM-MIB", "tacplusOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSnmpdError"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSsiMismatch"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSnmpdStateChange"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedStandbySyncing"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedStandbyReady"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedStandbySyncLost"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedSwitchover"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedCpmActive"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedSingleCpm"),
        ("TIMETRA-SYSTEM-MIB", "persistencyClosedAlarmRaised"),
        ("TIMETRA-SYSTEM-MIB", "persistencyClosedAlarmCleared"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSntpOperChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTimeSet"),
        ("TIMETRA-SYSTEM-MIB", "tmnxFtpClientFailure"),
        ("TIMETRA-SYSTEM-MIB", "tacplusInetSrvrOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "radiusInetServerOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "persistencyEventReport"))
)
if mibBuilder.loadTexts:
    tmnxSysNotificationV5v0Group.setStatus(
        "obsolete"
    )

tmnxSysObsoleteNotificationV5v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 24)
)
tmnxSysObsoleteNotificationV5v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tacplusServerOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "radiusServerOperStatusChange"))
)
if mibBuilder.loadTexts:
    tmnxSysObsoleteNotificationV5v0Group.setStatus(
        "current"
    )

tmnxSysNotificationV6v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 32)
)
tmnxSysNotificationV6v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "stiDateAndTimeChanged"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveConfigSucceeded"),
        ("TIMETRA-SYSTEM-MIB", "ssiSaveConfigFailed"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootConfig"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootSnmpd"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootConfigFailFileError"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootConfigOKFileError"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootLiConfig"),
        ("TIMETRA-SYSTEM-MIB", "radiusOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxConfigModify"),
        ("TIMETRA-SYSTEM-MIB", "tmnxConfigCreate"),
        ("TIMETRA-SYSTEM-MIB", "tmnxConfigDelete"),
        ("TIMETRA-SYSTEM-MIB", "tmnxStateChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxModuleMallocFailed"),
        ("TIMETRA-SYSTEM-MIB", "tmnxTrapDropped"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncConfigOK"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncConfigFailed"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncBootEnvOK"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncBootEnvFailed"),
        ("TIMETRA-SYSTEM-MIB", "sntpTimeDiffExceedsThreshold"),
        ("TIMETRA-SYSTEM-MIB", "tacplusOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSnmpdError"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSsiMismatch"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSnmpdStateChange"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedStandbySyncing"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedStandbyReady"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedStandbySyncLost"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedSwitchover"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedCpmActive"),
        ("TIMETRA-SYSTEM-MIB", "ssiRedSingleCpm"),
        ("TIMETRA-SYSTEM-MIB", "persistencyClosedAlarmRaised"),
        ("TIMETRA-SYSTEM-MIB", "persistencyClosedAlarmCleared"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSntpOperChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTimeSet"),
        ("TIMETRA-SYSTEM-MIB", "tmnxFtpClientFailure"),
        ("TIMETRA-SYSTEM-MIB", "tacplusInetSrvrOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "radiusInetServerOperStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "persistencyEventReport"),
        ("TIMETRA-SYSTEM-MIB", "mdSaveCommitHistoryFailed"),
        ("TIMETRA-SYSTEM-MIB", "sbiBootMdReadCommitHistoryFailed"))
)
if mibBuilder.loadTexts:
    tmnxSysNotificationV6v0Group.setStatus(
        "current"
    )

tmnxSysNotificationV9v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 43)
)
tmnxSysNotificationV9v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "persistenceRestoreProblem"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackStarted"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackSaveStatusChange"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackFileDeleteStatus"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncRollbackOK"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncRollbackFailed"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncCertOK"),
        ("TIMETRA-SYSTEM-MIB", "ssiSyncCertFailed"))
)
if mibBuilder.loadTexts:
    tmnxSysNotificationV9v0Group.setStatus(
        "current"
    )

tmnxSysNotificationV10v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 50)
)
tmnxSysNotificationV10v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "persistencyFileSysThresRaised"),
        ("TIMETRA-SYSTEM-MIB", "persistencyFileSysThresCleared"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysExecStarted"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysExecFinished"))
)
if mibBuilder.loadTexts:
    tmnxSysNotificationV10v0Group.setStatus(
        "current"
    )

tmnxSysNotificationRBGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 52)
)
tmnxSysNotificationRBGroup.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackSaveStarted"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackDeleteStarted"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNvsysFileError"))
)
if mibBuilder.loadTexts:
    tmnxSysNotificationRBGroup.setStatus(
        "current"
    )

tmnxSysDNSSecNotifV12v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 60, 3)
)
tmnxSysDNSSecNotifV12v0Group.setObjects(
    ("TIMETRA-SYSTEM-MIB", "sysDNSSecFailedAuthentication")
)
if mibBuilder.loadTexts:
    tmnxSysDNSSecNotifV12v0Group.setStatus(
        "current"
    )

tmnxSysNotificationV12v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 60, 4)
)
tmnxSysNotificationV12v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxConfigConflict"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseInvalid"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseExpiresSoon"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysVsdServerAvailable"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysVsdServerUnavailable"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServerFunctional"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppServerNotFunctional"))
)
if mibBuilder.loadTexts:
    tmnxSysNotificationV12v0Group.setStatus(
        "current"
    )

tmnxSysLicenseNotifV13v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 69)
)
tmnxSysLicenseNotifV13v0Group.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseValid")
)
if mibBuilder.loadTexts:
    tmnxSysLicenseNotifV13v0Group.setStatus(
        "current"
    )

tmnxSysNotificationV14v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 72, 2)
)
tmnxSysNotificationV14v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysBaseMacAddressNotSet"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSmLaunchStartFailed"),
        ("TIMETRA-SYSTEM-MIB", "tmnxEhsHandlerInvoked"),
        ("TIMETRA-SYSTEM-MIB", "tmnxEhsDroppedByMinDelay"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAppStats24HrsAvailable"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAppStatsWeekAvailable"))
)
if mibBuilder.loadTexts:
    tmnxSysNotificationV14v0Group.setStatus(
        "current"
    )

tmnxSysLicenseNotifV16v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 78, 2)
)
tmnxSysLicenseNotifV16v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseActivated"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysStandbyLicensingError"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysStandbyLicensingReady"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfModeChangeStart"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfModeChangeComplete"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfModeChangeFailure"))
)
if mibBuilder.loadTexts:
    tmnxSysLicenseNotifV16v0Group.setStatus(
        "current"
    )

tmnxSysSwFabNotifV16v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 78, 9)
)
tmnxSysSwFabNotifV16v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysSwFabFailRecStarted"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysSwFabFailRecCompleted"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysSwFabFailRecAborted"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysSwFabFailRecDetected"))
)
if mibBuilder.loadTexts:
    tmnxSysSwFabNotifV16v0Group.setStatus(
        "current"
    )

tmnxSysLicenseNotifV19v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 79, 2)
)
tmnxSysLicenseNotifV19v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysAppLicenseInsufficient"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseUpdateRequired"))
)
if mibBuilder.loadTexts:
    tmnxSysLicenseNotifV19v0Group.setStatus(
        "current"
    )

tmnxSysBootConfFmtNotifyGrp = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 79, 10)
)
tmnxSysBootConfFmtNotifyGrp.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfLiIncorrectFormat"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfLiCfgNotEncrypted"))
)
if mibBuilder.loadTexts:
    tmnxSysBootConfFmtNotifyGrp.setStatus(
        "current"
    )

tmnxSysNotificationV20v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 80, 1)
)
tmnxSysNotificationV20v0Group.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxEqOperStateChange"),
        ("TIMETRA-SYSTEM-MIB", "stiDateAndTimeChanging"))
)
if mibBuilder.loadTexts:
    tmnxSysNotificationV20v0Group.setStatus(
        "current"
    )

tmnxSysNotificationV22v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 2, 82, 2)
)
tmnxSysNotificationV22v0Group.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysDyingGasp")
)
if mibBuilder.loadTexts:
    tmnxSysNotificationV22v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxSysV4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 4)
)
tmnxSysV4v0Compliance.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysGeneralV3v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTimeV4v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysConfigV3v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRadiusServerGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTacPlusServerGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysBofGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV4v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistenceV4v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSysV4v0Compliance.setStatus(
        "obsolete"
    )

tmnxSysV5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 5)
)
tmnxSysV5v0Compliance.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysGeneralV3v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTimeV4v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysConfigV3v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRadiusServerV5v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTacPlusServerV5v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysBofGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV5v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistenceV5v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSysV5v0Compliance.setStatus(
        "obsolete"
    )

tmnxSysV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 6)
)
tmnxSysV6v0Compliance.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysGeneralV3v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTimeV4v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysConfigV3v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRadiusServerV5v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTacPlusServerV5v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysBofV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistenceV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysIpv6MgmtItfV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLiV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSysV6v0Compliance.setStatus(
        "obsolete"
    )

tmnxSysV7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 7)
)
tmnxSysV7v0Compliance.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysGeneralV3v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGeneralV7v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTimeV4v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysConfigV3v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRadiusServerV5v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTacPlusServerV5v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysBofV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistenceV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysIpv6MgmtItfV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLiV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSystemCpuMonitorGroup"))
)
if mibBuilder.loadTexts:
    tmnxSysV7v0Compliance.setStatus(
        "obsolete"
    )

tmnxSysV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 8)
)
tmnxSysV8v0Compliance.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysGeneralV3v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGeneralV7v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTimeV4v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysConfigV8v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLoginControlV8v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRadiusServerV5v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTacPlusServerV5v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysBofV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistenceV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysIpv6MgmtItfV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLiV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysIcmpVSV6v1Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysEthInfoGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSystemCpuMonitorGroup"))
)
if mibBuilder.loadTexts:
    tmnxSysV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxSysV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 9)
)
tmnxSysV9v0Compliance.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxPersistenceV9v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysBofV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysConfigV8v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysEthInfoGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGeneralV3v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGeneralV7v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysIcmpVSV6v1Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysIpv6MgmtItfV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLiFilterGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLiV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLoginControlSecGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLoginControlV8v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLoginControlV9v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV9v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRadiusServerV5v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackV9v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTacPlusServerV5v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTimeV4v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSystemCpuMonitorGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCertGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationRBGroup"))
)
if mibBuilder.loadTexts:
    tmnxSysV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxSysBootedBofCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 10)
)
tmnxSysBootedBofCompliance.setObjects(
    ("TIMETRA-SYSTEM-MIB", "tmnxSysBootedBofGroup")
)
if mibBuilder.loadTexts:
    tmnxSysBootedBofCompliance.setStatus(
        "current"
    )

tmnxSysV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 11)
)
tmnxSysV10v0Compliance.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxPersistenceV9v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysBofV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysConfigV8v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysEthInfoGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGeneralV3v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGeneralV7v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysIcmpVSV6v1Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysIpv6MgmtItfV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLiFilterGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLiV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLoginControlSecGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLoginControlV8v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLoginControlV9v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV9v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV10v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRadiusServerV5v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackV9v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTacPlusServerV5v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTimeV4v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSystemCpuMonitorGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCertGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationRBGroup"))
)
if mibBuilder.loadTexts:
    tmnxSysV10v0Compliance.setStatus(
        "obsolete"
    )

tmnxSysV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 12)
)
tmnxSysV11v0Compliance.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxPersistenceV11v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysBofV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysConfigV8v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysEthInfoGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGeneralV3v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGeneralV7v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysIcmpVSV6v1Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysIpv6MgmtItfV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLiFilterGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLiV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLoginControlSecGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLoginControlV8v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLoginControlV9v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV9v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV10v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRadiusServerV5v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackV9v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTacPlusServerV5v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTimeV4v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSystemCpuMonitorGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCertGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationRBGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGroupingSystemGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCandidateCfgGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfV11v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysStrmV11v0R4Group"))
)
if mibBuilder.loadTexts:
    tmnxSysV11v0Compliance.setStatus(
        "obsolete"
    )

tmnxSysV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 13)
)
tmnxSysV12v0Compliance.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxPersistenceV12v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysBofV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCandidateCfgGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCardResourceGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCertGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysConfigV8v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysDNSSecNotifV12v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysDNSSecV12v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysEthInfoGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGeneralV3v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGeneralV7v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGroupingSystemGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysIcmpVSV6v1Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysIpv6MgmtItfV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLiFilterGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLiV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLoginControlSecGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLoginControlV8v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLoginControlV9v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfV11v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationRBGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV10v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV12v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV9v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRadiusServerV5v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackV9v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysDhcpGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysStrmV11v0R4Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTacPlusServerV5v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTimeV4v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSystemCpuMonitorGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppV12v4Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysBofV12v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseV12v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSysV12v0Compliance.setStatus(
        "obsolete"
    )

tmnxSysV13v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 14)
)
tmnxSysV13v0Compliance.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxPersistenceV12v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysBofV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCandidateCfgGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCardResourceGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCertGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysConfigV8v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysDNSSecNotifV12v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysDNSSecV12v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysEthInfoGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGeneralV3v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGeneralV7v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGroupingSystemGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysIcmpVSV6v1Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysIpv6MgmtItfV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLiFilterGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLiV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLoginControlSecGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLoginControlV8v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLoginControlV9v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfV11v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationRBGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV10v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV12v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV9v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRadiusServerV5v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackV9v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysDhcpGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysStrmV11v0R4Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTacPlusServerV5v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTimeV4v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSystemCpuMonitorGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppV12v4Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysBofV12v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseV12v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFibV13v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfV13v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysSnmpSrcAccesLstV13v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtProtocolV13v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFileTransProfV13v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysEhsV13v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysBofV13v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseV13v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseNotifV13v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysSwReposV13v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSysV13v0Compliance.setStatus(
        "obsolete"
    )

tmnxSysV14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 15)
)
tmnxSysV14v0Compliance.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxPersistenceV12v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysBofV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCandidateCfgGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCardResourceGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysCertGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysConfigV8v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysDNSSecNotifV12v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysDNSSecV12v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysEthInfoGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGeneralV3v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGeneralV7v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGroupingSystemGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysIcmpVSV6v1Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysIpv6MgmtItfV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLiFilterGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLiV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLoginControlSecGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLoginControlV8v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLoginControlV9v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfV11v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationRBGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV10v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV12v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV6v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV9v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRadiusServerV5v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackRescueGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRollbackV9v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysDhcpGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysStrmV11v0R4Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTacPlusServerV5v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTimeV4v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSystemCpuMonitorGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppV12v4Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysBofV12v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseV12v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFibV13v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfV13v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysSnmpSrcAccesLstV13v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtProtocolV13v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFileTransProfV13v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysEhsV13v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysBofV13v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseV13v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseNotifV13v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysSwReposV13v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysBofV14v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV14v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxPersistenceV14v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysEhsParameterGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseApplicationGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotifyObjsV14v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysTimeV14v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSysV14v0Compliance.setStatus(
        "current"
    )

tmnxSysV15v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 16)
)
tmnxSysV15v0Compliance.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysLoginControlV15v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcV15v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysXmppMgmtGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseApp48HrsGroup"))
)
if mibBuilder.loadTexts:
    tmnxSysV15v0Compliance.setStatus(
        "current"
    )

tmnxSysV15v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 17)
)
tmnxSysV15v1Compliance.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfV15v1Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtProtocolV15v1Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysConfigSaveCtrlV15v1Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfMdCliGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfYangModulesGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFileTransProfV15v1Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysBofV15v1Group"))
)
if mibBuilder.loadTexts:
    tmnxSysV15v1Compliance.setStatus(
        "current"
    )

tmnxSysV16v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 18)
)
tmnxSysV16v0Compliance.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysHttpRdrV16v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseNotifV16v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfDsLocksV16v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicensingV16v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtInterfaceV16v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfNotifyObjsGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetworkElementV16v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysSwitchFabricV16v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysSwFabNotifV16v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSysV16v0Compliance.setStatus(
        "current"
    )

tmnxSysV19v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 19)
)
tmnxSysV19v0Compliance.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysLicNotifyObjsV19v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseNotifV19v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysResInfoV19v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysBofV19v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetworkElementV19v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicensingV19v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfV19v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysEhsV19v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysBootConfFmtNotifyObjsGrp"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFwdPathOptsV19v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysBootConfFmtNotifyGrp"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfMdCliCmdAccntGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysResItCamV19v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpCamAllocV19v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSysV19v0Compliance.setStatus(
        "obsolete"
    )

tmnxSysV20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 20)
)
tmnxSysV20v0Compliance.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV20v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFwdPathOptsV20v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAutoBootV20v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysSwitchFabricV20v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysUsbV20v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGeneralV20v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtInterfaceV20v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAutoNEDV20v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysAutoBootOspfV20v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRemoteMgmtV20v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfCountersExtension"))
)
if mibBuilder.loadTexts:
    tmnxSysV20v0Compliance.setStatus(
        "current"
    )

tmnxSysV21v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 21)
)
tmnxSysV21v0Compliance.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysLicensingV21v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfOpsGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfObsoleteGroup"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicNotifyObjsV19v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicenseNotifV19v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysResInfoV19v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysBofV19v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetworkElementV19v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysLicensingV19v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNetconfV19v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysEhsV19v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysBootConfFmtNotifyObjsGrp"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFwdPathOptsV19v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFwdPathOptsV21v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysBootConfFmtNotifyGrp"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysResItCamV19v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpCamAllocV19v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysBofV21v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpResAllocV21v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpResAllocPoolV21v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysMgmtIfComHistoryV21v0Grp"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpResAllocFecV21v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysGrpcTunnelV21v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSysV21v0Compliance.setStatus(
        "current"
    )

tmnxSysV22v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 1, 1, 22)
)
tmnxSysV22v0Compliance.setObjects(
      *(("TIMETRA-SYSTEM-MIB", "tmnxSysFwdPathOptsV22v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysNotificationV22v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFpLpmResAlcnV22v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysFanControlV22v0Group"),
        ("TIMETRA-SYSTEM-MIB", "tmnxSysRemoteMgmtV22v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSysV22v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SYSTEM-MIB",
    **{"TmnxSsiSyncMode": TmnxSsiSyncMode,
       "TmnxSsiSyncRollbackMode": TmnxSsiSyncRollbackMode,
       "TmnxSysLicenseApplication": TmnxSysLicenseApplication,
       "TmnxSysLicenseAppStatsType": TmnxSysLicenseAppStatsType,
       "TmnxSysLicensingGroup": TmnxSysLicensingGroup,
       "TmnxSysMonSampleTime": TmnxSysMonSampleTime,
       "TmnxSysMonUtilization": TmnxSysMonUtilization,
       "TmnxSysMgmtIfDstoreLockState": TmnxSysMgmtIfDstoreLockState,
       "TmnxSysNeid": TmnxSysNeid,
       "TmnxConfigFileFormatType": TmnxConfigFileFormatType,
       "TmnxSchemaPathState": TmnxSchemaPathState,
       "TmnxSysRmtMgmtLastRegStatus": TmnxSysRmtMgmtLastRegStatus,
       "TmnxSysRmtMgmtSrcDefaultPort": TmnxSysRmtMgmtSrcDefaultPort,
       "timetraSysMIBModule": timetraSysMIBModule,
       "tmnxSysConformance": tmnxSysConformance,
       "tmnxSysCompliances": tmnxSysCompliances,
       "tmnxSysV4v0Compliance": tmnxSysV4v0Compliance,
       "tmnxSysV5v0Compliance": tmnxSysV5v0Compliance,
       "tmnxSysV6v0Compliance": tmnxSysV6v0Compliance,
       "tmnxSysV7v0Compliance": tmnxSysV7v0Compliance,
       "tmnxSysV8v0Compliance": tmnxSysV8v0Compliance,
       "tmnxSysV9v0Compliance": tmnxSysV9v0Compliance,
       "tmnxSysBootedBofCompliance": tmnxSysBootedBofCompliance,
       "tmnxSysV10v0Compliance": tmnxSysV10v0Compliance,
       "tmnxSysV11v0Compliance": tmnxSysV11v0Compliance,
       "tmnxSysV12v0Compliance": tmnxSysV12v0Compliance,
       "tmnxSysV13v0Compliance": tmnxSysV13v0Compliance,
       "tmnxSysV14v0Compliance": tmnxSysV14v0Compliance,
       "tmnxSysV15v0Compliance": tmnxSysV15v0Compliance,
       "tmnxSysV15v1Compliance": tmnxSysV15v1Compliance,
       "tmnxSysV16v0Compliance": tmnxSysV16v0Compliance,
       "tmnxSysV19v0Compliance": tmnxSysV19v0Compliance,
       "tmnxSysV20v0Compliance": tmnxSysV20v0Compliance,
       "tmnxSysV21v0Compliance": tmnxSysV21v0Compliance,
       "tmnxSysV22v0Compliance": tmnxSysV22v0Compliance,
       "tmnxSysGroups": tmnxSysGroups,
       "tmnxSysRadiusServerGroup": tmnxSysRadiusServerGroup,
       "tmnxSysTacPlusServerGroup": tmnxSysTacPlusServerGroup,
       "tmnxSysBofGroup": tmnxSysBofGroup,
       "tmnxSysConfigV3v0Group": tmnxSysConfigV3v0Group,
       "tmnxSysGeneralV3v0Group": tmnxSysGeneralV3v0Group,
       "tmnxSysObsoleteGroup": tmnxSysObsoleteGroup,
       "tmnxPersistenceV4v0Group": tmnxPersistenceV4v0Group,
       "tmnxSysTimeV4v0Group": tmnxSysTimeV4v0Group,
       "tmnxSysNotifyObjsR4r0Group": tmnxSysNotifyObjsR4r0Group,
       "tmnxSysNotificationV4v0Group": tmnxSysNotificationV4v0Group,
       "tmnxSysNotifyObjsV5v0Group": tmnxSysNotifyObjsV5v0Group,
       "tmnxSysNotificationV5v0Group": tmnxSysNotificationV5v0Group,
       "tmnxSysObsoleteNotificationV5v0Group": tmnxSysObsoleteNotificationV5v0Group,
       "tmnxSysTacPlusServerV5v0Group": tmnxSysTacPlusServerV5v0Group,
       "tmnxSysRadiusServerV5v0Group": tmnxSysRadiusServerV5v0Group,
       "tmnxSysObsoleteV5v0Group": tmnxSysObsoleteV5v0Group,
       "tmnxPersistenceV5v0Group": tmnxPersistenceV5v0Group,
       "tmnxSysIpv6MgmtItfV6v0Group": tmnxSysIpv6MgmtItfV6v0Group,
       "tmnxPersistenceV6v0Group": tmnxPersistenceV6v0Group,
       "tmnxSysBofV6v0Group": tmnxSysBofV6v0Group,
       "tmnxSysNotificationV6v0Group": tmnxSysNotificationV6v0Group,
       "tmnxSysLiV6v0Group": tmnxSysLiV6v0Group,
       "tmnxSysNotifyObjsV6v0Group": tmnxSysNotifyObjsV6v0Group,
       "tmnxSysGeneralV7v0Group": tmnxSysGeneralV7v0Group,
       "tmnxSysIcmpVSV6v1Group": tmnxSysIcmpVSV6v1Group,
       "tmnxSysConfigV8v0Group": tmnxSysConfigV8v0Group,
       "tmnxSysLoginControlV8v0Group": tmnxSysLoginControlV8v0Group,
       "tmnxSysEthInfoGroup": tmnxSysEthInfoGroup,
       "tmnxPersistenceV9v0Group": tmnxPersistenceV9v0Group,
       "tmnxSysLoginControlSecGroup": tmnxSysLoginControlSecGroup,
       "tmnxSysLiFilterGroup": tmnxSysLiFilterGroup,
       "tmnxSysNotificationV9v0Group": tmnxSysNotificationV9v0Group,
       "tmnxSysRollbackV9v0Group": tmnxSysRollbackV9v0Group,
       "tmnxSysLoginControlV9v0Group": tmnxSysLoginControlV9v0Group,
       "tmnxSystemCpuMonitorGroup": tmnxSystemCpuMonitorGroup,
       "tmnxSysCertGroup": tmnxSysCertGroup,
       "tmnxSysBootedBofGroup": tmnxSysBootedBofGroup,
       "tmnxSysRollbackRescueGroup": tmnxSysRollbackRescueGroup,
       "tmnxSysNotificationV10v0Group": tmnxSysNotificationV10v0Group,
       "tmnxSysNotifyObjsV10v0Group": tmnxSysNotifyObjsV10v0Group,
       "tmnxSysNotificationRBGroup": tmnxSysNotificationRBGroup,
       "tmnxSysNotifyObjsGenGroup": tmnxSysNotifyObjsGenGroup,
       "tmnxSysGroupingSystemGroup": tmnxSysGroupingSystemGroup,
       "tmnxSysCandidateCfgGroup": tmnxSysCandidateCfgGroup,
       "tmnxPersistenceV11v0Group": tmnxPersistenceV11v0Group,
       "tmnxSysNetconfV11v0Group": tmnxSysNetconfV11v0Group,
       "tmnxSysStrmV11v0R4Group": tmnxSysStrmV11v0R4Group,
       "tmnxSysNotifyObjsV11v0Group": tmnxSysNotifyObjsV11v0Group,
       "tmnxSysV12v0Groups": tmnxSysV12v0Groups,
       "tmnxPersistenceV12v0Group": tmnxPersistenceV12v0Group,
       "tmnxSysDNSSecV12v0Group": tmnxSysDNSSecV12v0Group,
       "tmnxSysDNSSecNotifV12v0Group": tmnxSysDNSSecNotifV12v0Group,
       "tmnxSysNotificationV12v0Group": tmnxSysNotificationV12v0Group,
       "tmnxSysXmppV12v4Group": tmnxSysXmppV12v4Group,
       "tmnxSysCardResourceGroup": tmnxSysCardResourceGroup,
       "tmnxSysNotifyObjsV12v0Group": tmnxSysNotifyObjsV12v0Group,
       "tmnxSysBofV12v0Group": tmnxSysBofV12v0Group,
       "tmnxSysLicenseV12v0Group": tmnxSysLicenseV12v0Group,
       "tmnxSysDhcpGroup": tmnxSysDhcpGroup,
       "tmnxSysFibV13v0Group": tmnxSysFibV13v0Group,
       "tmnxSysNetconfV13v0Group": tmnxSysNetconfV13v0Group,
       "tmnxSysSnmpSrcAccesLstV13v0Group": tmnxSysSnmpSrcAccesLstV13v0Group,
       "tmnxSysMgmtProtocolV13v0Group": tmnxSysMgmtProtocolV13v0Group,
       "tmnxSysFileTransProfV13v0Group": tmnxSysFileTransProfV13v0Group,
       "tmnxSysEhsV13v0Group": tmnxSysEhsV13v0Group,
       "tmnxSysLicenseV13v0Group": tmnxSysLicenseV13v0Group,
       "tmnxSysLicenseNotifV13v0Group": tmnxSysLicenseNotifV13v0Group,
       "tmnxSysSwReposV13v0Group": tmnxSysSwReposV13v0Group,
       "tmnxSysBofV13v0Group": tmnxSysBofV13v0Group,
       "tmnxSysV14v0Groups": tmnxSysV14v0Groups,
       "tmnxSysBofV14v0Group": tmnxSysBofV14v0Group,
       "tmnxSysNotificationV14v0Group": tmnxSysNotificationV14v0Group,
       "tmnxPersistenceV14v0Group": tmnxPersistenceV14v0Group,
       "tmnxSysNetconfV14v0Group": tmnxSysNetconfV14v0Group,
       "tmnxSysEhsParameterGroup": tmnxSysEhsParameterGroup,
       "tmnxSysLicenseApplicationGroup": tmnxSysLicenseApplicationGroup,
       "tmnxSysNotifyObjsV14v0Group": tmnxSysNotifyObjsV14v0Group,
       "tmnxSysTimeV14v0Group": tmnxSysTimeV14v0Group,
       "tmnxSysLoginControlV15v0Group": tmnxSysLoginControlV15v0Group,
       "tmnxSysGrpcV15v0Group": tmnxSysGrpcV15v0Group,
       "tmnxSysXmppMgmtGroup": tmnxSysXmppMgmtGroup,
       "tmnxSysV15v0Groups": tmnxSysV15v0Groups,
       "tmnxSysLicenseApp48HrsGroup": tmnxSysLicenseApp48HrsGroup,
       "tmnxSysV15v1Groups": tmnxSysV15v1Groups,
       "tmnxSysNetconfV15v1Group": tmnxSysNetconfV15v1Group,
       "tmnxSysMgmtProtocolV15v1Group": tmnxSysMgmtProtocolV15v1Group,
       "tmnxSysConfigSaveCtrlV15v1Group": tmnxSysConfigSaveCtrlV15v1Group,
       "tmnxSysMgmtIfMdCliGroup": tmnxSysMgmtIfMdCliGroup,
       "tmnxSysMgmtIfYangModulesGroup": tmnxSysMgmtIfYangModulesGroup,
       "tmnxSysNetconfV15v1ObsoleteGroup": tmnxSysNetconfV15v1ObsoleteGroup,
       "tmnxSysFileTransProfV15v1Group": tmnxSysFileTransProfV15v1Group,
       "tmnxSysBofV15v1Group": tmnxSysBofV15v1Group,
       "tmnxSysV16v0Groups": tmnxSysV16v0Groups,
       "tmnxSysHttpRdrV16v0Group": tmnxSysHttpRdrV16v0Group,
       "tmnxSysLicenseNotifV16v0Group": tmnxSysLicenseNotifV16v0Group,
       "tmnxSysMgmtIfDsLocksV16v0Group": tmnxSysMgmtIfDsLocksV16v0Group,
       "tmnxSysLicensingV16v0Group": tmnxSysLicensingV16v0Group,
       "tmnxSysMgmtInterfaceV16v0Group": tmnxSysMgmtInterfaceV16v0Group,
       "tmnxSysMgmtIfNotifyObjsGroup": tmnxSysMgmtIfNotifyObjsGroup,
       "tmnxSysNetworkElementV16v0Group": tmnxSysNetworkElementV16v0Group,
       "tmnxSysSwitchFabricV16v0Group": tmnxSysSwitchFabricV16v0Group,
       "tmnxSysSwFabNotifV16v0Group": tmnxSysSwFabNotifV16v0Group,
       "tmnxSysV19v0Groups": tmnxSysV19v0Groups,
       "tmnxSysLicNotifyObjsV19v0Group": tmnxSysLicNotifyObjsV19v0Group,
       "tmnxSysLicenseNotifV19v0Group": tmnxSysLicenseNotifV19v0Group,
       "tmnxSysResInfoV19v0Group": tmnxSysResInfoV19v0Group,
       "tmnxSysBofV19v0Group": tmnxSysBofV19v0Group,
       "tmnxSysNetworkElementV19v0Group": tmnxSysNetworkElementV19v0Group,
       "tmnxSysLicensingV19v0Group": tmnxSysLicensingV19v0Group,
       "tmnxSysNetconfV19v0Group": tmnxSysNetconfV19v0Group,
       "tmnxSysEhsV19v0Group": tmnxSysEhsV19v0Group,
       "tmnxSysBootConfFmtNotifyObjsGrp": tmnxSysBootConfFmtNotifyObjsGrp,
       "tmnxSysBootConfFmtNotifyGrp": tmnxSysBootConfFmtNotifyGrp,
       "tmnxSysFwdPathOptsV19v0Group": tmnxSysFwdPathOptsV19v0Group,
       "tmnxSysMgmtIfMdCliCmdAccntGroup": tmnxSysMgmtIfMdCliCmdAccntGroup,
       "tmnxSysResItCamV19v0Group": tmnxSysResItCamV19v0Group,
       "tmnxSysFpCamAllocV19v0Group": tmnxSysFpCamAllocV19v0Group,
       "tmnxSysV20v0Groups": tmnxSysV20v0Groups,
       "tmnxSysNotificationV20v0Group": tmnxSysNotificationV20v0Group,
       "tmnxSysFwdPathOptsV20v0Group": tmnxSysFwdPathOptsV20v0Group,
       "tmnxSysAutoBootV20v0Group": tmnxSysAutoBootV20v0Group,
       "tmnxSysSwitchFabricV20v0Group": tmnxSysSwitchFabricV20v0Group,
       "tmnxSysUsbV20v0Group": tmnxSysUsbV20v0Group,
       "tmnxSysGeneralV20v0Group": tmnxSysGeneralV20v0Group,
       "tmnxSysMgmtInterfaceV20v0Group": tmnxSysMgmtInterfaceV20v0Group,
       "tmnxSysFpResAllocV20v0Group": tmnxSysFpResAllocV20v0Group,
       "tmnxSysAutoNEDV20v0Group": tmnxSysAutoNEDV20v0Group,
       "tmnxSysAutoBootOspfV20v0Group": tmnxSysAutoBootOspfV20v0Group,
       "tmnxSysRemoteMgmtV20v0Group": tmnxSysRemoteMgmtV20v0Group,
       "tmnxSysNetconfCountersExtension": tmnxSysNetconfCountersExtension,
       "tmnxSysFpResAllocObsoleteGroup": tmnxSysFpResAllocObsoleteGroup,
       "tmnxSysV21v0Groups": tmnxSysV21v0Groups,
       "tmnxSysLicensingV21v0Group": tmnxSysLicensingV21v0Group,
       "tmnxSysMgmtIfOpsGroup": tmnxSysMgmtIfOpsGroup,
       "tmnxSysMgmtIfObsoleteGroup": tmnxSysMgmtIfObsoleteGroup,
       "tmnxSysFwdPathOptsV21v0Group": tmnxSysFwdPathOptsV21v0Group,
       "tmnxSysBofV21v0Group": tmnxSysBofV21v0Group,
       "tmnxSysFpResAllocV21v0Group": tmnxSysFpResAllocV21v0Group,
       "tmnxSysFpResAllocPoolV21v0Group": tmnxSysFpResAllocPoolV21v0Group,
       "tmnxSysMgmtIfComHistoryV21v0Grp": tmnxSysMgmtIfComHistoryV21v0Grp,
       "tmnxSysFpResAllocFecV21v0Group": tmnxSysFpResAllocFecV21v0Group,
       "tmnxSysGrpcTunnelV21v0Group": tmnxSysGrpcTunnelV21v0Group,
       "tmnxSysV22v0Groups": tmnxSysV22v0Groups,
       "tmnxSysFwdPathOptsV22v0Group": tmnxSysFwdPathOptsV22v0Group,
       "tmnxSysNotificationV22v0Group": tmnxSysNotificationV22v0Group,
       "tmnxSysFpLpmResAlcnV22v0Group": tmnxSysFpLpmResAlcnV22v0Group,
       "tmnxSysFanControlV22v0Group": tmnxSysFanControlV22v0Group,
       "tmnxSysRemoteMgmtV22v0Group": tmnxSysRemoteMgmtV22v0Group,
       "tmnxSysRemoteMgmtObsoleteGroup": tmnxSysRemoteMgmtObsoleteGroup,
       "tmnxSysFpOptsV22v0ObsoleteGroup": tmnxSysFpOptsV22v0ObsoleteGroup,
       "tmnxSysFpResMacFltrObsoleteGroup": tmnxSysFpResMacFltrObsoleteGroup,
       "tmnxSysMGGroups": tmnxSysMGGroups,
       "tmnxSysMGCompliances": tmnxSysMGCompliances,
       "tmnxSysDCCompliance": tmnxSysDCCompliance,
       "tmnxSysDCGroups": tmnxSysDCGroups,
       "tmnxSysNspProxyCompliances": tmnxSysNspProxyCompliances,
       "tmnxSysNspProxyGroups": tmnxSysNspProxyGroups,
       "tmnxSysObjs": tmnxSysObjs,
       "sysGenInfo": sysGenInfo,
       "sgiCpuUsage": sgiCpuUsage,
       "sgiMemoryUsed": sgiMemoryUsed,
       "sgiMemoryAvailable": sgiMemoryAvailable,
       "sgiMemoryPoolAllocated": sgiMemoryPoolAllocated,
       "sgiSwMajorVersion": sgiSwMajorVersion,
       "sgiSwMinorVersion": sgiSwMinorVersion,
       "sgiSwVersionModifier": sgiSwVersionModifier,
       "sgiSnmpInGetBulks": sgiSnmpInGetBulks,
       "sgiKbMemoryUsed": sgiKbMemoryUsed,
       "sgiKbMemoryAvailable": sgiKbMemoryAvailable,
       "sgiKbMemoryPoolAllocated": sgiKbMemoryPoolAllocated,
       "tmnxSysCpuMonTable": tmnxSysCpuMonTable,
       "tmnxSysCpuMonEntry": tmnxSysCpuMonEntry,
       "tmnxSysCpuMonSampleTime": tmnxSysCpuMonSampleTime,
       "tmnxSysCpuMonCpuIdle": tmnxSysCpuMonCpuIdle,
       "tmnxSysCpuMonBusyCoreUtil": tmnxSysCpuMonBusyCoreUtil,
       "tmnxSysCpuMonBusyGroupName": tmnxSysCpuMonBusyGroupName,
       "tmnxSysCpuMonBusyGroupUtil": tmnxSysCpuMonBusyGroupUtil,
       "sgiGroupingIDs": sgiGroupingIDs,
       "sgiSystemGroupID": sgiSystemGroupID,
       "sgiSystemSubGroupID": sgiSystemSubGroupID,
       "sgiSnmpFailedSets": sgiSnmpFailedSets,
       "sgiCryptoModVersion": sgiCryptoModVersion,
       "sysTimeInfo": sysTimeInfo,
       "stiDateAndTime": stiDateAndTime,
       "stiActiveZone": stiActiveZone,
       "stiHoursOffset": stiHoursOffset,
       "stiMinutesOffset": stiMinutesOffset,
       "stiZoneType": stiZoneType,
       "stiSummerZoneTable": stiSummerZoneTable,
       "stiSummerZoneEntry": stiSummerZoneEntry,
       "stiSummerZoneName": stiSummerZoneName,
       "stiSummerZoneRowStatus": stiSummerZoneRowStatus,
       "stiSummerZoneStartDate": stiSummerZoneStartDate,
       "stiSummerZoneEndDate": stiSummerZoneEndDate,
       "stiSummerZoneOffset": stiSummerZoneOffset,
       "stiSummerZoneStartDay": stiSummerZoneStartDay,
       "stiSummerZoneStartWeek": stiSummerZoneStartWeek,
       "stiSummerZoneStartMonth": stiSummerZoneStartMonth,
       "stiSummerZoneStartHour": stiSummerZoneStartHour,
       "stiSummerZoneStartMinute": stiSummerZoneStartMinute,
       "stiSummerZoneEndDay": stiSummerZoneEndDay,
       "stiSummerZoneEndWeek": stiSummerZoneEndWeek,
       "stiSummerZoneEndMonth": stiSummerZoneEndMonth,
       "stiSummerZoneEndHour": stiSummerZoneEndHour,
       "stiSummerZoneEndMinute": stiSummerZoneEndMinute,
       "stiPreferLocalTime": stiPreferLocalTime,
       "sysSntpInfo": sysSntpInfo,
       "sntpState": sntpState,
       "sntpServerTable": sntpServerTable,
       "sntpServerEntry": sntpServerEntry,
       "sntpServerAddress": sntpServerAddress,
       "sntpServerRowStatus": sntpServerRowStatus,
       "sntpServerVersion": sntpServerVersion,
       "sntpServerPreference": sntpServerPreference,
       "sntpServerInterval": sntpServerInterval,
       "sntpAdminState": sntpAdminState,
       "sntpOperStatus": sntpOperStatus,
       "sysSyncInfo": sysSyncInfo,
       "ssiSaveConfig": ssiSaveConfig,
       "ssiSyncMode": ssiSyncMode,
       "ssiSyncForce": ssiSyncForce,
       "ssiSyncStatus": ssiSyncStatus,
       "ssiSyncConfigLastTime": ssiSyncConfigLastTime,
       "ssiSyncBootEnvLastTime": ssiSyncBootEnvLastTime,
       "ssiConfigMaxBackupRevisions": ssiConfigMaxBackupRevisions,
       "ssiSaveConfigResult": ssiSaveConfigResult,
       "ssiSaveBof": ssiSaveBof,
       "ssiSaveBofResult": ssiSaveBofResult,
       "ssiSaveConfigDest": ssiSaveConfigDest,
       "ssiSaveConfigDetail": ssiSaveConfigDetail,
       "ssiRedFailoverTime": ssiRedFailoverTime,
       "ssiRedFailoverReason": ssiRedFailoverReason,
       "ssiSyncRollbackLastTime": ssiSyncRollbackLastTime,
       "ssiSyncRollbackMode": ssiSyncRollbackMode,
       "ssiSyncRollbackForce": ssiSyncRollbackForce,
       "ssiSyncRollbackStatus": ssiSyncRollbackStatus,
       "ssiSyncCertLastTime": ssiSyncCertLastTime,
       "ssiSyncCertMode": ssiSyncCertMode,
       "ssiSyncCertForce": ssiSyncCertForce,
       "ssiSyncCertStatus": ssiSyncCertStatus,
       "sysBootInfo": sysBootInfo,
       "sbiConfigStatus": sbiConfigStatus,
       "sbiPersistStatus": sbiPersistStatus,
       "sbiPersistIndex": sbiPersistIndex,
       "sbiSnmpdAdminStatus": sbiSnmpdAdminStatus,
       "sbiSnmpdOperStatus": sbiSnmpdOperStatus,
       "sbiSnmpdMaxPktSize": sbiSnmpdMaxPktSize,
       "sbiSnmpdPortNum": sbiSnmpdPortNum,
       "sbiBootConfigOKScript": sbiBootConfigOKScript,
       "sbiConfigOKScriptStatus": sbiConfigOKScriptStatus,
       "sbiBootConfigFailScript": sbiBootConfigFailScript,
       "sbiConfigFailScriptStatus": sbiConfigFailScriptStatus,
       "sbiRedSwitchoverScript": sbiRedSwitchoverScript,
       "sbiRedSwitchoverScriptStatus": sbiRedSwitchoverScriptStatus,
       "sbiAllowBootLicenseViolations": sbiAllowBootLicenseViolations,
       "sysRadiusInfo": sysRadiusInfo,
       "radiusOperStatus": radiusOperStatus,
       "radiusServerTable": radiusServerTable,
       "radiusServerEntry": radiusServerEntry,
       "radiusServerIndex": radiusServerIndex,
       "radiusServerAddress": radiusServerAddress,
       "radiusServerOperStatus": radiusServerOperStatus,
       "radiusServerInetAddressType": radiusServerInetAddressType,
       "radiusServerInetAddress": radiusServerInetAddress,
       "tmnxSysNotifyObjs": tmnxSysNotifyObjs,
       "tmnxNotifyRow": tmnxNotifyRow,
       "tmnxNotifyRowAdminState": tmnxNotifyRowAdminState,
       "tmnxNotifyRowOperState": tmnxNotifyRowOperState,
       "tmnxMemoryModule": tmnxMemoryModule,
       "tmnxModuleMallocSize": tmnxModuleMallocSize,
       "tmnxDroppedTrapID": tmnxDroppedTrapID,
       "tmnxTrapDroppedReasonCode": tmnxTrapDroppedReasonCode,
       "tmnxTrapDroppedEntryID": tmnxTrapDroppedEntryID,
       "tmnxNotifyEntryOID": tmnxNotifyEntryOID,
       "tmnxSnmpdErrorMsg": tmnxSnmpdErrorMsg,
       "tmnxPersistencyClient": tmnxPersistencyClient,
       "tmnxPersistencyFileLocator": tmnxPersistencyFileLocator,
       "tmnxPersistencyNotifyMsg": tmnxPersistencyNotifyMsg,
       "tmnxPersistenceAffectedCpm": tmnxPersistenceAffectedCpm,
       "tmnxSysTimeSetBy": tmnxSysTimeSetBy,
       "tmnxFtpFailureMsg": tmnxFtpFailureMsg,
       "tmnxFtpFailureDestAddressType": tmnxFtpFailureDestAddressType,
       "tmnxFtpFailureDestAddress": tmnxFtpFailureDestAddress,
       "tmnxNotifyObjectName": tmnxNotifyObjectName,
       "tmnxSyncFailureReason": tmnxSyncFailureReason,
       "tmnxSysExecScript": tmnxSysExecScript,
       "tmnxSysExecResult": tmnxSysExecResult,
       "tmnxSysRollbackFileType": tmnxSysRollbackFileType,
       "tmnxSysFileErrorType": tmnxSysFileErrorType,
       "tmnxTrapDroppedCount": tmnxTrapDroppedCount,
       "tmnxSysDNSSecDomainName": tmnxSysDNSSecDomainName,
       "tmnxSysLicenseErrorReason": tmnxSysLicenseErrorReason,
       "tmnxSysLicenseTimeLeft": tmnxSysLicenseTimeLeft,
       "tmnxSysNotifVsdServerName": tmnxSysNotifVsdServerName,
       "tmnxSysNotifXmppServerName": tmnxSysNotifXmppServerName,
       "tmnxSysLicenseErrorAction": tmnxSysLicenseErrorAction,
       "tmnxSysNotifAppStatsApplication": tmnxSysNotifAppStatsApplication,
       "tmnxSysNotifAppStatsType": tmnxSysNotifAppStatsType,
       "tmnxSysNotifAppStatsTime": tmnxSysNotifAppStatsTime,
       "tmnxNotifySysMgmtIfOriginalMode": tmnxNotifySysMgmtIfOriginalMode,
       "tmnxSysLicensingNotifyGroup": tmnxSysLicensingNotifyGroup,
       "tmnxSysLicensedNotifyAppName": tmnxSysLicensedNotifyAppName,
       "tmnxPrimaryConfigFileFormatType": tmnxPrimaryConfigFileFormatType,
       "tmnxLiConfigFileFormatType": tmnxLiConfigFileFormatType,
       "sysLoginControlInfo": sysLoginControlInfo,
       "slcFtpInboundMaxSessions": slcFtpInboundMaxSessions,
       "slcTelnetInboundMaxSessions": slcTelnetInboundMaxSessions,
       "slcTelnetOutboundMaxSessions": slcTelnetOutboundMaxSessions,
       "slcPreLoginMessage": slcPreLoginMessage,
       "slcPreLoginMessageInclName": slcPreLoginMessageInclName,
       "slcMessageOfTheDay": slcMessageOfTheDay,
       "slcMessageOfTheDayType": slcMessageOfTheDayType,
       "slcLoginBanner": slcLoginBanner,
       "slcLoginExponentialBackOff": slcLoginExponentialBackOff,
       "slcTelnetGracefulShutdown": slcTelnetGracefulShutdown,
       "slcSSHGracefulShutdown": slcSSHGracefulShutdown,
       "slcTelnetMinTTLValue": slcTelnetMinTTLValue,
       "slcSSHMinTTLValue": slcSSHMinTTLValue,
       "slcSSHInboundMaxSessions": slcSSHInboundMaxSessions,
       "slcSSHOutboundMaxSessions": slcSSHOutboundMaxSessions,
       "slcIdleTimeout": slcIdleTimeout,
       "slcLoginScriptGlobal": slcLoginScriptGlobal,
       "slcLoginScriptPerUserDirectory": slcLoginScriptPerUserDirectory,
       "slcLoginScriptPerUserFilename": slcLoginScriptPerUserFilename,
       "sysLACPInfo": sysLACPInfo,
       "sysLACPSystemPriority": sysLACPSystemPriority,
       "sysTacplusInfo": sysTacplusInfo,
       "tacplusOperStatus": tacplusOperStatus,
       "tacplusServerTable": tacplusServerTable,
       "tacplusServerEntry": tacplusServerEntry,
       "tacplusServerIndex": tacplusServerIndex,
       "tacplusServerAddress": tacplusServerAddress,
       "tacplusServerOperStatus": tacplusServerOperStatus,
       "tacPlusServerInetAddressType": tacPlusServerInetAddressType,
       "tacPlusServerInetAddress": tacPlusServerInetAddress,
       "sysBofInfo": sysBofInfo,
       "sbiActiveIpAddr": sbiActiveIpAddr,
       "sbiActiveIpMask": sbiActiveIpMask,
       "sbiStandbyIpAddr": sbiStandbyIpAddr,
       "sbiStandbyIpMask": sbiStandbyIpMask,
       "sbiPrimaryImage": sbiPrimaryImage,
       "sbiSecondaryImage": sbiSecondaryImage,
       "sbiTertiaryImage": sbiTertiaryImage,
       "sbiPrimaryConfigFile": sbiPrimaryConfigFile,
       "sbiSecondaryConfigFile": sbiSecondaryConfigFile,
       "sbiTertiaryConfigFile": sbiTertiaryConfigFile,
       "sbiPersist": sbiPersist,
       "sbiConsoleSpeed": sbiConsoleSpeed,
       "sbiAutoNegotiate": sbiAutoNegotiate,
       "sbiSpeed": sbiSpeed,
       "sbiDuplex": sbiDuplex,
       "sbiPrimaryDns": sbiPrimaryDns,
       "sbiSecondaryDns": sbiSecondaryDns,
       "sbiTertiaryDns": sbiTertiaryDns,
       "sbiDnsDomain": sbiDnsDomain,
       "sbiWait": sbiWait,
       "sbiStaticRouteTable": sbiStaticRouteTable,
       "sbiStaticRouteEntry": sbiStaticRouteEntry,
       "sbiStaticRouteDest": sbiStaticRouteDest,
       "sbiStaticRouteMask": sbiStaticRouteMask,
       "sbiStaticRouteNextHop": sbiStaticRouteNextHop,
       "sbiStaticRouteRowStatus": sbiStaticRouteRowStatus,
       "sbiActiveIPv6Addr": sbiActiveIPv6Addr,
       "sbiActiveIPv6PfxLen": sbiActiveIPv6PfxLen,
       "sbiStandbyIPv6Addr": sbiStandbyIPv6Addr,
       "sbiStandbyIPv6PfxLen": sbiStandbyIPv6PfxLen,
       "sbiPrimaryDnsIPv6Addr": sbiPrimaryDnsIPv6Addr,
       "sbiSecondaryDnsIPv6Addr": sbiSecondaryDnsIPv6Addr,
       "sbiTertiaryDnsIPv6Addr": sbiTertiaryDnsIPv6Addr,
       "sbiStaticRouteIPv6Table": sbiStaticRouteIPv6Table,
       "sbiStaticRouteIPv6Entry": sbiStaticRouteIPv6Entry,
       "sbiStaticRouteIPv6Dest": sbiStaticRouteIPv6Dest,
       "sbiStaticRouteIPv6PfxLen": sbiStaticRouteIPv6PfxLen,
       "sbiStaticRouteIPv6NextHop": sbiStaticRouteIPv6NextHop,
       "sbiStaticRouteIPv6RowStatus": sbiStaticRouteIPv6RowStatus,
       "sbiLiSeparate": sbiLiSeparate,
       "sbiLiLocalSave": sbiLiLocalSave,
       "sbiLicenseFile": sbiLicenseFile,
       "sbiFips1402Level1": sbiFips1402Level1,
       "sbiSystemBaseMacAddress": sbiSystemBaseMacAddress,
       "sbiEssSystemType": sbiEssSystemType,
       "sbiSystemProfile": sbiSystemProfile,
       "sbiAutoBoot": sbiAutoBoot,
       "sbiAutoBootClientId": sbiAutoBootClientId,
       "sbiAutoBootClientIdType": sbiAutoBootClientIdType,
       "sbiAutoBootUsingMgmt": sbiAutoBootUsingMgmt,
       "sbiAutoBootUsingInband": sbiAutoBootUsingInband,
       "sbiAutoBootInbandVlan": sbiAutoBootInbandVlan,
       "sbiAutoBootUsingIpv4": sbiAutoBootUsingIpv4,
       "sbiAutoBootUsingIpv6": sbiAutoBootUsingIpv6,
       "sbiAutoBootIncludeUserClass": sbiAutoBootIncludeUserClass,
       "sbiAutoBootVlanDiscovery": sbiAutoBootVlanDiscovery,
       "sbiAutoBootMode": sbiAutoBootMode,
       "sbiAutoBootInfo": sbiAutoBootInfo,
       "sbiAutoBootPortMtu": sbiAutoBootPortMtu,
       "sbiAutoBootOspf": sbiAutoBootOspf,
       "sbiAutoBootOspfNeid": sbiAutoBootOspfNeid,
       "sbiAutoBootOspfVendorId": sbiAutoBootOspfVendorId,
       "sbiAutoBootOspfNeipV4Type": sbiAutoBootOspfNeipV4Type,
       "sbiAutoBootOspfNeipV4": sbiAutoBootOspfNeipV4,
       "sbiAutoBootOspfNeipV6Type": sbiAutoBootOspfNeipV6Type,
       "sbiAutoBootOspfNeipV6": sbiAutoBootOspfNeipV6,
       "sbiAutoBootOspfMtu": sbiAutoBootOspfMtu,
       "sbiAutoConfigure": sbiAutoConfigure,
       "sbiAutoIpv4": sbiAutoIpv4,
       "sbiAutoIpv4Dhcp": sbiAutoIpv4Dhcp,
       "sbiAutoIpv4DhcpClientIdType": sbiAutoIpv4DhcpClientIdType,
       "sbiAutoIpv4DhcpClientId": sbiAutoIpv4DhcpClientId,
       "sbiAutoIpv4DhcpOptUserClass": sbiAutoIpv4DhcpOptUserClass,
       "sbiAutoIpv4DhcpTimeout": sbiAutoIpv4DhcpTimeout,
       "sbiAutoIpv6": sbiAutoIpv6,
       "sbiAutoIpv6Dhcp": sbiAutoIpv6Dhcp,
       "sbiAutoIpv6DhcpClientIdType": sbiAutoIpv6DhcpClientIdType,
       "sbiAutoIpv6DhcpClientIdDuidType": sbiAutoIpv6DhcpClientIdDuidType,
       "sbiAutoIpv6DhcpClientIdDuid": sbiAutoIpv6DhcpClientIdDuid,
       "sbiAutoIpv6DhcpOptUserClass": sbiAutoIpv6DhcpOptUserClass,
       "sbiAutoIpv6DhcpTimeout": sbiAutoIpv6DhcpTimeout,
       "sbiStandbyAIpAddr": sbiStandbyAIpAddr,
       "sbiStandbyAIpMask": sbiStandbyAIpMask,
       "sbiStandbyAIPv6Addr": sbiStandbyAIPv6Addr,
       "sbiStandbyAIPv6PfxLen": sbiStandbyAIPv6PfxLen,
       "sbiStandbyBIpAddr": sbiStandbyBIpAddr,
       "sbiStandbyBIpMask": sbiStandbyBIpMask,
       "sbiStandbyBIPv6Addr": sbiStandbyBIPv6Addr,
       "sbiStandbyBIPv6PfxLen": sbiStandbyBIPv6PfxLen,
       "sbiStandbyCIpAddr": sbiStandbyCIpAddr,
       "sbiStandbyCIpMask": sbiStandbyCIpMask,
       "sbiStandbyCIPv6Addr": sbiStandbyCIPv6Addr,
       "sbiStandbyCIPv6PfxLen": sbiStandbyCIPv6PfxLen,
       "sbiStandbyDIpAddr": sbiStandbyDIpAddr,
       "sbiStandbyDIpMask": sbiStandbyDIpMask,
       "sbiStandbyDIPv6Addr": sbiStandbyDIPv6Addr,
       "sbiStandbyDIPv6PfxLen": sbiStandbyDIPv6PfxLen,
       "sbiMgmtIfIpMtu": sbiMgmtIfIpMtu,
       "sysPersistenceInfo": sysPersistenceInfo,
       "sysPersistenceDhcpL2Info": sysPersistenceDhcpL2Info,
       "spiDhcpL2PersistenceFileLocation": spiDhcpL2PersistenceFileLocation,
       "spiDhcpL2PersistenceDescription": spiDhcpL2PersistenceDescription,
       "sysPersistenceDhcpL3Info": sysPersistenceDhcpL3Info,
       "spiDhcpL3PersistenceFileLocation": spiDhcpL3PersistenceFileLocation,
       "spiDhcpL3PersistenceDescription": spiDhcpL3PersistenceDescription,
       "sysPersistenceSubMgmtInfo": sysPersistenceSubMgmtInfo,
       "spiSubMgmtPersistenceFileLocation": spiSubMgmtPersistenceFileLocation,
       "spiSubMgmtPersistenceDescription": spiSubMgmtPersistenceDescription,
       "sysPersistenceDhcpSrvInfo": sysPersistenceDhcpSrvInfo,
       "spiDhcpSrvPersistenceFileLoc": spiDhcpSrvPersistenceFileLoc,
       "spiDhcpSrvPersistenceDescr": spiDhcpSrvPersistenceDescr,
       "sysPersistenceNatInfo": sysPersistenceNatInfo,
       "spiNatFwdPersistenceFileLoc": spiNatFwdPersistenceFileLoc,
       "spiNatFwdPersistenceDescr": spiNatFwdPersistenceDescr,
       "sysPersistenceAAInfo": sysPersistenceAAInfo,
       "spiAAPersistenceFileLoc": spiAAPersistenceFileLoc,
       "spiAAPersistenceDescr": spiAAPersistenceDescr,
       "sysPersistenceAncpInfo": sysPersistenceAncpInfo,
       "spiAncpPersistenceFileLoc": spiAncpPersistenceFileLoc,
       "spiAncpPersistenceDescr": spiAncpPersistenceDescr,
       "sysPersistencePythonInfo": sysPersistencePythonInfo,
       "spiPythonPersistenceFileLoc": spiPythonPersistenceFileLoc,
       "spiPythonPersistenceDescr": spiPythonPersistenceDescr,
       "tmnxDhcpLeaseTimeModeThreshold": tmnxDhcpLeaseTimeModeThreshold,
       "sysLiInfo": sysLiInfo,
       "sliConfigStatus": sliConfigStatus,
       "sliSaveConfig": sliSaveConfig,
       "sliSaveConfigResult": sliSaveConfigResult,
       "sliConfigLastModified": sliConfigLastModified,
       "sliConfigLastSaved": sliConfigLastSaved,
       "sliFilterLock": sliFilterLock,
       "sysDNSInfo": sysDNSInfo,
       "sysDNSInfoLastChanged": sysDNSInfoLastChanged,
       "sysDNSAddressResolvePref": sysDNSAddressResolvePref,
       "sysDNSSecAdValidation": sysDNSSecAdValidation,
       "sysDNSSecRespCtrl": sysDNSSecRespCtrl,
       "sysIcmpVSInfo": sysIcmpVSInfo,
       "sysIcmpVSEnhancement": sysIcmpVSEnhancement,
       "sysEthInfo": sysEthInfo,
       "sysNewQinqUntaggedSap": sysNewQinqUntaggedSap,
       "tmnxSysRollbackInfo": tmnxSysRollbackInfo,
       "tmnxSysRollbackIndex": tmnxSysRollbackIndex,
       "tmnxSysRollbackStart": tmnxSysRollbackStart,
       "tmnxSysRollbackResult": tmnxSysRollbackResult,
       "tmnxSysRollbackSave": tmnxSysRollbackSave,
       "tmnxSysRollbackSaveResult": tmnxSysRollbackSaveResult,
       "tmnxSysRollbackLocation": tmnxSysRollbackLocation,
       "tmnxSysRollbackRevertIndex": tmnxSysRollbackRevertIndex,
       "tmnxSysRollbackRevertEndTime": tmnxSysRollbackRevertEndTime,
       "tmnxSysRollbackSavedTime": tmnxSysRollbackSavedTime,
       "tmnxSysRollbackRevertStartTime": tmnxSysRollbackRevertStartTime,
       "tmnxSysRollbackRevertUserName": tmnxSysRollbackRevertUserName,
       "tmnxSysRollbackRevertFilename": tmnxSysRollbackRevertFilename,
       "tmnxSysRollbackSaveComment": tmnxSysRollbackSaveComment,
       "tmnxSysRollbackFileDelete": tmnxSysRollbackFileDelete,
       "tmnxSysRollbackFileDeleteResult": tmnxSysRollbackFileDeleteResult,
       "tmnxSysRollbackAbortRevert": tmnxSysRollbackAbortRevert,
       "tmnxSysRollbackRescueLocation": tmnxSysRollbackRescueLocation,
       "tmnxSysRollbackRescueRevert": tmnxSysRollbackRescueRevert,
       "tmnxSysRollbackRescueSave": tmnxSysRollbackRescueSave,
       "tmnxSysRollbackRescueDelete": tmnxSysRollbackRescueDelete,
       "tmnxSysRollbackRescueSaveRes": tmnxSysRollbackRescueSaveRes,
       "tmnxSysRollbackRescueRevertRes": tmnxSysRollbackRescueRevertRes,
       "tmnxSysRollbackRescueDeleteRes": tmnxSysRollbackRescueDeleteRes,
       "tmnxSysRollbackRescueSavedTime": tmnxSysRollbackRescueSavedTime,
       "tmnxSysRollbackRescueRevStTime": tmnxSysRollbackRescueRevStTime,
       "tmnxSysRollbackRescueRevEdTime": tmnxSysRollbackRescueRevEdTime,
       "tmnxSysRollbackRescueRevUser": tmnxSysRollbackRescueRevUser,
       "tmnxSysRollbackRescueSaveComment": tmnxSysRollbackRescueSaveComment,
       "tmnxSysRollbackRescueAbortRevert": tmnxSysRollbackRescueAbortRevert,
       "tmnxSysRollbackRescueFileExists": tmnxSysRollbackRescueFileExists,
       "tmnxSysRollbackMaxLocalFiles": tmnxSysRollbackMaxLocalFiles,
       "tmnxSysRollbackMaxRemoteFiles": tmnxSysRollbackMaxRemoteFiles,
       "tmnxSysRollbackTableLastChanged": tmnxSysRollbackTableLastChanged,
       "tmnxSysRollbackFileTable": tmnxSysRollbackFileTable,
       "tmnxSysRollbackFileEntry": tmnxSysRollbackFileEntry,
       "tmnxSysRollbackFileIndex": tmnxSysRollbackFileIndex,
       "tmnxSysRollbackFileCreationTime": tmnxSysRollbackFileCreationTime,
       "tmnxSysRollbackFileComment": tmnxSysRollbackFileComment,
       "tmnxSysRollbackFileUserName": tmnxSysRollbackFileUserName,
       "tmnxSysRollbackFileVersion": tmnxSysRollbackFileVersion,
       "sysBootedBofInfo": sysBootedBofInfo,
       "sbbiLiSeparate": sbbiLiSeparate,
       "sbbiLiLocalSave": sbbiLiLocalSave,
       "sbbiEncryptConfig": sbbiEncryptConfig,
       "sysMGMCSwitchOverInfo": sysMGMCSwitchOverInfo,
       "tmnxSysCandidateCfgInfo": tmnxSysCandidateCfgInfo,
       "tmnxSysCandidateCfgState": tmnxSysCandidateCfgState,
       "tmnxSysCandidateCfgEditors": tmnxSysCandidateCfgEditors,
       "tmnxSysCandidateCfgCommitState": tmnxSysCandidateCfgCommitState,
       "tmnxSysCandidateCfgCommitTime": tmnxSysCandidateCfgCommitTime,
       "tmnxSysCandidateCfgRevertTime": tmnxSysCandidateCfgRevertTime,
       "tmnxSysCandidateCfgChckptCreated": tmnxSysCandidateCfgChckptCreated,
       "tmnxSysCandidateCfgUser": tmnxSysCandidateCfgUser,
       "tmnxSysCandidateCfgExclusiveUsr": tmnxSysCandidateCfgExclusiveUsr,
       "tmnxSysNetconfInfo": tmnxSysNetconfInfo,
       "tmnxSysNetconfAdminStatus": tmnxSysNetconfAdminStatus,
       "tmnxSysNetconfOperStatus": tmnxSysNetconfOperStatus,
       "tmnxSysNetconfRequests": tmnxSysNetconfRequests,
       "tmnxSysNetconfGetRequests": tmnxSysNetconfGetRequests,
       "tmnxSysNetconfGetConfigRequests": tmnxSysNetconfGetConfigRequests,
       "tmnxSysNetconfEditConfigRequests": tmnxSysNetconfEditConfigRequests,
       "tmnxSysNetconfCloseRequests": tmnxSysNetconfCloseRequests,
       "tmnxSysNetconfKillRequests": tmnxSysNetconfKillRequests,
       "tmnxSysNetconfResponses": tmnxSysNetconfResponses,
       "tmnxSysNetconfErrorResponses": tmnxSysNetconfErrorResponses,
       "tmnxSysNetconfCopyConfigRequests": tmnxSysNetconfCopyConfigRequests,
       "tmnxSysNetconfDelConfigRequests": tmnxSysNetconfDelConfigRequests,
       "tmnxSysNetconfValidateRequests": tmnxSysNetconfValidateRequests,
       "tmnxSysNetconfFailedEditCfgReqs": tmnxSysNetconfFailedEditCfgReqs,
       "tmnxSysNetconfFailedLockReqs": tmnxSysNetconfFailedLockReqs,
       "tmnxSysNetconfLockRequests": tmnxSysNetconfLockRequests,
       "tmnxSysNetconfUnlockRequests": tmnxSysNetconfUnlockRequests,
       "tmnxSysNetconfCommitRequests": tmnxSysNetconfCommitRequests,
       "tmnxSysNetconfDiscardRequests": tmnxSysNetconfDiscardRequests,
       "tmnxSysNetconfCapCandidateCfg": tmnxSysNetconfCapCandidateCfg,
       "tmnxSysNetconfCapRunningCfg": tmnxSysNetconfCapRunningCfg,
       "tmnxSysNetconfYangBaseR13": tmnxSysNetconfYangBaseR13,
       "tmnxSysNetconfYangNokia": tmnxSysNetconfYangNokia,
       "tmnxSysNetconfCreateSubRequests": tmnxSysNetconfCreateSubRequests,
       "tmnxSysNetconfAutoCfgSave": tmnxSysNetconfAutoCfgSave,
       "tmnxSysNetconfPort": tmnxSysNetconfPort,
       "tmnxSysNetconfGetSchemaRequests": tmnxSysNetconfGetSchemaRequests,
       "tmnxSysNetconfGetDataRequests": tmnxSysNetconfGetDataRequests,
       "tmnxSysNetconfActionRequests": tmnxSysNetconfActionRequests,
       "tmnxDCSysObjs": tmnxDCSysObjs,
       "tmnxSysStrmInfo": tmnxSysStrmInfo,
       "tmnxSysStrmAdminStatus": tmnxSysStrmAdminStatus,
       "tmnxSysStrmDumpSnmpRequests": tmnxSysStrmDumpSnmpRequests,
       "tmnxSysStrmGetManyRequests": tmnxSysStrmGetManyRequests,
       "tmnxSysStrmResponses": tmnxSysStrmResponses,
       "tmnxSysXmppInfo": tmnxSysXmppInfo,
       "tmnxSysXmppServerTable": tmnxSysXmppServerTable,
       "tmnxSysXmppServerEntry": tmnxSysXmppServerEntry,
       "tmnxSysXmppServName": tmnxSysXmppServName,
       "tmnxSysXmppServFQDN": tmnxSysXmppServFQDN,
       "tmnxSysXmppServRowStatus": tmnxSysXmppServRowStatus,
       "tmnxSysXmppServUserName": tmnxSysXmppServUserName,
       "tmnxSysXmppServPassword": tmnxSysXmppServPassword,
       "tmnxSysXmppServLastChanged": tmnxSysXmppServLastChanged,
       "tmnxSysXmppServUptime": tmnxSysXmppServUptime,
       "tmnxSysXmppServIQSent": tmnxSysXmppServIQSent,
       "tmnxSysXmppServIQRcvd": tmnxSysXmppServIQRcvd,
       "tmnxSysXmppServIQError": tmnxSysXmppServIQError,
       "tmnxSysXmppServIQTimedOut": tmnxSysXmppServIQTimedOut,
       "tmnxSysXmppServIQAckRcvd": tmnxSysXmppServIQAckRcvd,
       "tmnxSysXmppServIQMinRtt": tmnxSysXmppServIQMinRtt,
       "tmnxSysXmppServIQMaxRtt": tmnxSysXmppServIQMaxRtt,
       "tmnxSysXmppServVsdUpdatesRcvd": tmnxSysXmppServVsdUpdatesRcvd,
       "tmnxSysXmppServUpdatesRcvd": tmnxSysXmppServUpdatesRcvd,
       "tmnxSysXmppServMsgSent": tmnxSysXmppServMsgSent,
       "tmnxSysXmppServMsgRcvd": tmnxSysXmppServMsgRcvd,
       "tmnxSysXmppServMsgAckRcvd": tmnxSysXmppServMsgAckRcvd,
       "tmnxSysXmppServMsgError": tmnxSysXmppServMsgError,
       "tmnxSysXmppServMsgTimedOut": tmnxSysXmppServMsgTimedOut,
       "tmnxSysXmppServMsgMinRtt": tmnxSysXmppServMsgMinRtt,
       "tmnxSysXmppServMsgMaxRtt": tmnxSysXmppServMsgMaxRtt,
       "tmnxSysXmppServSubSent": tmnxSysXmppServSubSent,
       "tmnxSysXmppServUnSubSent": tmnxSysXmppServUnSubSent,
       "tmnxSysXmppServState": tmnxSysXmppServState,
       "tmnxSysXmppServAdminState": tmnxSysXmppServAdminState,
       "tmnxSysXmppServOperUserName": tmnxSysXmppServOperUserName,
       "tmnxSysXmppServAuthType": tmnxSysXmppServAuthType,
       "tmnxSysXmppServConnMode": tmnxSysXmppServConnMode,
       "tmnxSysXmppServServiceId": tmnxSysXmppServServiceId,
       "tmnxSysXmppServRouterId": tmnxSysXmppServRouterId,
       "tmnxSysVsdServerTable": tmnxSysVsdServerTable,
       "tmnxSysVsdServerEntry": tmnxSysVsdServerEntry,
       "tmnxSysVsdServerInstance": tmnxSysVsdServerInstance,
       "tmnxSysVsdServUptime": tmnxSysVsdServUptime,
       "tmnxSysVsdServUserName": tmnxSysVsdServUserName,
       "tmnxSysVsdServerStatus": tmnxSysVsdServerStatus,
       "tmnxSysVsdServMsgSent": tmnxSysVsdServMsgSent,
       "tmnxSysVsdServMsgRcvd": tmnxSysVsdServMsgRcvd,
       "tmnxSysVsdServMsgAckRcvd": tmnxSysVsdServMsgAckRcvd,
       "tmnxSysVsdServMsgError": tmnxSysVsdServMsgError,
       "tmnxSysVsdServMsgTimedOut": tmnxSysVsdServMsgTimedOut,
       "tmnxSysVsdServMsgMinRtt": tmnxSysVsdServMsgMinRtt,
       "tmnxSysVsdServMsgMaxRtt": tmnxSysVsdServMsgMaxRtt,
       "tmnxSysResInfo": tmnxSysResInfo,
       "tmnxSysResCardInfo": tmnxSysResCardInfo,
       "tmnxCardCpuResMonitorTable": tmnxCardCpuResMonitorTable,
       "tmnxCardCpuResMonitorEntry": tmnxCardCpuResMonitorEntry,
       "tmnxCardResourceSlotNum": tmnxCardResourceSlotNum,
       "tmnxCardCpuResSampleTime": tmnxCardCpuResSampleTime,
       "tmnxCardCpuResMonCpuIdle": tmnxCardCpuResMonCpuIdle,
       "tmnxCardCpuResMonBusyCoreUtil": tmnxCardCpuResMonBusyCoreUtil,
       "tmnxCardCpuResMonBusyGroupName": tmnxCardCpuResMonBusyGroupName,
       "tmnxCardCpuResMonBusyGroupUtil": tmnxCardCpuResMonBusyGroupUtil,
       "tmnxCardMemResMonitorTable": tmnxCardMemResMonitorTable,
       "tmnxCardMemResMonitorEntry": tmnxCardMemResMonitorEntry,
       "tmnxCardMemResMemoryUsed": tmnxCardMemResMemoryUsed,
       "tmnxCardMemResMemoryAvailable": tmnxCardMemResMemoryAvailable,
       "tmnxCardMemResPoolsAllocated": tmnxCardMemResPoolsAllocated,
       "tmnxSysResEcmpProfInfo": tmnxSysResEcmpProfInfo,
       "tmnxSysResEcmpProfTable": tmnxSysResEcmpProfTable,
       "tmnxSysResEcmpProfEntry": tmnxSysResEcmpProfEntry,
       "tmnxSysResEcmpProfId": tmnxSysResEcmpProfId,
       "tmnxSysResEcmpProfRowStatus": tmnxSysResEcmpProfRowStatus,
       "tmnxSysResEcmpProfType": tmnxSysResEcmpProfType,
       "tmnxSysResEcmpProfLinksPerGrp": tmnxSysResEcmpProfLinksPerGrp,
       "tmnxSysResEcmpProfNumGrps": tmnxSysResEcmpProfNumGrps,
       "tmnxSysResItCam": tmnxSysResItCam,
       "tmnxSysResItCamBank": tmnxSysResItCamBank,
       "tmnxSysResItCamBankV6Multicast": tmnxSysResItCamBankV6Multicast,
       "tmnxSysFpCam": tmnxSysFpCam,
       "tmnxSysFpCamAllocation": tmnxSysFpCamAllocation,
       "tmnxSysFpCamAllocAdmnV6Multicast": tmnxSysFpCamAllocAdmnV6Multicast,
       "tmnxSysFpCamAllocOperV6Multicast": tmnxSysFpCamAllocOperV6Multicast,
       "tmnxSysFpResAlloc": tmnxSysFpResAlloc,
       "tmnxSysFpResAllocation": tmnxSysFpResAllocation,
       "tmnxSysFpResAllocG8032Sap": tmnxSysFpResAllocG8032Sap,
       "tmnxSysFpResAllocOperG8032Sap": tmnxSysFpResAllocOperG8032Sap,
       "tmnxSysFpResAllocFilterIpv6": tmnxSysFpResAllocFilterIpv6,
       "tmnxSysFpResAllocOperFilterIpv6": tmnxSysFpResAllocOperFilterIpv6,
       "tmnxSysFpResAllocFecSysWdUnpd": tmnxSysFpResAllocFecSysWdUnpd,
       "tmnxSysFpResAllocFecOprSysWdUnpd": tmnxSysFpResAllocFecOprSysWdUnpd,
       "tmnxSysFpResAllocFecSysWdPd": tmnxSysFpResAllocFecSysWdPd,
       "tmnxSysFpResAllocFecOprSysWdPd": tmnxSysFpResAllocFecOprSysWdPd,
       "tmnxSysFpResAllocPoolTable": tmnxSysFpResAllocPoolTable,
       "tmnxSysFpResAllocPoolEntry": tmnxSysFpResAllocPoolEntry,
       "tmnxSysFpRAPoolId": tmnxSysFpRAPoolId,
       "tmnxSysFpRAPoolLgBndRsvMemCnt": tmnxSysFpRAPoolLgBndRsvMemCnt,
       "tmnxSysFpRAPoolOprLgBndRsvMemCnt": tmnxSysFpRAPoolOprLgBndRsvMemCnt,
       "tmnxSysDhcp": tmnxSysDhcp,
       "tmnxSysDhcp6AdvNoaddrsGlobal": tmnxSysDhcp6AdvNoaddrsGlobal,
       "tmnxSysVsdInfo": tmnxSysVsdInfo,
       "tmnxSysVsdSystemId": tmnxSysVsdSystemId,
       "tmnxSysVsdGwPubSubIsSubscrd": tmnxSysVsdGwPubSubIsSubscrd,
       "tmnxSysVsdGwPubSubNodeName": tmnxSysVsdGwPubSubNodeName,
       "tmnxSysVsdGwPubSubLstSubscrdTime": tmnxSysVsdGwPubSubLstSubscrdTime,
       "tmnxSysVsdGwLastAuditTxTime": tmnxSysVsdGwLastAuditTxTime,
       "tmnxSysLicense": tmnxSysLicense,
       "tmnxSysLicenseStatus": tmnxSysLicenseStatus,
       "tmnxSysLicenseName": tmnxSysLicenseName,
       "tmnxSysLicenseUuid": tmnxSysLicenseUuid,
       "tmnxSysLicenseDescription": tmnxSysLicenseDescription,
       "tmnxSysLicenseProduct": tmnxSysLicenseProduct,
       "tmnxSysLicenseSwVersion": tmnxSysLicenseSwVersion,
       "tmnxSysLicenseIssueDateAndTime": tmnxSysLicenseIssueDateAndTime,
       "tmnxSysLicenseStartDateAndTime": tmnxSysLicenseStartDateAndTime,
       "tmnxSysLicenseEndDateAndTime": tmnxSysLicenseEndDateAndTime,
       "tmnxSysLicenseVChassisType": tmnxSysLicenseVChassisType,
       "tmnxSysLicenseMaxNumCPMs": tmnxSysLicenseMaxNumCPMs,
       "tmnxSysLicenseMaxNumIOMs": tmnxSysLicenseMaxNumIOMs,
       "tmnxSysCpmCardLicenseTable": tmnxSysCpmCardLicenseTable,
       "tmnxSysCpmCardLicenseEntry": tmnxSysCpmCardLicenseEntry,
       "tmnxSysCpmCardLicStatus": tmnxSysCpmCardLicStatus,
       "tmnxSysCpmCardLicName": tmnxSysCpmCardLicName,
       "tmnxSysCpmCardLicUuid": tmnxSysCpmCardLicUuid,
       "tmnxSysCpmCardLicDescription": tmnxSysCpmCardLicDescription,
       "tmnxSysCpmCardLicProduct": tmnxSysCpmCardLicProduct,
       "tmnxSysCpmCardLicSwVersion": tmnxSysCpmCardLicSwVersion,
       "tmnxSysCpmCardLicIssueDateTime": tmnxSysCpmCardLicIssueDateTime,
       "tmnxSysCpmCardLicStartDateTime": tmnxSysCpmCardLicStartDateTime,
       "tmnxSysCpmCardLicEndDateTime": tmnxSysCpmCardLicEndDateTime,
       "tmnxSysCpmCardLicVChassisType": tmnxSysCpmCardLicVChassisType,
       "tmnxSysCpmCardLicMaxNumCPMs": tmnxSysCpmCardLicMaxNumCPMs,
       "tmnxSysCpmCardLicMaxNumIOMs": tmnxSysCpmCardLicMaxNumIOMs,
       "tmnxSysCpmCardLicFeatureTable": tmnxSysCpmCardLicFeatureTable,
       "tmnxSysCpmCardLicFeatureEntry": tmnxSysCpmCardLicFeatureEntry,
       "tmnxSysCpmCardLicFeatApplication": tmnxSysCpmCardLicFeatApplication,
       "tmnxSysCpmCardLicFeatNumber": tmnxSysCpmCardLicFeatNumber,
       "tmnxSysCpmCardLicFeatDescription": tmnxSysCpmCardLicFeatDescription,
       "tmnxSysLicensingTable": tmnxSysLicensingTable,
       "tmnxSysLicensingEntry": tmnxSysLicensingEntry,
       "tmnxSysLicensingGroup": tmnxSysLicensingGroup,
       "tmnxSysLicensedAppName": tmnxSysLicensedAppName,
       "tmnxSysAppLicenseDescription": tmnxSysAppLicenseDescription,
       "tmnxSysAppLicenseType": tmnxSysAppLicenseType,
       "tmnxSysAppLicensePoolSize": tmnxSysAppLicensePoolSize,
       "tmnxSysAppLicenseAllocated": tmnxSysAppLicenseAllocated,
       "tmnxSysAppLicensePresent": tmnxSysAppLicensePresent,
       "tmnxSysAppLicenseState": tmnxSysAppLicenseState,
       "tmnxSysAppLicense24HrDateTime": tmnxSysAppLicense24HrDateTime,
       "tmnxSysAppLicense24HrMax": tmnxSysAppLicense24HrMax,
       "tmnxSysAppLicenseCurrentMax": tmnxSysAppLicenseCurrentMax,
       "tmnxSysAvailableLicensesTable": tmnxSysAvailableLicensesTable,
       "tmnxSysAvailableLicensesEntry": tmnxSysAvailableLicensesEntry,
       "tmnxSysAvailLicenseIndex": tmnxSysAvailLicenseIndex,
       "tmnxSysAvailLicenseName": tmnxSysAvailLicenseName,
       "tmnxSysAvailLicenseUuid": tmnxSysAvailLicenseUuid,
       "tmnxSysAvailLicenseDescription": tmnxSysAvailLicenseDescription,
       "tmnxSysAvailLicenseSwVersion": tmnxSysAvailLicenseSwVersion,
       "tmnxSysAvailLicIssueDateTime": tmnxSysAvailLicIssueDateTime,
       "tmnxSysAvailLicStartDateTime": tmnxSysAvailLicStartDateTime,
       "tmnxSysAvailLicEndDateTime": tmnxSysAvailLicEndDateTime,
       "tmnxSysAvailLicenseProduct": tmnxSysAvailLicenseProduct,
       "tmnxSysLicensingState": tmnxSysLicensingState,
       "tmnxSysLicensingRebootPending": tmnxSysLicensingRebootPending,
       "tmnxSysLicenseStatistics": tmnxSysLicenseStatistics,
       "tmnxSysAppStats24HrsTable": tmnxSysAppStats24HrsTable,
       "tmnxSysAppStats24HrsEntry": tmnxSysAppStats24HrsEntry,
       "tmnxSysAppStats24HrsApplication": tmnxSysAppStats24HrsApplication,
       "tmnxSysAppStats24HrsType": tmnxSysAppStats24HrsType,
       "tmnxSysAppStats24HrsIndex": tmnxSysAppStats24HrsIndex,
       "tmnxSysAppStats24HrsName": tmnxSysAppStats24HrsName,
       "tmnxSysAppStats24HrsValue": tmnxSysAppStats24HrsValue,
       "tmnxSysAppStats24HrsTime": tmnxSysAppStats24HrsTime,
       "tmnxSysAppStatsWeekTable": tmnxSysAppStatsWeekTable,
       "tmnxSysAppStatsWeekEntry": tmnxSysAppStatsWeekEntry,
       "tmnxSysAppStatsWeekApplication": tmnxSysAppStatsWeekApplication,
       "tmnxSysAppStatsWeekType": tmnxSysAppStatsWeekType,
       "tmnxSysAppStatsWeekIndex": tmnxSysAppStatsWeekIndex,
       "tmnxSysAppStatsWeekName": tmnxSysAppStatsWeekName,
       "tmnxSysAppStatsWeekAverage": tmnxSysAppStatsWeekAverage,
       "tmnxSysAppStatsWeekPeak": tmnxSysAppStatsWeekPeak,
       "tmnxSysAppStatsWeekTime": tmnxSysAppStatsWeekTime,
       "tmnxSysAppStatsPeakTable": tmnxSysAppStatsPeakTable,
       "tmnxSysAppStatsPeakEntry": tmnxSysAppStatsPeakEntry,
       "tmnxSysAppStatsPeakApplication": tmnxSysAppStatsPeakApplication,
       "tmnxSysAppStatsPeakType": tmnxSysAppStatsPeakType,
       "tmnxSysAppStatsPeakName": tmnxSysAppStatsPeakName,
       "tmnxSysAppStatsPeakValue": tmnxSysAppStatsPeakValue,
       "tmnxSysAppStatsPeakTime": tmnxSysAppStatsPeakTime,
       "tmnxSysAppStats48HrsTable": tmnxSysAppStats48HrsTable,
       "tmnxSysAppStats48HrsEntry": tmnxSysAppStats48HrsEntry,
       "tmnxSysAppStats48HrsApplication": tmnxSysAppStats48HrsApplication,
       "tmnxSysAppStats48HrsType": tmnxSysAppStats48HrsType,
       "tmnxSysAppStats48HrsIndex": tmnxSysAppStats48HrsIndex,
       "tmnxSysAppStats48HrsName": tmnxSysAppStats48HrsName,
       "tmnxSysAppStats48HrsValue": tmnxSysAppStats48HrsValue,
       "tmnxSysAppStats48HrsTime": tmnxSysAppStats48HrsTime,
       "tmnxSysLicensingProduct": tmnxSysLicensingProduct,
       "tmnxSysLicensingUuid": tmnxSysLicensingUuid,
       "tmnxSysFibInfo": tmnxSysFibInfo,
       "tmnxSysFibSelective": tmnxSysFibSelective,
       "tmnxSysSnmpSrcAccessObjs": tmnxSysSnmpSrcAccessObjs,
       "tmnxSysSnmpConfigObjs": tmnxSysSnmpConfigObjs,
       "tmnxSysSnmpSrcAccessTblLstChgd": tmnxSysSnmpSrcAccessTblLstChgd,
       "tmnxSysSnmpSrcAccessLstTable": tmnxSysSnmpSrcAccessLstTable,
       "tmnxSysSnmpSrcAccessLstEntry": tmnxSysSnmpSrcAccessLstEntry,
       "tmnxSysSnmpSrcAccessLstName": tmnxSysSnmpSrcAccessLstName,
       "tmnxSysSnmpSrcAccessLstRowStatus": tmnxSysSnmpSrcAccessLstRowStatus,
       "tmnxSysSnmpSrcAccessLstLastChg": tmnxSysSnmpSrcAccessLstLastChg,
       "tmnxSysSnmpStatsObjs": tmnxSysSnmpStatsObjs,
       "tmnxSysSnmpCommunityStatsTable": tmnxSysSnmpCommunityStatsTable,
       "tmnxSysSnmpCommunityStatsEntry": tmnxSysSnmpCommunityStatsEntry,
       "tmnxSysSnmpCommunityPktDropped": tmnxSysSnmpCommunityPktDropped,
       "tmnxSysMgmtProtocolObjs": tmnxSysMgmtProtocolObjs,
       "tmnxSysMgmtProtocolTblLstChng": tmnxSysMgmtProtocolTblLstChng,
       "tmnxSysMgmtProtocolTable": tmnxSysMgmtProtocolTable,
       "tmnxSysMgmtProtocolEntry": tmnxSysMgmtProtocolEntry,
       "tmnxSysMgmtProtocol": tmnxSysMgmtProtocol,
       "tmnxSysMgmtProtLastChange": tmnxSysMgmtProtLastChange,
       "tmnxSysMgmtAllowImmediateChange": tmnxSysMgmtAllowImmediateChange,
       "tmnxSysMgmtCliEngine1": tmnxSysMgmtCliEngine1,
       "tmnxSysMgmtCliEngine2": tmnxSysMgmtCliEngine2,
       "tmnxSysFileTransProfObjs": tmnxSysFileTransProfObjs,
       "tmnxSysFileTransProfTableLstChgd": tmnxSysFileTransProfTableLstChgd,
       "tmnxSysFileTransProfTable": tmnxSysFileTransProfTable,
       "tmnxSysFileTransProfEntry": tmnxSysFileTransProfEntry,
       "tmnxSysFileTransProfName": tmnxSysFileTransProfName,
       "tmnxSysFileTransProfRowStatus": tmnxSysFileTransProfRowStatus,
       "tmnxSysFileTransProfLastChanged": tmnxSysFileTransProfLastChanged,
       "tmnxSysFileTransProfRtrId": tmnxSysFileTransProfRtrId,
       "tmnxSysFileTransProfSvcId": tmnxSysFileTransProfSvcId,
       "tmnxSysFileTransProfSrcAddrV4T": tmnxSysFileTransProfSrcAddrV4T,
       "tmnxSysFileTransProfSrcAddrV4": tmnxSysFileTransProfSrcAddrV4,
       "tmnxSysFileTransProfSrcAddrV6T": tmnxSysFileTransProfSrcAddrV6T,
       "tmnxSysFileTransProfSrcAddrV6": tmnxSysFileTransProfSrcAddrV6,
       "tmnxSysFileTransProfTimeout": tmnxSysFileTransProfTimeout,
       "tmnxSysFileTransProfRetry": tmnxSysFileTransProfRetry,
       "tmnxSysFileTransProfRedirection": tmnxSysFileTransProfRedirection,
       "tmnxSysFileTransProfSvcName": tmnxSysFileTransProfSvcName,
       "tmnxEhsExtObjs": tmnxEhsExtObjs,
       "tmnxSmLaunchExtTable": tmnxSmLaunchExtTable,
       "tmnxSmLaunchExtEntry": tmnxSmLaunchExtEntry,
       "tmnxSmLaunchExtAuthType": tmnxSmLaunchExtAuthType,
       "tmnxSmLaunchExtLockOverride": tmnxSmLaunchExtLockOverride,
       "tmnxSmRunExtTable": tmnxSmRunExtTable,
       "tmnxSmRunExtEntry": tmnxSmRunExtEntry,
       "tmnxSmRunExtAuthType": tmnxSmRunExtAuthType,
       "tmnxSmRunExtUserName": tmnxSmRunExtUserName,
       "tmnxSmRunArgsTable": tmnxSmRunArgsTable,
       "tmnxSmRunArgsEntry": tmnxSmRunArgsEntry,
       "tmnxSmRunEventArgIndex": tmnxSmRunEventArgIndex,
       "tmnxSmRunEventArgName": tmnxSmRunEventArgName,
       "tmnxSmRunEventArgValue": tmnxSmRunEventArgValue,
       "tmnxSysSwReposObjs": tmnxSysSwReposObjs,
       "tmnxSysSwReposTableLastChanged": tmnxSysSwReposTableLastChanged,
       "tmnxSysSoftwareRepositoryTable": tmnxSysSoftwareRepositoryTable,
       "tmnxSysSoftwareRepositoryEntry": tmnxSysSoftwareRepositoryEntry,
       "tmnxSysSwReposName": tmnxSysSwReposName,
       "tmnxSysSwReposRowStatus": tmnxSysSwReposRowStatus,
       "tmnxSysSwReposLastChanged": tmnxSysSwReposLastChanged,
       "tmnxSysSwReposDescription": tmnxSysSwReposDescription,
       "tmnxSysSwReposPrimaryLocation": tmnxSysSwReposPrimaryLocation,
       "tmnxSysSwReposSecondaryLocation": tmnxSysSwReposSecondaryLocation,
       "tmnxSysSwReposTertiaryLocation": tmnxSysSwReposTertiaryLocation,
       "tmnxSysNspProxyInfo": tmnxSysNspProxyInfo,
       "tmnxSysGrpcInfo": tmnxSysGrpcInfo,
       "tmnxSysGrpcAdminState": tmnxSysGrpcAdminState,
       "tmnxSysGrpcOperState": tmnxSysGrpcOperState,
       "tmnxSysGrpcTlsServerProfile": tmnxSysGrpcTlsServerProfile,
       "tmnxSysGrpcMaxMsgSize": tmnxSysGrpcMaxMsgSize,
       "tmnxSysGrpcAutoCfgSave": tmnxSysGrpcAutoCfgSave,
       "tmnxSysGrpcGnmiVersion": tmnxSysGrpcGnmiVersion,
       "tmnxSysGrpcAllowUnsecure": tmnxSysGrpcAllowUnsecure,
       "tmnxSysGrpcGnmiAdminState": tmnxSysGrpcGnmiAdminState,
       "tmnxSysGrpcTcpKaAdminState": tmnxSysGrpcTcpKaAdminState,
       "tmnxSysGrpcTcpKaIdle": tmnxSysGrpcTcpKaIdle,
       "tmnxSysGrpcTcpKaInterval": tmnxSysGrpcTcpKaInterval,
       "tmnxSysGrpcTcpKaCount": tmnxSysGrpcTcpKaCount,
       "tmnxSysGrpcRibApiAdminState": tmnxSysGrpcRibApiAdminState,
       "tmnxSysGrpcRibApiPurgeTimeout": tmnxSysGrpcRibApiPurgeTimeout,
       "tmnxSysGrpcRibApiVersion": tmnxSysGrpcRibApiVersion,
       "tmnxSysGrpcGnoiCertMgmtAdmnState": tmnxSysGrpcGnoiCertMgmtAdmnState,
       "tmnxSysGrpcGnoiCertMgmtVersion": tmnxSysGrpcGnoiCertMgmtVersion,
       "tmnxSysGrpcMdCliAdminState": tmnxSysGrpcMdCliAdminState,
       "tmnxSysGrpcMdCliVersion": tmnxSysGrpcMdCliVersion,
       "tmnxSysGrpcGnoiFileAdminState": tmnxSysGrpcGnoiFileAdminState,
       "tmnxSysGrpcGnoiFileVersion": tmnxSysGrpcGnoiFileVersion,
       "tmnxSysGrpcGnoiSystemAdminState": tmnxSysGrpcGnoiSystemAdminState,
       "tmnxSysGrpcGnoiSystemVersion": tmnxSysGrpcGnoiSystemVersion,
       "tmnxSysMgmtInterfaceMDCli": tmnxSysMgmtInterfaceMDCli,
       "tmnxSysMgmtIfMDCliAutoCfgSave": tmnxSysMgmtIfMDCliAutoCfgSave,
       "tmnxSysMgmtIfMDEnvComplEnter": tmnxSysMgmtIfMDEnvComplEnter,
       "tmnxSysMgmtIfMDEnvComplSpace": tmnxSysMgmtIfMDEnvComplSpace,
       "tmnxSysMgmtIfMDEnvComplTab": tmnxSysMgmtIfMDEnvComplTab,
       "tmnxSysMgmtIfMDEnvConsLength": tmnxSysMgmtIfMDEnvConsLength,
       "tmnxSysMgmtIfMDEnvConsWidth": tmnxSysMgmtIfMDEnvConsWidth,
       "tmnxSysMgmtIfMDEnvMore": tmnxSysMgmtIfMDEnvMore,
       "tmnxSysMgmtIfMDEnvPromptCtx": tmnxSysMgmtIfMDEnvPromptCtx,
       "tmnxSysMgmtIfMDEnvPromptNewline": tmnxSysMgmtIfMDEnvPromptNewline,
       "tmnxSysMgmtIfMDEnvPromptTime": tmnxSysMgmtIfMDEnvPromptTime,
       "tmnxSysMgmtIfMDEnvPromptIndic": tmnxSysMgmtIfMDEnvPromptIndic,
       "tmnxSysMgmtIfMDEnvTimeDisplay": tmnxSysMgmtIfMDEnvTimeDisplay,
       "tmnxSysMgmtIfMDEnvMsgCliSvrt": tmnxSysMgmtIfMDEnvMsgCliSvrt,
       "tmnxSysMgmtIfMDEnvProIndAdminSt": tmnxSysMgmtIfMDEnvProIndAdminSt,
       "tmnxSysMgmtIfMDEnvProIndType": tmnxSysMgmtIfMDEnvProIndType,
       "tmnxSysMgmtIfMDEnvProIndDelay": tmnxSysMgmtIfMDEnvProIndDelay,
       "tmnxSysMgmtIfMDCliCmdAccntLoad": tmnxSysMgmtIfMDCliCmdAccntLoad,
       "tmnxSysMgmtIfMDEnvTimeFormat": tmnxSysMgmtIfMDEnvTimeFormat,
       "tmnxMGSysObjs": tmnxMGSysObjs,
       "tmnxSysMgmtInterfaceYangModules": tmnxSysMgmtInterfaceYangModules,
       "tmnxSysMgmtIfYangBaseR13": tmnxSysMgmtIfYangBaseR13,
       "tmnxSysMgmtIfYangNokia": tmnxSysMgmtIfYangNokia,
       "tmnxSysMgmtIfYangOpenConfig": tmnxSysMgmtIfYangOpenConfig,
       "tmnxSysMgmtIfYangNokiaCombined": tmnxSysMgmtIfYangNokiaCombined,
       "tmnxSysMgmtIfYangNmdaSupport": tmnxSysMgmtIfYangNmdaSupport,
       "tmnxSysMgmtInterfaces": tmnxSysMgmtInterfaces,
       "tmnxSysMgmtIfWriteMode": tmnxSysMgmtIfWriteMode,
       "tmnxSysMgmtIfWriteOperMode": tmnxSysMgmtIfWriteOperMode,
       "tmnxSysMgmtIfModeLastSwitchTime": tmnxSysMgmtIfModeLastSwitchTime,
       "tmnxSysMgmtIfModeSwitchDuration": tmnxSysMgmtIfModeSwitchDuration,
       "tmnxSysMgmtIfDstoreLocksTable": tmnxSysMgmtIfDstoreLocksTable,
       "tmnxSysMgmtIfDstoreLocksEntry": tmnxSysMgmtIfDstoreLocksEntry,
       "tmnxSysMgmtIfDsLocksSessionId": tmnxSysMgmtIfDsLocksSessionId,
       "tmnxSysMgmtIfDsLocksRmtIpAddress": tmnxSysMgmtIfDsLocksRmtIpAddress,
       "tmnxSysMgmtIfDsLocksConsole": tmnxSysMgmtIfDsLocksConsole,
       "tmnxSysMgmtIfDsLocksUserName": tmnxSysMgmtIfDsLocksUserName,
       "tmnxSysMgmtIfDsLocksSessionMode": tmnxSysMgmtIfDsLocksSessionMode,
       "tmnxSysMgmtIfDsLocksSessionType": tmnxSysMgmtIfDsLocksSessionType,
       "tmnxSysMgmtIfDsLocksRegion": tmnxSysMgmtIfDsLocksRegion,
       "tmnxSysMgmtIfDsLocksRunLock": tmnxSysMgmtIfDsLocksRunLock,
       "tmnxSysMgmtIfDsLocksCndLock": tmnxSysMgmtIfDsLocksCndLock,
       "tmnxSysMgmtIfDsLocksIdleTime": tmnxSysMgmtIfDsLocksIdleTime,
       "tmnxSysMgmtIfDsLocksScratchCnt": tmnxSysMgmtIfDsLocksScratchCnt,
       "tmnxSysMgmtIfDsLocksCronEhs": tmnxSysMgmtIfDsLocksCronEhs,
       "tmnxSysMgmtIfSchemaPath": tmnxSysMgmtIfSchemaPath,
       "tmnxSysMgmtIfWriteSwitchReason": tmnxSysMgmtIfWriteSwitchReason,
       "tmnxSysMgmtIfPriSchemaPathState": tmnxSysMgmtIfPriSchemaPathState,
       "tmnxSysMgmtIfPriSchemaPathValue": tmnxSysMgmtIfPriSchemaPathValue,
       "tmnxSysMgmtIfSecSchemaPathState": tmnxSysMgmtIfSecSchemaPathState,
       "tmnxSysMgmtIfSecSchemaPathValue": tmnxSysMgmtIfSecSchemaPathValue,
       "tmnxSysMgmtIfTerSchemaPathState": tmnxSysMgmtIfTerSchemaPathState,
       "tmnxSysMgmtIfTerSchemaPathValue": tmnxSysMgmtIfTerSchemaPathValue,
       "tmnxSysMgmtIfOperSchemaPathState": tmnxSysMgmtIfOperSchemaPathState,
       "tmnxSysMgmtIfOperSchemaPathValue": tmnxSysMgmtIfOperSchemaPathValue,
       "tmnxSysMgmtIfCommitHistory": tmnxSysMgmtIfCommitHistory,
       "tmnxSysGrpcConnTable": tmnxSysGrpcConnTable,
       "tmnxSysGrpcConnEntry": tmnxSysGrpcConnEntry,
       "tmnxSysGrpcConnSrcIpAddType": tmnxSysGrpcConnSrcIpAddType,
       "tmnxSysGrpcConnSrcIpAddress": tmnxSysGrpcConnSrcIpAddress,
       "tmnxSysGrpcConnSrcPort": tmnxSysGrpcConnSrcPort,
       "tmnxSysGrpcConnStartTime": tmnxSysGrpcConnStartTime,
       "tmnxSysGrpcConnActRpcCnt": tmnxSysGrpcConnActRpcCnt,
       "tmnxSysGrpcConnTotRpcCnt": tmnxSysGrpcConnTotRpcCnt,
       "tmnxSysGrpcConnRxBytes": tmnxSysGrpcConnRxBytes,
       "tmnxSysGrpcConnTxBytes": tmnxSysGrpcConnTxBytes,
       "tmnxSysGrpcConnQos": tmnxSysGrpcConnQos,
       "tmnxSysGrpcConnSrcVRtrId": tmnxSysGrpcConnSrcVRtrId,
       "tmnxSysGrpcConnGrpcTunnel": tmnxSysGrpcConnGrpcTunnel,
       "tmnxSysHttpRdr": tmnxSysHttpRdr,
       "tmnxSysHttpRdrCpmOptimizedMode": tmnxSysHttpRdrCpmOptimizedMode,
       "tmnxSysGrpcRpcTable": tmnxSysGrpcRpcTable,
       "tmnxSysGrpcRpcEntry": tmnxSysGrpcRpcEntry,
       "tmnxSysGrpcRpcId": tmnxSysGrpcRpcId,
       "tmnxSysGrpcRpcName": tmnxSysGrpcRpcName,
       "tmnxSysGrpcRpcServiceName": tmnxSysGrpcRpcServiceName,
       "tmnxSysGrpcRpcStartTime": tmnxSysGrpcRpcStartTime,
       "tmnxSysGrpcRpcSrcIpAddType": tmnxSysGrpcRpcSrcIpAddType,
       "tmnxSysGrpcRpcSrcIpAddress": tmnxSysGrpcRpcSrcIpAddress,
       "tmnxSysGrpcRpcSrcPort": tmnxSysGrpcRpcSrcPort,
       "tmnxSysGrpcRpcUserName": tmnxSysGrpcRpcUserName,
       "tmnxSysGrpcRpcSessionId": tmnxSysGrpcRpcSessionId,
       "tmnxSysGrpcRpcGrpcTunnel": tmnxSysGrpcRpcGrpcTunnel,
       "tmnxSysNetworkElementObjs": tmnxSysNetworkElementObjs,
       "tmnxSysNEProfTableLstChgd": tmnxSysNEProfTableLstChgd,
       "tmnxSysNEProfTable": tmnxSysNEProfTable,
       "tmnxSysNEProfEntry": tmnxSysNEProfEntry,
       "tmnxSysNEProfName": tmnxSysNEProfName,
       "tmnxSysNEProfRowStatus": tmnxSysNEProfRowStatus,
       "tmnxSysNEProfLastChanged": tmnxSysNEProfLastChanged,
       "tmnxSysNEProfNeid": tmnxSysNEProfNeid,
       "tmnxSysNEProfNeipV4Type": tmnxSysNEProfNeipV4Type,
       "tmnxSysNEProfNeipV4": tmnxSysNEProfNeipV4,
       "tmnxSysNEProfNeipV6Type": tmnxSysNEProfNeipV6Type,
       "tmnxSysNEProfNeipV6": tmnxSysNEProfNeipV6,
       "tmnxSysNEProfSystemMac": tmnxSysNEProfSystemMac,
       "tmnxSysNEProfPlatformType": tmnxSysNEProfPlatformType,
       "tmnxSysNEProfVendorId": tmnxSysNEProfVendorId,
       "tmnxSysNEProfNeipV4AutoGenerate": tmnxSysNEProfNeipV4AutoGenerate,
       "tmnxSysNEProfNeipV4NeidVendorId": tmnxSysNEProfNeipV4NeidVendorId,
       "tmnxSysNEProfNeipV6AutoGenerate": tmnxSysNEProfNeipV6AutoGenerate,
       "tmnxSysNEProfNeipV6NeidVendorId": tmnxSysNEProfNeipV6NeidVendorId,
       "tmnxSysNEDiscoveryGenerateTraps": tmnxSysNEDiscoveryGenerateTraps,
       "tmnxSysFwdPathOptsObjs": tmnxSysFwdPathOptsObjs,
       "tmnxSysFpoDscpTransAdminState": tmnxSysFpoDscpTransAdminState,
       "tmnxSysFpoDscpTransOperState": tmnxSysFpoDscpTransOperState,
       "tmnxSysFpoEntropyLabelAdminState": tmnxSysFpoEntropyLabelAdminState,
       "tmnxSysFpoEntropyLabelOperState": tmnxSysFpoEntropyLabelOperState,
       "tmnxSysFpoMacFltOutVlanPrioAdmSt": tmnxSysFpoMacFltOutVlanPrioAdmSt,
       "tmnxSysFpoMacFltOutVlanPrioOprSt": tmnxSysFpoMacFltOutVlanPrioOprSt,
       "tmnxSysFpoVplsEvpnMplsAdminState": tmnxSysFpoVplsEvpnMplsAdminState,
       "tmnxSysFpoVplsEvpnMplsOperState": tmnxSysFpoVplsEvpnMplsOperState,
       "tmnxSysFpoQosFc4ProfAdminState": tmnxSysFpoQosFc4ProfAdminState,
       "tmnxSysFpoQosFc4ProfOperState": tmnxSysFpoQosFc4ProfOperState,
       "tmnxSysFpoMplsFastSwOvAdminState": tmnxSysFpoMplsFastSwOvAdminState,
       "tmnxSysFpoMplsFastSwOvOperState": tmnxSysFpoMplsFastSwOvOperState,
       "tmnxSysFpoRouterEcmpAdminState": tmnxSysFpoRouterEcmpAdminState,
       "tmnxSysFpoRouterEcmpOperState": tmnxSysFpoRouterEcmpOperState,
       "tmnxSysFpoQosMacCritAdminState": tmnxSysFpoQosMacCritAdminState,
       "tmnxSysFpoQosMacCritOperState": tmnxSysFpoQosMacCritOperState,
       "tmnxSysFpoQosIpv6CritAdminState": tmnxSysFpoQosIpv6CritAdminState,
       "tmnxSysFpoQosIpv6CritOperState": tmnxSysFpoQosIpv6CritOperState,
       "tmnxSysFpoQosBumPolAdminState": tmnxSysFpoQosBumPolAdminState,
       "tmnxSysFpoQosBumPolOperState": tmnxSysFpoQosBumPolOperState,
       "tmnxSysFpoLpmAlcnScl1AdminState": tmnxSysFpoLpmAlcnScl1AdminState,
       "tmnxSysFpoLpmAlcnScl1OperState": tmnxSysFpoLpmAlcnScl1OperState,
       "tmnxSysFpoLpmAlcnScl2AdminState": tmnxSysFpoLpmAlcnScl2AdminState,
       "tmnxSysFpoLpmAlcnScl2OperState": tmnxSysFpoLpmAlcnScl2OperState,
       "tmnxSysFpoLpmAlcnScl3AdminState": tmnxSysFpoLpmAlcnScl3AdminState,
       "tmnxSysFpoLpmAlcnScl3OperState": tmnxSysFpoLpmAlcnScl3OperState,
       "tmnxSysFpoDot1xHostAuthAdmState": tmnxSysFpoDot1xHostAuthAdmState,
       "tmnxSysFpoDot1xHostAuthOperState": tmnxSysFpoDot1xHostAuthOperState,
       "tmnxSysFpoIpv6FltrEgrAdminState": tmnxSysFpoIpv6FltrEgrAdminState,
       "tmnxSysFpoIpv6FltrEgrOperState": tmnxSysFpoIpv6FltrEgrOperState,
       "tmnxSysFpoIpv6FltrNxtHdrAdmState": tmnxSysFpoIpv6FltrNxtHdrAdmState,
       "tmnxSysFpoIpv6FltrNxtHdrOprState": tmnxSysFpoIpv6FltrNxtHdrOprState,
       "tmnxSysFpoIpv6FltrDstPrtAdmState": tmnxSysFpoIpv6FltrDstPrtAdmState,
       "tmnxSysFpoIpv6FltrDstPrtOprState": tmnxSysFpoIpv6FltrDstPrtOprState,
       "tmnxSysFpoIpv6FltrSrcPrtAdmState": tmnxSysFpoIpv6FltrSrcPrtAdmState,
       "tmnxSysFpoIpv6FltrSrcPrtOprState": tmnxSysFpoIpv6FltrSrcPrtOprState,
       "tmnxSysFpoIpv6FltrDstIpLsbAdmSt": tmnxSysFpoIpv6FltrDstIpLsbAdmSt,
       "tmnxSysFpoIpv6FltrDstIpLsbOprSt": tmnxSysFpoIpv6FltrDstIpLsbOprSt,
       "tmnxSysFpoIpv6FltrTcpFlgAdmState": tmnxSysFpoIpv6FltrTcpFlgAdmState,
       "tmnxSysFpoIpv6FltrTcpFlgOprState": tmnxSysFpoIpv6FltrTcpFlgOprState,
       "tmnxSysFpoIpv6FltStatColAdmState": tmnxSysFpoIpv6FltStatColAdmState,
       "tmnxSysFpoIpv6FltStatColOprState": tmnxSysFpoIpv6FltStatColOprState,
       "tmnxSysFpoIpv4FltStatColAdmState": tmnxSysFpoIpv4FltStatColAdmState,
       "tmnxSysFpoIpv4FltStatColOprState": tmnxSysFpoIpv4FltStatColOprState,
       "tmnxSysFpoIpv4FltPbrRdrtAdmState": tmnxSysFpoIpv4FltPbrRdrtAdmState,
       "tmnxSysFpoIpv4FltPbrRdrtOprState": tmnxSysFpoIpv4FltPbrRdrtOprState,
       "tmnxSysFpoIpv6FltPbrRdrtAdmState": tmnxSysFpoIpv6FltPbrRdrtAdmState,
       "tmnxSysFpoIpv6FltPbrRdrtOprState": tmnxSysFpoIpv6FltPbrRdrtOprState,
       "tmnxSysFpoRingApsAdminState": tmnxSysFpoRingApsAdminState,
       "tmnxSysFpoRingApsOperState": tmnxSysFpoRingApsOperState,
       "tmnxSysSwitchFabricObjs": tmnxSysSwitchFabricObjs,
       "tmnxSysSwFabSfmLossThresh": tmnxSysSwFabSfmLossThresh,
       "tmnxSysSwFabFailRecAdminState": tmnxSysSwFabFailRecAdminState,
       "tmnxSysSwFabFailRecOperState": tmnxSysSwFabFailRecOperState,
       "tmnxSysUsbTable": tmnxSysUsbTable,
       "tmnxSysUsbEntry": tmnxSysUsbEntry,
       "tmnxSysUsbCFlashId": tmnxSysUsbCFlashId,
       "tmnxSysUsbLastChgd": tmnxSysUsbLastChgd,
       "tmnxSysUsbAdminState": tmnxSysUsbAdminState,
       "tmnxSysRemoteMgmt": tmnxSysRemoteMgmt,
       "tmnxSysRmtMgmtAdminState": tmnxSysRmtMgmtAdminState,
       "tmnxSysRmtMgmtOperState": tmnxSysRmtMgmtOperState,
       "tmnxSysRmtMgmtOperDownReason": tmnxSysRmtMgmtOperDownReason,
       "tmnxSysRmtMgmtAllowUnsecure": tmnxSysRmtMgmtAllowUnsecure,
       "tmnxSysRmtMgmtTlsClientProf": tmnxSysRmtMgmtTlsClientProf,
       "tmnxSysRmtMgmtTimeout": tmnxSysRmtMgmtTimeout,
       "tmnxSysRmtMgmtVRtrId": tmnxSysRmtMgmtVRtrId,
       "tmnxSysRmtMgmtSrcIpAddType": tmnxSysRmtMgmtSrcIpAddType,
       "tmnxSysRmtMgmtSrcIpAddress": tmnxSysRmtMgmtSrcIpAddress,
       "tmnxSysRmtMgmtSrcPort": tmnxSysRmtMgmtSrcPort,
       "tmnxSysRmtMgmtSrcDefaultPort": tmnxSysRmtMgmtSrcDefaultPort,
       "tmnxSysRmtMgmtDeviceLabel": tmnxSysRmtMgmtDeviceLabel,
       "tmnxSysRmtMgmtDeviceName": tmnxSysRmtMgmtDeviceName,
       "tmnxSysRmtMgmtLastRegStatus": tmnxSysRmtMgmtLastRegStatus,
       "tmnxSysRmtMgmtLastRegTime": tmnxSysRmtMgmtLastRegTime,
       "tmnxSysRmtMgmtRegsCancelled": tmnxSysRmtMgmtRegsCancelled,
       "tmnxSysRmtMgmtRegsFailed": tmnxSysRmtMgmtRegsFailed,
       "tmnxSysRmtMgmtRegsSent": tmnxSysRmtMgmtRegsSent,
       "tmnxSysRmtMgmtHelloInterval": tmnxSysRmtMgmtHelloInterval,
       "tmnxSysRmtMgmtLastHelloTime": tmnxSysRmtMgmtLastHelloTime,
       "tmnxSysRmtMgmtManagerTable": tmnxSysRmtMgmtManagerTable,
       "tmnxSysRmtMgmtManagerEntry": tmnxSysRmtMgmtManagerEntry,
       "tmnxSysRmtMgmtMgrName": tmnxSysRmtMgmtMgrName,
       "tmnxSysRmtMgmtMgrRowStatus": tmnxSysRmtMgmtMgrRowStatus,
       "tmnxSysRmtMgmtMgrAdminState": tmnxSysRmtMgmtMgrAdminState,
       "tmnxSysRmtMgmtMgrOperState": tmnxSysRmtMgmtMgrOperState,
       "tmnxSysRmtMgmtMgrOperDownReason": tmnxSysRmtMgmtMgrOperDownReason,
       "tmnxSysRmtMgmtMgrFQDN": tmnxSysRmtMgmtMgrFQDN,
       "tmnxSysRmtMgmtMgrIpAddType": tmnxSysRmtMgmtMgrIpAddType,
       "tmnxSysRmtMgmtMgrIpAddress": tmnxSysRmtMgmtMgrIpAddress,
       "tmnxSysRmtMgmtMgrPort": tmnxSysRmtMgmtMgrPort,
       "tmnxSysRmtMgmtMgrAllowUnsecure": tmnxSysRmtMgmtMgrAllowUnsecure,
       "tmnxSysRmtMgmtMgrTlsClientProf": tmnxSysRmtMgmtMgrTlsClientProf,
       "tmnxSysRmtMgmtMgrDescription": tmnxSysRmtMgmtMgrDescription,
       "tmnxSysRmtMgmtMgrTimeout": tmnxSysRmtMgmtMgrTimeout,
       "tmnxSysRmtMgmtMgrVRtrId": tmnxSysRmtMgmtMgrVRtrId,
       "tmnxSysRmtMgmtMgrSrcIpAddType": tmnxSysRmtMgmtMgrSrcIpAddType,
       "tmnxSysRmtMgmtMgrSrcIpAddress": tmnxSysRmtMgmtMgrSrcIpAddress,
       "tmnxSysRmtMgmtMgrSrcPort": tmnxSysRmtMgmtMgrSrcPort,
       "tmnxSysRmtMgmtMgrSrcDefaultPort": tmnxSysRmtMgmtMgrSrcDefaultPort,
       "tmnxSysRmtMgmtMgrDeviceLabel": tmnxSysRmtMgmtMgrDeviceLabel,
       "tmnxSysRmtMgmtMgrDeviceName": tmnxSysRmtMgmtMgrDeviceName,
       "tmnxSysRmtMgmtMgrLastRegStatus": tmnxSysRmtMgmtMgrLastRegStatus,
       "tmnxSysRmtMgmtMgrLastRegTime": tmnxSysRmtMgmtMgrLastRegTime,
       "tmnxSysRmtMgmtMgrRegsCancelled": tmnxSysRmtMgmtMgrRegsCancelled,
       "tmnxSysRmtMgmtMgrRegsFailed": tmnxSysRmtMgmtMgrRegsFailed,
       "tmnxSysRmtMgmtMgrRegsSent": tmnxSysRmtMgmtMgrRegsSent,
       "tmnxSysRmtMgmtMgrOperTlsProf": tmnxSysRmtMgmtMgrOperTlsProf,
       "tmnxSysRmtMgmtMgrOperTranspType": tmnxSysRmtMgmtMgrOperTranspType,
       "tmnxSysRmtMgmtMgrOperTimeout": tmnxSysRmtMgmtMgrOperTimeout,
       "tmnxSysRmtMgmtMgrOperVRtrId": tmnxSysRmtMgmtMgrOperVRtrId,
       "tmnxSysRmtMgmtMgrOperDevName": tmnxSysRmtMgmtMgrOperDevName,
       "tmnxSysRmtMgmtMgrOperDevLabel": tmnxSysRmtMgmtMgrOperDevLabel,
       "tmnxSysRmtMgmtMgrOperSrcIpAdType": tmnxSysRmtMgmtMgrOperSrcIpAdType,
       "tmnxSysRmtMgmtMgrOperSrcIpAddr": tmnxSysRmtMgmtMgrOperSrcIpAddr,
       "tmnxSysRmtMgmtMgrOperSrcPort": tmnxSysRmtMgmtMgrOperSrcPort,
       "tmnxSysRmtMgmtHelloIntervalSec": tmnxSysRmtMgmtHelloIntervalSec,
       "tmnxSysMgmtInterfaceOperations": tmnxSysMgmtInterfaceOperations,
       "tmnxSysMgmtIfOpsAsyncExecTimeout": tmnxSysMgmtIfOpsAsyncExecTimeout,
       "tmnxSysMgmtIfOpsAsyncRetTimeout": tmnxSysMgmtIfOpsAsyncRetTimeout,
       "tmnxSysMgmtIfOpsSyncExecTimeout": tmnxSysMgmtIfOpsSyncExecTimeout,
       "tmnxSysSwFabFailRecSfmStatsTable": tmnxSysSwFabFailRecSfmStatsTable,
       "tmnxSysSwFabFailRecSfmStatsEntry": tmnxSysSwFabFailRecSfmStatsEntry,
       "tmnxSysSwFabFailRecSfmState": tmnxSysSwFabFailRecSfmState,
       "tmnxSysSwFabFailRecSfmStateTime": tmnxSysSwFabFailRecSfmStateTime,
       "sysBofInfoExt": sysBofInfoExt,
       "sbiEncryptConfig": sbiEncryptConfig,
       "sbiPassword": sbiPassword,
       "sbiEncryptKey": sbiEncryptKey,
       "tmnxSysGrpcPendRebTable": tmnxSysGrpcPendRebTable,
       "tmnxSysGrpcPendRebEntry": tmnxSysGrpcPendRebEntry,
       "tmnxSysGrpcPendRebComp": tmnxSysGrpcPendRebComp,
       "tmnxSysGrpcPendRebOperState": tmnxSysGrpcPendRebOperState,
       "tmnxSysGrpcPendRebDelay": tmnxSysGrpcPendRebDelay,
       "tmnxSysGrpcPendRebMsg": tmnxSysGrpcPendRebMsg,
       "tmnxSysGrpcPendRebCount": tmnxSysGrpcPendRebCount,
       "tmnxSysGrpcTunnelObjs": tmnxSysGrpcTunnelObjs,
       "tmnxSysGrpcTunnelLastChangedObjs": tmnxSysGrpcTunnelLastChangedObjs,
       "tmnxGTnlDestGrpTblLastChgd": tmnxGTnlDestGrpTblLastChgd,
       "tmnxGTnlDestGrpDestTblLastChgd": tmnxGTnlDestGrpDestTblLastChgd,
       "tmnxGTnlTunnelTblLastChgd": tmnxGTnlTunnelTblLastChgd,
       "tmnxGTnlTunnelHandlerTblLastChgd": tmnxGTnlTunnelHandlerTblLastChgd,
       "tmnxGrpcTunnelDestGroupTable": tmnxGrpcTunnelDestGroupTable,
       "tmnxGrpcTunnelDestGroupEntry": tmnxGrpcTunnelDestGroupEntry,
       "tmnxGTnlDestGrpName": tmnxGTnlDestGrpName,
       "tmnxGTnlDestGrpRowStatus": tmnxGTnlDestGrpRowStatus,
       "tmnxGTnlDestGrpLastChgd": tmnxGTnlDestGrpLastChgd,
       "tmnxGTnlDestGrpDescription": tmnxGTnlDestGrpDescription,
       "tmnxGTnlDestGrpTlsClientProf": tmnxGTnlDestGrpTlsClientProf,
       "tmnxGTnlDestGrpAllowUnsecConn": tmnxGTnlDestGrpAllowUnsecConn,
       "tmnxGTnlDestGrpTcpKaAdminState": tmnxGTnlDestGrpTcpKaAdminState,
       "tmnxGTnlDestGrpTcpKaIdle": tmnxGTnlDestGrpTcpKaIdle,
       "tmnxGTnlDestGrpTcpKaInterval": tmnxGTnlDestGrpTcpKaInterval,
       "tmnxGTnlDestGrpTcpKaCount": tmnxGTnlDestGrpTcpKaCount,
       "tmnxGrpcTunnelDestGroupDestTable": tmnxGrpcTunnelDestGroupDestTable,
       "tmnxGrpcTunnelDestGroupDestEntry": tmnxGrpcTunnelDestGroupDestEntry,
       "tmnxGTnlDestGrpDestIndex": tmnxGTnlDestGrpDestIndex,
       "tmnxGTnlDestGrpDestRowStatus": tmnxGTnlDestGrpDestRowStatus,
       "tmnxGTnlDestGrpDestLastChgd": tmnxGTnlDestGrpDestLastChgd,
       "tmnxGTnlDestGrpDestAddType": tmnxGTnlDestGrpDestAddType,
       "tmnxGTnlDestGrpDestAddress": tmnxGTnlDestGrpDestAddress,
       "tmnxGTnlDestGrpDestPort": tmnxGTnlDestGrpDestPort,
       "tmnxGTnlDestGrpDestVRtrId": tmnxGTnlDestGrpDestVRtrId,
       "tmnxGTnlDestGrpDestLclSrcAddType": tmnxGTnlDestGrpDestLclSrcAddType,
       "tmnxGTnlDestGrpDestLclSrcAddress": tmnxGTnlDestGrpDestLclSrcAddress,
       "tmnxGTnlDestGrpDestOrigQosMark": tmnxGTnlDestGrpDestOrigQosMark,
       "tmnxGTnlTunnelTable": tmnxGTnlTunnelTable,
       "tmnxGTnlTunnelEntry": tmnxGTnlTunnelEntry,
       "tmnxGTnlTunnelName": tmnxGTnlTunnelName,
       "tmnxGTnlTunnelRowStatus": tmnxGTnlTunnelRowStatus,
       "tmnxGTnlTunnelLastChgd": tmnxGTnlTunnelLastChgd,
       "tmnxGTnlTunnelAdminState": tmnxGTnlTunnelAdminState,
       "tmnxGTnlTunnelOperState": tmnxGTnlTunnelOperState,
       "tmnxGTnlTunnelOperDownReason": tmnxGTnlTunnelOperDownReason,
       "tmnxGTnlTunnelDescription": tmnxGTnlTunnelDescription,
       "tmnxGTnlTunnelDestGrp": tmnxGTnlTunnelDestGrp,
       "tmnxGTnlTunnelTgtNameCustomStr": tmnxGTnlTunnelTgtNameCustomStr,
       "tmnxGTnlTunnelTgtNameUserAgent": tmnxGTnlTunnelTgtNameUserAgent,
       "tmnxGTnlTunnelTgtNameNodeName": tmnxGTnlTunnelTgtNameNodeName,
       "tmnxGTnlTunnelOperTargetName": tmnxGTnlTunnelOperTargetName,
       "tmnxGTnlTunnelHandlerTable": tmnxGTnlTunnelHandlerTable,
       "tmnxGTnlTunnelHandlerEntry": tmnxGTnlTunnelHandlerEntry,
       "tmnxGTnlTunnelHandlerName": tmnxGTnlTunnelHandlerName,
       "tmnxGTnlTunnelHandlerRowStatus": tmnxGTnlTunnelHandlerRowStatus,
       "tmnxGTnlTunnelHandlerLastChgd": tmnxGTnlTunnelHandlerLastChgd,
       "tmnxGTnlTunnelHandlerAdminState": tmnxGTnlTunnelHandlerAdminState,
       "tmnxGTnlTunnelHandlerPort": tmnxGTnlTunnelHandlerPort,
       "tmnxGTnlTunnelHandlerCustomType": tmnxGTnlTunnelHandlerCustomType,
       "tmnxGTnlTunnelHandlerGrpcServer": tmnxGTnlTunnelHandlerGrpcServer,
       "tmnxGTnlTunnelHandlerSshServer": tmnxGTnlTunnelHandlerSshServer,
       "tmnxGTnlTunnelDestTable": tmnxGTnlTunnelDestTable,
       "tmnxGTnlTunnelDestEntry": tmnxGTnlTunnelDestEntry,
       "tmnxGTnlTunnelDestIndex": tmnxGTnlTunnelDestIndex,
       "tmnxGTnlTunnelDestAddType": tmnxGTnlTunnelDestAddType,
       "tmnxGTnlTunnelDestAddress": tmnxGTnlTunnelDestAddress,
       "tmnxGTnlTunnelDestPort": tmnxGTnlTunnelDestPort,
       "tmnxGTnlTunnelDestOperState": tmnxGTnlTunnelDestOperState,
       "tmnxGTnlTunnelDestOperDownReason": tmnxGTnlTunnelDestOperDownReason,
       "tmnxGTnlTunnelDestOperVRtrId": tmnxGTnlTunnelDestOperVRtrId,
       "tmnxGTnlTunnelDestLastOperChange": tmnxGTnlTunnelDestLastOperChange,
       "tmnxGTnlTunnelDestConnAttempts": tmnxGTnlTunnelDestConnAttempts,
       "tmnxGTnlTunnelSessionTable": tmnxGTnlTunnelSessionTable,
       "tmnxGTnlTunnelSessionEntry": tmnxGTnlTunnelSessionEntry,
       "tmnxGTnlTunnelSessionTag": tmnxGTnlTunnelSessionTag,
       "tmnxGTnlTunnelSessionStartTime": tmnxGTnlTunnelSessionStartTime,
       "tmnxGTnlTunnelSessionTargetType": tmnxGTnlTunnelSessionTargetType,
       "tmnxGTnlTunnelSessionLclSrcPort": tmnxGTnlTunnelSessionLclSrcPort,
       "tmnxGTnlTunnelSessionRxBytes": tmnxGTnlTunnelSessionRxBytes,
       "tmnxGTnlTunnelSessionTxBytes": tmnxGTnlTunnelSessionTxBytes,
       "tmnxSysFanControl": tmnxSysFanControl,
       "tmnxSysFanIncMinimumSpeed": tmnxSysFanIncMinimumSpeed,
       "tmnxSysFpResourceAllocationObjs": tmnxSysFpResourceAllocationObjs,
       "tmnxSysFpResAlcnLpmTblLastChg": tmnxSysFpResAlcnLpmTblLastChg,
       "tmnxSysFpResAlcnLpmTable": tmnxSysFpResAlcnLpmTable,
       "tmnxSysFpResAlcnLpmEntry": tmnxSysFpResAlcnLpmEntry,
       "tmnxSysFpResAlcnLpmScaleOption": tmnxSysFpResAlcnLpmScaleOption,
       "tmnxSysFpResAlcnLpmLastChanged": tmnxSysFpResAlcnLpmLastChanged,
       "tmnxSysFpResAlcnLpmAdminState": tmnxSysFpResAlcnLpmAdminState,
       "tmnxSysFpResAlcnLpmOperState": tmnxSysFpResAlcnLpmOperState,
       "tmnxSysMIBNotifyPrefix": tmnxSysMIBNotifyPrefix,
       "tmnxSysNotifications": tmnxSysNotifications,
       "stiDateAndTimeChanged": stiDateAndTimeChanged,
       "ssiSaveConfigSucceeded": ssiSaveConfigSucceeded,
       "ssiSaveConfigFailed": ssiSaveConfigFailed,
       "sbiBootConfig": sbiBootConfig,
       "sbiBootSnmpd": sbiBootSnmpd,
       "radiusServerOperStatusChange": radiusServerOperStatusChange,
       "radiusOperStatusChange": radiusOperStatusChange,
       "tmnxConfigModify": tmnxConfigModify,
       "tmnxConfigCreate": tmnxConfigCreate,
       "tmnxConfigDelete": tmnxConfigDelete,
       "tmnxStateChange": tmnxStateChange,
       "tmnxModuleMallocFailed": tmnxModuleMallocFailed,
       "tmnxTrapDropped": tmnxTrapDropped,
       "ssiSyncConfigOK": ssiSyncConfigOK,
       "ssiSyncConfigFailed": ssiSyncConfigFailed,
       "ssiSyncBootEnvOK": ssiSyncBootEnvOK,
       "ssiSyncBootEnvFailed": ssiSyncBootEnvFailed,
       "sntpTimeDiffExceedsThreshold": sntpTimeDiffExceedsThreshold,
       "tacplusServerOperStatusChange": tacplusServerOperStatusChange,
       "tacplusOperStatusChange": tacplusOperStatusChange,
       "tmnxSnmpdError": tmnxSnmpdError,
       "tmnxSsiMismatch": tmnxSsiMismatch,
       "tmnxSnmpdStateChange": tmnxSnmpdStateChange,
       "ssiRedStandbySyncing": ssiRedStandbySyncing,
       "ssiRedStandbyReady": ssiRedStandbyReady,
       "ssiRedStandbySyncLost": ssiRedStandbySyncLost,
       "ssiRedSwitchover": ssiRedSwitchover,
       "ssiRedCpmActive": ssiRedCpmActive,
       "ssiRedSingleCpm": ssiRedSingleCpm,
       "persistencyClosedAlarmRaised": persistencyClosedAlarmRaised,
       "persistencyClosedAlarmCleared": persistencyClosedAlarmCleared,
       "tmnxSntpOperChange": tmnxSntpOperChange,
       "tmnxSysTimeSet": tmnxSysTimeSet,
       "tmnxFtpClientFailure": tmnxFtpClientFailure,
       "tacplusInetSrvrOperStatusChange": tacplusInetSrvrOperStatusChange,
       "radiusInetServerOperStatusChange": radiusInetServerOperStatusChange,
       "persistencyEventReport": persistencyEventReport,
       "sbiBootConfigFailFileError": sbiBootConfigFailFileError,
       "sbiBootConfigOKFileError": sbiBootConfigOKFileError,
       "sbiBootLiConfig": sbiBootLiConfig,
       "persistenceRestoreProblem": persistenceRestoreProblem,
       "tmnxSysRollbackStarted": tmnxSysRollbackStarted,
       "tmnxSysRollbackStatusChange": tmnxSysRollbackStatusChange,
       "tmnxSysRollbackSaveStatusChange": tmnxSysRollbackSaveStatusChange,
       "tmnxSysRollbackFileDeleteStatus": tmnxSysRollbackFileDeleteStatus,
       "ssiSyncRollbackOK": ssiSyncRollbackOK,
       "ssiSyncRollbackFailed": ssiSyncRollbackFailed,
       "ssiSyncCertOK": ssiSyncCertOK,
       "ssiSyncCertFailed": ssiSyncCertFailed,
       "persistencyFileSysThresRaised": persistencyFileSysThresRaised,
       "persistencyFileSysThresCleared": persistencyFileSysThresCleared,
       "tmnxSysExecStarted": tmnxSysExecStarted,
       "tmnxSysExecFinished": tmnxSysExecFinished,
       "tmnxSysRollbackSaveStarted": tmnxSysRollbackSaveStarted,
       "tmnxSysRollbackDeleteStarted": tmnxSysRollbackDeleteStarted,
       "tmnxSysNvsysFileError": tmnxSysNvsysFileError,
       "sysDNSSecFailedAuthentication": sysDNSSecFailedAuthentication,
       "tmnxConfigConflict": tmnxConfigConflict,
       "tmnxSysLicenseInvalid": tmnxSysLicenseInvalid,
       "tmnxSysLicenseExpiresSoon": tmnxSysLicenseExpiresSoon,
       "tmnxSysVsdServerAvailable": tmnxSysVsdServerAvailable,
       "tmnxSysVsdServerUnavailable": tmnxSysVsdServerUnavailable,
       "tmnxSysXmppServerFunctional": tmnxSysXmppServerFunctional,
       "tmnxSysXmppServerNotFunctional": tmnxSysXmppServerNotFunctional,
       "tmnxSysLicenseValid": tmnxSysLicenseValid,
       "tmnxSysBaseMacAddressNotSet": tmnxSysBaseMacAddressNotSet,
       "tmnxSmLaunchStartFailed": tmnxSmLaunchStartFailed,
       "tmnxEhsHandlerInvoked": tmnxEhsHandlerInvoked,
       "tmnxEhsDroppedByMinDelay": tmnxEhsDroppedByMinDelay,
       "tmnxSysAppStats24HrsAvailable": tmnxSysAppStats24HrsAvailable,
       "tmnxSysAppStatsWeekAvailable": tmnxSysAppStatsWeekAvailable,
       "tmnxSysLicenseActivated": tmnxSysLicenseActivated,
       "tmnxSysStandbyLicensingError": tmnxSysStandbyLicensingError,
       "tmnxSysStandbyLicensingReady": tmnxSysStandbyLicensingReady,
       "tmnxSysMgmtIfModeChangeStart": tmnxSysMgmtIfModeChangeStart,
       "tmnxSysMgmtIfModeChangeComplete": tmnxSysMgmtIfModeChangeComplete,
       "tmnxSysMgmtIfModeChangeFailure": tmnxSysMgmtIfModeChangeFailure,
       "tmnxSysAppLicenseInsufficient": tmnxSysAppLicenseInsufficient,
       "tmnxSysMgmtIfLiIncorrectFormat": tmnxSysMgmtIfLiIncorrectFormat,
       "tmnxSysMgmtIfLiCfgNotEncrypted": tmnxSysMgmtIfLiCfgNotEncrypted,
       "tmnxSysLicenseUpdateRequired": tmnxSysLicenseUpdateRequired,
       "tmnxEqOperStateChange": tmnxEqOperStateChange,
       "stiDateAndTimeChanging": stiDateAndTimeChanging,
       "tmnxSysSwFabFailRecStarted": tmnxSysSwFabFailRecStarted,
       "tmnxSysSwFabFailRecCompleted": tmnxSysSwFabFailRecCompleted,
       "tmnxSysSwFabFailRecAborted": tmnxSysSwFabFailRecAborted,
       "tmnxSysSwFabFailRecDetected": tmnxSysSwFabFailRecDetected,
       "mdSaveCommitHistoryFailed": mdSaveCommitHistoryFailed,
       "sbiBootMdReadCommitHistoryFailed": sbiBootMdReadCommitHistoryFailed,
       "tmnxSysDyingGasp": tmnxSysDyingGasp,
       "tmnxSysMGNotifications": tmnxSysMGNotifications}
)
