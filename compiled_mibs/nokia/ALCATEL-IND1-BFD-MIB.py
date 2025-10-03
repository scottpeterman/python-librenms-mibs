# SNMP MIB module (ALCATEL-IND1-BFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-BFD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:13:07 2025
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

(softentIND1BFD,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1BFD")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1BfdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1BfdMIB.setRevisions(
        ("2008-05-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaBfdInterval(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class AlaBfdDiag(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("noDiagnostic", 1),
          ("controlDetectionTimeExpired", 2),
          ("echoFunctionFailed", 3),
          ("neighborSignaledSessionDown", 4),
          ("forwardingPlaneReset", 5),
          ("pathDown", 6),
          ("concatenatedPathDown", 7),
          ("administrativelyDown", 8),
          ("reverseConcatenatedPathDown", 9))
    )



class AlaBfdStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AlaBfdObjects_ObjectIdentity = ObjectIdentity
alaBfdObjects = _AlaBfdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1)
)
if mibBuilder.loadTexts:
    alaBfdObjects.setStatus("current")
_AlaBfdGlobalObjects_ObjectIdentity = ObjectIdentity
alaBfdGlobalObjects = _AlaBfdGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 1)
)


class _AlaBfdGlobalAdminStatus_Type(AlaBfdStatus):
    """Custom type alaBfdGlobalAdminStatus based on AlaBfdStatus"""
    defaultValue = 1


_AlaBfdGlobalAdminStatus_Type.__name__ = "AlaBfdStatus"
_AlaBfdGlobalAdminStatus_Object = MibScalar
alaBfdGlobalAdminStatus = _AlaBfdGlobalAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 1, 1),
    _AlaBfdGlobalAdminStatus_Type()
)
alaBfdGlobalAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBfdGlobalAdminStatus.setStatus("current")


class _AlaBfdGlobalTxInterval_Type(AlaBfdInterval):
    """Custom type alaBfdGlobalTxInterval based on AlaBfdInterval"""
    defaultValue = 300


_AlaBfdGlobalTxInterval_Type.__name__ = "AlaBfdInterval"
_AlaBfdGlobalTxInterval_Object = MibScalar
alaBfdGlobalTxInterval = _AlaBfdGlobalTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 1, 2),
    _AlaBfdGlobalTxInterval_Type()
)
alaBfdGlobalTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBfdGlobalTxInterval.setStatus("current")


class _AlaBfdGlobalRxInterval_Type(AlaBfdInterval):
    """Custom type alaBfdGlobalRxInterval based on AlaBfdInterval"""
    defaultValue = 300


_AlaBfdGlobalRxInterval_Type.__name__ = "AlaBfdInterval"
_AlaBfdGlobalRxInterval_Object = MibScalar
alaBfdGlobalRxInterval = _AlaBfdGlobalRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 1, 3),
    _AlaBfdGlobalRxInterval_Type()
)
alaBfdGlobalRxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBfdGlobalRxInterval.setStatus("current")


class _AlaBfdGlobalOperMode_Type(Integer32):
    """Custom type alaBfdGlobalOperMode based on Integer32"""
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
        *(("asyncMode", 1),
          ("demandMode", 2),
          ("echoOnly", 3))
    )


_AlaBfdGlobalOperMode_Type.__name__ = "Integer32"
_AlaBfdGlobalOperMode_Object = MibScalar
alaBfdGlobalOperMode = _AlaBfdGlobalOperMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 1, 4),
    _AlaBfdGlobalOperMode_Type()
)
alaBfdGlobalOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBfdGlobalOperMode.setStatus("current")


class _AlaBfdGlobalVersionNumber_Type(Unsigned32):
    """Custom type alaBfdGlobalVersionNumber based on Unsigned32"""
    defaultValue = 1


_AlaBfdGlobalVersionNumber_Type.__name__ = "Unsigned32"
_AlaBfdGlobalVersionNumber_Object = MibScalar
alaBfdGlobalVersionNumber = _AlaBfdGlobalVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 1, 5),
    _AlaBfdGlobalVersionNumber_Type()
)
alaBfdGlobalVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdGlobalVersionNumber.setStatus("current")


class _AlaBfdGlobalL2HoldTimer_Type(AlaBfdInterval):
    """Custom type alaBfdGlobalL2HoldTimer based on AlaBfdInterval"""
    defaultValue = 500


