# SNMP MIB module (FORTINET-FORTISANDBOX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fortinet\FORTINET-FORTISANDBOX-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:54 2025
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

(FnBoolState,
 FnIndex,
 fnAdminEntry,
 fnSysSerial,
 fortinet) = mibBuilder.importSymbols(
    "FORTINET-CORE-MIB",
    "FnBoolState",
    "FnIndex",
    "fnAdminEntry",
    "fnSysSerial",
    "fortinet")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(ifEntry,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry",
    "ifName")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

(AutonomousType,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fnFortiSandboxMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118)
)
if mibBuilder.loadTexts:
    fnFortiSandboxMib.setRevisions(
        ("2014-02-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FsaAdminPermLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              15,
              255)
        )
    )
    namedValues = NamedValues(
        *(("readAdmin", 0),
          ("writeAdmin", 1),
          ("domainAdmin", 15),
          ("superAdmin", 255))
    )



class FsaUserAuthType(TextualConvention, Integer32):
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
        *(("local", 1),
          ("radiusSingle", 2),
          ("radiusMultiple", 3),
          ("ldap", 4))
    )



class FsaSessProto(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6,
              8,
              12,
              17,
              22,
              41,
              46,
              47,
              50,
              51,
              89,
              103,
              108,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ip", 0),
          ("icmp", 1),
          ("igmp", 2),
          ("ipip", 4),
          ("tcp", 6),
          ("egp", 8),
          ("pup", 12),
          ("udp", 17),
          ("idp", 22),
          ("ipv6", 41),
          ("rsvp", 46),
          ("gre", 47),
          ("esp", 50),
          ("ah", 51),
          ("ospf", 89),
          ("pim", 103),
          ("comp", 108),
          ("raw", 255))
    )



# MIB Managed Objects in the order of their OIDs

_FsaModel_ObjectIdentity = ObjectIdentity
fsaModel = _FsaModel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1)
)
_Fsa1000D_ObjectIdentity = ObjectIdentity
fsa1000D = _Fsa1000D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 10004)
)
_FsaVM_ObjectIdentity = ObjectIdentity
fsaVM = _FsaVM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 20000)
)
_Fsa3000D_ObjectIdentity = ObjectIdentity
fsa3000D = _Fsa3000D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 30004)
)
_Fsa3500D_ObjectIdentity = ObjectIdentity
fsa3500D = _Fsa3500D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 30005)
)
_Fsa3000E_ObjectIdentity = ObjectIdentity
fsa3000E = _Fsa3000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 30006)
)
_Fsa2000E_ObjectIdentity = ObjectIdentity
fsa2000E = _Fsa2000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 30007)
)
_Fsa1000F_ObjectIdentity = ObjectIdentity
fsa1000F = _Fsa1000F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 30008)
)
_Fsa500F_ObjectIdentity = ObjectIdentity
fsa500F = _Fsa500F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 30009)
)
_FsaTraps_ObjectIdentity = ObjectIdentity
fsaTraps = _FsaTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2)
)
_FsaTrapPrefix_ObjectIdentity = ObjectIdentity
fsaTrapPrefix = _FsaTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 0)
)
_FsaSystem_ObjectIdentity = ObjectIdentity
fsaSystem = _FsaSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3)
)
_FsaSystemInfo_ObjectIdentity = ObjectIdentity
fsaSystemInfo = _FsaSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1)
)


class _FsaSysVersion_Type(DisplayString):
    """Custom type fsaSysVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FsaSysVersion_Type.__name__ = "DisplayString"
_FsaSysVersion_Object = MibScalar
fsaSysVersion = _FsaSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1, 1),
    _FsaSysVersion_Type()
)
fsaSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaSysVersion.setStatus("current")


class _FsaSysCpuUsage_Type(Gauge32):
    """Custom type fsaSysCpuUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsaSysCpuUsage_Type.__name__ = "Gauge32"
