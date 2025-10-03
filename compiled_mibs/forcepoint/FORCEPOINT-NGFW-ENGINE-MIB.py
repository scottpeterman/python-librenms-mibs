# SNMP MIB module (FORCEPOINT-NGFW-ENGINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\forcepoint\FORCEPOINT-NGFW-ENGINE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:40 2025
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

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
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

forcepointNGFWEngineMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1)
)
if mibBuilder.loadTexts:
    forcepointNGFWEngineMib.setRevisions(
        ("2021-12-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VpnEndpointType(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("static", 1),
          ("dynamic", 2),
          ("mobile", 3))
    )



class FwHwComponentStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", -1),
          ("ok", 0),
          ("warning", 1),
          ("error", 2),
          ("fatalError", 3))
    )



class FwFixedThousandths(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-3"


# MIB Managed Objects in the order of their OIDs

_EngineNotifications_ObjectIdentity = ObjectIdentity
engineNotifications = _EngineNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 0)
)
_EngineObjects_ObjectIdentity = ObjectIdentity
engineObjects = _EngineObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1)
)
_FwSoftwareVersion_Type = DisplayString
_FwSoftwareVersion_Object = MibScalar
fwSoftwareVersion = _FwSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 1),
    _FwSoftwareVersion_Type()
)
fwSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSoftwareVersion.setStatus("current")
_FwSecurityPolicy_Type = DisplayString
_FwSecurityPolicy_Object = MibScalar
fwSecurityPolicy = _FwSecurityPolicy_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 2),
    _FwSecurityPolicy_Type()
)
fwSecurityPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSecurityPolicy.setStatus("current")
_FwPolicyTime_Type = TimeStamp
_FwPolicyTime_Object = MibScalar
fwPolicyTime = _FwPolicyTime_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 3),
    _FwPolicyTime_Type()
)
fwPolicyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwPolicyTime.setStatus("current")
_FwConnNumber_Type = CounterBasedGauge64
_FwConnNumber_Object = MibScalar
fwConnNumber = _FwConnNumber_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 4),
    _FwConnNumber_Type()
)
fwConnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwConnNumber.setStatus("current")
_FwAccepted_Type = Counter64
_FwAccepted_Object = MibScalar
fwAccepted = _FwAccepted_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 5),
    _FwAccepted_Type()
)
fwAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwAccepted.setStatus("current")
_FwDropped_Type = Counter64
_FwDropped_Object = MibScalar
fwDropped = _FwDropped_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 6),
    _FwDropped_Type()
)
fwDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDropped.setStatus("current")
_FwLogged_Type = Counter64
_FwLogged_Object = MibScalar
fwLogged = _FwLogged_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 7),
    _FwLogged_Type()
)
fwLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwLogged.setStatus("current")
_FwAccounted_Type = Counter64
_FwAccounted_Object = MibScalar
fwAccounted = _FwAccounted_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 8),
    _FwAccounted_Type()
)
fwAccounted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwAccounted.setStatus("current")
_FwRejected_Type = Counter64
_FwRejected_Object = MibScalar
fwRejected = _FwRejected_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 9),
    _FwRejected_Type()
)
fwRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwRejected.setStatus("current")
_FwIfStatsTable_Object = MibTable
fwIfStatsTable = _FwIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    fwIfStatsTable.setStatus("current")
_FwIfStatsEntry_Object = MibTableRow
fwIfStatsEntry = _FwIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 10, 1)
)
fwIfStatsEntry.setIndexNames(
    (0, "FORCEPOINT-NGFW-ENGINE-MIB", "fwIfStatsIndex"),
)
if mibBuilder.loadTexts:
    fwIfStatsEntry.setStatus("current")


class _FwIfStatsIndex_Type(Integer32):
    """Custom type fwIfStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FwIfStatsIndex_Type.__name__ = "Integer32"
_FwIfStatsIndex_Object = MibTableColumn
fwIfStatsIndex = _FwIfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 10, 1, 1),
    _FwIfStatsIndex_Type()
)
fwIfStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwIfStatsIndex.setStatus("current")
_FwIfName_Type = DisplayString
_FwIfName_Object = MibTableColumn
fwIfName = _FwIfName_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 10, 1, 2),
    _FwIfName_Type()
)
fwIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfName.setStatus("current")
_FwIfAcceptedPkts_Type = Counter64
_FwIfAcceptedPkts_Object = MibTableColumn
fwIfAcceptedPkts = _FwIfAcceptedPkts_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 10, 1, 3),
    _FwIfAcceptedPkts_Type()
)
fwIfAcceptedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfAcceptedPkts.setStatus("current")
_FwIfDroppedPkts_Type = Counter64
_FwIfDroppedPkts_Object = MibTableColumn
fwIfDroppedPkts = _FwIfDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 10, 1, 4),
    _FwIfDroppedPkts_Type()
)
fwIfDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfDroppedPkts.setStatus("current")
_FwIfLoggedPkts_Type = Counter64
_FwIfLoggedPkts_Object = MibTableColumn
fwIfLoggedPkts = _FwIfLoggedPkts_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 10, 1, 5),
    _FwIfLoggedPkts_Type()
)
fwIfLoggedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfLoggedPkts.setStatus("current")
_FwIfAccountedPkts_Type = Counter64
_FwIfAccountedPkts_Object = MibTableColumn
fwIfAccountedPkts = _FwIfAccountedPkts_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 10, 1, 6),
    _FwIfAccountedPkts_Type()
)
fwIfAccountedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfAccountedPkts.setStatus("current")
_FwIfRejectedPkts_Type = Counter64
_FwIfRejectedPkts_Object = MibTableColumn
fwIfRejectedPkts = _FwIfRejectedPkts_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 10, 1, 7),
    _FwIfRejectedPkts_Type()
)
fwIfRejectedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfRejectedPkts.setStatus("current")
_FwIfAcceptedBytes_Type = Counter64
_FwIfAcceptedBytes_Object = MibTableColumn
fwIfAcceptedBytes = _FwIfAcceptedBytes_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 10, 1, 8),
    _FwIfAcceptedBytes_Type()
)
fwIfAcceptedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfAcceptedBytes.setStatus("current")
_FwIfDroppedBytes_Type = Counter64
_FwIfDroppedBytes_Object = MibTableColumn
fwIfDroppedBytes = _FwIfDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 10, 1, 9),
    _FwIfDroppedBytes_Type()
)
fwIfDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfDroppedBytes.setStatus("current")
_FwIfLoggedBytes_Type = Counter64
_FwIfLoggedBytes_Object = MibTableColumn
fwIfLoggedBytes = _FwIfLoggedBytes_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 10, 1, 10),
    _FwIfLoggedBytes_Type()
)
fwIfLoggedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfLoggedBytes.setStatus("current")
_FwIfAccountedBytes_Type = Counter64
_FwIfAccountedBytes_Object = MibTableColumn
fwIfAccountedBytes = _FwIfAccountedBytes_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 10, 1, 11),
    _FwIfAccountedBytes_Type()
)
fwIfAccountedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfAccountedBytes.setStatus("current")
_FwIfRejectedBytes_Type = Counter64
_FwIfRejectedBytes_Object = MibTableColumn
fwIfRejectedBytes = _FwIfRejectedBytes_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 10, 1, 12),
    _FwIfRejectedBytes_Type()
)
fwIfRejectedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfRejectedBytes.setStatus("current")
_FwIfForwardedPkts_Type = Counter64
_FwIfForwardedPkts_Object = MibTableColumn
fwIfForwardedPkts = _FwIfForwardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 10, 1, 13),
    _FwIfForwardedPkts_Type()
)
fwIfForwardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfForwardedPkts.setStatus("current")
_FwIfForwardedBytes_Type = Counter64
_FwIfForwardedBytes_Object = MibTableColumn
fwIfForwardedBytes = _FwIfForwardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 10, 1, 14),
    _FwIfForwardedBytes_Type()
)
fwIfForwardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfForwardedBytes.setStatus("current")
_FwIfComment_Type = DisplayString
_FwIfComment_Object = MibTableColumn
fwIfComment = _FwIfComment_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 10, 1, 15),
    _FwIfComment_Type()
)
fwIfComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfComment.setStatus("current")
_FwHardware_ObjectIdentity = ObjectIdentity
fwHardware = _FwHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11)
)
_FwCpuStatsTable_Object = MibTable
fwCpuStatsTable = _FwCpuStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    fwCpuStatsTable.setStatus("current")
_FwCpuStatsEntry_Object = MibTableRow
fwCpuStatsEntry = _FwCpuStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 1, 1)
)
fwCpuStatsEntry.setIndexNames(
    (0, "FORCEPOINT-NGFW-ENGINE-MIB", "fwCpuStatsId"),
)
if mibBuilder.loadTexts:
    fwCpuStatsEntry.setStatus("current")


class _FwCpuStatsId_Type(Integer32):
    """Custom type fwCpuStatsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FwCpuStatsId_Type.__name__ = "Integer32"