_AlaBfdGlobalL2HoldTimer_Type.__name__ = "AlaBfdInterval"
_AlaBfdGlobalL2HoldTimer_Object = MibScalar
alaBfdGlobalL2HoldTimer = _AlaBfdGlobalL2HoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 1, 6),
    _AlaBfdGlobalL2HoldTimer_Type()
)
alaBfdGlobalL2HoldTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBfdGlobalL2HoldTimer.setStatus("current")


class _AlaBfdGlobalProtocols_Type(Bits):
    """Custom type alaBfdGlobalProtocols based on Bits"""
    namedValues = NamedValues(
        *(("ospf", 0),
          ("bgp", 1),
          ("dvmrp", 2),
          ("vrrp", 3))
    )

_AlaBfdGlobalProtocols_Type.__name__ = "Bits"
_AlaBfdGlobalProtocols_Object = MibScalar
alaBfdGlobalProtocols = _AlaBfdGlobalProtocols_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 1, 7),
    _AlaBfdGlobalProtocols_Type()
)
alaBfdGlobalProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdGlobalProtocols.setStatus("current")
_AlaBfdGlobalEchoObjects_ObjectIdentity = ObjectIdentity
alaBfdGlobalEchoObjects = _AlaBfdGlobalEchoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 2)
)
_AlaBfdGlobalEcho_Type = AlaBfdStatus
_AlaBfdGlobalEcho_Object = MibScalar
alaBfdGlobalEcho = _AlaBfdGlobalEcho_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 2, 1),
    _AlaBfdGlobalEcho_Type()
)
alaBfdGlobalEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBfdGlobalEcho.setStatus("current")


class _AlaBfdGlobalEchoRxInterval_Type(AlaBfdInterval):
    """Custom type alaBfdGlobalEchoRxInterval based on AlaBfdInterval"""
    defaultValue = 300


_AlaBfdGlobalEchoRxInterval_Type.__name__ = "AlaBfdInterval"
_AlaBfdGlobalEchoRxInterval_Object = MibScalar
alaBfdGlobalEchoRxInterval = _AlaBfdGlobalEchoRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 2, 2),
    _AlaBfdGlobalEchoRxInterval_Type()
)
alaBfdGlobalEchoRxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBfdGlobalEchoRxInterval.setStatus("current")
_AlaBfdIntfTable_Object = MibTable
alaBfdIntfTable = _AlaBfdIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaBfdIntfTable.setStatus("current")
_AlaBfdIntfEntry_Object = MibTableRow
alaBfdIntfEntry = _AlaBfdIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 3, 1)
)
alaBfdIntfEntry.setIndexNames(
    (0, "ALCATEL-IND1-BFD-MIB", "alaBfdIntfAddrType"),
    (0, "ALCATEL-IND1-BFD-MIB", "alaBfdIntfAddr"),
)
if mibBuilder.loadTexts:
    alaBfdIntfEntry.setStatus("current")
_AlaBfdIntfAddrType_Type = InetAddressType
_AlaBfdIntfAddrType_Object = MibTableColumn
alaBfdIntfAddrType = _AlaBfdIntfAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 3, 1, 1),
    _AlaBfdIntfAddrType_Type()
)
alaBfdIntfAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaBfdIntfAddrType.setStatus("current")
_AlaBfdIntfAddr_Type = InetAddress
_AlaBfdIntfAddr_Object = MibTableColumn
alaBfdIntfAddr = _AlaBfdIntfAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 3, 1, 2),
    _AlaBfdIntfAddr_Type()
)
alaBfdIntfAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaBfdIntfAddr.setStatus("current")
_AlaBfdIntfIndex_Type = InterfaceIndex
_AlaBfdIntfIndex_Object = MibTableColumn
alaBfdIntfIndex = _AlaBfdIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 3, 1, 3),
    _AlaBfdIntfIndex_Type()
)
alaBfdIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdIntfIndex.setStatus("current")


class _AlabfdIntfAdminStatus_Type(AlaBfdStatus):
    """Custom type alabfdIntfAdminStatus based on AlaBfdStatus"""
    defaultValue = 2


