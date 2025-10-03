# SNMP MIB module (FIREBRICK-L2TP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\firebrick\FIREBRICK-L2TP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:37 2025
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

(firebrickNewStyle,) = mibBuilder.importSymbols(
    "FIREBRICK-MIB",
    "firebrickNewStyle")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fbL2tpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701)
)
if mibBuilder.loadTexts:
    fbL2tpMib.setRevisions(
        ("2020-04-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FbL2tpGeneral_ObjectIdentity = ObjectIdentity
fbL2tpGeneral = _FbL2tpGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 0)
)
_FbL2tpGeneralTunnels_ObjectIdentity = ObjectIdentity
fbL2tpGeneralTunnels = _FbL2tpGeneralTunnels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 0, 1)
)
_FbL2tpFreeTunnels_Type = Integer32
_FbL2tpFreeTunnels_Object = MibScalar
fbL2tpFreeTunnels = _FbL2tpFreeTunnels_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 0, 1, 0),
    _FbL2tpFreeTunnels_Type()
)
fbL2tpFreeTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbL2tpFreeTunnels.setStatus("current")
_FbL2tpOpeningTunnels_Type = Integer32
_FbL2tpOpeningTunnels_Object = MibScalar
fbL2tpOpeningTunnels = _FbL2tpOpeningTunnels_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 0, 1, 1),
    _FbL2tpOpeningTunnels_Type()
)
fbL2tpOpeningTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbL2tpOpeningTunnels.setStatus("current")
_FbL2tpLiveIncomingTunnels_Type = Integer32
_FbL2tpLiveIncomingTunnels_Object = MibScalar
fbL2tpLiveIncomingTunnels = _FbL2tpLiveIncomingTunnels_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 0, 1, 2),
    _FbL2tpLiveIncomingTunnels_Type()
)
fbL2tpLiveIncomingTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbL2tpLiveIncomingTunnels.setStatus("current")
_FbL2tpLiveOutgoingTunnels_Type = Integer32
_FbL2tpLiveOutgoingTunnels_Object = MibScalar
fbL2tpLiveOutgoingTunnels = _FbL2tpLiveOutgoingTunnels_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 0, 1, 3),
    _FbL2tpLiveOutgoingTunnels_Type()
)
fbL2tpLiveOutgoingTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbL2tpLiveOutgoingTunnels.setStatus("current")
_FbL2tpClosingTunnels_Type = Integer32
_FbL2tpClosingTunnels_Object = MibScalar
fbL2tpClosingTunnels = _FbL2tpClosingTunnels_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 0, 1, 4),
    _FbL2tpClosingTunnels_Type()
)
fbL2tpClosingTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbL2tpClosingTunnels.setStatus("current")
_FbL2tpFailedTunnels_Type = Integer32
_FbL2tpFailedTunnels_Object = MibScalar
fbL2tpFailedTunnels = _FbL2tpFailedTunnels_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 0, 1, 5),
    _FbL2tpFailedTunnels_Type()
)
fbL2tpFailedTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbL2tpFailedTunnels.setStatus("current")
_FbL2tpClosedTunnels_Type = Integer32
_FbL2tpClosedTunnels_Object = MibScalar
fbL2tpClosedTunnels = _FbL2tpClosedTunnels_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 0, 1, 6),
    _FbL2tpClosedTunnels_Type()
)
fbL2tpClosedTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbL2tpClosedTunnels.setStatus("current")
_FbL2tpGeneralSessions_ObjectIdentity = ObjectIdentity
fbL2tpGeneralSessions = _FbL2tpGeneralSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 0, 2)
)
_FbL2tpFreeSessions_Type = Integer32
_FbL2tpFreeSessions_Object = MibScalar
fbL2tpFreeSessions = _FbL2tpFreeSessions_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 0, 2, 0),
    _FbL2tpFreeSessions_Type()
)
fbL2tpFreeSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbL2tpFreeSessions.setStatus("current")
_FbL2tpWaitingSessions_Type = Integer32
_FbL2tpWaitingSessions_Object = MibScalar
fbL2tpWaitingSessions = _FbL2tpWaitingSessions_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 0, 2, 1),
    _FbL2tpWaitingSessions_Type()
)
fbL2tpWaitingSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbL2tpWaitingSessions.setStatus("current")
_FbL2tpOpeningSessions_Type = Integer32
_FbL2tpOpeningSessions_Object = MibScalar
fbL2tpOpeningSessions = _FbL2tpOpeningSessions_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 0, 2, 2),
    _FbL2tpOpeningSessions_Type()
)
fbL2tpOpeningSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbL2tpOpeningSessions.setStatus("current")
_FbL2tpNegotiatingSessions_Type = Integer32
_FbL2tpNegotiatingSessions_Object = MibScalar
fbL2tpNegotiatingSessions = _FbL2tpNegotiatingSessions_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 0, 2, 3),
    _FbL2tpNegotiatingSessions_Type()
)
fbL2tpNegotiatingSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbL2tpNegotiatingSessions.setStatus("current")
_FbL2tpAuthPendingSessions_Type = Integer32
_FbL2tpAuthPendingSessions_Object = MibScalar
fbL2tpAuthPendingSessions = _FbL2tpAuthPendingSessions_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 0, 2, 4),
    _FbL2tpAuthPendingSessions_Type()
)
fbL2tpAuthPendingSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbL2tpAuthPendingSessions.setStatus("current")
_FbL2tpStartedSessions_Type = Integer32
_FbL2tpStartedSessions_Object = MibScalar
fbL2tpStartedSessions = _FbL2tpStartedSessions_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 0, 2, 5),
    _FbL2tpStartedSessions_Type()
)
fbL2tpStartedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbL2tpStartedSessions.setStatus("current")
_FbL2tpLiveSessions_Type = Integer32
_FbL2tpLiveSessions_Object = MibScalar
fbL2tpLiveSessions = _FbL2tpLiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 0, 2, 6),
    _FbL2tpLiveSessions_Type()
)
fbL2tpLiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbL2tpLiveSessions.setStatus("current")
_FbL2tpAcctPendingSessions_Type = Integer32
_FbL2tpAcctPendingSessions_Object = MibScalar
fbL2tpAcctPendingSessions = _FbL2tpAcctPendingSessions_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 0, 2, 7),
    _FbL2tpAcctPendingSessions_Type()
)
fbL2tpAcctPendingSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbL2tpAcctPendingSessions.setStatus("current")
_FbL2tpClosingSessions_Type = Integer32
_FbL2tpClosingSessions_Object = MibScalar
fbL2tpClosingSessions = _FbL2tpClosingSessions_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 0, 2, 8),
    _FbL2tpClosingSessions_Type()
)
fbL2tpClosingSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbL2tpClosingSessions.setStatus("current")
_FbL2tpClosedSessions_Type = Integer32
_FbL2tpClosedSessions_Object = MibScalar
fbL2tpClosedSessions = _FbL2tpClosedSessions_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 0, 2, 9),
    _FbL2tpClosedSessions_Type()
)
fbL2tpClosedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbL2tpClosedSessions.setStatus("current")
_FbL2tpSessionNegotiationSlotsFree_Type = Integer32
_FbL2tpSessionNegotiationSlotsFree_Object = MibScalar
fbL2tpSessionNegotiationSlotsFree = _FbL2tpSessionNegotiationSlotsFree_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 0, 2, 10),
    _FbL2tpSessionNegotiationSlotsFree_Type()
)
fbL2tpSessionNegotiationSlotsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbL2tpSessionNegotiationSlotsFree.setStatus("current")
_FbL2tpPeerTable_Object = MibTable
fbL2tpPeerTable = _FbL2tpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 1)
)
if mibBuilder.loadTexts:
    fbL2tpPeerTable.setStatus("current")