_FwCpuStatsId_Object = MibTableColumn
fwCpuStatsId = _FwCpuStatsId_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 1, 1, 1),
    _FwCpuStatsId_Type()
)
fwCpuStatsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwCpuStatsId.setStatus("current")
_FwCpuName_Type = DisplayString
_FwCpuName_Object = MibTableColumn
fwCpuName = _FwCpuName_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 1, 1, 2),
    _FwCpuName_Type()
)
fwCpuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwCpuName.setStatus("current")
_FwCpuTotal_Type = Unsigned32
_FwCpuTotal_Object = MibTableColumn
fwCpuTotal = _FwCpuTotal_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 1, 1, 3),
    _FwCpuTotal_Type()
)
fwCpuTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwCpuTotal.setStatus("current")
if mibBuilder.loadTexts:
    fwCpuTotal.setUnits("percent")
_FwCpuUser_Type = Unsigned32
_FwCpuUser_Object = MibTableColumn
fwCpuUser = _FwCpuUser_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 1, 1, 4),
    _FwCpuUser_Type()
)
fwCpuUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwCpuUser.setStatus("current")
if mibBuilder.loadTexts:
    fwCpuUser.setUnits("percent")
_FwCpuSystem_Type = Unsigned32
_FwCpuSystem_Object = MibTableColumn
fwCpuSystem = _FwCpuSystem_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 1, 1, 5),
    _FwCpuSystem_Type()
)
fwCpuSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwCpuSystem.setStatus("current")
if mibBuilder.loadTexts:
    fwCpuSystem.setUnits("percent")
_FwCpuNice_Type = Unsigned32
_FwCpuNice_Object = MibTableColumn
fwCpuNice = _FwCpuNice_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 1, 1, 6),
    _FwCpuNice_Type()
)
fwCpuNice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwCpuNice.setStatus("current")
if mibBuilder.loadTexts:
    fwCpuNice.setUnits("percent")
_FwCpuIdle_Type = Unsigned32
_FwCpuIdle_Object = MibTableColumn
fwCpuIdle = _FwCpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 1, 1, 7),
    _FwCpuIdle_Type()
)
fwCpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwCpuIdle.setStatus("current")
if mibBuilder.loadTexts:
    fwCpuIdle.setUnits("percent")
_FwCpuIoWait_Type = Unsigned32
_FwCpuIoWait_Object = MibTableColumn
fwCpuIoWait = _FwCpuIoWait_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 1, 1, 8),
    _FwCpuIoWait_Type()
)
fwCpuIoWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwCpuIoWait.setStatus("current")
if mibBuilder.loadTexts:
    fwCpuIoWait.setUnits("percent")
_FwCpuHwIrq_Type = Unsigned32
_FwCpuHwIrq_Object = MibTableColumn
fwCpuHwIrq = _FwCpuHwIrq_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 1, 1, 9),
    _FwCpuHwIrq_Type()
)
fwCpuHwIrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwCpuHwIrq.setStatus("current")
if mibBuilder.loadTexts:
    fwCpuHwIrq.setUnits("percent")
_FwCpuSoftIrq_Type = Unsigned32
_FwCpuSoftIrq_Object = MibTableColumn
fwCpuSoftIrq = _FwCpuSoftIrq_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 1, 1, 10),
    _FwCpuSoftIrq_Type()
)
fwCpuSoftIrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwCpuSoftIrq.setStatus("current")
if mibBuilder.loadTexts:
    fwCpuSoftIrq.setUnits("percent")
_FwMemoryInfo_ObjectIdentity = ObjectIdentity
fwMemoryInfo = _FwMemoryInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 2)
)
_FwSwapBytesTotal_Type = CounterBasedGauge64
_FwSwapBytesTotal_Object = MibScalar
fwSwapBytesTotal = _FwSwapBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 2, 1),
    _FwSwapBytesTotal_Type()
)
fwSwapBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSwapBytesTotal.setStatus("current")
if mibBuilder.loadTexts:
    fwSwapBytesTotal.setUnits("bytes")
_FwSwapBytesUsed_Type = CounterBasedGauge64
_FwSwapBytesUsed_Object = MibScalar
fwSwapBytesUsed = _FwSwapBytesUsed_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 2, 2),
    _FwSwapBytesUsed_Type()
)
fwSwapBytesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSwapBytesUsed.setStatus("current")
if mibBuilder.loadTexts:
    fwSwapBytesUsed.setUnits("bytes")
_FwSwapBytesUnused_Type = CounterBasedGauge64
_FwSwapBytesUnused_Object = MibScalar
fwSwapBytesUnused = _FwSwapBytesUnused_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 2, 3),
    _FwSwapBytesUnused_Type()
)
fwSwapBytesUnused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSwapBytesUnused.setStatus("current")
if mibBuilder.loadTexts:
    fwSwapBytesUnused.setUnits("bytes")
_FwMemBytesTotal_Type = CounterBasedGauge64
_FwMemBytesTotal_Object = MibScalar
fwMemBytesTotal = _FwMemBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 2, 4),
    _FwMemBytesTotal_Type()
)
fwMemBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMemBytesTotal.setStatus("current")
if mibBuilder.loadTexts:
    fwMemBytesTotal.setUnits("bytes")
_FwMemBytesUsed_Type = CounterBasedGauge64
_FwMemBytesUsed_Object = MibScalar
fwMemBytesUsed = _FwMemBytesUsed_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 2, 5),
    _FwMemBytesUsed_Type()
)
fwMemBytesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMemBytesUsed.setStatus("current")
if mibBuilder.loadTexts:
    fwMemBytesUsed.setUnits("bytes")
_FwMemBytesUnused_Type = CounterBasedGauge64
_FwMemBytesUnused_Object = MibScalar
fwMemBytesUnused = _FwMemBytesUnused_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 2, 6),
    _FwMemBytesUnused_Type()
)
fwMemBytesUnused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMemBytesUnused.setStatus("current")
if mibBuilder.loadTexts:
    fwMemBytesUnused.setUnits("bytes")
_FwMemBytesBuffers_Type = CounterBasedGauge64
_FwMemBytesBuffers_Object = MibScalar
fwMemBytesBuffers = _FwMemBytesBuffers_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 2, 7),
    _FwMemBytesBuffers_Type()
)
fwMemBytesBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMemBytesBuffers.setStatus("current")
if mibBuilder.loadTexts:
    fwMemBytesBuffers.setUnits("bytes")
_FwMemBytesCached_Type = CounterBasedGauge64
_FwMemBytesCached_Object = MibScalar
fwMemBytesCached = _FwMemBytesCached_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 2, 8),
    _FwMemBytesCached_Type()
)
fwMemBytesCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMemBytesCached.setStatus("current")
if mibBuilder.loadTexts:
    fwMemBytesCached.setUnits("bytes")
