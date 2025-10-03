# SNMP MIB module (FIREBRICK-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\firebrick\FIREBRICK-BGP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:33 2025
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

fbBgpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 24693, 100, 179)
)
if mibBuilder.loadTexts:
    fbBgpMib.setRevisions(
        ("2020-04-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FbBgpPeerTable_Object = MibTable
fbBgpPeerTable = _FbBgpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 179, 1)
)
if mibBuilder.loadTexts:
    fbBgpPeerTable.setStatus("current")
_FbBgpPeerEntry_Object = MibTableRow
fbBgpPeerEntry = _FbBgpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 179, 1, 1)
)
fbBgpPeerEntry.setIndexNames(
    (0, "FIREBRICK-BGP-MIB", "fbBgpPeerAddressType"),
    (0, "FIREBRICK-BGP-MIB", "fbBgpPeerAddress"),
)
if mibBuilder.loadTexts:
    fbBgpPeerEntry.setStatus("current")
_FbBgpPeerAddressType_Type = InetAddressType
_FbBgpPeerAddressType_Object = MibTableColumn
fbBgpPeerAddressType = _FbBgpPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 179, 1, 1, 1),
    _FbBgpPeerAddressType_Type()
)
fbBgpPeerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbBgpPeerAddressType.setStatus("current")
_FbBgpPeerAddress_Type = InetAddress
_FbBgpPeerAddress_Object = MibTableColumn
fbBgpPeerAddress = _FbBgpPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 179, 1, 1, 2),
    _FbBgpPeerAddress_Type()
)
fbBgpPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbBgpPeerAddress.setStatus("current")
_FbBgpPeerName_Type = DisplayString
_FbBgpPeerName_Object = MibTableColumn
fbBgpPeerName = _FbBgpPeerName_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 179, 1, 1, 3),
    _FbBgpPeerName_Type()
)
fbBgpPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbBgpPeerName.setStatus("current")
_FbBgpPeerState_Type = Integer32
_FbBgpPeerState_Object = MibTableColumn
fbBgpPeerState = _FbBgpPeerState_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 179, 1, 1, 4),
    _FbBgpPeerState_Type()
)
fbBgpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbBgpPeerState.setStatus("current")
_FbBgpPeerRemoteAS_Type = Integer32
_FbBgpPeerRemoteAS_Object = MibTableColumn
fbBgpPeerRemoteAS = _FbBgpPeerRemoteAS_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 179, 1, 1, 5),
    _FbBgpPeerRemoteAS_Type()
)
fbBgpPeerRemoteAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbBgpPeerRemoteAS.setStatus("current")
_FbBgpPeerReceivedIpv4Prefixes_Type = Integer32
_FbBgpPeerReceivedIpv4Prefixes_Object = MibTableColumn
fbBgpPeerReceivedIpv4Prefixes = _FbBgpPeerReceivedIpv4Prefixes_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 179, 1, 1, 6),
    _FbBgpPeerReceivedIpv4Prefixes_Type()
)
fbBgpPeerReceivedIpv4Prefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbBgpPeerReceivedIpv4Prefixes.setStatus("current")
_FbBgpPeerSecondsSinceLastChange_Type = Integer32
_FbBgpPeerSecondsSinceLastChange_Object = MibTableColumn
fbBgpPeerSecondsSinceLastChange = _FbBgpPeerSecondsSinceLastChange_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 179, 1, 1, 7),
    _FbBgpPeerSecondsSinceLastChange_Type()
)
fbBgpPeerSecondsSinceLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbBgpPeerSecondsSinceLastChange.setStatus("current")
_FbBgpPeerReceivedIpv6Prefixes_Type = Integer32
_FbBgpPeerReceivedIpv6Prefixes_Object = MibTableColumn
fbBgpPeerReceivedIpv6Prefixes = _FbBgpPeerReceivedIpv6Prefixes_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 179, 1, 1, 8),
    _FbBgpPeerReceivedIpv6Prefixes_Type()
)
fbBgpPeerReceivedIpv6Prefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbBgpPeerReceivedIpv6Prefixes.setStatus("current")
_FbBgpPeerExported_Type = Integer32
_FbBgpPeerExported_Object = MibScalar
fbBgpPeerExported = _FbBgpPeerExported_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 179, 1, 1, 9),
    _FbBgpPeerExported_Type()
)
fbBgpPeerExported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbBgpPeerExported.setStatus("current")
_FbBgpPeerLocalAddressType_Type = InetAddressType
_FbBgpPeerLocalAddressType_Object = MibScalar
fbBgpPeerLocalAddressType = _FbBgpPeerLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 179, 1, 1, 10),
    _FbBgpPeerLocalAddressType_Type()
)
fbBgpPeerLocalAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbBgpPeerLocalAddressType.setStatus("current")
_FbBgpPeerLocalAddress_Type = InetAddress
_FbBgpPeerLocalAddress_Object = MibScalar
fbBgpPeerLocalAddress = _FbBgpPeerLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 179, 1, 1, 11),
    _FbBgpPeerLocalAddress_Type()
)
fbBgpPeerLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbBgpPeerLocalAddress.setStatus("current")
_FbBgpPeerLocalAS_Type = Integer32
_FbBgpPeerLocalAS_Object = MibScalar
fbBgpPeerLocalAS = _FbBgpPeerLocalAS_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 179, 1, 1, 12),
    _FbBgpPeerLocalAS_Type()
)
fbBgpPeerLocalAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbBgpPeerLocalAS.setStatus("current")
_FbBgpPeerTableId_Type = Integer32
_FbBgpPeerTableId_Object = MibScalar
fbBgpPeerTableId = _FbBgpPeerTableId_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 179, 1, 1, 13),
    _FbBgpPeerTableId_Type()
)
fbBgpPeerTableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbBgpPeerTableId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIREBRICK-BGP-MIB",
    **{"fbBgpMib": fbBgpMib,
       "fbBgpPeerTable": fbBgpPeerTable,
       "fbBgpPeerEntry": fbBgpPeerEntry,
       "fbBgpPeerAddressType": fbBgpPeerAddressType,
       "fbBgpPeerAddress": fbBgpPeerAddress,
       "fbBgpPeerName": fbBgpPeerName,
       "fbBgpPeerState": fbBgpPeerState,
       "fbBgpPeerRemoteAS": fbBgpPeerRemoteAS,
       "fbBgpPeerReceivedIpv4Prefixes": fbBgpPeerReceivedIpv4Prefixes,
       "fbBgpPeerSecondsSinceLastChange": fbBgpPeerSecondsSinceLastChange,
       "fbBgpPeerReceivedIpv6Prefixes": fbBgpPeerReceivedIpv6Prefixes,
       "fbBgpPeerExported": fbBgpPeerExported,
       "fbBgpPeerLocalAddressType": fbBgpPeerLocalAddressType,
       "fbBgpPeerLocalAddress": fbBgpPeerLocalAddress,
       "fbBgpPeerLocalAS": fbBgpPeerLocalAS,
       "fbBgpPeerTableId": fbBgpPeerTableId}
)
