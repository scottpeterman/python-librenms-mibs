# SNMP MIB module (SLE-MPLS-TP-TUNNEL-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-MPLS-TP-TUNNEL-STATISTICS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:48 2025
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

(sleMgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "sleMgmt")

(mplsStdMIB,) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "mplsStdMIB")

(SleControlRequestResultType,
 SleControlStatusType) = mibBuilder.importSymbols(
    "SLE-TC-MIB",
    "SleControlRequestResultType",
    "SleControlStatusType")

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
 iso,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "zeroDotZero")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sleMplsTpTunnelStats = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 20)
)
if mibBuilder.loadTexts:
    sleMplsTpTunnelStats.setRevisions(
        ("2016-01-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleMpls_ObjectIdentity = ObjectIdentity
sleMpls = _SleMpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16)
)
_SleMplsTpTunnelStatsTable_ObjectIdentity = ObjectIdentity
sleMplsTpTunnelStatsTable = _SleMplsTpTunnelStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 20, 1)
)
_SleMplsTpTunnelStatsInfoTable_Object = MibTable
sleMplsTpTunnelStatsInfoTable = _SleMplsTpTunnelStatsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 20, 1, 1)
)
if mibBuilder.loadTexts:
    sleMplsTpTunnelStatsInfoTable.setStatus("current")
_SleMplsTpTunnelStatsInfoEntry_Object = MibTableRow
sleMplsTpTunnelStatsInfoEntry = _SleMplsTpTunnelStatsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 20, 1, 1, 1)
)
sleMplsTpTunnelStatsInfoEntry.setIndexNames(
    (0, "SLE-MPLS-TP-TUNNEL-STATISTICS-MIB", "sleMplsTpTunnelStatsInfoIndex"),
)
if mibBuilder.loadTexts:
    sleMplsTpTunnelStatsInfoEntry.setStatus("current")


class _SleMplsTpTunnelStatsInfoIndex_Type(Unsigned32):
    """Custom type sleMplsTpTunnelStatsInfoIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleMplsTpTunnelStatsInfoIndex_Type.__name__ = "Unsigned32"
_SleMplsTpTunnelStatsInfoIndex_Object = MibTableColumn
sleMplsTpTunnelStatsInfoIndex = _SleMplsTpTunnelStatsInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 20, 1, 1, 1, 1),
    _SleMplsTpTunnelStatsInfoIndex_Type()
)
sleMplsTpTunnelStatsInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMplsTpTunnelStatsInfoIndex.setStatus("current")
_SleMplsTpTunnelStatsInfoTunnelName_Type = OctetString
_SleMplsTpTunnelStatsInfoTunnelName_Object = MibTableColumn
sleMplsTpTunnelStatsInfoTunnelName = _SleMplsTpTunnelStatsInfoTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 20, 1, 1, 1, 2),
    _SleMplsTpTunnelStatsInfoTunnelName_Type()
)
sleMplsTpTunnelStatsInfoTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelStatsInfoTunnelName.setStatus("current")


class _SleMplsTpTunnelStatsInfoRole_Type(Integer32):
    """Custom type sleMplsTpTunnelStatsInfoRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("source", 0),
          ("transit", 1),
          ("destination", 2))
    )