_FwMemBytesSReclaimable_Type = CounterBasedGauge64
_FwMemBytesSReclaimable_Object = MibScalar
fwMemBytesSReclaimable = _FwMemBytesSReclaimable_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 2, 9),
    _FwMemBytesSReclaimable_Type()
)
fwMemBytesSReclaimable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMemBytesSReclaimable.setStatus("current")
if mibBuilder.loadTexts:
    fwMemBytesSReclaimable.setUnits("bytes")
_FwMemBytesAvailable_Type = CounterBasedGauge64
_FwMemBytesAvailable_Object = MibScalar
fwMemBytesAvailable = _FwMemBytesAvailable_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 2, 10),
    _FwMemBytesAvailable_Type()
)
fwMemBytesAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMemBytesAvailable.setStatus("current")
if mibBuilder.loadTexts:
    fwMemBytesAvailable.setUnits("bytes")
_FwDiskStatsTable_Object = MibTable
fwDiskStatsTable = _FwDiskStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 3)
)
if mibBuilder.loadTexts:
    fwDiskStatsTable.setStatus("current")
_FwDiskStatsEntry_Object = MibTableRow
fwDiskStatsEntry = _FwDiskStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 3, 1)
)
fwDiskStatsEntry.setIndexNames(
    (0, "FORCEPOINT-NGFW-ENGINE-MIB", "fwPartitionIndex"),
)
if mibBuilder.loadTexts:
    fwDiskStatsEntry.setStatus("current")


class _FwPartitionIndex_Type(Integer32):
    """Custom type fwPartitionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FwPartitionIndex_Type.__name__ = "Integer32"
_FwPartitionIndex_Object = MibTableColumn
fwPartitionIndex = _FwPartitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 3, 1, 1),
    _FwPartitionIndex_Type()
)
fwPartitionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwPartitionIndex.setStatus("current")
_FwPartitionDevName_Type = DisplayString
_FwPartitionDevName_Object = MibTableColumn
fwPartitionDevName = _FwPartitionDevName_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 3, 1, 2),
    _FwPartitionDevName_Type()
)
fwPartitionDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwPartitionDevName.setStatus("current")
_FwMountPointName_Type = DisplayString
_FwMountPointName_Object = MibTableColumn
fwMountPointName = _FwMountPointName_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 3, 1, 3),
    _FwMountPointName_Type()
)
fwMountPointName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMountPointName.setStatus("current")
_FwPartitionSize_Type = CounterBasedGauge64
_FwPartitionSize_Object = MibTableColumn
fwPartitionSize = _FwPartitionSize_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 3, 1, 4),
    _FwPartitionSize_Type()
)
fwPartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwPartitionSize.setStatus("current")
if mibBuilder.loadTexts:
    fwPartitionSize.setUnits("kbytes")
_FwPartitionUsed_Type = CounterBasedGauge64
_FwPartitionUsed_Object = MibTableColumn
fwPartitionUsed = _FwPartitionUsed_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 3, 1, 5),
    _FwPartitionUsed_Type()
)
fwPartitionUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwPartitionUsed.setStatus("current")
if mibBuilder.loadTexts:
    fwPartitionUsed.setUnits("kbytes")
_FwPartitionAvail_Type = CounterBasedGauge64
_FwPartitionAvail_Object = MibTableColumn
fwPartitionAvail = _FwPartitionAvail_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 3, 1, 6),
    _FwPartitionAvail_Type()
)
fwPartitionAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwPartitionAvail.setStatus("current")
if mibBuilder.loadTexts:
    fwPartitionAvail.setUnits("kbytes")
_FwNewConnectionsS_Type = Counter64
_FwNewConnectionsS_Object = MibScalar
fwNewConnectionsS = _FwNewConnectionsS_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 4),
    _FwNewConnectionsS_Type()
)
fwNewConnectionsS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwNewConnectionsS.setStatus("current")
_FwDiscardedConnectionsS_Type = Counter64
_FwDiscardedConnectionsS_Object = MibScalar
fwDiscardedConnectionsS = _FwDiscardedConnectionsS_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 5),
    _FwDiscardedConnectionsS_Type()
)
fwDiscardedConnectionsS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDiscardedConnectionsS.setStatus("current")
_FwRefusedConnectionsS_Type = Counter64
_FwRefusedConnectionsS_Object = MibScalar
fwRefusedConnectionsS = _FwRefusedConnectionsS_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 11, 6),
    _FwRefusedConnectionsS_Type()
)
fwRefusedConnectionsS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwRefusedConnectionsS.setStatus("current")
_FwVpnEp4Table_Object = MibTable
fwVpnEp4Table = _FwVpnEp4Table_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 12)
)
if mibBuilder.loadTexts:
    fwVpnEp4Table.setStatus("current")
_FwVpnEp4Entry_Object = MibTableRow
fwVpnEp4Entry = _FwVpnEp4Entry_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 12, 1)
)
fwVpnEp4Entry.setIndexNames(
    (0, "FORCEPOINT-NGFW-ENGINE-MIB", "fwVpnEp4Index"),
)
if mibBuilder.loadTexts:
    fwVpnEp4Entry.setStatus("current")


class _FwVpnEp4Index_Type(Integer32):
    """Custom type fwVpnEp4Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FwVpnEp4Index_Type.__name__ = "Integer32"
_FwVpnEp4Index_Object = MibTableColumn
fwVpnEp4Index = _FwVpnEp4Index_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 12, 1, 1),
    _FwVpnEp4Index_Type()
)
fwVpnEp4Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwVpnEp4Index.setStatus("current")
_FwVpnEp4Local_Type = InetAddressIPv4
_FwVpnEp4Local_Object = MibTableColumn
fwVpnEp4Local = _FwVpnEp4Local_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 12, 1, 2),
    _FwVpnEp4Local_Type()
)
fwVpnEp4Local.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVpnEp4Local.setStatus("current")
_FwVpnEp4Remote_Type = InetAddressIPv4
_FwVpnEp4Remote_Object = MibTableColumn
fwVpnEp4Remote = _FwVpnEp4Remote_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 12, 1, 3),
    _FwVpnEp4Remote_Type()
)
fwVpnEp4Remote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVpnEp4Remote.setStatus("current")
_FwVpnEp4RemoteType_Type = VpnEndpointType
_FwVpnEp4RemoteType_Object = MibTableColumn
fwVpnEp4RemoteType = _FwVpnEp4RemoteType_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 12, 1, 4),
    _FwVpnEp4RemoteType_Type()
)
fwVpnEp4RemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVpnEp4RemoteType.setStatus("current")
_FwVpnEp4ReceivedBytes_Type = Counter64
_FwVpnEp4ReceivedBytes_Object = MibTableColumn
fwVpnEp4ReceivedBytes = _FwVpnEp4ReceivedBytes_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 12, 1, 5),
    _FwVpnEp4ReceivedBytes_Type()
)
fwVpnEp4ReceivedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVpnEp4ReceivedBytes.setStatus("current")
_FwVpnEp4SentBytes_Type = Counter64
_FwVpnEp4SentBytes_Object = MibTableColumn
fwVpnEp4SentBytes = _FwVpnEp4SentBytes_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 12, 1, 6),
    _FwVpnEp4SentBytes_Type()
)
fwVpnEp4SentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVpnEp4SentBytes.setStatus("current")
_FwVpnEp4IpsecSa_Type = Counter32
_FwVpnEp4IpsecSa_Object = MibTableColumn
fwVpnEp4IpsecSa = _FwVpnEp4IpsecSa_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 12, 1, 7),
    _FwVpnEp4IpsecSa_Type()
)
fwVpnEp4IpsecSa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVpnEp4IpsecSa.setStatus("current")
_FwVpnEp6Table_Object = MibTable
fwVpnEp6Table = _FwVpnEp6Table_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 13)
)
if mibBuilder.loadTexts:
    fwVpnEp6Table.setStatus("current")