_FbL2tpPeerEntry_Object = MibTableRow
fbL2tpPeerEntry = _FbL2tpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 1, 1)
)
fbL2tpPeerEntry.setIndexNames(
    (0, "FIREBRICK-L2TP-MIB", "fbL2tpPeerAddressType"),
    (0, "FIREBRICK-L2TP-MIB", "fbL2tpPeerAddress"),
)
if mibBuilder.loadTexts:
    fbL2tpPeerEntry.setStatus("current")
_FbL2tpPeerAddressType_Type = InetAddressType
_FbL2tpPeerAddressType_Object = MibTableColumn
fbL2tpPeerAddressType = _FbL2tpPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 1, 1, 1),
    _FbL2tpPeerAddressType_Type()
)
fbL2tpPeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fbL2tpPeerAddressType.setStatus("current")


class _FbL2tpPeerAddress_Type(InetAddress):
    """Custom type fbL2tpPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_FbL2tpPeerAddress_Type.__name__ = "InetAddress"
_FbL2tpPeerAddress_Object = MibTableColumn
fbL2tpPeerAddress = _FbL2tpPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 1, 1, 2),
    _FbL2tpPeerAddress_Type()
)
fbL2tpPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fbL2tpPeerAddress.setStatus("current")
_FbL2tpPeerLoginName_Type = DisplayString
_FbL2tpPeerLoginName_Object = MibTableColumn
fbL2tpPeerLoginName = _FbL2tpPeerLoginName_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 1, 1, 3),
    _FbL2tpPeerLoginName_Type()
)
fbL2tpPeerLoginName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fbL2tpPeerLoginName.setStatus("current")
_FbL2tpPeerHostName_Type = DisplayString
_FbL2tpPeerHostName_Object = MibTableColumn
fbL2tpPeerHostName = _FbL2tpPeerHostName_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 1, 1, 4),
    _FbL2tpPeerHostName_Type()
)
fbL2tpPeerHostName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fbL2tpPeerHostName.setStatus("current")
_FbL2tpPeerInTunnels_Type = Integer32
_FbL2tpPeerInTunnels_Object = MibTableColumn
fbL2tpPeerInTunnels = _FbL2tpPeerInTunnels_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 1, 1, 5),
    _FbL2tpPeerInTunnels_Type()
)
fbL2tpPeerInTunnels.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fbL2tpPeerInTunnels.setStatus("current")
_FbL2tpPeerOutTunnels_Type = Integer32
_FbL2tpPeerOutTunnels_Object = MibTableColumn
fbL2tpPeerOutTunnels = _FbL2tpPeerOutTunnels_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 1, 1, 6),
    _FbL2tpPeerOutTunnels_Type()
)
fbL2tpPeerOutTunnels.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fbL2tpPeerOutTunnels.setStatus("current")
_FbL2tpPeerOldestUptime_Type = Integer32
_FbL2tpPeerOldestUptime_Object = MibTableColumn
fbL2tpPeerOldestUptime = _FbL2tpPeerOldestUptime_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 1, 1, 7),
    _FbL2tpPeerOldestUptime_Type()
)
fbL2tpPeerOldestUptime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fbL2tpPeerOldestUptime.setStatus("current")
_FbL2tpPeerLiveTunnels_Type = Integer32
_FbL2tpPeerLiveTunnels_Object = MibTableColumn
fbL2tpPeerLiveTunnels = _FbL2tpPeerLiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 1, 1, 8),
    _FbL2tpPeerLiveTunnels_Type()
)
fbL2tpPeerLiveTunnels.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fbL2tpPeerLiveTunnels.setStatus("current")
_FbL2tpPeerSessions_Type = Integer32
_FbL2tpPeerSessions_Object = MibTableColumn
fbL2tpPeerSessions = _FbL2tpPeerSessions_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1701, 1, 1, 9),
    _FbL2tpPeerSessions_Type()
)
fbL2tpPeerSessions.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fbL2tpPeerSessions.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIREBRICK-L2TP-MIB",
    **{"fbL2tpMib": fbL2tpMib,
       "fbL2tpGeneral": fbL2tpGeneral,
       "fbL2tpGeneralTunnels": fbL2tpGeneralTunnels,
       "fbL2tpFreeTunnels": fbL2tpFreeTunnels,
       "fbL2tpOpeningTunnels": fbL2tpOpeningTunnels,
       "fbL2tpLiveIncomingTunnels": fbL2tpLiveIncomingTunnels,
       "fbL2tpLiveOutgoingTunnels": fbL2tpLiveOutgoingTunnels,
       "fbL2tpClosingTunnels": fbL2tpClosingTunnels,
       "fbL2tpFailedTunnels": fbL2tpFailedTunnels,
       "fbL2tpClosedTunnels": fbL2tpClosedTunnels,
       "fbL2tpGeneralSessions": fbL2tpGeneralSessions,
       "fbL2tpFreeSessions": fbL2tpFreeSessions,
       "fbL2tpWaitingSessions": fbL2tpWaitingSessions,
       "fbL2tpOpeningSessions": fbL2tpOpeningSessions,
       "fbL2tpNegotiatingSessions": fbL2tpNegotiatingSessions,
       "fbL2tpAuthPendingSessions": fbL2tpAuthPendingSessions,
       "fbL2tpStartedSessions": fbL2tpStartedSessions,
       "fbL2tpLiveSessions": fbL2tpLiveSessions,
       "fbL2tpAcctPendingSessions": fbL2tpAcctPendingSessions,
       "fbL2tpClosingSessions": fbL2tpClosingSessions,
       "fbL2tpClosedSessions": fbL2tpClosedSessions,
       "fbL2tpSessionNegotiationSlotsFree": fbL2tpSessionNegotiationSlotsFree,
       "fbL2tpPeerTable": fbL2tpPeerTable,
       "fbL2tpPeerEntry": fbL2tpPeerEntry,
       "fbL2tpPeerAddressType": fbL2tpPeerAddressType,
       "fbL2tpPeerAddress": fbL2tpPeerAddress,
       "fbL2tpPeerLoginName": fbL2tpPeerLoginName,
       "fbL2tpPeerHostName": fbL2tpPeerHostName,
       "fbL2tpPeerInTunnels": fbL2tpPeerInTunnels,
       "fbL2tpPeerOutTunnels": fbL2tpPeerOutTunnels,
       "fbL2tpPeerOldestUptime": fbL2tpPeerOldestUptime,
       "fbL2tpPeerLiveTunnels": fbL2tpPeerLiveTunnels,
       "fbL2tpPeerSessions": fbL2tpPeerSessions}
)
