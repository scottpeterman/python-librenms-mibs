# SNMP MIB module (SLE-DEBUG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-DEBUG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:23 2025
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

(SleControlRequestResultType,
 SleControlStatusType) = mibBuilder.importSymbols(
    "SLE-TC-MIB",
    "SleControlRequestResultType",
    "SleControlStatusType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Bits,
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sleDebug = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99)
)


# Types definitions



class OwnerString(OctetString):
    """Custom type OwnerString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleDebugBase_ObjectIdentity = ObjectIdentity
sleDebugBase = _SleDebugBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1)
)
_SleDebugStatus_ObjectIdentity = ObjectIdentity
sleDebugStatus = _SleDebugStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 1)
)


class _SleDebugDhcpStatus_Type(Bits):
    """Custom type sleDebugDhcpStatus based on Bits"""
    namedValues = NamedValues(
        *(("debugFilter", 0),
          ("debugLease", 1),
          ("debugPacket", 2),
          ("debugServices", 3))
    )

_SleDebugDhcpStatus_Type.__name__ = "Bits"
_SleDebugDhcpStatus_Object = MibScalar
sleDebugDhcpStatus = _SleDebugDhcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 1, 1),
    _SleDebugDhcpStatus_Type()
)
sleDebugDhcpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDebugDhcpStatus.setStatus("current")


class _SleDebugIgmpStatus_Type(Bits):
    """Custom type sleDebugIgmpStatus based on Bits"""
    namedValues = NamedValues(
        *(("debugDecode", 0),
          ("debugEncode", 1),
          ("debugEvents", 2),
          ("debugFsm", 3),
          ("debugTib", 4))
    )

_SleDebugIgmpStatus_Type.__name__ = "Bits"
_SleDebugIgmpStatus_Object = MibScalar
sleDebugIgmpStatus = _SleDebugIgmpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 1, 2),
    _SleDebugIgmpStatus_Type()
)
sleDebugIgmpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDebugIgmpStatus.setStatus("current")


class _SleDebugIgmpSnoopStatus_Type(Bits):
    """Custom type sleDebugIgmpSnoopStatus based on Bits"""
    namedValues = NamedValues(
        ("debugTcn", 0)
    )

_SleDebugIgmpSnoopStatus_Type.__name__ = "Bits"
_SleDebugIgmpSnoopStatus_Object = MibScalar
sleDebugIgmpSnoopStatus = _SleDebugIgmpSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 1, 3),
    _SleDebugIgmpSnoopStatus_Type()
)
sleDebugIgmpSnoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDebugIgmpSnoopStatus.setStatus("current")


class _SleDebugNsmStatus_Type(Bits):
    """Custom type sleDebugNsmStatus based on Bits"""
    namedValues = NamedValues(
        *(("debugEvents", 0),
          ("debugKernel", 1),
          ("debugPacketDetail", 2),
          ("debugPacketRecv", 3),
          ("debugPacketSend", 4))
    )

_SleDebugNsmStatus_Type.__name__ = "Bits"
_SleDebugNsmStatus_Object = MibScalar
sleDebugNsmStatus = _SleDebugNsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 1, 4),
    _SleDebugNsmStatus_Type()
)
sleDebugNsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDebugNsmStatus.setStatus("current")


class _SleDebugNsmMcastStatus_Type(Bits):
    """Custom type sleDebugNsmMcastStatus based on Bits"""
    namedValues = NamedValues(
        *(("debugMcastFibMsg", 0),
          ("debugMcastMrt", 1),
          ("debugMcastRegister", 2),
          ("debugMcastStats", 3),
          ("debugMcastVif", 4))
    )

_SleDebugNsmMcastStatus_Type.__name__ = "Bits"
_SleDebugNsmMcastStatus_Object = MibScalar
sleDebugNsmMcastStatus = _SleDebugNsmMcastStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 1, 5),
    _SleDebugNsmMcastStatus_Type()
)
sleDebugNsmMcastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDebugNsmMcastStatus.setStatus("current")


class _SleDebugBgpStatus_Type(Bits):
    """Custom type sleDebugBgpStatus based on Bits"""
    namedValues = NamedValues(
        *(("debugNormal", 0),
          ("debugDampening", 1),
          ("debugEvents", 2),
          ("debugFilters", 3),
          ("debugFsm", 4),
          ("debugKeepalives", 5),
          ("debugNsm", 6),
          ("debugUpdatesIn", 7),
          ("debugUpdatesOut", 8))
    )

_SleDebugBgpStatus_Type.__name__ = "Bits"
_SleDebugBgpStatus_Object = MibScalar
sleDebugBgpStatus = _SleDebugBgpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 1, 6),
    _SleDebugBgpStatus_Type()
)
sleDebugBgpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDebugBgpStatus.setStatus("current")


class _SleDebugOspfStatus_Type(Bits):
    """Custom type sleDebugOspfStatus based on Bits"""
    namedValues = NamedValues(
        *(("debugEventAbr", 0),
          ("debugEventAsbr", 1),
          ("debugEventLsa", 2),
          ("debugEventNssa", 3),
          ("debugEventOs", 4),
          ("debugEventRouter", 5),
          ("debugEventVlink", 6),
          ("debugIfsmEvent", 7),
          ("debugIfsmStatus", 8),
          ("debugIfsmTimers", 9),
          ("debugLsaFlooding", 10),
          ("debugLsaGenerate", 11),
          ("debugLsaInstall", 12),
          ("debugLsaMaxage", 13),
          ("debugLsaRefrash", 14),
          ("debugNfsmEvents", 15),
          ("debugNfsmStatus", 16),
          ("debugNfsmTimers", 17),
          ("debugNsmInterface", 18),
          ("debugNsmRedistribute", 19),
          ("debugRouteAse", 20),
          ("debugRouteIa", 21),
          ("debugRouteInstall", 22),
          ("debugRouteSpf", 23),
          ("debugPacketDDDetail", 24),
          ("debugPacketDDRecv", 25),
          ("debugPacketDDSend", 26),
          ("debugPacketHelloDetail", 27),
          ("debugPacketHelloRecv", 28),
          ("debugPacketHelloSend", 29),
          ("debugPacketLsAckDetail", 30),
          ("debugPacketLsAckRecv", 31),
          ("debugPacketLsAckSend", 32),
          ("debugPacketLsRequestDetail", 33),
          ("debugPacketLsRequestRecv", 34),
          ("debugPacketLsRequestSend", 35),
          ("debugPacketLsUpdateDetail", 36),
          ("debugPacketLsUpdateRecv", 37),
          ("debugPacketLsUpdateSend", 38))
    )

_SleDebugOspfStatus_Type.__name__ = "Bits"
_SleDebugOspfStatus_Object = MibScalar
sleDebugOspfStatus = _SleDebugOspfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 1, 7),
    _SleDebugOspfStatus_Type()
)
sleDebugOspfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDebugOspfStatus.setStatus("current")


class _SleDebugPimStatus_Type(Bits):
    """Custom type sleDebugPimStatus based on Bits"""
    namedValues = NamedValues(
        *(("debugEvent", 0),
          ("debugMfc", 1),
          ("debugMib", 2),
          ("debugNexthop", 3),
          ("debugNsm", 4),
          ("debugPacketIn", 5),
          ("debugPacketOut", 6),
          ("debugState", 7),
          ("debugTimerAssertAt", 8),
          ("debugTimerBsr", 9),
          ("debugTimerBsrBst", 10),
          ("debugTimerBsrCrp", 11),
          ("debugTimerHello", 12),
          ("debugTimerHelloHt", 13),
          ("debugTimerHelloNlt", 14),
          ("debugTimerHelloTht", 15),
          ("debugTimerJoinprune", 16),
          ("debugTimerJoinpruneEt", 17),
          ("debugTimerJoinpruneJt", 18),
          ("debugTimerJoinpruneKat", 19),
          ("debugTimerJoinpruneOt", 20),
          ("debugTimerJoinprunePpt", 21),
          ("debugTimerRegister", 22))
    )

_SleDebugPimStatus_Type.__name__ = "Bits"
_SleDebugPimStatus_Object = MibScalar
sleDebugPimStatus = _SleDebugPimStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 1, 8),
    _SleDebugPimStatus_Type()
)
sleDebugPimStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDebugPimStatus.setStatus("current")


class _SleDebugRipStatus_Type(Bits):
    """Custom type sleDebugRipStatus based on Bits"""
    namedValues = NamedValues(
        *(("debugEvents", 0),
          ("debugNsm", 1),
          ("debugPacketDetail", 2),
          ("debugPacketRecv", 3),
          ("debugPacketSend", 4))
    )

_SleDebugRipStatus_Type.__name__ = "Bits"
_SleDebugRipStatus_Object = MibScalar
sleDebugRipStatus = _SleDebugRipStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 1, 9),
    _SleDebugRipStatus_Type()
)
sleDebugRipStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDebugRipStatus.setStatus("current")
_SleDebugStatusControl_ObjectIdentity = ObjectIdentity
sleDebugStatusControl = _SleDebugStatusControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 2)
)


class _SleDebugControlRequest_Type(Integer32):
    """Custom type sleDebugControlRequest based on Integer32"""
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
        *(("setDhcpDebugStatus", 1),
          ("setIgmpDebugStatus", 2),
          ("setIgmpSnoopDebugStats", 3),
          ("setNsmDebugStatus", 4),
          ("setNsmMcastDebugStatus", 5),
          ("setBgpDebugStatus", 6),
          ("setOspfDebugStatus", 7),
          ("setPimDebugStatus", 8),
          ("setRipDebugStatus", 9))
    )


_SleDebugControlRequest_Type.__name__ = "Integer32"
_SleDebugControlRequest_Object = MibScalar
sleDebugControlRequest = _SleDebugControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 2, 1),
    _SleDebugControlRequest_Type()
)
sleDebugControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDebugControlRequest.setStatus("current")
_SleDebugControlStatus_Type = SleControlStatusType
_SleDebugControlStatus_Object = MibScalar
sleDebugControlStatus = _SleDebugControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 2, 2),
    _SleDebugControlStatus_Type()
)
sleDebugControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDebugControlStatus.setStatus("current")
_SleDebugControlTimer_Type = Gauge32
_SleDebugControlTimer_Object = MibScalar
sleDebugControlTimer = _SleDebugControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 2, 3),
    _SleDebugControlTimer_Type()
)
sleDebugControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDebugControlTimer.setStatus("current")
_SleDebugControlTimeStamp_Type = TimeTicks
_SleDebugControlTimeStamp_Object = MibScalar
sleDebugControlTimeStamp = _SleDebugControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 2, 4),
    _SleDebugControlTimeStamp_Type()
)
sleDebugControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDebugControlTimeStamp.setStatus("current")
_SleDebugControlReqResult_Type = SleControlRequestResultType
_SleDebugControlReqResult_Object = MibScalar
sleDebugControlReqResult = _SleDebugControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 2, 5),
    _SleDebugControlReqResult_Type()
)
sleDebugControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDebugControlReqResult.setStatus("current")


class _SleDebugControlDhcpStatus_Type(Bits):
    """Custom type sleDebugControlDhcpStatus based on Bits"""
    namedValues = NamedValues(
        *(("debugFilter", 0),
          ("debugLease", 1),
          ("debugPacket", 2),
          ("debugServices", 3))
    )

_SleDebugControlDhcpStatus_Type.__name__ = "Bits"
_SleDebugControlDhcpStatus_Object = MibScalar
sleDebugControlDhcpStatus = _SleDebugControlDhcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 2, 6),
    _SleDebugControlDhcpStatus_Type()
)
sleDebugControlDhcpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDebugControlDhcpStatus.setStatus("current")


class _SleDebugControlIgmpStatus_Type(Bits):
    """Custom type sleDebugControlIgmpStatus based on Bits"""
    namedValues = NamedValues(
        *(("debugDecode", 0),
          ("debugEncode", 1),
          ("debugEvents", 2),
          ("debugFsm", 3),
          ("debugTib", 4))
    )

_SleDebugControlIgmpStatus_Type.__name__ = "Bits"
_SleDebugControlIgmpStatus_Object = MibScalar
sleDebugControlIgmpStatus = _SleDebugControlIgmpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 2, 7),
    _SleDebugControlIgmpStatus_Type()
)
sleDebugControlIgmpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDebugControlIgmpStatus.setStatus("current")


class _SleDebugControlIgmpSnoopStatus_Type(Bits):
    """Custom type sleDebugControlIgmpSnoopStatus based on Bits"""
    namedValues = NamedValues(
        ("debugTcn", 0)
    )

_SleDebugControlIgmpSnoopStatus_Type.__name__ = "Bits"
_SleDebugControlIgmpSnoopStatus_Object = MibScalar
sleDebugControlIgmpSnoopStatus = _SleDebugControlIgmpSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 2, 8),
    _SleDebugControlIgmpSnoopStatus_Type()
)
sleDebugControlIgmpSnoopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDebugControlIgmpSnoopStatus.setStatus("current")


class _SleDebugControlNsmStatus_Type(Bits):
    """Custom type sleDebugControlNsmStatus based on Bits"""
    namedValues = NamedValues(
        *(("debugEvents", 0),
          ("debugKernel", 1),
          ("debugPacketDetail", 2),
          ("debugPacketRecv", 3),
          ("debugPacketSend", 4))
    )

_SleDebugControlNsmStatus_Type.__name__ = "Bits"
_SleDebugControlNsmStatus_Object = MibScalar
sleDebugControlNsmStatus = _SleDebugControlNsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 2, 9),
    _SleDebugControlNsmStatus_Type()
)
sleDebugControlNsmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDebugControlNsmStatus.setStatus("current")


class _SleDebugControlNsmMcastStatus_Type(Bits):
    """Custom type sleDebugControlNsmMcastStatus based on Bits"""
    namedValues = NamedValues(
        *(("debugMcastFibMsg", 0),
          ("debugMcastMrt", 1),
          ("debugMcastRegister", 2),
          ("debugMcastStats", 3),
          ("debugMcastVif", 4))
    )

_SleDebugControlNsmMcastStatus_Type.__name__ = "Bits"
_SleDebugControlNsmMcastStatus_Object = MibScalar
sleDebugControlNsmMcastStatus = _SleDebugControlNsmMcastStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 2, 10),
    _SleDebugControlNsmMcastStatus_Type()
)
sleDebugControlNsmMcastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDebugControlNsmMcastStatus.setStatus("current")


class _SleDebugControlBgpStatus_Type(Bits):
    """Custom type sleDebugControlBgpStatus based on Bits"""
    namedValues = NamedValues(
        *(("debugNormal", 0),
          ("debugDampening", 1),
          ("debugEvents", 2),
          ("debugFilters", 3),
          ("debugFsm", 4),
          ("debugKeepalives", 5),
          ("debugNsm", 6),
          ("debugUpdatesIn", 7),
          ("debugUpdatesOut", 8))
    )

_SleDebugControlBgpStatus_Type.__name__ = "Bits"
_SleDebugControlBgpStatus_Object = MibScalar
sleDebugControlBgpStatus = _SleDebugControlBgpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 2, 11),
    _SleDebugControlBgpStatus_Type()
)
sleDebugControlBgpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDebugControlBgpStatus.setStatus("current")


class _SleDebugControlOspfStatus_Type(Bits):
    """Custom type sleDebugControlOspfStatus based on Bits"""
    namedValues = NamedValues(
        *(("debugEventAbr", 0),
          ("debugEventAsbr", 1),
          ("debugEventLsa", 2),
          ("debugEventNssa", 3),
          ("debugEventOs", 4),
          ("debugEventRouter", 5),
          ("debugEventVlink", 6),
          ("debugIfsmEvent", 7),
          ("debugIfsmStatus", 8),
          ("debugIfsmTimers", 9),
          ("debugLsaFlooding", 10),
          ("debugLsaGenerate", 11),
          ("debugLsaInstall", 12),
          ("debugLsaMaxage", 13),
          ("debugLsaRefrash", 14),
          ("debugNfsmEvents", 15),
          ("debugNfsmStatus", 16),
          ("debugNfsmTimers", 17),
          ("debugNsmInterface", 18),
          ("debugNsmRedistribute", 19),
          ("debugRouteAse", 20),
          ("debugRouteIa", 21),
          ("debugRouteInstall", 22),
          ("debugRouteSpf", 23),
          ("debugPacketDDDetail", 24),
          ("debugPacketDDRecv", 25),
          ("debugPacketDDSend", 26),
          ("debugPacketHelloDetail", 27),
          ("debugPacketHelloRecv", 28),
          ("debugPacketHelloSend", 29),
          ("debugPacketLsAckDetail", 30),
          ("debugPacketLsAckRecv", 31),
          ("debugPacketLsAckSend", 32),
          ("debugPacketLsRequestDetail", 33),
          ("debugPacketLsRequestRecv", 34),
          ("debugPacketLsRequestSend", 35),
          ("debugPacketLsUpdateDetail", 36),
          ("debugPacketLsUpdateRecv", 37),
          ("debugPacketLsUpdateSend", 38))
    )

_SleDebugControlOspfStatus_Type.__name__ = "Bits"
_SleDebugControlOspfStatus_Object = MibScalar
sleDebugControlOspfStatus = _SleDebugControlOspfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 2, 12),
    _SleDebugControlOspfStatus_Type()
)
sleDebugControlOspfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDebugControlOspfStatus.setStatus("current")


class _SleDebugControlPimStatus_Type(Bits):
    """Custom type sleDebugControlPimStatus based on Bits"""
    namedValues = NamedValues(
        *(("debugEvent", 0),
          ("debugMfc", 1),
          ("debugMib", 2),
          ("debugNexthop", 3),
          ("debugNsm", 4),
          ("debugPacketIn", 5),
          ("debugPacketOut", 6),
          ("debugState", 7),
          ("debugTimerAssertAt", 8),
          ("debugTimerBsr", 9),
          ("debugTimerBsrBst", 10),
          ("debugTimerBsrCrp", 11),
          ("debugTimerHello", 12),
          ("debugTimerHelloHt", 13),
          ("debugTimerHelloNlt", 14),
          ("debugTimerHelloTht", 15),
          ("debugTimerJoinprune", 16),
          ("debugTimerJoinpruneEt", 17),
          ("debugTimerJoinpruneJt", 18),
          ("debugTimerJoinpruneKat", 19),
          ("debugTimerJoinpruneOt", 20),
          ("debugTimerJoinprunePpt", 21),
          ("debugTimerRegister", 22))
    )

_SleDebugControlPimStatus_Type.__name__ = "Bits"
_SleDebugControlPimStatus_Object = MibScalar
sleDebugControlPimStatus = _SleDebugControlPimStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 2, 13),
    _SleDebugControlPimStatus_Type()
)
sleDebugControlPimStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDebugControlPimStatus.setStatus("current")


class _SleDebugControlRipStatus_Type(Bits):
    """Custom type sleDebugControlRipStatus based on Bits"""
    namedValues = NamedValues(
        *(("debugEvents", 0),
          ("debugNsm", 1),
          ("debugPacketDetail", 2),
          ("debugPacketRecv", 3),
          ("debugPacketSend", 4))
    )

_SleDebugControlRipStatus_Type.__name__ = "Bits"
_SleDebugControlRipStatus_Object = MibScalar
sleDebugControlRipStatus = _SleDebugControlRipStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 2, 14),
    _SleDebugControlRipStatus_Type()
)
sleDebugControlRipStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDebugControlRipStatus.setStatus("current")
_SleDebugStatusNotification_ObjectIdentity = ObjectIdentity
sleDebugStatusNotification = _SleDebugStatusNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 3)
)

# Managed Objects groups

sleDebugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 2)
)
sleDebugGroup.setObjects(
      *(("SLE-DEBUG-MIB", "sleDebugDhcpStatus"),
        ("SLE-DEBUG-MIB", "sleDebugIgmpStatus"),
        ("SLE-DEBUG-MIB", "sleDebugIgmpSnoopStatus"),
        ("SLE-DEBUG-MIB", "sleDebugNsmStatus"),
        ("SLE-DEBUG-MIB", "sleDebugNsmMcastStatus"),
        ("SLE-DEBUG-MIB", "sleDebugBgpStatus"),
        ("SLE-DEBUG-MIB", "sleDebugOspfStatus"),
        ("SLE-DEBUG-MIB", "sleDebugPimStatus"),
        ("SLE-DEBUG-MIB", "sleDebugRipStatus"),
        ("SLE-DEBUG-MIB", "sleDebugControlRequest"),
        ("SLE-DEBUG-MIB", "sleDebugControlStatus"),
        ("SLE-DEBUG-MIB", "sleDebugControlTimer"),
        ("SLE-DEBUG-MIB", "sleDebugControlTimeStamp"),
        ("SLE-DEBUG-MIB", "sleDebugControlReqResult"),
        ("SLE-DEBUG-MIB", "sleDebugControlDhcpStatus"),
        ("SLE-DEBUG-MIB", "sleDebugControlIgmpStatus"),
        ("SLE-DEBUG-MIB", "sleDebugControlIgmpSnoopStatus"),
        ("SLE-DEBUG-MIB", "sleDebugControlNsmStatus"),
        ("SLE-DEBUG-MIB", "sleDebugControlNsmMcastStatus"),
        ("SLE-DEBUG-MIB", "sleDebugControlBgpStatus"),
        ("SLE-DEBUG-MIB", "sleDebugControlOspfStatus"),
        ("SLE-DEBUG-MIB", "sleDebugControlPimStatus"),
        ("SLE-DEBUG-MIB", "sleDebugControlRipStatus"))
)
if mibBuilder.loadTexts:
    sleDebugGroup.setStatus("current")


# Notification objects

sleDebugDhcpStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 3, 1)
)
sleDebugDhcpStatusChanged.setObjects(
      *(("SLE-DEBUG-MIB", "sleDebugControlRequest"),
        ("SLE-DEBUG-MIB", "sleDebugControlTimeStamp"),
        ("SLE-DEBUG-MIB", "sleDebugControlReqResult"),
        ("SLE-DEBUG-MIB", "sleDebugDhcpStatus"))
)
if mibBuilder.loadTexts:
    sleDebugDhcpStatusChanged.setStatus(
        "current"
    )

sleDebugIgmpStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 3, 2)
)
sleDebugIgmpStatusChanged.setObjects(
      *(("SLE-DEBUG-MIB", "sleDebugControlRequest"),
        ("SLE-DEBUG-MIB", "sleDebugControlTimeStamp"),
        ("SLE-DEBUG-MIB", "sleDebugControlReqResult"),
        ("SLE-DEBUG-MIB", "sleDebugIgmpStatus"))
)
if mibBuilder.loadTexts:
    sleDebugIgmpStatusChanged.setStatus(
        "current"
    )

sleDebugIgmpSnoopStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 3, 3)
)
sleDebugIgmpSnoopStatusChanged.setObjects(
      *(("SLE-DEBUG-MIB", "sleDebugControlRequest"),
        ("SLE-DEBUG-MIB", "sleDebugControlTimeStamp"),
        ("SLE-DEBUG-MIB", "sleDebugControlReqResult"),
        ("SLE-DEBUG-MIB", "sleDebugIgmpSnoopStatus"))
)
if mibBuilder.loadTexts:
    sleDebugIgmpSnoopStatusChanged.setStatus(
        "current"
    )

sleDebugNsmStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 3, 4)
)
sleDebugNsmStatusChanged.setObjects(
      *(("SLE-DEBUG-MIB", "sleDebugControlRequest"),
        ("SLE-DEBUG-MIB", "sleDebugControlTimeStamp"),
        ("SLE-DEBUG-MIB", "sleDebugControlReqResult"),
        ("SLE-DEBUG-MIB", "sleDebugNsmStatus"))
)
if mibBuilder.loadTexts:
    sleDebugNsmStatusChanged.setStatus(
        "current"
    )

sleDebugNsmMcastStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 3, 5)
)
sleDebugNsmMcastStatusChanged.setObjects(
      *(("SLE-DEBUG-MIB", "sleDebugControlRequest"),
        ("SLE-DEBUG-MIB", "sleDebugControlTimeStamp"),
        ("SLE-DEBUG-MIB", "sleDebugControlReqResult"),
        ("SLE-DEBUG-MIB", "sleDebugNsmMcastStatus"))
)
if mibBuilder.loadTexts:
    sleDebugNsmMcastStatusChanged.setStatus(
        "current"
    )

sleDebugBgpStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 3, 6)
)
sleDebugBgpStatusChanged.setObjects(
      *(("SLE-DEBUG-MIB", "sleDebugControlRequest"),
        ("SLE-DEBUG-MIB", "sleDebugControlTimeStamp"),
        ("SLE-DEBUG-MIB", "sleDebugControlReqResult"),
        ("SLE-DEBUG-MIB", "sleDebugBgpStatus"))
)
if mibBuilder.loadTexts:
    sleDebugBgpStatusChanged.setStatus(
        "current"
    )

sleDebugOspfStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 3, 7)
)
sleDebugOspfStatusChanged.setObjects(
      *(("SLE-DEBUG-MIB", "sleDebugControlRequest"),
        ("SLE-DEBUG-MIB", "sleDebugControlTimeStamp"),
        ("SLE-DEBUG-MIB", "sleDebugControlReqResult"),
        ("SLE-DEBUG-MIB", "sleDebugOspfStatus"))
)
if mibBuilder.loadTexts:
    sleDebugOspfStatusChanged.setStatus(
        "current"
    )

sleDebugPimStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 3, 8)
)
sleDebugPimStatusChanged.setObjects(
      *(("SLE-DEBUG-MIB", "sleDebugControlRequest"),
        ("SLE-DEBUG-MIB", "sleDebugControlTimeStamp"),
        ("SLE-DEBUG-MIB", "sleDebugControlReqResult"),
        ("SLE-DEBUG-MIB", "sleDebugPimStatus"))
)
if mibBuilder.loadTexts:
    sleDebugPimStatusChanged.setStatus(
        "current"
    )

sleDebugRipStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 1, 3, 9)
)
sleDebugRipStatusChanged.setObjects(
      *(("SLE-DEBUG-MIB", "sleDebugControlRequest"),
        ("SLE-DEBUG-MIB", "sleDebugControlTimeStamp"),
        ("SLE-DEBUG-MIB", "sleDebugControlReqResult"),
        ("SLE-DEBUG-MIB", "sleDebugRipStatus"))
)
if mibBuilder.loadTexts:
    sleDebugRipStatusChanged.setStatus(
        "current"
    )


# Notifications groups

sleDebugNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 99, 3)
)
sleDebugNotificationGroup.setObjects(
      *(("SLE-DEBUG-MIB", "sleDebugDhcpStatusChanged"),
        ("SLE-DEBUG-MIB", "sleDebugIgmpStatusChanged"),
        ("SLE-DEBUG-MIB", "sleDebugIgmpSnoopStatusChanged"),
        ("SLE-DEBUG-MIB", "sleDebugNsmStatusChanged"),
        ("SLE-DEBUG-MIB", "sleDebugNsmMcastStatusChanged"),
        ("SLE-DEBUG-MIB", "sleDebugBgpStatusChanged"),
        ("SLE-DEBUG-MIB", "sleDebugOspfStatusChanged"),
        ("SLE-DEBUG-MIB", "sleDebugPimStatusChanged"),
        ("SLE-DEBUG-MIB", "sleDebugRipStatusChanged"))
)
if mibBuilder.loadTexts:
    sleDebugNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-DEBUG-MIB",
    **{"OwnerString": OwnerString,
       "sleDebug": sleDebug,
       "sleDebugBase": sleDebugBase,
       "sleDebugStatus": sleDebugStatus,
       "sleDebugDhcpStatus": sleDebugDhcpStatus,
       "sleDebugIgmpStatus": sleDebugIgmpStatus,
       "sleDebugIgmpSnoopStatus": sleDebugIgmpSnoopStatus,
       "sleDebugNsmStatus": sleDebugNsmStatus,
       "sleDebugNsmMcastStatus": sleDebugNsmMcastStatus,
       "sleDebugBgpStatus": sleDebugBgpStatus,
       "sleDebugOspfStatus": sleDebugOspfStatus,
       "sleDebugPimStatus": sleDebugPimStatus,
       "sleDebugRipStatus": sleDebugRipStatus,
       "sleDebugStatusControl": sleDebugStatusControl,
       "sleDebugControlRequest": sleDebugControlRequest,
       "sleDebugControlStatus": sleDebugControlStatus,
       "sleDebugControlTimer": sleDebugControlTimer,
       "sleDebugControlTimeStamp": sleDebugControlTimeStamp,
       "sleDebugControlReqResult": sleDebugControlReqResult,
       "sleDebugControlDhcpStatus": sleDebugControlDhcpStatus,
       "sleDebugControlIgmpStatus": sleDebugControlIgmpStatus,
       "sleDebugControlIgmpSnoopStatus": sleDebugControlIgmpSnoopStatus,
       "sleDebugControlNsmStatus": sleDebugControlNsmStatus,
       "sleDebugControlNsmMcastStatus": sleDebugControlNsmMcastStatus,
       "sleDebugControlBgpStatus": sleDebugControlBgpStatus,
       "sleDebugControlOspfStatus": sleDebugControlOspfStatus,
       "sleDebugControlPimStatus": sleDebugControlPimStatus,
       "sleDebugControlRipStatus": sleDebugControlRipStatus,
       "sleDebugStatusNotification": sleDebugStatusNotification,
       "sleDebugDhcpStatusChanged": sleDebugDhcpStatusChanged,
       "sleDebugIgmpStatusChanged": sleDebugIgmpStatusChanged,
       "sleDebugIgmpSnoopStatusChanged": sleDebugIgmpSnoopStatusChanged,
       "sleDebugNsmStatusChanged": sleDebugNsmStatusChanged,
       "sleDebugNsmMcastStatusChanged": sleDebugNsmMcastStatusChanged,
       "sleDebugBgpStatusChanged": sleDebugBgpStatusChanged,
       "sleDebugOspfStatusChanged": sleDebugOspfStatusChanged,
       "sleDebugPimStatusChanged": sleDebugPimStatusChanged,
       "sleDebugRipStatusChanged": sleDebugRipStatusChanged,
       "sleDebugGroup": sleDebugGroup,
       "sleDebugNotificationGroup": sleDebugNotificationGroup}
)
