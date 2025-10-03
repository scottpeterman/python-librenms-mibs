# SNMP MIB module (SLE-MPLS-TP-PW-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-MPLS-TP-PW-STATISTICS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:46 2025
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

(PwIDType,) = mibBuilder.importSymbols(
    "PW-TC-STD-MIB",
    "PwIDType")

(SleControlRequestResultType,
 SleControlStatusType) = mibBuilder.importSymbols(
    "SLE-TC-MIB",
    "SleControlRequestResultType",
    "SleControlStatusType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

sleMplsTpPwStats = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 21)
)
if mibBuilder.loadTexts:
    sleMplsTpPwStats.setRevisions(
        ("2015-01-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleMpls_ObjectIdentity = ObjectIdentity
sleMpls = _SleMpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16)
)
_SleMplsTpPwStatsTable_ObjectIdentity = ObjectIdentity
sleMplsTpPwStatsTable = _SleMplsTpPwStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 21, 1)
)
_SleMplsTpPwStatsInfoTable_Object = MibTable
sleMplsTpPwStatsInfoTable = _SleMplsTpPwStatsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 21, 1, 1)
)
if mibBuilder.loadTexts:
    sleMplsTpPwStatsInfoTable.setStatus("current")
_SleMplsTpPwStatsInfoEntry_Object = MibTableRow
sleMplsTpPwStatsInfoEntry = _SleMplsTpPwStatsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 21, 1, 1, 1)
)
sleMplsTpPwStatsInfoEntry.setIndexNames(
    (0, "SLE-MPLS-TP-PW-STATISTICS-MIB", "sleMplsTpPwStatsInfoPwId"),
)
if mibBuilder.loadTexts:
    sleMplsTpPwStatsInfoEntry.setStatus("current")


class _SleMplsTpPwStatsInfoPwId_Type(PwIDType):
    """Custom type sleMplsTpPwStatsInfoPwId based on PwIDType"""
    subtypeSpec = PwIDType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleMplsTpPwStatsInfoPwId_Type.__name__ = "PwIDType"
_SleMplsTpPwStatsInfoPwId_Object = MibTableColumn
sleMplsTpPwStatsInfoPwId = _SleMplsTpPwStatsInfoPwId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 21, 1, 1, 1, 1),
    _SleMplsTpPwStatsInfoPwId_Type()
)
sleMplsTpPwStatsInfoPwId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMplsTpPwStatsInfoPwId.setStatus("current")
_SleMplsTpPwStatsInfoPwName_Type = SnmpAdminString
_SleMplsTpPwStatsInfoPwName_Object = MibTableColumn
sleMplsTpPwStatsInfoPwName = _SleMplsTpPwStatsInfoPwName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 21, 1, 1, 1, 2),
    _SleMplsTpPwStatsInfoPwName_Type()
)
sleMplsTpPwStatsInfoPwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwStatsInfoPwName.setStatus("current")
_SleMplsTpPwStatsInfoTxPkts_Type = Counter64
_SleMplsTpPwStatsInfoTxPkts_Object = MibTableColumn
sleMplsTpPwStatsInfoTxPkts = _SleMplsTpPwStatsInfoTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 21, 1, 1, 1, 3),
    _SleMplsTpPwStatsInfoTxPkts_Type()
)
sleMplsTpPwStatsInfoTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwStatsInfoTxPkts.setStatus("current")
_SleMplsTpPwStatsInfoRxPkts_Type = Counter64
_SleMplsTpPwStatsInfoRxPkts_Object = MibTableColumn
sleMplsTpPwStatsInfoRxPkts = _SleMplsTpPwStatsInfoRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 21, 1, 1, 1, 4),
    _SleMplsTpPwStatsInfoRxPkts_Type()
)
sleMplsTpPwStatsInfoRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwStatsInfoRxPkts.setStatus("current")
_SleMplsTpPwStatsInfoTxBytes_Type = Counter64
_SleMplsTpPwStatsInfoTxBytes_Object = MibTableColumn
sleMplsTpPwStatsInfoTxBytes = _SleMplsTpPwStatsInfoTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 21, 1, 1, 1, 5),
    _SleMplsTpPwStatsInfoTxBytes_Type()
)
sleMplsTpPwStatsInfoTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwStatsInfoTxBytes.setStatus("current")
_SleMplsTpPwStatsInfoRxBytes_Type = Counter64
_SleMplsTpPwStatsInfoRxBytes_Object = MibTableColumn
sleMplsTpPwStatsInfoRxBytes = _SleMplsTpPwStatsInfoRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 21, 1, 1, 1, 6),
    _SleMplsTpPwStatsInfoRxBytes_Type()
)
sleMplsTpPwStatsInfoRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwStatsInfoRxBytes.setStatus("current")
_SleMplsTpPwStatsControl_ObjectIdentity = ObjectIdentity
sleMplsTpPwStatsControl = _SleMplsTpPwStatsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 21, 1, 2)
)