_AlabfdIntfAdminStatus_Type.__name__ = "AlaBfdStatus"
_AlabfdIntfAdminStatus_Object = MibTableColumn
alabfdIntfAdminStatus = _AlabfdIntfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 3, 1, 4),
    _AlabfdIntfAdminStatus_Type()
)
alabfdIntfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alabfdIntfAdminStatus.setStatus("current")
_AlaBfdIntfDesiredMinTxInterval_Type = AlaBfdInterval
_AlaBfdIntfDesiredMinTxInterval_Object = MibTableColumn
alaBfdIntfDesiredMinTxInterval = _AlaBfdIntfDesiredMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 3, 1, 5),
    _AlaBfdIntfDesiredMinTxInterval_Type()
)
alaBfdIntfDesiredMinTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBfdIntfDesiredMinTxInterval.setStatus("current")
_AlaBfdIntfReqMinRxInterval_Type = AlaBfdInterval
_AlaBfdIntfReqMinRxInterval_Object = MibTableColumn
alaBfdIntfReqMinRxInterval = _AlaBfdIntfReqMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 3, 1, 6),
    _AlaBfdIntfReqMinRxInterval_Type()
)
alaBfdIntfReqMinRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBfdIntfReqMinRxInterval.setStatus("current")


class _AlaBfdIntfOperMode_Type(Integer32):
    """Custom type alaBfdIntfOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asyncMode", 1),
          ("demandMode", 2),
          ("echoOnly", 3))
    )


_AlaBfdIntfOperMode_Type.__name__ = "Integer32"
_AlaBfdIntfOperMode_Object = MibTableColumn
alaBfdIntfOperMode = _AlaBfdIntfOperMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 3, 1, 7),
    _AlaBfdIntfOperMode_Type()
)
alaBfdIntfOperMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBfdIntfOperMode.setStatus("current")
_AlaBfdIntfEchoMode_Type = AlaBfdStatus
_AlaBfdIntfEchoMode_Object = MibTableColumn
alaBfdIntfEchoMode = _AlaBfdIntfEchoMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 3, 1, 8),
    _AlaBfdIntfEchoMode_Type()
)
alaBfdIntfEchoMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBfdIntfEchoMode.setStatus("current")
_AlaBfdIntfReqMinEchoRxInterval_Type = AlaBfdInterval
_AlaBfdIntfReqMinEchoRxInterval_Object = MibTableColumn
alaBfdIntfReqMinEchoRxInterval = _AlaBfdIntfReqMinEchoRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 3, 1, 9),
    _AlaBfdIntfReqMinEchoRxInterval_Type()
)
alaBfdIntfReqMinEchoRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBfdIntfReqMinEchoRxInterval.setStatus("current")


class _AlaBfdIntfDetectMult_Type(Unsigned32):
    """Custom type alaBfdIntfDetectMult based on Unsigned32"""
    defaultValue = 3


_AlaBfdIntfDetectMult_Type.__name__ = "Unsigned32"
_AlaBfdIntfDetectMult_Object = MibTableColumn
alaBfdIntfDetectMult = _AlaBfdIntfDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 3, 1, 10),
    _AlaBfdIntfDetectMult_Type()
)
alaBfdIntfDetectMult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBfdIntfDetectMult.setStatus("current")


class _AlaBfdIntfsesstype_Type(Integer32):
    """Custom type alaBfdIntfsesstype based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("singleHop", 1),
          ("multiHop", 2))
    )


_AlaBfdIntfsesstype_Type.__name__ = "Integer32"
_AlaBfdIntfsesstype_Object = MibTableColumn
alaBfdIntfsesstype = _AlaBfdIntfsesstype_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 3, 1, 11),
    _AlaBfdIntfsesstype_Type()
)
alaBfdIntfsesstype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBfdIntfsesstype.setStatus("current")


class _AlaBfdIntfAuthPresFlag_Type(TruthValue):
    """Custom type alaBfdIntfAuthPresFlag based on TruthValue"""
    defaultValue = 2


_AlaBfdIntfAuthPresFlag_Type.__name__ = "TruthValue"
_AlaBfdIntfAuthPresFlag_Object = MibTableColumn
alaBfdIntfAuthPresFlag = _AlaBfdIntfAuthPresFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 3, 1, 12),
    _AlaBfdIntfAuthPresFlag_Type()
)
alaBfdIntfAuthPresFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBfdIntfAuthPresFlag.setStatus("current")


