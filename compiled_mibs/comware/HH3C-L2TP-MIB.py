# SNMP MIB module (HH3C-L2TP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-L2TP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:31:57 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hh3cL2tp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139)
)
if mibBuilder.loadTexts:
    hh3cL2tp.setRevisions(
        ("2020-09-05 00:00",
         "2019-11-21 14:52")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cL2tpObjects_ObjectIdentity = ObjectIdentity
hh3cL2tpObjects = _Hh3cL2tpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1)
)
_Hh3cL2tpScalar_ObjectIdentity = ObjectIdentity
hh3cL2tpScalar = _Hh3cL2tpScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1)
)
_Hh3cL2tpStats_ObjectIdentity = ObjectIdentity
hh3cL2tpStats = _Hh3cL2tpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1, 1)
)
_Hh3cL2tpStatsTotalTunnels_Type = Counter32
_Hh3cL2tpStatsTotalTunnels_Object = MibScalar
hh3cL2tpStatsTotalTunnels = _Hh3cL2tpStatsTotalTunnels_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1, 1, 1),
    _Hh3cL2tpStatsTotalTunnels_Type()
)
hh3cL2tpStatsTotalTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2tpStatsTotalTunnels.setStatus("current")
_Hh3cL2tpStatsTotalSessions_Type = Counter32
_Hh3cL2tpStatsTotalSessions_Object = MibScalar
hh3cL2tpStatsTotalSessions = _Hh3cL2tpStatsTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1, 1, 2),
    _Hh3cL2tpStatsTotalSessions_Type()
)
hh3cL2tpStatsTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2tpStatsTotalSessions.setStatus("current")
_Hh3cL2tpSessionRate_Type = Integer32
_Hh3cL2tpSessionRate_Object = MibScalar
hh3cL2tpSessionRate = _Hh3cL2tpSessionRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1, 1, 3),
    _Hh3cL2tpSessionRate_Type()
)
hh3cL2tpSessionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2tpSessionRate.setStatus("current")
_Hh3cL2tpStatsTemporarySessions_Type = Unsigned32
_Hh3cL2tpStatsTemporarySessions_Object = MibScalar
hh3cL2tpStatsTemporarySessions = _Hh3cL2tpStatsTemporarySessions_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1, 1, 4),
    _Hh3cL2tpStatsTemporarySessions_Type()
)
hh3cL2tpStatsTemporarySessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2tpStatsTemporarySessions.setStatus("current")
_Hh3cL2tpStatsMaxSessions_Type = Unsigned32
_Hh3cL2tpStatsMaxSessions_Object = MibScalar
hh3cL2tpStatsMaxSessions = _Hh3cL2tpStatsMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1, 1, 5),
    _Hh3cL2tpStatsMaxSessions_Type()
)
hh3cL2tpStatsMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2tpStatsMaxSessions.setStatus("current")
_Hh3cL2tpTunnel_ObjectIdentity = ObjectIdentity
hh3cL2tpTunnel = _Hh3cL2tpTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 2)
)
_Hh3cL2tpTunnelTable_Object = MibTable
hh3cL2tpTunnelTable = _Hh3cL2tpTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cL2tpTunnelTable.setStatus("current")
_Hh3cL2tpTunnelEntry_Object = MibTableRow
hh3cL2tpTunnelEntry = _Hh3cL2tpTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 2, 1, 1)
)
hh3cL2tpTunnelEntry.setIndexNames(
    (0, "HH3C-L2TP-MIB", "hh3cL2tpTunnelType"),
    (0, "HH3C-L2TP-MIB", "hh3cL2tpLocalIpAddress"),
    (0, "HH3C-L2TP-MIB", "hh3cL2tpLocalTunnelID"),
)
if mibBuilder.loadTexts:
    hh3cL2tpTunnelEntry.setStatus("current")


class _Hh3cL2tpTunnelType_Type(Integer32):
    """Custom type hh3cL2tpTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("global", 1),
          ("instance", 2))
    )


_Hh3cL2tpTunnelType_Type.__name__ = "Integer32"
_Hh3cL2tpTunnelType_Object = MibTableColumn
hh3cL2tpTunnelType = _Hh3cL2tpTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 2, 1, 1, 1),
    _Hh3cL2tpTunnelType_Type()
)
hh3cL2tpTunnelType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cL2tpTunnelType.setStatus("current")
_Hh3cL2tpLocalIpAddress_Type = IpAddress
_Hh3cL2tpLocalIpAddress_Object = MibTableColumn
hh3cL2tpLocalIpAddress = _Hh3cL2tpLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 2, 1, 1, 2),
    _Hh3cL2tpLocalIpAddress_Type()
)
hh3cL2tpLocalIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cL2tpLocalIpAddress.setStatus("current")


class _Hh3cL2tpLocalTunnelID_Type(Unsigned32):
    """Custom type hh3cL2tpLocalTunnelID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cL2tpLocalTunnelID_Type.__name__ = "Unsigned32"
