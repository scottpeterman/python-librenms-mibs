# SNMP MIB module (FIREBRICK-IPSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\firebrick\FIREBRICK-IPSEC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:36 2025
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

fbIPsecMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 24693, 100, 500)
)
if mibBuilder.loadTexts:
    fbIPsecMib.setRevisions(
        ("2020-06-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FbIPsecGeneral_ObjectIdentity = ObjectIdentity
fbIPsecGeneral = _FbIPsecGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24693, 100, 500, 1)
)
_FbIPsecEstablished_Type = Integer32
_FbIPsecEstablished_Object = MibScalar
fbIPsecEstablished = _FbIPsecEstablished_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 500, 1, 1),
    _FbIPsecEstablished_Type()
)
fbIPsecEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbIPsecEstablished.setStatus("current")
_FbIPsecHalfOpen_Type = Integer32
_FbIPsecHalfOpen_Object = MibScalar
fbIPsecHalfOpen = _FbIPsecHalfOpen_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 500, 1, 2),
    _FbIPsecHalfOpen_Type()
)
fbIPsecHalfOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbIPsecHalfOpen.setStatus("current")
_FbIPsecConnectionTable_Object = MibTable
fbIPsecConnectionTable = _FbIPsecConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 500, 2)
)
if mibBuilder.loadTexts:
    fbIPsecConnectionTable.setStatus("current")
_FbIPsecConnectionEntry_Object = MibTableRow
fbIPsecConnectionEntry = _FbIPsecConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 500, 2, 1)
)
fbIPsecConnectionEntry.setIndexNames(
    (0, "FIREBRICK-IPSEC-MIB", "fbIPsecConnectionIndex"),
)
if mibBuilder.loadTexts:
    fbIPsecConnectionEntry.setStatus("current")
_FbIPsecConnectionIndex_Type = Integer32
_FbIPsecConnectionIndex_Object = MibTableColumn
fbIPsecConnectionIndex = _FbIPsecConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 500, 2, 1, 1),
    _FbIPsecConnectionIndex_Type()
)
fbIPsecConnectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fbIPsecConnectionIndex.setStatus("current")
_FbIPsecConnectionName_Type = DisplayString
_FbIPsecConnectionName_Object = MibTableColumn
fbIPsecConnectionName = _FbIPsecConnectionName_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 500, 2, 1, 2),
    _FbIPsecConnectionName_Type()
)
fbIPsecConnectionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbIPsecConnectionName.setStatus("current")
_FbIPsecConnectionState_Type = Integer32
_FbIPsecConnectionState_Object = MibTableColumn
fbIPsecConnectionState = _FbIPsecConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 500, 2, 1, 3),
    _FbIPsecConnectionState_Type()
)
fbIPsecConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbIPsecConnectionState.setStatus("current")
_FbIPsecConnectionUptime_Type = TimeTicks
_FbIPsecConnectionUptime_Object = MibTableColumn
fbIPsecConnectionUptime = _FbIPsecConnectionUptime_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 500, 2, 1, 4),
    _FbIPsecConnectionUptime_Type()
)
fbIPsecConnectionUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbIPsecConnectionUptime.setStatus("current")
_FbIPsecConnectionLocalID_Type = DisplayString
_FbIPsecConnectionLocalID_Object = MibScalar
fbIPsecConnectionLocalID = _FbIPsecConnectionLocalID_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 500, 2, 1, 5),
    _FbIPsecConnectionLocalID_Type()
)
fbIPsecConnectionLocalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbIPsecConnectionLocalID.setStatus("current")
_FbIPsecConnectionPeerID_Type = DisplayString
_FbIPsecConnectionPeerID_Object = MibScalar
fbIPsecConnectionPeerID = _FbIPsecConnectionPeerID_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 500, 2, 1, 6),
    _FbIPsecConnectionPeerID_Type()
)
fbIPsecConnectionPeerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbIPsecConnectionPeerID.setStatus("current")
_FbIPsecConnectionPeerAddress_Type = DisplayString
_FbIPsecConnectionPeerAddress_Object = MibTableColumn
fbIPsecConnectionPeerAddress = _FbIPsecConnectionPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 500, 2, 1, 7),
    _FbIPsecConnectionPeerAddress_Type()
)
fbIPsecConnectionPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbIPsecConnectionPeerAddress.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIREBRICK-IPSEC-MIB",
    **{"fbIPsecMib": fbIPsecMib,
       "fbIPsecGeneral": fbIPsecGeneral,
       "fbIPsecEstablished": fbIPsecEstablished,
       "fbIPsecHalfOpen": fbIPsecHalfOpen,
       "fbIPsecConnectionTable": fbIPsecConnectionTable,
       "fbIPsecConnectionEntry": fbIPsecConnectionEntry,
       "fbIPsecConnectionIndex": fbIPsecConnectionIndex,
       "fbIPsecConnectionName": fbIPsecConnectionName,
       "fbIPsecConnectionState": fbIPsecConnectionState,
       "fbIPsecConnectionUptime": fbIPsecConnectionUptime,
       "fbIPsecConnectionLocalID": fbIPsecConnectionLocalID,
       "fbIPsecConnectionPeerID": fbIPsecConnectionPeerID,
       "fbIPsecConnectionPeerAddress": fbIPsecConnectionPeerAddress}
)