class _AlaBfdIntfAuthenticationType_Type(Integer32):
    """Custom type alaBfdIntfAuthenticationType based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("simplePassword", 2),
          ("keyedMD5", 3),
          ("meticulousKeyedMD5", 4),
          ("keyedSHA1", 5),
          ("meticulousKeyedSHA1", 6))
    )


_AlaBfdIntfAuthenticationType_Type.__name__ = "Integer32"
_AlaBfdIntfAuthenticationType_Object = MibTableColumn
alaBfdIntfAuthenticationType = _AlaBfdIntfAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 3, 1, 13),
    _AlaBfdIntfAuthenticationType_Type()
)
alaBfdIntfAuthenticationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBfdIntfAuthenticationType.setStatus("current")
_AlaBfdIntfL2HoldTimer_Type = AlaBfdInterval
_AlaBfdIntfL2HoldTimer_Object = MibTableColumn
alaBfdIntfL2HoldTimer = _AlaBfdIntfL2HoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 3, 1, 14),
    _AlaBfdIntfL2HoldTimer_Type()
)
alaBfdIntfL2HoldTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBfdIntfL2HoldTimer.setStatus("current")
_AlaBfdIntfRowStatus_Type = RowStatus
_AlaBfdIntfRowStatus_Object = MibTableColumn
alaBfdIntfRowStatus = _AlaBfdIntfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 3, 1, 15),
    _AlaBfdIntfRowStatus_Type()
)
alaBfdIntfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBfdIntfRowStatus.setStatus("current")
_AlaBfdSessTable_Object = MibTable
alaBfdSessTable = _AlaBfdSessTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaBfdSessTable.setStatus("current")
_AlaBfdSessEntry_Object = MibTableRow
alaBfdSessEntry = _AlaBfdSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 4, 1)
)
alaBfdSessEntry.setIndexNames(
    (0, "ALCATEL-IND1-BFD-MIB", "alaBfdSessDiscriminator"),
)
if mibBuilder.loadTexts:
    alaBfdSessEntry.setStatus("current")


class _AlaBfdSessDiscriminator_Type(Unsigned32):
    """Custom type alaBfdSessDiscriminator based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AlaBfdSessDiscriminator_Type.__name__ = "Unsigned32"
_AlaBfdSessDiscriminator_Object = MibTableColumn
alaBfdSessDiscriminator = _AlaBfdSessDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 4, 1, 1),
    _AlaBfdSessDiscriminator_Type()
)
alaBfdSessDiscriminator.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaBfdSessDiscriminator.setStatus("current")
_AlaBfdSessNeighborAddrType_Type = InetAddressType
_AlaBfdSessNeighborAddrType_Object = MibTableColumn
alaBfdSessNeighborAddrType = _AlaBfdSessNeighborAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 4, 1, 2),
    _AlaBfdSessNeighborAddrType_Type()
)
alaBfdSessNeighborAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessNeighborAddrType.setStatus("current")
_AlaBfdSessNeighborAddr_Type = InetAddress
_AlaBfdSessNeighborAddr_Object = MibTableColumn
alaBfdSessNeighborAddr = _AlaBfdSessNeighborAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 4, 1, 3),
    _AlaBfdSessNeighborAddr_Type()
)
alaBfdSessNeighborAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessNeighborAddr.setStatus("current")


