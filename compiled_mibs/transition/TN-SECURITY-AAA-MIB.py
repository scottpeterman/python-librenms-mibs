# SNMP MIB module (TN-SECURITY-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-SECURITY-AAA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:23 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(tnDevMgmt,) = mibBuilder.importSymbols(
    "TN-MGMT-MIB",
    "tnDevMgmt")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class TnAAAProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tacacsplus", 1),
          ("radius", 2))
    )



class TnAAAType(TextualConvention, Integer32):
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
        *(("authentication", 1),
          ("authorization", 2),
          ("accounting", 3))
    )



# MIB Managed Objects in the order of their OIDs

_TnSecurityAAAMIB_ObjectIdentity = ObjectIdentity
tnSecurityAAAMIB = _TnSecurityAAAMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20)
)


class _TnAAAServerTimeout_Type(Integer32):
    """Custom type tnAAAServerTimeout based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3600),
    )


_TnAAAServerTimeout_Type.__name__ = "Integer32"
_TnAAAServerTimeout_Object = MibScalar
tnAAAServerTimeout = _TnAAAServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 1),
    _TnAAAServerTimeout_Type()
)
tnAAAServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAAAServerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tnAAAServerTimeout.setUnits("seconds")


class _TnAAAServerDeadTime_Type(Integer32):
    """Custom type tnAAAServerDeadTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_TnAAAServerDeadTime_Type.__name__ = "Integer32"
_TnAAAServerDeadTime_Object = MibScalar
tnAAAServerDeadTime = _TnAAAServerDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 2),
    _TnAAAServerDeadTime_Type()
)
tnAAAServerDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAAAServerDeadTime.setStatus("current")
if mibBuilder.loadTexts:
    tnAAAServerDeadTime.setUnits("seconds")
_TnAAAServerTable_Object = MibTable
tnAAAServerTable = _TnAAAServerTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 3)
)
if mibBuilder.loadTexts:
    tnAAAServerTable.setStatus("current")
_TnAAAServerEntry_Object = MibTableRow
tnAAAServerEntry = _TnAAAServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 3, 1)
)
tnAAAServerEntry.setIndexNames(
    (0, "TN-SECURITY-AAA-MIB", "tnAAAProtocol"),
    (0, "TN-SECURITY-AAA-MIB", "tnAAAType"),
    (0, "TN-SECURITY-AAA-MIB", "tnAAAServerIndex"),
)
if mibBuilder.loadTexts:
    tnAAAServerEntry.setStatus("current")
_TnAAAProtocol_Type = TnAAAProtocol
_TnAAAProtocol_Object = MibTableColumn
tnAAAProtocol = _TnAAAProtocol_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 3, 1, 1),
    _TnAAAProtocol_Type()
)
tnAAAProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnAAAProtocol.setStatus("current")
_TnAAAType_Type = TnAAAType
_TnAAAType_Object = MibTableColumn
tnAAAType = _TnAAAType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 3, 1, 2),
    _TnAAAType_Type()
)
tnAAAType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnAAAType.setStatus("current")


class _TnAAAServerIndex_Type(Unsigned32):
    """Custom type tnAAAServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnAAAServerIndex_Type.__name__ = "Unsigned32"
_TnAAAServerIndex_Object = MibTableColumn
tnAAAServerIndex = _TnAAAServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 3, 1, 3),
    _TnAAAServerIndex_Type()
)
tnAAAServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnAAAServerIndex.setStatus("current")


class _TnAAAServerEnable_Type(TruthValue):
    """Custom type tnAAAServerEnable based on TruthValue"""
    defaultValue = 2


_TnAAAServerEnable_Type.__name__ = "TruthValue"
_TnAAAServerEnable_Object = MibTableColumn
tnAAAServerEnable = _TnAAAServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 3, 1, 4),
    _TnAAAServerEnable_Type()
)
tnAAAServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAAAServerEnable.setStatus("current")
_TnAAAServerAddrType_Type = InetAddressType
_TnAAAServerAddrType_Object = MibTableColumn
tnAAAServerAddrType = _TnAAAServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 3, 1, 5),
    _TnAAAServerAddrType_Type()
)
tnAAAServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAAAServerAddrType.setStatus("current")
_TnAAAServerAddr_Type = InetAddress
_TnAAAServerAddr_Object = MibTableColumn
tnAAAServerAddr = _TnAAAServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 3, 1, 6),
    _TnAAAServerAddr_Type()
)
tnAAAServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAAAServerAddr.setStatus("current")


class _TnAAAServerPort_Type(Integer32):
    """Custom type tnAAAServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnAAAServerPort_Type.__name__ = "Integer32"
_TnAAAServerPort_Object = MibTableColumn
tnAAAServerPort = _TnAAAServerPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 3, 1, 7),
    _TnAAAServerPort_Type()
)
tnAAAServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAAAServerPort.setStatus("current")


