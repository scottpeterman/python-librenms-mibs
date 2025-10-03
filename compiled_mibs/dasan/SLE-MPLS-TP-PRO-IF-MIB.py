# SNMP MIB module (SLE-MPLS-TP-PRO-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-MPLS-TP-PRO-IF-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:42 2025
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

(mplsTunnelEgressLSRId,
 mplsTunnelIndex,
 mplsTunnelIngressLSRId,
 mplsTunnelInstance) = mibBuilder.importSymbols(
    "MPLS-TE-STD-MIB",
    "mplsTunnelEgressLSRId",
    "mplsTunnelIndex",
    "mplsTunnelIngressLSRId",
    "mplsTunnelInstance")

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

sleMplsTpNode = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 13)
)
if mibBuilder.loadTexts:
    sleMplsTpNode.setRevisions(
        ("2012-07-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleMpls_ObjectIdentity = ObjectIdentity
sleMpls = _SleMpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16)
)
if mibBuilder.loadTexts:
    sleMpls.setStatus("current")
_SleMplsTpProIf_ObjectIdentity = ObjectIdentity
sleMplsTpProIf = _SleMplsTpProIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 13, 2)
)
_SleMplsTpProIfInfoTable_Object = MibTable
sleMplsTpProIfInfoTable = _SleMplsTpProIfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 13, 2, 1)
)
if mibBuilder.loadTexts:
    sleMplsTpProIfInfoTable.setStatus("current")
_SleMplsTpProIfInfoEntry_Object = MibTableRow
sleMplsTpProIfInfoEntry = _SleMplsTpProIfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 13, 2, 1, 1)
)
sleMplsTpProIfInfoEntry.setIndexNames(
    (0, "SLE-MPLS-TP-PRO-IF-MIB", "sleMplsTPProIfInfoIfIndex"),
)
if mibBuilder.loadTexts:
    sleMplsTpProIfInfoEntry.setStatus("current")


class _SleMplsTPProIfInfoIfIndex_Type(Unsigned32):
    """Custom type sleMplsTPProIfInfoIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleMplsTPProIfInfoIfIndex_Type.__name__ = "Unsigned32"
_SleMplsTPProIfInfoIfIndex_Object = MibTableColumn
sleMplsTPProIfInfoIfIndex = _SleMplsTPProIfInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 13, 2, 1, 1, 1),
    _SleMplsTPProIfInfoIfIndex_Type()
)
sleMplsTPProIfInfoIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMplsTPProIfInfoIfIndex.setStatus("current")
_SleMplsTPProIfInfoIpAddr_Type = IpAddress
_SleMplsTPProIfInfoIpAddr_Object = MibTableColumn
sleMplsTPProIfInfoIpAddr = _SleMplsTPProIfInfoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 13, 2, 1, 1, 2),
    _SleMplsTPProIfInfoIpAddr_Type()
)
sleMplsTPProIfInfoIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTPProIfInfoIpAddr.setStatus("current")
_SleMplsTpProIfControl_ObjectIdentity = ObjectIdentity
sleMplsTpProIfControl = _SleMplsTpProIfControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 13, 2, 2)
)


class _SleMplsTpProIfControlRequest_Type(Integer32):
    """Custom type sleMplsTpProIfControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setMplsTpProIfIpAddr", 1),
          ("unSetMplsTpProIfIpAddr", 2))
    )


_SleMplsTpProIfControlRequest_Type.__name__ = "Integer32"
_SleMplsTpProIfControlRequest_Object = MibScalar
sleMplsTpProIfControlRequest = _SleMplsTpProIfControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 13, 2, 2, 1),
    _SleMplsTpProIfControlRequest_Type()
)
sleMplsTpProIfControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpProIfControlRequest.setStatus("current")
_SleMplsTpProIfControlStatus_Type = SleControlStatusType
_SleMplsTpProIfControlStatus_Object = MibScalar
sleMplsTpProIfControlStatus = _SleMplsTpProIfControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 13, 2, 2, 2),
    _SleMplsTpProIfControlStatus_Type()
)
sleMplsTpProIfControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpProIfControlStatus.setStatus("current")
_SleMplsTpProIfControlTimer_Type = Gauge32
_SleMplsTpProIfControlTimer_Object = MibScalar
sleMplsTpProIfControlTimer = _SleMplsTpProIfControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 13, 2, 2, 3),
    _SleMplsTpProIfControlTimer_Type()
)
sleMplsTpProIfControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpProIfControlTimer.setStatus("current")
_SleMplsTpProIfControlTimestamp_Type = TimeTicks
_SleMplsTpProIfControlTimestamp_Object = MibScalar
sleMplsTpProIfControlTimestamp = _SleMplsTpProIfControlTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 13, 2, 2, 4),
    _SleMplsTpProIfControlTimestamp_Type()
)
sleMplsTpProIfControlTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpProIfControlTimestamp.setStatus("current")
_SleMplsTpProIfControlReqResult_Type = SleControlRequestResultType
_SleMplsTpProIfControlReqResult_Object = MibScalar
sleMplsTpProIfControlReqResult = _SleMplsTpProIfControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 13, 2, 2, 5),
    _SleMplsTpProIfControlReqResult_Type()
)
sleMplsTpProIfControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpProIfControlReqResult.setStatus("current")
_SleMplsTpProIfControlIfIndex_Type = Unsigned32
_SleMplsTpProIfControlIfIndex_Object = MibScalar
sleMplsTpProIfControlIfIndex = _SleMplsTpProIfControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 13, 2, 2, 6),
    _SleMplsTpProIfControlIfIndex_Type()
)
sleMplsTpProIfControlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpProIfControlIfIndex.setStatus("current")
_SleMplsTpProIfControlIpAddr_Type = IpAddress
_SleMplsTpProIfControlIpAddr_Object = MibScalar
sleMplsTpProIfControlIpAddr = _SleMplsTpProIfControlIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 13, 2, 2, 7),
    _SleMplsTpProIfControlIpAddr_Type()
)
sleMplsTpProIfControlIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpProIfControlIpAddr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-MPLS-TP-PRO-IF-MIB",
    **{"sleMpls": sleMpls,
       "sleMplsTpNode": sleMplsTpNode,
       "sleMplsTpProIf": sleMplsTpProIf,
       "sleMplsTpProIfInfoTable": sleMplsTpProIfInfoTable,
       "sleMplsTpProIfInfoEntry": sleMplsTpProIfInfoEntry,
       "sleMplsTPProIfInfoIfIndex": sleMplsTPProIfInfoIfIndex,
       "sleMplsTPProIfInfoIpAddr": sleMplsTPProIfInfoIpAddr,
       "sleMplsTpProIfControl": sleMplsTpProIfControl,
       "sleMplsTpProIfControlRequest": sleMplsTpProIfControlRequest,
       "sleMplsTpProIfControlStatus": sleMplsTpProIfControlStatus,
       "sleMplsTpProIfControlTimer": sleMplsTpProIfControlTimer,
       "sleMplsTpProIfControlTimestamp": sleMplsTpProIfControlTimestamp,
       "sleMplsTpProIfControlReqResult": sleMplsTpProIfControlReqResult,
       "sleMplsTpProIfControlIfIndex": sleMplsTpProIfControlIfIndex,
       "sleMplsTpProIfControlIpAddr": sleMplsTpProIfControlIpAddr}
)