class _AlaBfdSessRemoteDiscr_Type(Unsigned32):
    """Custom type alaBfdSessRemoteDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AlaBfdSessRemoteDiscr_Type.__name__ = "Unsigned32"
_AlaBfdSessRemoteDiscr_Object = MibTableColumn
alaBfdSessRemoteDiscr = _AlaBfdSessRemoteDiscr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 4, 1, 4),
    _AlaBfdSessRemoteDiscr_Type()
)
alaBfdSessRemoteDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessRemoteDiscr.setStatus("current")
_AlaBfdSessUdpPort_Type = InetPortNumber
_AlaBfdSessUdpPort_Object = MibTableColumn
alaBfdSessUdpPort = _AlaBfdSessUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 4, 1, 5),
    _AlaBfdSessUdpPort_Type()
)
alaBfdSessUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessUdpPort.setStatus("current")


class _AlaBfdSessState_Type(Integer32):
    """Custom type alaBfdSessState based on Integer32"""
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
        *(("adminDown", 1),
          ("down", 2),
          ("init", 3),
          ("up", 4),
          ("failing", 5))
    )


_AlaBfdSessState_Type.__name__ = "Integer32"
_AlaBfdSessState_Object = MibTableColumn
alaBfdSessState = _AlaBfdSessState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 4, 1, 6),
    _AlaBfdSessState_Type()
)
alaBfdSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessState.setStatus("current")
_AlaBfdSessRemoteHeardFlag_Type = TruthValue
_AlaBfdSessRemoteHeardFlag_Object = MibTableColumn
alaBfdSessRemoteHeardFlag = _AlaBfdSessRemoteHeardFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 4, 1, 7),
    _AlaBfdSessRemoteHeardFlag_Type()
)
alaBfdSessRemoteHeardFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessRemoteHeardFlag.setStatus("current")
_AlaBfdSessDiag_Type = AlaBfdDiag
_AlaBfdSessDiag_Object = MibTableColumn
alaBfdSessDiag = _AlaBfdSessDiag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 4, 1, 8),
    _AlaBfdSessDiag_Type()
)
alaBfdSessDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessDiag.setStatus("current")


class _AlaBfdSessOperMode_Type(Integer32):
    """Custom type alaBfdSessOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asyncMode", 1),
          ("demandMode", 2),
          ("echoOnly", 3))
    )


_AlaBfdSessOperMode_Type.__name__ = "Integer32"
_AlaBfdSessOperMode_Object = MibTableColumn
alaBfdSessOperMode = _AlaBfdSessOperMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 4, 1, 9),
    _AlaBfdSessOperMode_Type()
)
alaBfdSessOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessOperMode.setStatus("current")
_AlaBfdSessEchoFuncModeDesiredFlag_Type = TruthValue
_AlaBfdSessEchoFuncModeDesiredFlag_Object = MibTableColumn
alaBfdSessEchoFuncModeDesiredFlag = _AlaBfdSessEchoFuncModeDesiredFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 4, 1, 10),
    _AlaBfdSessEchoFuncModeDesiredFlag_Type()
)
alaBfdSessEchoFuncModeDesiredFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessEchoFuncModeDesiredFlag.setStatus("current")


class _AlaBfdSessControlPlanIndepFlag_Type(TruthValue):
    """Custom type alaBfdSessControlPlanIndepFlag based on TruthValue"""
    defaultValue = 1


_AlaBfdSessControlPlanIndepFlag_Type.__name__ = "TruthValue"
_AlaBfdSessControlPlanIndepFlag_Object = MibTableColumn
alaBfdSessControlPlanIndepFlag = _AlaBfdSessControlPlanIndepFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 4, 1, 11),
    _AlaBfdSessControlPlanIndepFlag_Type()
)
alaBfdSessControlPlanIndepFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessControlPlanIndepFlag.setStatus("current")
_AlaBfdSessInterface_Type = InterfaceIndexOrZero
_AlaBfdSessInterface_Object = MibTableColumn
alaBfdSessInterface = _AlaBfdSessInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 4, 1, 12),
    _AlaBfdSessInterface_Type()
)
alaBfdSessInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessInterface.setStatus("current")
_AlaBfdSessNegotiatedTxInterval_Type = AlaBfdInterval
_AlaBfdSessNegotiatedTxInterval_Object = MibTableColumn
alaBfdSessNegotiatedTxInterval = _AlaBfdSessNegotiatedTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 4, 1, 13),
    _AlaBfdSessNegotiatedTxInterval_Type()
)
alaBfdSessNegotiatedTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessNegotiatedTxInterval.setStatus("current")
_AlaBfdSessNegotiatedRxInterval_Type = AlaBfdInterval
_AlaBfdSessNegotiatedRxInterval_Object = MibTableColumn
alaBfdSessNegotiatedRxInterval = _AlaBfdSessNegotiatedRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 4, 1, 14),
    _AlaBfdSessNegotiatedRxInterval_Type()
)
alaBfdSessNegotiatedRxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessNegotiatedRxInterval.setStatus("current")