_FsaSysCpuUsage_Object = MibScalar
fsaSysCpuUsage = _FsaSysCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1, 2),
    _FsaSysCpuUsage_Type()
)
fsaSysCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaSysCpuUsage.setStatus("current")


class _FsaSysMemUsage_Type(Gauge32):
    """Custom type fsaSysMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsaSysMemUsage_Type.__name__ = "Gauge32"
_FsaSysMemUsage_Object = MibScalar
fsaSysMemUsage = _FsaSysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1, 3),
    _FsaSysMemUsage_Type()
)
fsaSysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaSysMemUsage.setStatus("current")
_FsaSysMemCapacity_Type = Gauge32
_FsaSysMemCapacity_Object = MibScalar
fsaSysMemCapacity = _FsaSysMemCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1, 4),
    _FsaSysMemCapacity_Type()
)
fsaSysMemCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaSysMemCapacity.setStatus("current")
_FsaSysDiskUsage_Type = Gauge32
_FsaSysDiskUsage_Object = MibScalar
fsaSysDiskUsage = _FsaSysDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1, 5),
    _FsaSysDiskUsage_Type()
)
fsaSysDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaSysDiskUsage.setStatus("current")
_FsaSysDiskCapacity_Type = Gauge32
_FsaSysDiskCapacity_Object = MibScalar
fsaSysDiskCapacity = _FsaSysDiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1, 6),
    _FsaSysDiskCapacity_Type()
)
fsaSysDiskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaSysDiskCapacity.setStatus("current")


class _FsaSysCpuUsageExcludedNice_Type(Gauge32):
    """Custom type fsaSysCpuUsageExcludedNice based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsaSysCpuUsageExcludedNice_Type.__name__ = "Gauge32"
_FsaSysCpuUsageExcludedNice_Object = MibScalar
fsaSysCpuUsageExcludedNice = _FsaSysCpuUsageExcludedNice_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1, 7),
    _FsaSysCpuUsageExcludedNice_Type()
)
fsaSysCpuUsageExcludedNice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaSysCpuUsageExcludedNice.setStatus("current")
_FsaSysUpTime_Type = Counter64
_FsaSysUpTime_Object = MibScalar
fsaSysUpTime = _FsaSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1, 8),
    _FsaSysUpTime_Type()
)
fsaSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaSysUpTime.setStatus("current")
if mibBuilder.loadTexts:
    fsaSysUpTime.setUnits("hundredths of a second")
_FsaSoftware_ObjectIdentity = ObjectIdentity
fsaSoftware = _FsaSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 2)
)


class _FsaSysTracer_Type(DisplayString):
    """Custom type fsaSysTracer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FsaSysTracer_Type.__name__ = "DisplayString"
_FsaSysTracer_Object = MibScalar
fsaSysTracer = _FsaSysTracer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 2, 1),
    _FsaSysTracer_Type()
)
fsaSysTracer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaSysTracer.setStatus("current")


class _FsaSysRating_Type(DisplayString):
    """Custom type fsaSysRating based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FsaSysRating_Type.__name__ = "DisplayString"
_FsaSysRating_Object = MibScalar
fsaSysRating = _FsaSysRating_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 2, 2),
    _FsaSysRating_Type()
)
fsaSysRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaSysRating.setStatus("current")


class _FsaSysTool_Type(DisplayString):
    """Custom type fsaSysTool based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FsaSysTool_Type.__name__ = "DisplayString"
_FsaSysTool_Object = MibScalar
fsaSysTool = _FsaSysTool_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 2, 3),
    _FsaSysTool_Type()
)
fsaSysTool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaSysTool.setStatus("current")


class _FsaSysSniffer_Type(DisplayString):
    """Custom type fsaSysSniffer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FsaSysSniffer_Type.__name__ = "DisplayString"
_FsaSysSniffer_Object = MibScalar
fsaSysSniffer = _FsaSysSniffer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 2, 4),
    _FsaSysSniffer_Type()
)
fsaSysSniffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaSysSniffer.setStatus("current")