class _TnAAAServerSecret_Type(DisplayString):
    """Custom type tnAAAServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 29),
    )


_TnAAAServerSecret_Type.__name__ = "DisplayString"
_TnAAAServerSecret_Object = MibTableColumn
tnAAAServerSecret = _TnAAAServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 3, 1, 8),
    _TnAAAServerSecret_Type()
)
tnAAAServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAAAServerSecret.setStatus("current")
_TnStatisticsTable_Object = MibTable
tnStatisticsTable = _TnStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 4)
)
if mibBuilder.loadTexts:
    tnStatisticsTable.setStatus("current")
_TnStatisticsEntry_Object = MibTableRow
tnStatisticsEntry = _TnStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 4, 1)
)
if mibBuilder.loadTexts:
    tnStatisticsEntry.setStatus("current")
_TnAcceptPkts_Type = Counter32
_TnAcceptPkts_Object = MibTableColumn
tnAcceptPkts = _TnAcceptPkts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 4, 1, 1),
    _TnAcceptPkts_Type()
)
tnAcceptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAcceptPkts.setStatus("current")
_TnRejectPkts_Type = Counter32
_TnRejectPkts_Object = MibTableColumn
tnRejectPkts = _TnRejectPkts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 4, 1, 2),
    _TnRejectPkts_Type()
)
tnRejectPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRejectPkts.setStatus("current")
_TnChallengesPkts_Type = Counter32
_TnChallengesPkts_Object = MibTableColumn
tnChallengesPkts = _TnChallengesPkts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 4, 1, 3),
    _TnChallengesPkts_Type()
)
tnChallengesPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnChallengesPkts.setStatus("current")
_TnMalResponsePkts_Type = Counter32
_TnMalResponsePkts_Object = MibTableColumn
tnMalResponsePkts = _TnMalResponsePkts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 4, 1, 4),
    _TnMalResponsePkts_Type()
)
tnMalResponsePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMalResponsePkts.setStatus("current")
_TnBadAuthPkts_Type = Counter32
_TnBadAuthPkts_Object = MibTableColumn
tnBadAuthPkts = _TnBadAuthPkts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 4, 1, 5),
    _TnBadAuthPkts_Type()
)
tnBadAuthPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnBadAuthPkts.setStatus("current")
_TnUnknownTypePkts_Type = Counter32
_TnUnknownTypePkts_Object = MibTableColumn
tnUnknownTypePkts = _TnUnknownTypePkts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 4, 1, 6),
    _TnUnknownTypePkts_Type()
)
tnUnknownTypePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUnknownTypePkts.setStatus("current")
_TnDroppedPkts_Type = Counter32
_TnDroppedPkts_Object = MibTableColumn
tnDroppedPkts = _TnDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 4, 1, 7),
    _TnDroppedPkts_Type()
)
tnDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDroppedPkts.setStatus("current")
_TnRequestPkts_Type = Counter32
_TnRequestPkts_Object = MibTableColumn
tnRequestPkts = _TnRequestPkts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 4, 1, 8),
    _TnRequestPkts_Type()
)
tnRequestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRequestPkts.setStatus("current")
_TnRetransPkts_Type = Counter32
_TnRetransPkts_Object = MibTableColumn
tnRetransPkts = _TnRetransPkts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 4, 1, 9),
    _TnRetransPkts_Type()
)
tnRetransPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRetransPkts.setStatus("current")
_TnPendRequestPkts_Type = Counter32
_TnPendRequestPkts_Object = MibTableColumn
tnPendRequestPkts = _TnPendRequestPkts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 4, 1, 10),
    _TnPendRequestPkts_Type()
)
tnPendRequestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPendRequestPkts.setStatus("current")
_TnTimeouts_Type = Counter32
_TnTimeouts_Object = MibTableColumn
tnTimeouts = _TnTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 4, 1, 11),
    _TnTimeouts_Type()
)
tnTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTimeouts.setStatus("current")


class _TnState_Type(Integer32):
    """Custom type tnState based on Integer32"""
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
        *(("disabled", 1),
          ("notready", 2),
          ("ready", 3),
          ("dead", 4))
    )


_TnState_Type.__name__ = "Integer32"
_TnState_Object = MibTableColumn
tnState = _TnState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 4, 1, 12),
    _TnState_Type()
)
tnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnState.setStatus("current")
_TnRoundTripTime_Type = Counter32
_TnRoundTripTime_Object = MibTableColumn
tnRoundTripTime = _TnRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 20, 4, 1, 13),
    _TnRoundTripTime_Type()
)
tnRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoundTripTime.setStatus("current")
if mibBuilder.loadTexts:
    tnRoundTripTime.setUnits("millisecond")
tnAAAServerEntry.registerAugmentions(
    ("TN-SECURITY-AAA-MIB",
     "tnStatisticsEntry")
)
tnStatisticsEntry.setIndexNames(*tnAAAServerEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-SECURITY-AAA-MIB",
    **{"TnAAAProtocol": TnAAAProtocol,
       "TnAAAType": TnAAAType,
       "tnSecurityAAAMIB": tnSecurityAAAMIB,
       "tnAAAServerTimeout": tnAAAServerTimeout,
       "tnAAAServerDeadTime": tnAAAServerDeadTime,
       "tnAAAServerTable": tnAAAServerTable,
       "tnAAAServerEntry": tnAAAServerEntry,
       "tnAAAProtocol": tnAAAProtocol,
       "tnAAAType": tnAAAType,
       "tnAAAServerIndex": tnAAAServerIndex,
       "tnAAAServerEnable": tnAAAServerEnable,
       "tnAAAServerAddrType": tnAAAServerAddrType,
       "tnAAAServerAddr": tnAAAServerAddr,
       "tnAAAServerPort": tnAAAServerPort,
       "tnAAAServerSecret": tnAAAServerSecret,
       "tnStatisticsTable": tnStatisticsTable,
       "tnStatisticsEntry": tnStatisticsEntry,
       "tnAcceptPkts": tnAcceptPkts,
       "tnRejectPkts": tnRejectPkts,
       "tnChallengesPkts": tnChallengesPkts,
       "tnMalResponsePkts": tnMalResponsePkts,
       "tnBadAuthPkts": tnBadAuthPkts,
       "tnUnknownTypePkts": tnUnknownTypePkts,
       "tnDroppedPkts": tnDroppedPkts,
       "tnRequestPkts": tnRequestPkts,
       "tnRetransPkts": tnRetransPkts,
       "tnPendRequestPkts": tnPendRequestPkts,
       "tnTimeouts": tnTimeouts,
       "tnState": tnState,
       "tnRoundTripTime": tnRoundTripTime}
)