class _AlaBfdSessProtocols_Type(Bits):
    """Custom type alaBfdSessProtocols based on Bits"""
    namedValues = NamedValues(
        *(("ospf", 0),
          ("bgp", 1),
          ("dvmrp", 2),
          ("vrrp", 3),
          ("iprm", 4))
    )

_AlaBfdSessProtocols_Type.__name__ = "Bits"
_AlaBfdSessProtocols_Object = MibTableColumn
alaBfdSessProtocols = _AlaBfdSessProtocols_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 4, 1, 15),
    _AlaBfdSessProtocols_Type()
)
alaBfdSessProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessProtocols.setStatus("current")
_AlaBfdSessPerfTable_Object = MibTable
alaBfdSessPerfTable = _AlaBfdSessPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alaBfdSessPerfTable.setStatus("current")
_AlaBfdSessPerfEntry_Object = MibTableRow
alaBfdSessPerfEntry = _AlaBfdSessPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    alaBfdSessPerfEntry.setStatus("current")
_AlaBfdSessPerfPktIn_Type = Counter64
_AlaBfdSessPerfPktIn_Object = MibTableColumn
alaBfdSessPerfPktIn = _AlaBfdSessPerfPktIn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 5, 1, 1),
    _AlaBfdSessPerfPktIn_Type()
)
alaBfdSessPerfPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessPerfPktIn.setStatus("current")
_AlaBfdSessPerfPktOut_Type = Counter64
_AlaBfdSessPerfPktOut_Object = MibTableColumn
alaBfdSessPerfPktOut = _AlaBfdSessPerfPktOut_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 5, 1, 2),
    _AlaBfdSessPerfPktOut_Type()
)
alaBfdSessPerfPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessPerfPktOut.setStatus("current")
_AlaBfdSessPerfEchoOut_Type = Counter64
_AlaBfdSessPerfEchoOut_Object = MibTableColumn
alaBfdSessPerfEchoOut = _AlaBfdSessPerfEchoOut_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 5, 1, 3),
    _AlaBfdSessPerfEchoOut_Type()
)
alaBfdSessPerfEchoOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessPerfEchoOut.setStatus("current")
_AlaBfdSessPerfUpTime_Type = TimeTicks
_AlaBfdSessPerfUpTime_Object = MibTableColumn
alaBfdSessPerfUpTime = _AlaBfdSessPerfUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 5, 1, 4),
    _AlaBfdSessPerfUpTime_Type()
)
alaBfdSessPerfUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessPerfUpTime.setStatus("current")
_AlaBfdSessPerfLastSessDownTime_Type = TimeTicks
_AlaBfdSessPerfLastSessDownTime_Object = MibTableColumn
alaBfdSessPerfLastSessDownTime = _AlaBfdSessPerfLastSessDownTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 5, 1, 5),
    _AlaBfdSessPerfLastSessDownTime_Type()
)
alaBfdSessPerfLastSessDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessPerfLastSessDownTime.setStatus("current")
_AlaBfdSessPerfLastCommLostDiag_Type = AlaBfdDiag
_AlaBfdSessPerfLastCommLostDiag_Object = MibTableColumn
alaBfdSessPerfLastCommLostDiag = _AlaBfdSessPerfLastCommLostDiag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 5, 1, 6),
    _AlaBfdSessPerfLastCommLostDiag_Type()
)
alaBfdSessPerfLastCommLostDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessPerfLastCommLostDiag.setStatus("current")
_AlaBfdSessPerfSessUpCount_Type = Counter64
_AlaBfdSessPerfSessUpCount_Object = MibTableColumn
alaBfdSessPerfSessUpCount = _AlaBfdSessPerfSessUpCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 5, 1, 7),
    _AlaBfdSessPerfSessUpCount_Type()
)
alaBfdSessPerfSessUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessPerfSessUpCount.setStatus("current")
_AlaBfdSessPerfDiscTime_Type = TimeTicks
_AlaBfdSessPerfDiscTime_Object = MibTableColumn
alaBfdSessPerfDiscTime = _AlaBfdSessPerfDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 1, 5, 1, 8),
    _AlaBfdSessPerfDiscTime_Type()
)
alaBfdSessPerfDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessPerfDiscTime.setStatus("current")
_AlcatelIND1BfdMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1BfdMIBConformance = _AlcatelIND1BfdMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1BfdMIBConformance.setStatus("current")
_AlcatelIND1BfdMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1BfdMIBGroups = _AlcatelIND1BfdMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 2, 1)
)
_AlcatelIND1BfdMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1BfdMIBCompliances = _AlcatelIND1BfdMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 2, 2)
)
alaBfdSessEntry.registerAugmentions(
    ("ALCATEL-IND1-BFD-MIB",
     "alaBfdSessPerfEntry")
)
alaBfdSessPerfEntry.setIndexNames(*alaBfdSessEntry.getIndexNames())