class _FsaSysIPS_Type(DisplayString):
    """Custom type fsaSysIPS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FsaSysIPS_Type.__name__ = "DisplayString"
_FsaSysIPS_Object = MibScalar
fsaSysIPS = _FsaSysIPS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 2, 5),
    _FsaSysIPS_Type()
)
fsaSysIPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaSysIPS.setStatus("current")


class _FsaSysAndroidA_Type(DisplayString):
    """Custom type fsaSysAndroidA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FsaSysAndroidA_Type.__name__ = "DisplayString"
_FsaSysAndroidA_Object = MibScalar
fsaSysAndroidA = _FsaSysAndroidA_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 2, 6),
    _FsaSysAndroidA_Type()
)
fsaSysAndroidA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaSysAndroidA.setStatus("current")


class _FsaSysAndroidR_Type(DisplayString):
    """Custom type fsaSysAndroidR based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FsaSysAndroidR_Type.__name__ = "DisplayString"
_FsaSysAndroidR_Object = MibScalar
fsaSysAndroidR = _FsaSysAndroidR_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 2, 7),
    _FsaSysAndroidR_Type()
)
fsaSysAndroidR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaSysAndroidR.setStatus("current")
_FsaFwUsers_ObjectIdentity = ObjectIdentity
fsaFwUsers = _FsaFwUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 4)
)
_FsaFwUserInfo_ObjectIdentity = ObjectIdentity
fsaFwUserInfo = _FsaFwUserInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 4, 1)
)
_FsaFwUserNumber_Type = Integer32
_FsaFwUserNumber_Object = MibScalar
fsaFwUserNumber = _FsaFwUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 4, 1, 1),
    _FsaFwUserNumber_Type()
)
fsaFwUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaFwUserNumber.setStatus("current")
_FsaFwUserAuthTimeout_Type = Integer32
_FsaFwUserAuthTimeout_Object = MibScalar
fsaFwUserAuthTimeout = _FsaFwUserAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 4, 1, 2),
    _FsaFwUserAuthTimeout_Type()
)
fsaFwUserAuthTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaFwUserAuthTimeout.setStatus("current")
_FsaFwUserTables_ObjectIdentity = ObjectIdentity
fsaFwUserTables = _FsaFwUserTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 4, 2)
)
_FsaFwUserTable_Object = MibTable
fsaFwUserTable = _FsaFwUserTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 4, 2, 1)
)
if mibBuilder.loadTexts:
    fsaFwUserTable.setStatus("current")
_FsaFwUserEntry_Object = MibTableRow
fsaFwUserEntry = _FsaFwUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 4, 2, 1, 1)
)
fsaFwUserEntry.setIndexNames(
    (0, "FORTINET-FORTISANDBOX-MIB", "fsaFwUserIndex"),
)
if mibBuilder.loadTexts:
    fsaFwUserEntry.setStatus("current")
_FsaFwUserIndex_Type = FnIndex
_FsaFwUserIndex_Object = MibTableColumn
fsaFwUserIndex = _FsaFwUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 4, 2, 1, 1, 1),
    _FsaFwUserIndex_Type()
)
fsaFwUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsaFwUserIndex.setStatus("current")
_FsaFwUserName_Type = DisplayString
_FsaFwUserName_Object = MibTableColumn
fsaFwUserName = _FsaFwUserName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 4, 2, 1, 1, 2),
    _FsaFwUserName_Type()
)
fsaFwUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaFwUserName.setStatus("current")
_FsaFwUserAuth_Type = FsaUserAuthType
_FsaFwUserAuth_Object = MibTableColumn
fsaFwUserAuth = _FsaFwUserAuth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 4, 2, 1, 1, 3),
    _FsaFwUserAuth_Type()
)
fsaFwUserAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaFwUserAuth.setStatus("current")
_FsaFwUserState_Type = FnBoolState
_FsaFwUserState_Object = MibTableColumn
fsaFwUserState = _FsaFwUserState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 4, 2, 1, 1, 4),
    _FsaFwUserState_Type()
)
fsaFwUserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaFwUserState.setStatus("current")
_FsaJobInfo_ObjectIdentity = ObjectIdentity
fsaJobInfo = _FsaJobInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 5)
)
_FsaJobQueue_ObjectIdentity = ObjectIdentity
fsaJobQueue = _FsaJobQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 5, 1)
)
_FsaFTypeExe_Type = Integer32
_FsaFTypeExe_Object = MibScalar
fsaFTypeExe = _FsaFTypeExe_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 5, 1, 1),
    _FsaFTypeExe_Type()
)
fsaFTypeExe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaFTypeExe.setStatus("current")
_FsaFTypePDF_Type = Integer32
_FsaFTypePDF_Object = MibScalar
fsaFTypePDF = _FsaFTypePDF_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 5, 1, 2),
    _FsaFTypePDF_Type()
)
fsaFTypePDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaFTypePDF.setStatus("current")
_FsaFTypeDOC_Type = Integer32
_FsaFTypeDOC_Object = MibScalar
fsaFTypeDOC = _FsaFTypeDOC_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 5, 1, 3),
    _FsaFTypeDOC_Type()
)
fsaFTypeDOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaFTypeDOC.setStatus("current")
_FsaFTypeFLASH_Type = Integer32
_FsaFTypeFLASH_Object = MibScalar
fsaFTypeFLASH = _FsaFTypeFLASH_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 5, 1, 4),
    _FsaFTypeFLASH_Type()
)
fsaFTypeFLASH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaFTypeFLASH.setStatus("current")
_FsaFTypeWEB_Type = Integer32
_FsaFTypeWEB_Object = MibScalar
fsaFTypeWEB = _FsaFTypeWEB_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 5, 1, 5),
    _FsaFTypeWEB_Type()
)
fsaFTypeWEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaFTypeWEB.setStatus("current")
_FsaFTypeAndroid_Type = Integer32
_FsaFTypeAndroid_Object = MibScalar
fsaFTypeAndroid = _FsaFTypeAndroid_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 5, 1, 6),
    _FsaFTypeAndroid_Type()
)
fsaFTypeAndroid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaFTypeAndroid.setStatus("current")
_FsaFTypeMAC_Type = Integer32
_FsaFTypeMAC_Object = MibScalar
fsaFTypeMAC = _FsaFTypeMAC_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 5, 1, 7),
    _FsaFTypeMAC_Type()
)
fsaFTypeMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaFTypeMAC.setStatus("current")
_FsaFTypeURL_Type = Integer32
_FsaFTypeURL_Object = MibScalar
fsaFTypeURL = _FsaFTypeURL_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 5, 1, 8),
    _FsaFTypeURL_Type()
)
fsaFTypeURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaFTypeURL.setStatus("current")
_FsaFTypeExtra_Type = Integer32
_FsaFTypeExtra_Object = MibScalar
fsaFTypeExtra = _FsaFTypeExtra_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 5, 1, 9),
    _FsaFTypeExtra_Type()
)
fsaFTypeExtra.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaFTypeExtra.setStatus("current")
_FsaFTypeNOVM_Type = Integer32
_FsaFTypeNOVM_Object = MibScalar
fsaFTypeNOVM = _FsaFTypeNOVM_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 5, 1, 10),
    _FsaFTypeNOVM_Type()
)
fsaFTypeNOVM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaFTypeNOVM.setStatus("current")
_FsaFTypePre_Type = Integer32
_FsaFTypePre_Object = MibScalar
fsaFTypePre = _FsaFTypePre_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 5, 1, 11),
    _FsaFTypePre_Type()
)
fsaFTypePre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaFTypePre.setStatus("current")
_FsaJobProcessing_Type = Integer32
_FsaJobProcessing_Object = MibScalar
fsaJobProcessing = _FsaJobProcessing_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 5, 1, 12),
    _FsaJobProcessing_Type()
)
fsaJobProcessing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsaJobProcessing.setStatus("current")
_FsaTrapObjects_ObjectIdentity = ObjectIdentity
fsaTrapObjects = _FsaTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6)
)
_FsaTrapJobId_Type = DisplayString
_FsaTrapJobId_Object = MibScalar
fsaTrapJobId = _FsaTrapJobId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 1),
    _FsaTrapJobId_Type()
)
fsaTrapJobId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsaTrapJobId.setStatus("current")
_FsaTrapCPUrate_Type = DisplayString
_FsaTrapCPUrate_Object = MibScalar
fsaTrapCPUrate = _FsaTrapCPUrate_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 2),
    _FsaTrapCPUrate_Type()
)
fsaTrapCPUrate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsaTrapCPUrate.setStatus("current")
_FsaTrapMUrate_Type = DisplayString
_FsaTrapMUrate_Object = MibScalar
fsaTrapMUrate = _FsaTrapMUrate_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 3),
    _FsaTrapMUrate_Type()
)
fsaTrapMUrate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsaTrapMUrate.setStatus("current")
_FsaTrapDUrate_Type = DisplayString
_FsaTrapDUrate_Object = MibScalar
fsaTrapDUrate = _FsaTrapDUrate_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 4),
    _FsaTrapDUrate_Type()
)
fsaTrapDUrate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsaTrapDUrate.setStatus("current")
_FsaTrapPSUFailure_Type = DisplayString
_FsaTrapPSUFailure_Object = MibScalar
fsaTrapPSUFailure = _FsaTrapPSUFailure_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5),
    _FsaTrapPSUFailure_Type()
)
fsaTrapPSUFailure.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsaTrapPSUFailure.setStatus("current")
_FsaTrapHCTopology_Type = DisplayString
_FsaTrapHCTopology_Object = MibScalar
fsaTrapHCTopology = _FsaTrapHCTopology_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 6),
    _FsaTrapHCTopology_Type()
)
fsaTrapHCTopology.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsaTrapHCTopology.setStatus("current")
_FsaTrapHCHealth_Type = DisplayString
_FsaTrapHCHealth_Object = MibScalar
fsaTrapHCHealth = _FsaTrapHCHealth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 7),
    _FsaTrapHCHealth_Type()
)
fsaTrapHCHealth.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsaTrapHCHealth.setStatus("current")
_FsaMibConformance_ObjectIdentity = ObjectIdentity
fsaMibConformance = _FsaMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 10)
)

# Managed Objects groups

fsaSystemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 118, 10, 1)
)
fsaSystemObjectGroup.setObjects(
      *(("FORTINET-FORTISANDBOX-MIB", "fsaSysVersion"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaSysCpuUsage"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaSysMemUsage"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaSysMemCapacity"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaSysDiskUsage"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaSysDiskCapacity"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaSysCpuUsageExcludedNice"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaSysUpTime"))
)
if mibBuilder.loadTexts:
    fsaSystemObjectGroup.setStatus("current")

fsaSoftwareObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 118, 10, 2)
)
fsaSoftwareObjectGroup.setObjects(
      *(("FORTINET-FORTISANDBOX-MIB", "fsaSysTracer"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaSysRating"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaSysTool"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaSysSniffer"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaSysIPS"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaSysAndroidA"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaSysAndroidR"))
)
if mibBuilder.loadTexts:
    fsaSoftwareObjectGroup.setStatus("current")

fsaUserObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 118, 10, 3)
)
fsaUserObjectGroup.setObjects(
      *(("FORTINET-FORTISANDBOX-MIB", "fsaFwUserNumber"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaFwUserAuthTimeout"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaFwUserName"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaFwUserAuth"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaFwUserState"))
)
if mibBuilder.loadTexts:
    fsaUserObjectGroup.setStatus("current")

fsaJobObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 118, 10, 4)
)
fsaJobObjectGroup.setObjects(
      *(("FORTINET-FORTISANDBOX-MIB", "fsaFTypeExe"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaFTypePDF"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaFTypeDOC"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaFTypeFLASH"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaFTypeWEB"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaFTypeAndroid"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaFTypeMAC"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaFTypeURL"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaFTypeExtra"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaFTypeNOVM"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaFTypePre"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaJobProcessing"))
)
if mibBuilder.loadTexts:
    fsaJobObjectGroup.setStatus("current")


# Notification objects

fsaTrapMalware = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 0, 501)
)
fsaTrapMalware.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaTrapJobId"))
)
if mibBuilder.loadTexts:
    fsaTrapMalware.setStatus(
        "current"
    )

fsaTrapCPUHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 0, 502)
)
fsaTrapCPUHigh.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaTrapCPUrate"))
)
if mibBuilder.loadTexts:
    fsaTrapCPUHigh.setStatus(
        "current"
    )

fsaTrapMemHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 0, 503)
)
fsaTrapMemHigh.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaTrapMUrate"))
)
if mibBuilder.loadTexts:
    fsaTrapMemHigh.setStatus(
        "current"
    )

fsaTrapDUHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 0, 504)
)
fsaTrapDUHigh.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaTrapDUrate"))
)
if mibBuilder.loadTexts:
    fsaTrapDUHigh.setStatus(
        "current"
    )

fsaTrapPSUC = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 0, 505)
)
fsaTrapPSUC.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaTrapPSUFailure"))
)
if mibBuilder.loadTexts:
    fsaTrapPSUC.setStatus(
        "current"
    )

fsaTrapHCT = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 0, 506)
)
fsaTrapHCT.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaTrapHCTopology"))
)
if mibBuilder.loadTexts:
    fsaTrapHCT.setStatus(
        "current"
    )

fsaTrapHCH = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 0, 507)
)
fsaTrapHCH.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaTrapHCHealth"))
)
if mibBuilder.loadTexts:
    fsaTrapHCH.setStatus(
        "current"
    )


# Notifications groups

fsaNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12356, 118, 10, 5)
)
fsaNotificationGroup.setObjects(
      *(("FORTINET-FORTISANDBOX-MIB", "fsaTrapMalware"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaTrapCPUHigh"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaTrapMemHigh"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaTrapDUHigh"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaTrapPSUC"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaTrapHCT"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaTrapHCH"))
)
if mibBuilder.loadTexts:
    fsaNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fsaMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12356, 118, 10, 100)
)
fsaMIBCompliance.setObjects(
      *(("FORTINET-FORTISANDBOX-MIB", "fsaNotificationGroup"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaSystemObjectGroup"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaSoftwareObjectGroup"),
        ("FORTINET-FORTISANDBOX-MIB", "fsaJobObjectGroup"))
)
if mibBuilder.loadTexts:
    fsaMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORTINET-FORTISANDBOX-MIB",
    **{"FsaAdminPermLevel": FsaAdminPermLevel,
       "FsaUserAuthType": FsaUserAuthType,
       "FsaSessProto": FsaSessProto,
       "fnFortiSandboxMib": fnFortiSandboxMib,
       "fsaModel": fsaModel,
       "fsa1000D": fsa1000D,
       "fsaVM": fsaVM,
       "fsa3000D": fsa3000D,
       "fsa3500D": fsa3500D,
       "fsa3000E": fsa3000E,
       "fsa2000E": fsa2000E,
       "fsa1000F": fsa1000F,
       "fsa500F": fsa500F,
       "fsaTraps": fsaTraps,
       "fsaTrapPrefix": fsaTrapPrefix,
       "fsaTrapMalware": fsaTrapMalware,
       "fsaTrapCPUHigh": fsaTrapCPUHigh,
       "fsaTrapMemHigh": fsaTrapMemHigh,
       "fsaTrapDUHigh": fsaTrapDUHigh,
       "fsaTrapPSUC": fsaTrapPSUC,
       "fsaTrapHCT": fsaTrapHCT,
       "fsaTrapHCH": fsaTrapHCH,
       "fsaSystem": fsaSystem,
       "fsaSystemInfo": fsaSystemInfo,
       "fsaSysVersion": fsaSysVersion,
       "fsaSysCpuUsage": fsaSysCpuUsage,
       "fsaSysMemUsage": fsaSysMemUsage,
       "fsaSysMemCapacity": fsaSysMemCapacity,
       "fsaSysDiskUsage": fsaSysDiskUsage,
       "fsaSysDiskCapacity": fsaSysDiskCapacity,
       "fsaSysCpuUsageExcludedNice": fsaSysCpuUsageExcludedNice,
       "fsaSysUpTime": fsaSysUpTime,
       "fsaSoftware": fsaSoftware,
       "fsaSysTracer": fsaSysTracer,
       "fsaSysRating": fsaSysRating,
       "fsaSysTool": fsaSysTool,
       "fsaSysSniffer": fsaSysSniffer,
       "fsaSysIPS": fsaSysIPS,
       "fsaSysAndroidA": fsaSysAndroidA,
       "fsaSysAndroidR": fsaSysAndroidR,
       "fsaFwUsers": fsaFwUsers,
       "fsaFwUserInfo": fsaFwUserInfo,
       "fsaFwUserNumber": fsaFwUserNumber,
       "fsaFwUserAuthTimeout": fsaFwUserAuthTimeout,
       "fsaFwUserTables": fsaFwUserTables,
       "fsaFwUserTable": fsaFwUserTable,
       "fsaFwUserEntry": fsaFwUserEntry,
       "fsaFwUserIndex": fsaFwUserIndex,
       "fsaFwUserName": fsaFwUserName,
       "fsaFwUserAuth": fsaFwUserAuth,
       "fsaFwUserState": fsaFwUserState,
       "fsaJobInfo": fsaJobInfo,
       "fsaJobQueue": fsaJobQueue,
       "fsaFTypeExe": fsaFTypeExe,
       "fsaFTypePDF": fsaFTypePDF,
       "fsaFTypeDOC": fsaFTypeDOC,
       "fsaFTypeFLASH": fsaFTypeFLASH,
       "fsaFTypeWEB": fsaFTypeWEB,
       "fsaFTypeAndroid": fsaFTypeAndroid,
       "fsaFTypeMAC": fsaFTypeMAC,
       "fsaFTypeURL": fsaFTypeURL,
       "fsaFTypeExtra": fsaFTypeExtra,
       "fsaFTypeNOVM": fsaFTypeNOVM,
       "fsaFTypePre": fsaFTypePre,
       "fsaJobProcessing": fsaJobProcessing,
       "fsaTrapObjects": fsaTrapObjects,
       "fsaTrapJobId": fsaTrapJobId,
       "fsaTrapCPUrate": fsaTrapCPUrate,
       "fsaTrapMUrate": fsaTrapMUrate,
       "fsaTrapDUrate": fsaTrapDUrate,
       "fsaTrapPSUFailure": fsaTrapPSUFailure,
       "fsaTrapHCTopology": fsaTrapHCTopology,
       "fsaTrapHCHealth": fsaTrapHCHealth,
       "fsaMibConformance": fsaMibConformance,
       "fsaSystemObjectGroup": fsaSystemObjectGroup,
       "fsaSoftwareObjectGroup": fsaSoftwareObjectGroup,
       "fsaUserObjectGroup": fsaUserObjectGroup,
       "fsaJobObjectGroup": fsaJobObjectGroup,
       "fsaNotificationGroup": fsaNotificationGroup,
       "fsaMIBCompliance": fsaMIBCompliance}
)