_SleMplsTpTunnelStatsInfoRole_Type.__name__ = "Integer32"
_SleMplsTpTunnelStatsInfoRole_Object = MibTableColumn
sleMplsTpTunnelStatsInfoRole = _SleMplsTpTunnelStatsInfoRole_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 20, 1, 1, 1, 3),
    _SleMplsTpTunnelStatsInfoRole_Type()
)
sleMplsTpTunnelStatsInfoRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelStatsInfoRole.setStatus("current")
_SleMplsTpTunnelStatsInfoFwdTxPkts_Type = Counter64
_SleMplsTpTunnelStatsInfoFwdTxPkts_Object = MibTableColumn
sleMplsTpTunnelStatsInfoFwdTxPkts = _SleMplsTpTunnelStatsInfoFwdTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 20, 1, 1, 1, 4),
    _SleMplsTpTunnelStatsInfoFwdTxPkts_Type()
)
sleMplsTpTunnelStatsInfoFwdTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelStatsInfoFwdTxPkts.setStatus("current")
_SleMplsTpTunnelStatsInfoFwdTxBytes_Type = Counter64
_SleMplsTpTunnelStatsInfoFwdTxBytes_Object = MibTableColumn
sleMplsTpTunnelStatsInfoFwdTxBytes = _SleMplsTpTunnelStatsInfoFwdTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 20, 1, 1, 1, 5),
    _SleMplsTpTunnelStatsInfoFwdTxBytes_Type()
)
sleMplsTpTunnelStatsInfoFwdTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelStatsInfoFwdTxBytes.setStatus("current")
_SleMplsTpTunnelStatsInfoFwdRxPkts_Type = Counter64
_SleMplsTpTunnelStatsInfoFwdRxPkts_Object = MibTableColumn
sleMplsTpTunnelStatsInfoFwdRxPkts = _SleMplsTpTunnelStatsInfoFwdRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 20, 1, 1, 1, 6),
    _SleMplsTpTunnelStatsInfoFwdRxPkts_Type()
)
sleMplsTpTunnelStatsInfoFwdRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelStatsInfoFwdRxPkts.setStatus("current")
_SleMplsTpTunnelStatsInfoFwdRxBytes_Type = Counter64
_SleMplsTpTunnelStatsInfoFwdRxBytes_Object = MibTableColumn
sleMplsTpTunnelStatsInfoFwdRxBytes = _SleMplsTpTunnelStatsInfoFwdRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 20, 1, 1, 1, 7),
    _SleMplsTpTunnelStatsInfoFwdRxBytes_Type()
)
sleMplsTpTunnelStatsInfoFwdRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelStatsInfoFwdRxBytes.setStatus("current")
_SleMplsTpTunnelStatsInfoRevTxPkts_Type = Counter64
_SleMplsTpTunnelStatsInfoRevTxPkts_Object = MibTableColumn
sleMplsTpTunnelStatsInfoRevTxPkts = _SleMplsTpTunnelStatsInfoRevTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 20, 1, 1, 1, 8),
    _SleMplsTpTunnelStatsInfoRevTxPkts_Type()
)
sleMplsTpTunnelStatsInfoRevTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelStatsInfoRevTxPkts.setStatus("current")
_SleMplsTpTunnelStatsInfoRevTxBytes_Type = Counter64
_SleMplsTpTunnelStatsInfoRevTxBytes_Object = MibTableColumn
sleMplsTpTunnelStatsInfoRevTxBytes = _SleMplsTpTunnelStatsInfoRevTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 20, 1, 1, 1, 9),
    _SleMplsTpTunnelStatsInfoRevTxBytes_Type()
)
sleMplsTpTunnelStatsInfoRevTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelStatsInfoRevTxBytes.setStatus("current")
_SleMplsTpTunnelStatsInfoRevRxPkts_Type = Counter64
_SleMplsTpTunnelStatsInfoRevRxPkts_Object = MibTableColumn
sleMplsTpTunnelStatsInfoRevRxPkts = _SleMplsTpTunnelStatsInfoRevRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 20, 1, 1, 1, 10),
    _SleMplsTpTunnelStatsInfoRevRxPkts_Type()
)
sleMplsTpTunnelStatsInfoRevRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelStatsInfoRevRxPkts.setStatus("current")
_SleMplsTpTunnelStatsInfoRevRxBytes_Type = Counter64
_SleMplsTpTunnelStatsInfoRevRxBytes_Object = MibTableColumn
sleMplsTpTunnelStatsInfoRevRxBytes = _SleMplsTpTunnelStatsInfoRevRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 20, 1, 1, 1, 11),
    _SleMplsTpTunnelStatsInfoRevRxBytes_Type()
)
sleMplsTpTunnelStatsInfoRevRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelStatsInfoRevRxBytes.setStatus("current")
_SleMplsTpTunnelStatsControl_ObjectIdentity = ObjectIdentity
sleMplsTpTunnelStatsControl = _SleMplsTpTunnelStatsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 20, 1, 2)
)