_FwVpnEp6Entry_Object = MibTableRow
fwVpnEp6Entry = _FwVpnEp6Entry_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 13, 1)
)
fwVpnEp6Entry.setIndexNames(
    (0, "FORCEPOINT-NGFW-ENGINE-MIB", "fwVpnEp6Index"),
)
if mibBuilder.loadTexts:
    fwVpnEp6Entry.setStatus("current")


class _FwVpnEp6Index_Type(Integer32):
    """Custom type fwVpnEp6Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FwVpnEp6Index_Type.__name__ = "Integer32"
_FwVpnEp6Index_Object = MibTableColumn
fwVpnEp6Index = _FwVpnEp6Index_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 13, 1, 1),
    _FwVpnEp6Index_Type()
)
fwVpnEp6Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwVpnEp6Index.setStatus("current")
_FwVpnEp6Local_Type = InetAddressIPv6
_FwVpnEp6Local_Object = MibTableColumn
fwVpnEp6Local = _FwVpnEp6Local_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 13, 1, 2),
    _FwVpnEp6Local_Type()
)
fwVpnEp6Local.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVpnEp6Local.setStatus("current")
_FwVpnEp6Remote_Type = InetAddressIPv6
_FwVpnEp6Remote_Object = MibTableColumn
fwVpnEp6Remote = _FwVpnEp6Remote_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 13, 1, 3),
    _FwVpnEp6Remote_Type()
)
fwVpnEp6Remote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVpnEp6Remote.setStatus("current")
_FwVpnEp6RemoteType_Type = VpnEndpointType
_FwVpnEp6RemoteType_Object = MibTableColumn
fwVpnEp6RemoteType = _FwVpnEp6RemoteType_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 13, 1, 4),
    _FwVpnEp6RemoteType_Type()
)
fwVpnEp6RemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVpnEp6RemoteType.setStatus("current")
_FwVpnEp6ReceivedBytes_Type = Counter64
_FwVpnEp6ReceivedBytes_Object = MibTableColumn
fwVpnEp6ReceivedBytes = _FwVpnEp6ReceivedBytes_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 13, 1, 5),
    _FwVpnEp6ReceivedBytes_Type()
)
fwVpnEp6ReceivedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVpnEp6ReceivedBytes.setStatus("current")
_FwVpnEp6SentBytes_Type = Counter64
_FwVpnEp6SentBytes_Object = MibTableColumn
fwVpnEp6SentBytes = _FwVpnEp6SentBytes_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 13, 1, 6),
    _FwVpnEp6SentBytes_Type()
)
fwVpnEp6SentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVpnEp6SentBytes.setStatus("current")
_FwVpnEp6IpsecSa_Type = Counter32
_FwVpnEp6IpsecSa_Object = MibTableColumn
fwVpnEp6IpsecSa = _FwVpnEp6IpsecSa_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 13, 1, 7),
    _FwVpnEp6IpsecSa_Type()
)
fwVpnEp6IpsecSa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVpnEp6IpsecSa.setStatus("current")
_FwMbrInterfaceTable_Object = MibTable
fwMbrInterfaceTable = _FwMbrInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 14)
)
if mibBuilder.loadTexts:
    fwMbrInterfaceTable.setStatus("current")
_FwMbrInterfaceEntry_Object = MibTableRow
fwMbrInterfaceEntry = _FwMbrInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 14, 1)
)
fwMbrInterfaceEntry.setIndexNames(
    (0, "FORCEPOINT-NGFW-ENGINE-MIB", "fwMbrInterfaceIndex"),
)
if mibBuilder.loadTexts:
    fwMbrInterfaceEntry.setStatus("current")


class _FwMbrInterfaceIndex_Type(Integer32):
    """Custom type fwMbrInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FwMbrInterfaceIndex_Type.__name__ = "Integer32"
_FwMbrInterfaceIndex_Object = MibTableColumn
fwMbrInterfaceIndex = _FwMbrInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 14, 1, 1),
    _FwMbrInterfaceIndex_Type()
)
fwMbrInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwMbrInterfaceIndex.setStatus("current")
_FwMbrName_Type = DisplayString
_FwMbrName_Object = MibTableColumn
fwMbrName = _FwMbrName_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 14, 1, 2),
    _FwMbrName_Type()
)
fwMbrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMbrName.setStatus("current")
_FwMbrBandUsed_Type = DisplayString
_FwMbrBandUsed_Object = MibTableColumn
fwMbrBandUsed = _FwMbrBandUsed_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 14, 1, 3),
    _FwMbrBandUsed_Type()
)
fwMbrBandUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMbrBandUsed.setStatus("current")
_FwMbrSignalStrength_Type = Integer32
_FwMbrSignalStrength_Object = MibTableColumn
fwMbrSignalStrength = _FwMbrSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 14, 1, 4),
    _FwMbrSignalStrength_Type()
)
fwMbrSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMbrSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    fwMbrSignalStrength.setUnits("dBm")
_FwMbrStatus_Type = FwHwComponentStatus
_FwMbrStatus_Object = MibTableColumn
fwMbrStatus = _FwMbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 14, 1, 5),
    _FwMbrStatus_Type()
)
fwMbrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMbrStatus.setStatus("current")
_FwDiskSerialNumber_Type = DisplayString
_FwDiskSerialNumber_Object = MibScalar
fwDiskSerialNumber = _FwDiskSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 15),
    _FwDiskSerialNumber_Type()
)
fwDiskSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDiskSerialNumber.setStatus("current")
_FwHwTempSensorTable_Object = MibTable
fwHwTempSensorTable = _FwHwTempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 16)
)
if mibBuilder.loadTexts:
    fwHwTempSensorTable.setStatus("current")
_FwHwTempSensorEntry_Object = MibTableRow
fwHwTempSensorEntry = _FwHwTempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 16, 1)
)
fwHwTempSensorEntry.setIndexNames(
    (0, "FORCEPOINT-NGFW-ENGINE-MIB", "fwHwTempSensorIndex"),
)
if mibBuilder.loadTexts:
    fwHwTempSensorEntry.setStatus("current")


class _FwHwTempSensorIndex_Type(Integer32):
    """Custom type fwHwTempSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FwHwTempSensorIndex_Type.__name__ = "Integer32"
_FwHwTempSensorIndex_Object = MibTableColumn
fwHwTempSensorIndex = _FwHwTempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 16, 1, 1),
    _FwHwTempSensorIndex_Type()
)
fwHwTempSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwHwTempSensorIndex.setStatus("current")
_FwHwTemperatureName_Type = DisplayString
_FwHwTemperatureName_Object = MibTableColumn
fwHwTemperatureName = _FwHwTemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 16, 1, 2),
    _FwHwTemperatureName_Type()
)
fwHwTemperatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHwTemperatureName.setStatus("current")
_FwHwTemperature_Type = Integer32
_FwHwTemperature_Object = MibTableColumn
fwHwTemperature = _FwHwTemperature_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 16, 1, 3),
    _FwHwTemperature_Type()
)
fwHwTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHwTemperature.setStatus("current")
if mibBuilder.loadTexts:
    fwHwTemperature.setUnits("degrees C")
_FwHwTemperatureStatus_Type = FwHwComponentStatus
_FwHwTemperatureStatus_Object = MibTableColumn
fwHwTemperatureStatus = _FwHwTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 16, 1, 4),
    _FwHwTemperatureStatus_Type()
)
fwHwTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHwTemperatureStatus.setStatus("current")
_FwPsuTable_Object = MibTable
fwPsuTable = _FwPsuTable_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 17)
)
if mibBuilder.loadTexts:
    fwPsuTable.setStatus("current")
_FwPsuEntry_Object = MibTableRow
fwPsuEntry = _FwPsuEntry_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 17, 1)
)
fwPsuEntry.setIndexNames(
    (0, "FORCEPOINT-NGFW-ENGINE-MIB", "fwPsuIndex"),
)
if mibBuilder.loadTexts:
    fwPsuEntry.setStatus("current")


class _FwPsuIndex_Type(Integer32):
    """Custom type fwPsuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FwPsuIndex_Type.__name__ = "Integer32"