# Managed Objects groups

alaBfdbasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 2, 1, 1)
)
alaBfdbasicGroup.setObjects(
      *(("ALCATEL-IND1-BFD-MIB", "alaBfdGlobalAdminStatus"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdGlobalTxInterval"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdGlobalRxInterval"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdGlobalOperMode"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdGlobalVersionNumber"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdGlobalL2HoldTimer"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdGlobalProtocols"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdGlobalEcho"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdGlobalEchoRxInterval"))
)
if mibBuilder.loadTexts:
    alaBfdbasicGroup.setStatus("current")

alaBfdIntfCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 2, 1, 2)
)
alaBfdIntfCfgGroup.setObjects(
      *(("ALCATEL-IND1-BFD-MIB", "alaBfdIntfIndex"),
        ("ALCATEL-IND1-BFD-MIB", "alabfdIntfAdminStatus"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfDesiredMinTxInterval"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfReqMinRxInterval"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfEchoMode"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfReqMinEchoRxInterval"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfDetectMult"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfOperMode"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfsesstype"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfAuthPresFlag"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfAuthenticationType"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfL2HoldTimer"))
)
if mibBuilder.loadTexts:
    alaBfdIntfCfgGroup.setStatus("current")

alaBfdSessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 2, 1, 3)
)
alaBfdSessGroup.setObjects(
      *(("ALCATEL-IND1-BFD-MIB", "alaBfdSessNeighborAddrType"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessNeighborAddr"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessRemoteDiscr"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessUdpPort"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessState"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessRemoteHeardFlag"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessDiag"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessOperMode"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessEchoFuncModeDesiredFlag"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessControlPlanIndepFlag"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessInterface"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessNegotiatedTxInterval"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessNegotiatedRxInterval"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessProtocols"))
)
if mibBuilder.loadTexts:
    alaBfdSessGroup.setStatus("current")

alaBfdSessPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 2, 1, 4)
)
alaBfdSessPerfGroup.setObjects(
      *(("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfPktIn"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfPktOut"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfEchoOut"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfUpTime"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfLastSessDownTime"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfLastCommLostDiag"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfSessUpCount"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfDiscTime"))
)
if mibBuilder.loadTexts:
    alaBfdSessPerfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1BfdMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 45, 1, 2, 2, 1)
)
alcatelIND1BfdMIBCompliance.setObjects(
      *(("ALCATEL-IND1-BFD-MIB", "alaBfdbasicGroup"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfCfgGroup"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessGroup"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1BfdMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-BFD-MIB",
    **{"AlaBfdInterval": AlaBfdInterval,
       "AlaBfdDiag": AlaBfdDiag,
       "AlaBfdStatus": AlaBfdStatus,
       "alcatelIND1BfdMIB": alcatelIND1BfdMIB,
       "alaBfdObjects": alaBfdObjects,
       "alaBfdGlobalObjects": alaBfdGlobalObjects,
       "alaBfdGlobalAdminStatus": alaBfdGlobalAdminStatus,
       "alaBfdGlobalTxInterval": alaBfdGlobalTxInterval,
       "alaBfdGlobalRxInterval": alaBfdGlobalRxInterval,
       "alaBfdGlobalOperMode": alaBfdGlobalOperMode,
       "alaBfdGlobalVersionNumber": alaBfdGlobalVersionNumber,
       "alaBfdGlobalL2HoldTimer": alaBfdGlobalL2HoldTimer,
       "alaBfdGlobalProtocols": alaBfdGlobalProtocols,
       "alaBfdGlobalEchoObjects": alaBfdGlobalEchoObjects,
       "alaBfdGlobalEcho": alaBfdGlobalEcho,
       "alaBfdGlobalEchoRxInterval": alaBfdGlobalEchoRxInterval,
       "alaBfdIntfTable": alaBfdIntfTable,
       "alaBfdIntfEntry": alaBfdIntfEntry,
       "alaBfdIntfAddrType": alaBfdIntfAddrType,
       "alaBfdIntfAddr": alaBfdIntfAddr,
       "alaBfdIntfIndex": alaBfdIntfIndex,
       "alabfdIntfAdminStatus": alabfdIntfAdminStatus,
       "alaBfdIntfDesiredMinTxInterval": alaBfdIntfDesiredMinTxInterval,
       "alaBfdIntfReqMinRxInterval": alaBfdIntfReqMinRxInterval,
       "alaBfdIntfOperMode": alaBfdIntfOperMode,
       "alaBfdIntfEchoMode": alaBfdIntfEchoMode,
       "alaBfdIntfReqMinEchoRxInterval": alaBfdIntfReqMinEchoRxInterval,
       "alaBfdIntfDetectMult": alaBfdIntfDetectMult,
       "alaBfdIntfsesstype": alaBfdIntfsesstype,
       "alaBfdIntfAuthPresFlag": alaBfdIntfAuthPresFlag,
       "alaBfdIntfAuthenticationType": alaBfdIntfAuthenticationType,
       "alaBfdIntfL2HoldTimer": alaBfdIntfL2HoldTimer,
       "alaBfdIntfRowStatus": alaBfdIntfRowStatus,
       "alaBfdSessTable": alaBfdSessTable,
       "alaBfdSessEntry": alaBfdSessEntry,
       "alaBfdSessDiscriminator": alaBfdSessDiscriminator,
       "alaBfdSessNeighborAddrType": alaBfdSessNeighborAddrType,
       "alaBfdSessNeighborAddr": alaBfdSessNeighborAddr,
       "alaBfdSessRemoteDiscr": alaBfdSessRemoteDiscr,
       "alaBfdSessUdpPort": alaBfdSessUdpPort,
       "alaBfdSessState": alaBfdSessState,
       "alaBfdSessRemoteHeardFlag": alaBfdSessRemoteHeardFlag,
       "alaBfdSessDiag": alaBfdSessDiag,
       "alaBfdSessOperMode": alaBfdSessOperMode,
       "alaBfdSessEchoFuncModeDesiredFlag": alaBfdSessEchoFuncModeDesiredFlag,
       "alaBfdSessControlPlanIndepFlag": alaBfdSessControlPlanIndepFlag,
       "alaBfdSessInterface": alaBfdSessInterface,
       "alaBfdSessNegotiatedTxInterval": alaBfdSessNegotiatedTxInterval,
       "alaBfdSessNegotiatedRxInterval": alaBfdSessNegotiatedRxInterval,
       "alaBfdSessProtocols": alaBfdSessProtocols,
       "alaBfdSessPerfTable": alaBfdSessPerfTable,
       "alaBfdSessPerfEntry": alaBfdSessPerfEntry,
       "alaBfdSessPerfPktIn": alaBfdSessPerfPktIn,
       "alaBfdSessPerfPktOut": alaBfdSessPerfPktOut,
       "alaBfdSessPerfEchoOut": alaBfdSessPerfEchoOut,
       "alaBfdSessPerfUpTime": alaBfdSessPerfUpTime,
       "alaBfdSessPerfLastSessDownTime": alaBfdSessPerfLastSessDownTime,
       "alaBfdSessPerfLastCommLostDiag": alaBfdSessPerfLastCommLostDiag,
       "alaBfdSessPerfSessUpCount": alaBfdSessPerfSessUpCount,
       "alaBfdSessPerfDiscTime": alaBfdSessPerfDiscTime,
       "alcatelIND1BfdMIBConformance": alcatelIND1BfdMIBConformance,
       "alcatelIND1BfdMIBGroups": alcatelIND1BfdMIBGroups,
       "alaBfdbasicGroup": alaBfdbasicGroup,
       "alaBfdIntfCfgGroup": alaBfdIntfCfgGroup,
       "alaBfdSessGroup": alaBfdSessGroup,
       "alaBfdSessPerfGroup": alaBfdSessPerfGroup,
       "alcatelIND1BfdMIBCompliances": alcatelIND1BfdMIBCompliances,
       "alcatelIND1BfdMIBCompliance": alcatelIND1BfdMIBCompliance}
)