class _SleMplsTpPwStatsControlRequest_Type(Integer32):
    """Custom type sleMplsTpPwStatsControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setToClearPwStats", 1)
    )


_SleMplsTpPwStatsControlRequest_Type.__name__ = "Integer32"
_SleMplsTpPwStatsControlRequest_Object = MibScalar
sleMplsTpPwStatsControlRequest = _SleMplsTpPwStatsControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 21, 1, 2, 1),
    _SleMplsTpPwStatsControlRequest_Type()
)
sleMplsTpPwStatsControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwStatsControlRequest.setStatus("current")
_SleMplsTpPwStatsControlStatus_Type = SleControlStatusType
_SleMplsTpPwStatsControlStatus_Object = MibScalar
sleMplsTpPwStatsControlStatus = _SleMplsTpPwStatsControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 21, 1, 2, 2),
    _SleMplsTpPwStatsControlStatus_Type()
)
sleMplsTpPwStatsControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwStatsControlStatus.setStatus("current")
_SleMplsTpPwStatsControlTimer_Type = Gauge32
_SleMplsTpPwStatsControlTimer_Object = MibScalar
sleMplsTpPwStatsControlTimer = _SleMplsTpPwStatsControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 21, 1, 2, 3),
    _SleMplsTpPwStatsControlTimer_Type()
)
sleMplsTpPwStatsControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwStatsControlTimer.setStatus("current")
_SleMplsTpPwStatsControlTimeStamp_Type = TimeTicks
_SleMplsTpPwStatsControlTimeStamp_Object = MibScalar
sleMplsTpPwStatsControlTimeStamp = _SleMplsTpPwStatsControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 21, 1, 2, 4),
    _SleMplsTpPwStatsControlTimeStamp_Type()
)
sleMplsTpPwStatsControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwStatsControlTimeStamp.setStatus("current")
_SleMplsTpPwStatsReqResult_Type = SleControlRequestResultType
_SleMplsTpPwStatsReqResult_Object = MibScalar
sleMplsTpPwStatsReqResult = _SleMplsTpPwStatsReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 21, 1, 2, 5),
    _SleMplsTpPwStatsReqResult_Type()
)
sleMplsTpPwStatsReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwStatsReqResult.setStatus("current")
_SleMplsTpPwStatsControlPwId_Type = Unsigned32
_SleMplsTpPwStatsControlPwId_Object = MibScalar
sleMplsTpPwStatsControlPwId = _SleMplsTpPwStatsControlPwId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 21, 1, 2, 6),
    _SleMplsTpPwStatsControlPwId_Type()
)
sleMplsTpPwStatsControlPwId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwStatsControlPwId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-MPLS-TP-PW-STATISTICS-MIB",
    **{"sleMpls": sleMpls,
       "sleMplsTpPwStats": sleMplsTpPwStats,
       "sleMplsTpPwStatsTable": sleMplsTpPwStatsTable,
       "sleMplsTpPwStatsInfoTable": sleMplsTpPwStatsInfoTable,
       "sleMplsTpPwStatsInfoEntry": sleMplsTpPwStatsInfoEntry,
       "sleMplsTpPwStatsInfoPwId": sleMplsTpPwStatsInfoPwId,
       "sleMplsTpPwStatsInfoPwName": sleMplsTpPwStatsInfoPwName,
       "sleMplsTpPwStatsInfoTxPkts": sleMplsTpPwStatsInfoTxPkts,
       "sleMplsTpPwStatsInfoRxPkts": sleMplsTpPwStatsInfoRxPkts,
       "sleMplsTpPwStatsInfoTxBytes": sleMplsTpPwStatsInfoTxBytes,
       "sleMplsTpPwStatsInfoRxBytes": sleMplsTpPwStatsInfoRxBytes,
       "sleMplsTpPwStatsControl": sleMplsTpPwStatsControl,
       "sleMplsTpPwStatsControlRequest": sleMplsTpPwStatsControlRequest,
       "sleMplsTpPwStatsControlStatus": sleMplsTpPwStatsControlStatus,
       "sleMplsTpPwStatsControlTimer": sleMplsTpPwStatsControlTimer,
       "sleMplsTpPwStatsControlTimeStamp": sleMplsTpPwStatsControlTimeStamp,
       "sleMplsTpPwStatsReqResult": sleMplsTpPwStatsReqResult,
       "sleMplsTpPwStatsControlPwId": sleMplsTpPwStatsControlPwId}
)