_FwPsuIndex_Object = MibTableColumn
fwPsuIndex = _FwPsuIndex_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 17, 1, 1),
    _FwPsuIndex_Type()
)
fwPsuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwPsuIndex.setStatus("current")
_FwPsuName_Type = DisplayString
_FwPsuName_Object = MibTableColumn
fwPsuName = _FwPsuName_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 17, 1, 2),
    _FwPsuName_Type()
)
fwPsuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwPsuName.setStatus("current")
_FwPsuStatus_Type = FwHwComponentStatus
_FwPsuStatus_Object = MibTableColumn
fwPsuStatus = _FwPsuStatus_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 17, 1, 3),
    _FwPsuStatus_Type()
)
fwPsuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwPsuStatus.setStatus("current")
_FwFanTable_Object = MibTable
fwFanTable = _FwFanTable_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 18)
)
if mibBuilder.loadTexts:
    fwFanTable.setStatus("current")
_FwFanEntry_Object = MibTableRow
fwFanEntry = _FwFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 18, 1)
)
fwFanEntry.setIndexNames(
    (0, "FORCEPOINT-NGFW-ENGINE-MIB", "fwFanIndex"),
)
if mibBuilder.loadTexts:
    fwFanEntry.setStatus("current")


class _FwFanIndex_Type(Integer32):
    """Custom type fwFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FwFanIndex_Type.__name__ = "Integer32"
_FwFanIndex_Object = MibTableColumn
fwFanIndex = _FwFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 18, 1, 1),
    _FwFanIndex_Type()
)
fwFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwFanIndex.setStatus("current")
_FwFanName_Type = DisplayString
_FwFanName_Object = MibTableColumn
fwFanName = _FwFanName_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 18, 1, 2),
    _FwFanName_Type()
)
fwFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwFanName.setStatus("current")
_FwFan_Type = Integer32
_FwFan_Object = MibTableColumn
fwFan = _FwFan_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 18, 1, 3),
    _FwFan_Type()
)
fwFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwFan.setStatus("current")
if mibBuilder.loadTexts:
    fwFan.setUnits("RPM")
_FwFanStatus_Type = FwHwComponentStatus
_FwFanStatus_Object = MibTableColumn
fwFanStatus = _FwFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 18, 1, 4),
    _FwFanStatus_Type()
)
fwFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwFanStatus.setStatus("current")
_NetNodeObjects_ObjectIdentity = ObjectIdentity
netNodeObjects = _NetNodeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 19)
)


class _NodeClusterId_Type(Integer32):
    """Custom type nodeClusterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NodeClusterId_Type.__name__ = "Integer32"
_NodeClusterId_Object = MibScalar
nodeClusterId = _NodeClusterId_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 19, 1),
    _NodeClusterId_Type()
)
nodeClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeClusterId.setStatus("current")


class _NodeMemberId_Type(Integer32):
    """Custom type nodeMemberId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NodeMemberId_Type.__name__ = "Integer32"
_NodeMemberId_Object = MibScalar
nodeMemberId = _NodeMemberId_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 19, 2),
    _NodeMemberId_Type()
)
nodeMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeMemberId.setStatus("current")


class _NodeOperState_Type(Integer32):
    """Custom type nodeOperState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("online", 1),
          ("goingOnline", 2),
          ("lockedOnline", 3),
          ("goingLockedOnline", 4),
          ("offline", 5),
          ("goingOffline", 6),
          ("lockedOffline", 7),
          ("goingLockedOffline", 8),
          ("standby", 9),
          ("goingStandby", 10))
    )


_NodeOperState_Type.__name__ = "Integer32"
_NodeOperState_Object = MibScalar
nodeOperState = _NodeOperState_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 19, 3),
    _NodeOperState_Type()
)
nodeOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeOperState.setStatus("current")


class _NodeCPULoad_Type(Integer32):
    """Custom type nodeCPULoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NodeCPULoad_Type.__name__ = "Integer32"
_NodeCPULoad_Object = MibScalar
nodeCPULoad = _NodeCPULoad_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 19, 4),
    _NodeCPULoad_Type()
)
nodeCPULoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeCPULoad.setStatus("current")
_NodeLastLogin_Type = DisplayString
_NodeLastLogin_Object = MibScalar
nodeLastLogin = _NodeLastLogin_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 19, 5),
    _NodeLastLogin_Type()
)
nodeLastLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeLastLogin.setStatus("current")
_NodeLastLoginTime_Type = TimeStamp
_NodeLastLoginTime_Object = MibScalar
nodeLastLoginTime = _NodeLastLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 19, 6),
    _NodeLastLoginTime_Type()
)
nodeLastLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeLastLoginTime.setStatus("current")
_NodeTestTable_Object = MibTable
nodeTestTable = _NodeTestTable_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 19, 7)
)
if mibBuilder.loadTexts:
    nodeTestTable.setStatus("current")
_NodeTestEntry_Object = MibTableRow
nodeTestEntry = _NodeTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 19, 7, 1)
)
nodeTestEntry.setIndexNames(
    (0, "FORCEPOINT-NGFW-ENGINE-MIB", "nodeTestIndex"),
)
if mibBuilder.loadTexts:
    nodeTestEntry.setStatus("current")


class _NodeTestIndex_Type(Unsigned32):
    """Custom type nodeTestIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NodeTestIndex_Type.__name__ = "Unsigned32"
_NodeTestIndex_Object = MibTableColumn
nodeTestIndex = _NodeTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 19, 7, 1, 1),
    _NodeTestIndex_Type()
)
nodeTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nodeTestIndex.setStatus("current")
_NodeTestIdentity_Type = DisplayString
_NodeTestIdentity_Object = MibTableColumn
nodeTestIdentity = _NodeTestIdentity_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 19, 7, 1, 2),
    _NodeTestIdentity_Type()
)
nodeTestIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeTestIdentity.setStatus("current")


class _NodeTestResult_Type(Integer32):
    """Custom type nodeTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failure", 2))
    )


_NodeTestResult_Type.__name__ = "Integer32"
_NodeTestResult_Object = MibTableColumn
nodeTestResult = _NodeTestResult_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 19, 7, 1, 3),
    _NodeTestResult_Type()
)
nodeTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeTestResult.setStatus("current")
_NodeTestResultTime_Type = TimeStamp
_NodeTestResultTime_Object = MibTableColumn
nodeTestResultTime = _NodeTestResultTime_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 19, 7, 1, 4),
    _NodeTestResultTime_Type()
)
nodeTestResultTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeTestResultTime.setStatus("current")
_NodeHwmonEvent_Type = DisplayString
_NodeHwmonEvent_Object = MibScalar
nodeHwmonEvent = _NodeHwmonEvent_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 19, 8),
    _NodeHwmonEvent_Type()
)
nodeHwmonEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeHwmonEvent.setStatus("current")
_NodeApplianceModel_Type = DisplayString
_NodeApplianceModel_Object = MibScalar
nodeApplianceModel = _NodeApplianceModel_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 19, 9),
    _NodeApplianceModel_Type()
)
nodeApplianceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeApplianceModel.setStatus("current")
_NodePosCode_Type = DisplayString
_NodePosCode_Object = MibScalar
nodePosCode = _NodePosCode_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 19, 10),
    _NodePosCode_Type()
)
nodePosCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePosCode.setStatus("current")
_NodeLoginTime_Type = DateAndTime
_NodeLoginTime_Object = MibScalar
nodeLoginTime = _NodeLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 19, 11),
    _NodeLoginTime_Type()
)
nodeLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeLoginTime.setStatus("current")
_NodePolicyApplyTime_Type = DateAndTime
_NodePolicyApplyTime_Object = MibScalar
nodePolicyApplyTime = _NodePolicyApplyTime_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 19, 12),
    _NodePolicyApplyTime_Type()
)
nodePolicyApplyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePolicyApplyTime.setStatus("current")
_NodeHardwareSerialNumber_Type = DisplayString
_NodeHardwareSerialNumber_Object = MibScalar
nodeHardwareSerialNumber = _NodeHardwareSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 19, 13),
    _NodeHardwareSerialNumber_Type()
)
nodeHardwareSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeHardwareSerialNumber.setStatus("current")
_FwVoltageTable_Object = MibTable
fwVoltageTable = _FwVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 20)
)
if mibBuilder.loadTexts:
    fwVoltageTable.setStatus("current")
_FwVoltageEntry_Object = MibTableRow
fwVoltageEntry = _FwVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 20, 1)
)
fwVoltageEntry.setIndexNames(
    (0, "FORCEPOINT-NGFW-ENGINE-MIB", "fwVoltageIndex"),
)
if mibBuilder.loadTexts:
    fwVoltageEntry.setStatus("current")


class _FwVoltageIndex_Type(Integer32):
    """Custom type fwVoltageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FwVoltageIndex_Type.__name__ = "Integer32"