class _SleMplsTpTunnelStatsControlRequest_Type(Integer32):
    """Custom type sleMplsTpTunnelStatsControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setToClearTunnelStats", 1)
    )


_SleMplsTpTunnelStatsControlRequest_Type.__name__ = "Integer32"
_SleMplsTpTunnelStatsControlRequest_Object = MibScalar
sleMplsTpTunnelStatsControlRequest = _SleMplsTpTunnelStatsControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 20, 1, 2, 1),
    _SleMplsTpTunnelStatsControlRequest_Type()
)
sleMplsTpTunnelStatsControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelStatsControlRequest.setStatus("current")
_SleMplsTpTunnelStatsControlStatus_Type = SleControlStatusType
_SleMplsTpTunnelStatsControlStatus_Object = MibScalar
sleMplsTpTunnelStatsControlStatus = _SleMplsTpTunnelStatsControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 20, 1, 2, 2),
    _SleMplsTpTunnelStatsControlStatus_Type()
)
sleMplsTpTunnelStatsControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelStatsControlStatus.setStatus("current")
_SleMplsTpTunnelStatsControlTimer_Type = Gauge32
_SleMplsTpTunnelStatsControlTimer_Object = MibScalar
sleMplsTpTunnelStatsControlTimer = _SleMplsTpTunnelStatsControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 20, 1, 2, 3),
    _SleMplsTpTunnelStatsControlTimer_Type()
)
sleMplsTpTunnelStatsControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelStatsControlTimer.setStatus("current")
_SleMplsTpTunnelStatsControlTimeStamp_Type = TimeTicks
_SleMplsTpTunnelStatsControlTimeStamp_Object = MibScalar
sleMplsTpTunnelStatsControlTimeStamp = _SleMplsTpTunnelStatsControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 20, 1, 2, 4),
    _SleMplsTpTunnelStatsControlTimeStamp_Type()
)
sleMplsTpTunnelStatsControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelStatsControlTimeStamp.setStatus("current")
_SleMplsTpTunnelStatsReqResult_Type = SleControlRequestResultType
_SleMplsTpTunnelStatsReqResult_Object = MibScalar
sleMplsTpTunnelStatsReqResult = _SleMplsTpTunnelStatsReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 20, 1, 2, 5),
    _SleMplsTpTunnelStatsReqResult_Type()
)
sleMplsTpTunnelStatsReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelStatsReqResult.setStatus("current")
_SleMplsTpTunnelStatsControlName_Type = OctetString
_SleMplsTpTunnelStatsControlName_Object = MibScalar
sleMplsTpTunnelStatsControlName = _SleMplsTpTunnelStatsControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 20, 1, 2, 6),
    _SleMplsTpTunnelStatsControlName_Type()
)
sleMplsTpTunnelStatsControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelStatsControlName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-MPLS-TP-TUNNEL-STATISTICS-MIB",
    **{"sleMpls": sleMpls,
       "sleMplsTpTunnelStats": sleMplsTpTunnelStats,
       "sleMplsTpTunnelStatsTable": sleMplsTpTunnelStatsTable,
       "sleMplsTpTunnelStatsInfoTable": sleMplsTpTunnelStatsInfoTable,
       "sleMplsTpTunnelStatsInfoEntry": sleMplsTpTunnelStatsInfoEntry,
       "sleMplsTpTunnelStatsInfoIndex": sleMplsTpTunnelStatsInfoIndex,
       "sleMplsTpTunnelStatsInfoTunnelName": sleMplsTpTunnelStatsInfoTunnelName,
       "sleMplsTpTunnelStatsInfoRole": sleMplsTpTunnelStatsInfoRole,
       "sleMplsTpTunnelStatsInfoFwdTxPkts": sleMplsTpTunnelStatsInfoFwdTxPkts,
       "sleMplsTpTunnelStatsInfoFwdTxBytes": sleMplsTpTunnelStatsInfoFwdTxBytes,
       "sleMplsTpTunnelStatsInfoFwdRxPkts": sleMplsTpTunnelStatsInfoFwdRxPkts,
       "sleMplsTpTunnelStatsInfoFwdRxBytes": sleMplsTpTunnelStatsInfoFwdRxBytes,
       "sleMplsTpTunnelStatsInfoRevTxPkts": sleMplsTpTunnelStatsInfoRevTxPkts,
       "sleMplsTpTunnelStatsInfoRevTxBytes": sleMplsTpTunnelStatsInfoRevTxBytes,
       "sleMplsTpTunnelStatsInfoRevRxPkts": sleMplsTpTunnelStatsInfoRevRxPkts,
       "sleMplsTpTunnelStatsInfoRevRxBytes": sleMplsTpTunnelStatsInfoRevRxBytes,
       "sleMplsTpTunnelStatsControl": sleMplsTpTunnelStatsControl,
       "sleMplsTpTunnelStatsControlRequest": sleMplsTpTunnelStatsControlRequest,
       "sleMplsTpTunnelStatsControlStatus": sleMplsTpTunnelStatsControlStatus,
       "sleMplsTpTunnelStatsControlTimer": sleMplsTpTunnelStatsControlTimer,
       "sleMplsTpTunnelStatsControlTimeStamp": sleMplsTpTunnelStatsControlTimeStamp,
       "sleMplsTpTunnelStatsReqResult": sleMplsTpTunnelStatsReqResult,
       "sleMplsTpTunnelStatsControlName": sleMplsTpTunnelStatsControlName}
)
