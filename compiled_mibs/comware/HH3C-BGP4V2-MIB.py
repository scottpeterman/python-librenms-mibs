# SNMP MIB module (HH3C-BGP4V2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-BGP4V2-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:30:48 2025
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

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hh3cBgp4v2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 183)
)
if mibBuilder.loadTexts:
    hh3cBgp4v2.setRevisions(
        ("2019-07-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cBgp4v2Notification_ObjectIdentity = ObjectIdentity
hh3cBgp4v2Notification = _Hh3cBgp4v2Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 183, 0)
)
_Hh3cBgp4v2Objects_ObjectIdentity = ObjectIdentity
hh3cBgp4v2Objects = _Hh3cBgp4v2Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 183, 1)
)
_Hh3cBgp4v2PeerTable_Object = MibTable
hh3cBgp4v2PeerTable = _Hh3cBgp4v2PeerTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 183, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cBgp4v2PeerTable.setStatus("current")
_Hh3cBgp4v2PeerEntry_Object = MibTableRow
hh3cBgp4v2PeerEntry = _Hh3cBgp4v2PeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 183, 1, 1, 1)
)
hh3cBgp4v2PeerEntry.setIndexNames(
    (0, "HH3C-BGP4V2-MIB", "hh3cBgp4v2PeerRemoteAddr"),
)
if mibBuilder.loadTexts:
    hh3cBgp4v2PeerEntry.setStatus("current")
_Hh3cBgp4v2PeerRemoteAddr_Type = InetAddressIPv6
_Hh3cBgp4v2PeerRemoteAddr_Object = MibTableColumn
hh3cBgp4v2PeerRemoteAddr = _Hh3cBgp4v2PeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 183, 1, 1, 1, 1),
    _Hh3cBgp4v2PeerRemoteAddr_Type()
)
hh3cBgp4v2PeerRemoteAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cBgp4v2PeerRemoteAddr.setStatus("current")