_FwVoltageIndex_Object = MibTableColumn
fwVoltageIndex = _FwVoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 20, 1, 1),
    _FwVoltageIndex_Type()
)
fwVoltageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwVoltageIndex.setStatus("current")
_FwVoltageName_Type = DisplayString
_FwVoltageName_Object = MibTableColumn
fwVoltageName = _FwVoltageName_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 20, 1, 2),
    _FwVoltageName_Type()
)
fwVoltageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVoltageName.setStatus("current")
_FwVoltage_Type = FwFixedThousandths
_FwVoltage_Object = MibTableColumn
fwVoltage = _FwVoltage_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 20, 1, 3),
    _FwVoltage_Type()
)
fwVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVoltage.setStatus("current")
if mibBuilder.loadTexts:
    fwVoltage.setUnits("V")
_FwVoltageStatus_Type = FwHwComponentStatus
_FwVoltageStatus_Object = MibTableColumn
fwVoltageStatus = _FwVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 20, 1, 4),
    _FwVoltageStatus_Type()
)
fwVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVoltageStatus.setStatus("current")
_FwVETable_Object = MibTable
fwVETable = _FwVETable_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 21)
)
if mibBuilder.loadTexts:
    fwVETable.setStatus("current")
_FwVEEntry_Object = MibTableRow
fwVEEntry = _FwVEEntry_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 21, 1)
)
fwVEEntry.setIndexNames(
    (0, "FORCEPOINT-NGFW-ENGINE-MIB", "fwVEIndex"),
)
if mibBuilder.loadTexts:
    fwVEEntry.setStatus("current")


class _FwVEIndex_Type(Integer32):
    """Custom type fwVEIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_FwVEIndex_Type.__name__ = "Integer32"
_FwVEIndex_Object = MibTableColumn
fwVEIndex = _FwVEIndex_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 21, 1, 1),
    _FwVEIndex_Type()
)
fwVEIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwVEIndex.setStatus("current")


class _FwVEEngineId_Type(Integer32):
    """Custom type fwVEEngineId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_FwVEEngineId_Type.__name__ = "Integer32"
_FwVEEngineId_Object = MibTableColumn
fwVEEngineId = _FwVEEngineId_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 21, 1, 2),
    _FwVEEngineId_Type()
)
fwVEEngineId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVEEngineId.setStatus("current")
_FwVEName_Type = DisplayString
_FwVEName_Object = MibTableColumn
fwVEName = _FwVEName_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 21, 1, 3),
    _FwVEName_Type()
)
fwVEName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVEName.setStatus("current")
_FwVEStatus_Type = DisplayString
_FwVEStatus_Object = MibTableColumn
fwVEStatus = _FwVEStatus_Object(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 1, 21, 1, 4),
    _FwVEStatus_Type()
)
fwVEStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVEStatus.setStatus("current")
_EngineGroups_ObjectIdentity = ObjectIdentity
engineGroups = _EngineGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 2)
)

# Managed Objects groups

firewallGeneralInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 2, 1)
)
firewallGeneralInformationGroup.setObjects(
      *(("FORCEPOINT-NGFW-ENGINE-MIB", "fwSoftwareVersion"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwSecurityPolicy"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwPolicyTime"))
)
if mibBuilder.loadTexts:
    firewallGeneralInformationGroup.setStatus("current")

firewallIfaceStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 2, 2)
)
firewallIfaceStatsGroup.setObjects(
      *(("FORCEPOINT-NGFW-ENGINE-MIB", "fwIfName"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwIfAcceptedPkts"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwIfDroppedPkts"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwIfLoggedPkts"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwIfAccountedPkts"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwIfRejectedPkts"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwIfForwardedPkts"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwIfAcceptedBytes"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwIfDroppedBytes"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwIfLoggedBytes"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwIfAccountedBytes"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwIfRejectedBytes"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwIfForwardedBytes"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwIfComment"))
)
if mibBuilder.loadTexts:
    firewallIfaceStatsGroup.setStatus("current")

firewallGeneralStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 2, 3)
)
firewallGeneralStatsGroup.setObjects(
      *(("FORCEPOINT-NGFW-ENGINE-MIB", "fwConnNumber"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwAccepted"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwDropped"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwLogged"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwAccounted"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwRejected"))
)
if mibBuilder.loadTexts:
    firewallGeneralStatsGroup.setStatus("current")

firewallHardwareGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 2, 4)
)
firewallHardwareGroup.setObjects(
      *(("FORCEPOINT-NGFW-ENGINE-MIB", "fwCpuName"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwCpuTotal"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwCpuUser"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwCpuSystem"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwCpuHwIrq"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwCpuSoftIrq"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwSwapBytesTotal"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwMemBytesTotal"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwMemBytesBuffers"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwHwTemperatureName"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwHwTemperature"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwHwTemperatureStatus"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwPsuName"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwPsuStatus"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwFanName"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwFan"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwFanStatus"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwVoltageName"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwVoltage"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwVoltageStatus"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwPartitionDevName"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwMountPointName"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwDiskSerialNumber"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwPartitionSize"))
)
if mibBuilder.loadTexts:
    firewallHardwareGroup.setStatus("current")

firewallMbrInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 2, 5)
)
firewallMbrInterfaceGroup.setObjects(
      *(("FORCEPOINT-NGFW-ENGINE-MIB", "fwMbrName"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwMbrBandUsed"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwMbrSignalStrength"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwMbrStatus"))
)
if mibBuilder.loadTexts:
    firewallMbrInterfaceGroup.setStatus("current")

firewallPerformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 2, 6)
)
firewallPerformanceGroup.setObjects(
      *(("FORCEPOINT-NGFW-ENGINE-MIB", "fwCpuNice"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwCpuIdle"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwCpuIoWait"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwSwapBytesUsed"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwSwapBytesUnused"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwMemBytesUsed"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwMemBytesUnused"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwMemBytesCached"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwMemBytesAvailable"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwMemBytesSReclaimable"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwPartitionUsed"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwPartitionAvail"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwNewConnectionsS"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwDiscardedConnectionsS"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwRefusedConnectionsS"))
)
if mibBuilder.loadTexts:
    firewallPerformanceGroup.setStatus("current")

firewallVpnEpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 2, 7)
)
firewallVpnEpGroup.setObjects(
      *(("FORCEPOINT-NGFW-ENGINE-MIB", "fwVpnEp4Local"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwVpnEp4Remote"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwVpnEp4RemoteType"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwVpnEp4ReceivedBytes"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwVpnEp4SentBytes"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwVpnEp4IpsecSa"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwVpnEp6Local"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwVpnEp6Remote"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwVpnEp6RemoteType"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwVpnEp6ReceivedBytes"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwVpnEp6SentBytes"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwVpnEp6IpsecSa"))
)
if mibBuilder.loadTexts:
    firewallVpnEpGroup.setStatus("current")

nodeIdentificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 2, 8)
)
nodeIdentificationGroup.setObjects(
      *(("FORCEPOINT-NGFW-ENGINE-MIB", "nodeClusterId"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "nodeMemberId"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "nodeApplianceModel"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "nodePosCode"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "nodeHardwareSerialNumber"))
)
if mibBuilder.loadTexts:
    nodeIdentificationGroup.setStatus("current")

nodeStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 2, 9)
)
nodeStatusGroup.setObjects(
      *(("FORCEPOINT-NGFW-ENGINE-MIB", "nodeOperState"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "nodeCPULoad"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "nodePolicyApplyTime"))
)
if mibBuilder.loadTexts:
    nodeStatusGroup.setStatus("current")

nodeLoginGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 2, 10)
)
nodeLoginGroup.setObjects(
      *(("FORCEPOINT-NGFW-ENGINE-MIB", "nodeLastLogin"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "nodeLastLoginTime"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "nodeLoginTime"))
)
if mibBuilder.loadTexts:
    nodeLoginGroup.setStatus("current")

nodeTesterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 2, 11)
)
nodeTesterGroup.setObjects(
      *(("FORCEPOINT-NGFW-ENGINE-MIB", "nodeTestIdentity"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "nodeTestResult"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "nodeTestResultTime"))
)
if mibBuilder.loadTexts:
    nodeTesterGroup.setStatus("current")

nodeHwmonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 2, 17)
)
nodeHwmonGroup.setObjects(
    ("FORCEPOINT-NGFW-ENGINE-MIB", "nodeHwmonEvent")
)
if mibBuilder.loadTexts:
    nodeHwmonGroup.setStatus("current")

engineVEGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 2, 18)
)
engineVEGroup.setObjects(
      *(("FORCEPOINT-NGFW-ENGINE-MIB", "fwVEEngineId"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwVEName"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "fwVEStatus"))
)
if mibBuilder.loadTexts:
    engineVEGroup.setStatus("current")


# Notification objects

fwPolicyInstall = NotificationType(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 0, 1)
)
fwPolicyInstall.setObjects(
    ("FORCEPOINT-NGFW-ENGINE-MIB", "fwSecurityPolicy")
)
if mibBuilder.loadTexts:
    fwPolicyInstall.setStatus(
        "current"
    )

nodeOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 0, 2)
)
nodeOnline.setObjects(
    ("FORCEPOINT-NGFW-ENGINE-MIB", "nodeOperState")
)
if mibBuilder.loadTexts:
    nodeOnline.setStatus(
        "current"
    )

nodeOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 0, 3)
)
nodeOffline.setObjects(
    ("FORCEPOINT-NGFW-ENGINE-MIB", "nodeOperState")
)
if mibBuilder.loadTexts:
    nodeOffline.setStatus(
        "current"
    )

nodeBoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 0, 4)
)
if mibBuilder.loadTexts:
    nodeBoot.setStatus(
        "current"
    )

nodeShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 0, 5)
)
if mibBuilder.loadTexts:
    nodeShutdown.setStatus(
        "current"
    )

nodeUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 0, 6)
)
nodeUserLogin.setObjects(
    ("FORCEPOINT-NGFW-ENGINE-MIB", "nodeLastLogin")
)
if mibBuilder.loadTexts:
    nodeUserLogin.setStatus(
        "current"
    )

nodeFailedUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 0, 7)
)
if mibBuilder.loadTexts:
    nodeFailedUserLogin.setStatus(
        "current"
    )

nodeUserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 0, 8)
)
if mibBuilder.loadTexts:
    nodeUserLogout.setStatus(
        "current"
    )

nodeTestFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 0, 9)
)
nodeTestFailure.setObjects(
    ("FORCEPOINT-NGFW-ENGINE-MIB", "nodeTestIdentity")
)
if mibBuilder.loadTexts:
    nodeTestFailure.setStatus(
        "current"
    )

nodeHwmon = NotificationType(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 0, 10)
)
nodeHwmon.setObjects(
    ("FORCEPOINT-NGFW-ENGINE-MIB", "nodeHwmonEvent")
)
if mibBuilder.loadTexts:
    nodeHwmon.setStatus(
        "current"
    )


# Notifications groups

firewallGeneralNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 2, 12)
)
firewallGeneralNotifGroup.setObjects(
    ("FORCEPOINT-NGFW-ENGINE-MIB", "fwPolicyInstall")
)
if mibBuilder.loadTexts:
    firewallGeneralNotifGroup.setStatus(
        "current"
    )

nodeStatusNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 2, 13)
)
nodeStatusNotificationsGroup.setObjects(
      *(("FORCEPOINT-NGFW-ENGINE-MIB", "nodeOnline"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "nodeOffline"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "nodeBoot"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "nodeShutdown"))
)
if mibBuilder.loadTexts:
    nodeStatusNotificationsGroup.setStatus(
        "current"
    )

nodeLoginNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 2, 14)
)
nodeLoginNotificationsGroup.setObjects(
      *(("FORCEPOINT-NGFW-ENGINE-MIB", "nodeUserLogin"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "nodeFailedUserLogin"),
        ("FORCEPOINT-NGFW-ENGINE-MIB", "nodeUserLogout"))
)
if mibBuilder.loadTexts:
    nodeLoginNotificationsGroup.setStatus(
        "current"
    )

nodeTesterNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 2, 15)
)
nodeTesterNotificationsGroup.setObjects(
    ("FORCEPOINT-NGFW-ENGINE-MIB", "nodeTestFailure")
)
if mibBuilder.loadTexts:
    nodeTesterNotificationsGroup.setStatus(
        "current"
    )

nodeHwmonNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47565, 1, 1, 2, 16)
)
nodeHwmonNotificationsGroup.setObjects(
    ("FORCEPOINT-NGFW-ENGINE-MIB", "nodeHwmon")
)
if mibBuilder.loadTexts:
    nodeHwmonNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORCEPOINT-NGFW-ENGINE-MIB",
    **{"VpnEndpointType": VpnEndpointType,
       "FwHwComponentStatus": FwHwComponentStatus,
       "FwFixedThousandths": FwFixedThousandths,
       "forcepointNGFWEngineMib": forcepointNGFWEngineMib,
       "engineNotifications": engineNotifications,
       "fwPolicyInstall": fwPolicyInstall,
       "nodeOnline": nodeOnline,
       "nodeOffline": nodeOffline,
       "nodeBoot": nodeBoot,
       "nodeShutdown": nodeShutdown,
       "nodeUserLogin": nodeUserLogin,
       "nodeFailedUserLogin": nodeFailedUserLogin,
       "nodeUserLogout": nodeUserLogout,
       "nodeTestFailure": nodeTestFailure,
       "nodeHwmon": nodeHwmon,
       "engineObjects": engineObjects,
       "fwSoftwareVersion": fwSoftwareVersion,
       "fwSecurityPolicy": fwSecurityPolicy,
       "fwPolicyTime": fwPolicyTime,
       "fwConnNumber": fwConnNumber,
       "fwAccepted": fwAccepted,
       "fwDropped": fwDropped,
       "fwLogged": fwLogged,
       "fwAccounted": fwAccounted,
       "fwRejected": fwRejected,
       "fwIfStatsTable": fwIfStatsTable,
       "fwIfStatsEntry": fwIfStatsEntry,
       "fwIfStatsIndex": fwIfStatsIndex,
       "fwIfName": fwIfName,
       "fwIfAcceptedPkts": fwIfAcceptedPkts,
       "fwIfDroppedPkts": fwIfDroppedPkts,
       "fwIfLoggedPkts": fwIfLoggedPkts,
       "fwIfAccountedPkts": fwIfAccountedPkts,
       "fwIfRejectedPkts": fwIfRejectedPkts,
       "fwIfAcceptedBytes": fwIfAcceptedBytes,
       "fwIfDroppedBytes": fwIfDroppedBytes,
       "fwIfLoggedBytes": fwIfLoggedBytes,
       "fwIfAccountedBytes": fwIfAccountedBytes,
       "fwIfRejectedBytes": fwIfRejectedBytes,
       "fwIfForwardedPkts": fwIfForwardedPkts,
       "fwIfForwardedBytes": fwIfForwardedBytes,
       "fwIfComment": fwIfComment,
       "fwHardware": fwHardware,
       "fwCpuStatsTable": fwCpuStatsTable,
       "fwCpuStatsEntry": fwCpuStatsEntry,
       "fwCpuStatsId": fwCpuStatsId,
       "fwCpuName": fwCpuName,
       "fwCpuTotal": fwCpuTotal,
       "fwCpuUser": fwCpuUser,
       "fwCpuSystem": fwCpuSystem,
       "fwCpuNice": fwCpuNice,
       "fwCpuIdle": fwCpuIdle,
       "fwCpuIoWait": fwCpuIoWait,
       "fwCpuHwIrq": fwCpuHwIrq,
       "fwCpuSoftIrq": fwCpuSoftIrq,
       "fwMemoryInfo": fwMemoryInfo,
       "fwSwapBytesTotal": fwSwapBytesTotal,
       "fwSwapBytesUsed": fwSwapBytesUsed,
       "fwSwapBytesUnused": fwSwapBytesUnused,
       "fwMemBytesTotal": fwMemBytesTotal,
       "fwMemBytesUsed": fwMemBytesUsed,
       "fwMemBytesUnused": fwMemBytesUnused,
       "fwMemBytesBuffers": fwMemBytesBuffers,
       "fwMemBytesCached": fwMemBytesCached,
       "fwMemBytesSReclaimable": fwMemBytesSReclaimable,
       "fwMemBytesAvailable": fwMemBytesAvailable,
       "fwDiskStatsTable": fwDiskStatsTable,
       "fwDiskStatsEntry": fwDiskStatsEntry,
       "fwPartitionIndex": fwPartitionIndex,
       "fwPartitionDevName": fwPartitionDevName,
       "fwMountPointName": fwMountPointName,
       "fwPartitionSize": fwPartitionSize,
       "fwPartitionUsed": fwPartitionUsed,
       "fwPartitionAvail": fwPartitionAvail,
       "fwNewConnectionsS": fwNewConnectionsS,
       "fwDiscardedConnectionsS": fwDiscardedConnectionsS,
       "fwRefusedConnectionsS": fwRefusedConnectionsS,
       "fwVpnEp4Table": fwVpnEp4Table,
       "fwVpnEp4Entry": fwVpnEp4Entry,
       "fwVpnEp4Index": fwVpnEp4Index,
       "fwVpnEp4Local": fwVpnEp4Local,
       "fwVpnEp4Remote": fwVpnEp4Remote,
       "fwVpnEp4RemoteType": fwVpnEp4RemoteType,
       "fwVpnEp4ReceivedBytes": fwVpnEp4ReceivedBytes,
       "fwVpnEp4SentBytes": fwVpnEp4SentBytes,
       "fwVpnEp4IpsecSa": fwVpnEp4IpsecSa,
       "fwVpnEp6Table": fwVpnEp6Table,
       "fwVpnEp6Entry": fwVpnEp6Entry,
       "fwVpnEp6Index": fwVpnEp6Index,
       "fwVpnEp6Local": fwVpnEp6Local,
       "fwVpnEp6Remote": fwVpnEp6Remote,
       "fwVpnEp6RemoteType": fwVpnEp6RemoteType,
       "fwVpnEp6ReceivedBytes": fwVpnEp6ReceivedBytes,
       "fwVpnEp6SentBytes": fwVpnEp6SentBytes,
       "fwVpnEp6IpsecSa": fwVpnEp6IpsecSa,
       "fwMbrInterfaceTable": fwMbrInterfaceTable,
       "fwMbrInterfaceEntry": fwMbrInterfaceEntry,
       "fwMbrInterfaceIndex": fwMbrInterfaceIndex,
       "fwMbrName": fwMbrName,
       "fwMbrBandUsed": fwMbrBandUsed,
       "fwMbrSignalStrength": fwMbrSignalStrength,
       "fwMbrStatus": fwMbrStatus,
       "fwDiskSerialNumber": fwDiskSerialNumber,
       "fwHwTempSensorTable": fwHwTempSensorTable,
       "fwHwTempSensorEntry": fwHwTempSensorEntry,
       "fwHwTempSensorIndex": fwHwTempSensorIndex,
       "fwHwTemperatureName": fwHwTemperatureName,
       "fwHwTemperature": fwHwTemperature,
       "fwHwTemperatureStatus": fwHwTemperatureStatus,
       "fwPsuTable": fwPsuTable,
       "fwPsuEntry": fwPsuEntry,
       "fwPsuIndex": fwPsuIndex,
       "fwPsuName": fwPsuName,
       "fwPsuStatus": fwPsuStatus,
       "fwFanTable": fwFanTable,
       "fwFanEntry": fwFanEntry,
       "fwFanIndex": fwFanIndex,
       "fwFanName": fwFanName,
       "fwFan": fwFan,
       "fwFanStatus": fwFanStatus,
       "netNodeObjects": netNodeObjects,
       "nodeClusterId": nodeClusterId,
       "nodeMemberId": nodeMemberId,
       "nodeOperState": nodeOperState,
       "nodeCPULoad": nodeCPULoad,
       "nodeLastLogin": nodeLastLogin,
       "nodeLastLoginTime": nodeLastLoginTime,
       "nodeTestTable": nodeTestTable,
       "nodeTestEntry": nodeTestEntry,
       "nodeTestIndex": nodeTestIndex,
       "nodeTestIdentity": nodeTestIdentity,
       "nodeTestResult": nodeTestResult,
       "nodeTestResultTime": nodeTestResultTime,
       "nodeHwmonEvent": nodeHwmonEvent,
       "nodeApplianceModel": nodeApplianceModel,
       "nodePosCode": nodePosCode,
       "nodeLoginTime": nodeLoginTime,
       "nodePolicyApplyTime": nodePolicyApplyTime,
       "nodeHardwareSerialNumber": nodeHardwareSerialNumber,
       "fwVoltageTable": fwVoltageTable,
       "fwVoltageEntry": fwVoltageEntry,
       "fwVoltageIndex": fwVoltageIndex,
       "fwVoltageName": fwVoltageName,
       "fwVoltage": fwVoltage,
       "fwVoltageStatus": fwVoltageStatus,
       "fwVETable": fwVETable,
       "fwVEEntry": fwVEEntry,
       "fwVEIndex": fwVEIndex,
       "fwVEEngineId": fwVEEngineId,
       "fwVEName": fwVEName,
       "fwVEStatus": fwVEStatus,
       "engineGroups": engineGroups,
       "firewallGeneralInformationGroup": firewallGeneralInformationGroup,
       "firewallIfaceStatsGroup": firewallIfaceStatsGroup,
       "firewallGeneralStatsGroup": firewallGeneralStatsGroup,
       "firewallHardwareGroup": firewallHardwareGroup,
       "firewallMbrInterfaceGroup": firewallMbrInterfaceGroup,
       "firewallPerformanceGroup": firewallPerformanceGroup,
       "firewallVpnEpGroup": firewallVpnEpGroup,
       "nodeIdentificationGroup": nodeIdentificationGroup,
       "nodeStatusGroup": nodeStatusGroup,
       "nodeLoginGroup": nodeLoginGroup,
       "nodeTesterGroup": nodeTesterGroup,
       "firewallGeneralNotifGroup": firewallGeneralNotifGroup,
       "nodeStatusNotificationsGroup": nodeStatusNotificationsGroup,
       "nodeLoginNotificationsGroup": nodeLoginNotificationsGroup,
       "nodeTesterNotificationsGroup": nodeTesterNotificationsGroup,
       "nodeHwmonNotificationsGroup": nodeHwmonNotificationsGroup,
       "nodeHwmonGroup": nodeHwmonGroup,
       "engineVEGroup": engineVEGroup}
)