_Hh3cL2tpLocalTunnelID_Object = MibTableColumn
hh3cL2tpLocalTunnelID = _Hh3cL2tpLocalTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 2, 1, 1, 3),
    _Hh3cL2tpLocalTunnelID_Type()
)
hh3cL2tpLocalTunnelID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cL2tpLocalTunnelID.setStatus("current")


class _Hh3cL2tpSessions_Type(Unsigned32):
    """Custom type hh3cL2tpSessions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3cL2tpSessions_Type.__name__ = "Unsigned32"
_Hh3cL2tpSessions_Object = MibTableColumn
hh3cL2tpSessions = _Hh3cL2tpSessions_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 2, 1, 1, 4),
    _Hh3cL2tpSessions_Type()
)
hh3cL2tpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2tpSessions.setStatus("current")
_Hh3cL2tpRemoteIpAddress_Type = IpAddress
_Hh3cL2tpRemoteIpAddress_Object = MibTableColumn
hh3cL2tpRemoteIpAddress = _Hh3cL2tpRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 2, 1, 1, 5),
    _Hh3cL2tpRemoteIpAddress_Type()
)
hh3cL2tpRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2tpRemoteIpAddress.setStatus("current")


class _Hh3cL2tpRemoteTunnelID_Type(Unsigned32):
    """Custom type hh3cL2tpRemoteTunnelID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cL2tpRemoteTunnelID_Type.__name__ = "Unsigned32"
_Hh3cL2tpRemoteTunnelID_Object = MibTableColumn
hh3cL2tpRemoteTunnelID = _Hh3cL2tpRemoteTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 2, 1, 1, 6),
    _Hh3cL2tpRemoteTunnelID_Type()
)
hh3cL2tpRemoteTunnelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2tpRemoteTunnelID.setStatus("current")


class _Hh3cL2tpRemotePort_Type(Unsigned32):
    """Custom type hh3cL2tpRemotePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cL2tpRemotePort_Type.__name__ = "Unsigned32"
_Hh3cL2tpRemotePort_Object = MibTableColumn
hh3cL2tpRemotePort = _Hh3cL2tpRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 2, 1, 1, 7),
    _Hh3cL2tpRemotePort_Type()
)
hh3cL2tpRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2tpRemotePort.setStatus("current")


class _Hh3cL2tpRemoteName_Type(DisplayString):
    """Custom type hh3cL2tpRemoteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cL2tpRemoteName_Type.__name__ = "DisplayString"
_Hh3cL2tpRemoteName_Object = MibTableColumn
hh3cL2tpRemoteName = _Hh3cL2tpRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 2, 1, 1, 8),
    _Hh3cL2tpRemoteName_Type()
)
hh3cL2tpRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2tpRemoteName.setStatus("current")


class _Hh3cL2tpTunnelState_Type(Integer32):
    """Custom type hh3cL2tpTunnelState based on Integer32"""
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
        *(("idle", 0),
          ("waitReply", 1),
          ("established", 2),
          ("stopping", 3))
    )


_Hh3cL2tpTunnelState_Type.__name__ = "Integer32"
_Hh3cL2tpTunnelState_Object = MibTableColumn
hh3cL2tpTunnelState = _Hh3cL2tpTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 2, 1, 1, 9),
    _Hh3cL2tpTunnelState_Type()
)
hh3cL2tpTunnelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2tpTunnelState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-L2TP-MIB",
    **{"hh3cL2tp": hh3cL2tp,
       "hh3cL2tpObjects": hh3cL2tpObjects,
       "hh3cL2tpScalar": hh3cL2tpScalar,
       "hh3cL2tpStats": hh3cL2tpStats,
       "hh3cL2tpStatsTotalTunnels": hh3cL2tpStatsTotalTunnels,
       "hh3cL2tpStatsTotalSessions": hh3cL2tpStatsTotalSessions,
       "hh3cL2tpSessionRate": hh3cL2tpSessionRate,
       "hh3cL2tpStatsTemporarySessions": hh3cL2tpStatsTemporarySessions,
       "hh3cL2tpStatsMaxSessions": hh3cL2tpStatsMaxSessions,
       "hh3cL2tpTunnel": hh3cL2tpTunnel,
       "hh3cL2tpTunnelTable": hh3cL2tpTunnelTable,
       "hh3cL2tpTunnelEntry": hh3cL2tpTunnelEntry,
       "hh3cL2tpTunnelType": hh3cL2tpTunnelType,
       "hh3cL2tpLocalIpAddress": hh3cL2tpLocalIpAddress,
       "hh3cL2tpLocalTunnelID": hh3cL2tpLocalTunnelID,
       "hh3cL2tpSessions": hh3cL2tpSessions,
       "hh3cL2tpRemoteIpAddress": hh3cL2tpRemoteIpAddress,
       "hh3cL2tpRemoteTunnelID": hh3cL2tpRemoteTunnelID,
       "hh3cL2tpRemotePort": hh3cL2tpRemotePort,
       "hh3cL2tpRemoteName": hh3cL2tpRemoteName,
       "hh3cL2tpTunnelState": hh3cL2tpTunnelState}
)