class _Hh3cBgp4v2PeerLastError_Type(OctetString):
    """Custom type hh3cBgp4v2PeerLastError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_Hh3cBgp4v2PeerLastError_Type.__name__ = "OctetString"
_Hh3cBgp4v2PeerLastError_Object = MibTableColumn
hh3cBgp4v2PeerLastError = _Hh3cBgp4v2PeerLastError_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 183, 1, 1, 1, 2),
    _Hh3cBgp4v2PeerLastError_Type()
)
hh3cBgp4v2PeerLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBgp4v2PeerLastError.setStatus("current")


class _Hh3cBgp4v2PeerState_Type(Integer32):
    """Custom type hh3cBgp4v2PeerState based on Integer32"""
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
        *(("idle", 1),
          ("connect", 2),
          ("active", 3),
          ("opensent", 4),
          ("openconfirm", 5),
          ("established", 6))
    )


_Hh3cBgp4v2PeerState_Type.__name__ = "Integer32"
_Hh3cBgp4v2PeerState_Object = MibTableColumn
hh3cBgp4v2PeerState = _Hh3cBgp4v2PeerState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 183, 1, 1, 1, 3),
    _Hh3cBgp4v2PeerState_Type()
)
hh3cBgp4v2PeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBgp4v2PeerState.setStatus("current")
_Hh3cBgp4v2Conformance_ObjectIdentity = ObjectIdentity
hh3cBgp4v2Conformance = _Hh3cBgp4v2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 183, 2)
)
_Hh3cBgp4v2Compliances_ObjectIdentity = ObjectIdentity
hh3cBgp4v2Compliances = _Hh3cBgp4v2Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 183, 2, 1)
)
_Hh3cBgp4v2Groups_ObjectIdentity = ObjectIdentity
hh3cBgp4v2Groups = _Hh3cBgp4v2Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 183, 2, 2)
)

# Managed Objects groups

hh3cBgp4v2ErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 183, 2, 2, 1)
)
hh3cBgp4v2ErrorsGroup.setObjects(
    ("HH3C-BGP4V2-MIB", "hh3cBgp4v2PeerLastError")
)
if mibBuilder.loadTexts:
    hh3cBgp4v2ErrorsGroup.setStatus("current")

hh3cBgp4v2PeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 183, 2, 2, 2)
)
hh3cBgp4v2PeerGroup.setObjects(
      *(("HH3C-BGP4V2-MIB", "hh3cBgp4v2PeerState"),
        ("HH3C-BGP4V2-MIB", "hh3cBgp4v2PeerRemoteAddr"))
)
if mibBuilder.loadTexts:
    hh3cBgp4v2PeerGroup.setStatus("current")


# Notification objects

hh3cBgp4v2Established = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 183, 0, 1)
)
hh3cBgp4v2Established.setObjects(
      *(("HH3C-BGP4V2-MIB", "hh3cBgp4v2PeerRemoteAddr"),
        ("HH3C-BGP4V2-MIB", "hh3cBgp4v2PeerLastError"),
        ("HH3C-BGP4V2-MIB", "hh3cBgp4v2PeerState"))
)
if mibBuilder.loadTexts:
    hh3cBgp4v2Established.setStatus(
        "current"
    )

hh3cBgp4v2BackwardTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 183, 0, 2)
)
hh3cBgp4v2BackwardTransition.setObjects(
      *(("HH3C-BGP4V2-MIB", "hh3cBgp4v2PeerRemoteAddr"),
        ("HH3C-BGP4V2-MIB", "hh3cBgp4v2PeerLastError"),
        ("HH3C-BGP4V2-MIB", "hh3cBgp4v2PeerState"))
)
if mibBuilder.loadTexts:
    hh3cBgp4v2BackwardTransition.setStatus(
        "current"
    )


# Notifications groups

hh3cBgp4v2NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 183, 2, 2, 3)
)
hh3cBgp4v2NotificationGroup.setObjects(
      *(("HH3C-BGP4V2-MIB", "hh3cBgp4v2Established"),
        ("HH3C-BGP4V2-MIB", "hh3cBgp4v2BackwardTransition"))
)
if mibBuilder.loadTexts:
    hh3cBgp4v2NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hh3cBgp4v2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 183, 2, 1, 1)
)
hh3cBgp4v2Compliance.setObjects(
      *(("HH3C-BGP4V2-MIB", "hh3cBgp4v2ErrorsGroup"),
        ("HH3C-BGP4V2-MIB", "hh3cBgp4v2PeerGroup"),
        ("HH3C-BGP4V2-MIB", "hh3cBgp4v2NotificationGroup"))
)
if mibBuilder.loadTexts:
    hh3cBgp4v2Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-BGP4V2-MIB",
    **{"hh3cBgp4v2": hh3cBgp4v2,
       "hh3cBgp4v2Notification": hh3cBgp4v2Notification,
       "hh3cBgp4v2Established": hh3cBgp4v2Established,
       "hh3cBgp4v2BackwardTransition": hh3cBgp4v2BackwardTransition,
       "hh3cBgp4v2Objects": hh3cBgp4v2Objects,
       "hh3cBgp4v2PeerTable": hh3cBgp4v2PeerTable,
       "hh3cBgp4v2PeerEntry": hh3cBgp4v2PeerEntry,
       "hh3cBgp4v2PeerRemoteAddr": hh3cBgp4v2PeerRemoteAddr,
       "hh3cBgp4v2PeerLastError": hh3cBgp4v2PeerLastError,
       "hh3cBgp4v2PeerState": hh3cBgp4v2PeerState,
       "hh3cBgp4v2Conformance": hh3cBgp4v2Conformance,
       "hh3cBgp4v2Compliances": hh3cBgp4v2Compliances,
       "hh3cBgp4v2Compliance": hh3cBgp4v2Compliance,
       "hh3cBgp4v2Groups": hh3cBgp4v2Groups,
       "hh3cBgp4v2ErrorsGroup": hh3cBgp4v2ErrorsGroup,
       "hh3cBgp4v2PeerGroup": hh3cBgp4v2PeerGroup,
       "hh3cBgp4v2NotificationGroup": hh3cBgp4v2NotificationGroup}
)
