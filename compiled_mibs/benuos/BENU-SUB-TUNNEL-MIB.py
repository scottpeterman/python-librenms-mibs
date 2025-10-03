# SNMP MIB module (BENU-SUB-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\benuos\BENU-SUB-TUNNEL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:10 2025
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

(benuWAG,) = mibBuilder.importSymbols(
    "BENU-WAG-MIB",
    "benuWAG")

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

benuWagSubTunMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 2)
)
if mibBuilder.loadTexts:
    benuWagSubTunMIB.setRevisions(
        ("2015-11-13 00:00",
         "2015-01-02 00:00",
         "2012-12-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BWagSubTunnelMIBNotifications_ObjectIdentity = ObjectIdentity
bWagSubTunnelMIBNotifications = _BWagSubTunnelMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 0)
)
if mibBuilder.loadTexts:
    bWagSubTunnelMIBNotifications.setStatus("current")
_BWagSubMIBObjects_ObjectIdentity = ObjectIdentity
bWagSubMIBObjects = _BWagSubMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    bWagSubMIBObjects.setStatus("current")
_BWagSubMaxNumOfSubscribers_Type = Unsigned32
_BWagSubMaxNumOfSubscribers_Object = MibScalar
bWagSubMaxNumOfSubscribers = _BWagSubMaxNumOfSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 1, 1),
    _BWagSubMaxNumOfSubscribers_Type()
)
bWagSubMaxNumOfSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubMaxNumOfSubscribers.setStatus("current")
_BWagSubMIBNotifObjects_ObjectIdentity = ObjectIdentity
bWagSubMIBNotifObjects = _BWagSubMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    bWagSubMIBNotifObjects.setStatus("current")
_BWagSubHighThreshold_Type = Unsigned32
_BWagSubHighThreshold_Object = MibScalar
bWagSubHighThreshold = _BWagSubHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 2, 1),
    _BWagSubHighThreshold_Type()
)
bWagSubHighThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bWagSubHighThreshold.setStatus("current")
_BWagSubLowThreshold_Type = Unsigned32
_BWagSubLowThreshold_Object = MibScalar
bWagSubLowThreshold = _BWagSubLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 2, 2),
    _BWagSubLowThreshold_Type()
)
bWagSubLowThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bWagSubLowThreshold.setStatus("current")
_BWagTunnelMIBObjects_ObjectIdentity = ObjectIdentity
bWagTunnelMIBObjects = _BWagTunnelMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    bWagTunnelMIBObjects.setStatus("current")
_BWagTunMaxNumOfTunnels_Type = Unsigned32
_BWagTunMaxNumOfTunnels_Object = MibScalar
bWagTunMaxNumOfTunnels = _BWagTunMaxNumOfTunnels_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 3, 1),
    _BWagTunMaxNumOfTunnels_Type()
)
bWagTunMaxNumOfTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunMaxNumOfTunnels.setStatus("current")
_BWagTunnelMIBNotifObjects_ObjectIdentity = ObjectIdentity
bWagTunnelMIBNotifObjects = _BWagTunnelMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    bWagTunnelMIBNotifObjects.setStatus("current")
_BWagTunHighThreshold_Type = Unsigned32
_BWagTunHighThreshold_Object = MibScalar
bWagTunHighThreshold = _BWagTunHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 4, 1),
    _BWagTunHighThreshold_Type()
)
bWagTunHighThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bWagTunHighThreshold.setStatus("current")
_BWagTunLowThreshold_Type = Unsigned32
_BWagTunLowThreshold_Object = MibScalar
bWagTunLowThreshold = _BWagTunLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 4, 2),
    _BWagTunLowThreshold_Type()
)
bWagTunLowThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bWagTunLowThreshold.setStatus("current")

# Managed Objects groups


# Notification objects

bWagSubHighThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 0, 1)
)
bWagSubHighThresholdReached.setObjects(
      *(("BENU-SUB-TUNNEL-MIB", "bWagSubMaxNumOfSubscribers"),
        ("BENU-SUB-TUNNEL-MIB", "bWagSubHighThreshold"))
)
if mibBuilder.loadTexts:
    bWagSubHighThresholdReached.setStatus(
        "current"
    )

bWagSubLowThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 0, 2)
)
bWagSubLowThresholdReached.setObjects(
      *(("BENU-SUB-TUNNEL-MIB", "bWagSubMaxNumOfSubscribers"),
        ("BENU-SUB-TUNNEL-MIB", "bWagSubLowThreshold"))
)
if mibBuilder.loadTexts:
    bWagSubLowThresholdReached.setStatus(
        "current"
    )

bWagTunHighThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 0, 3)
)
bWagTunHighThresholdReached.setObjects(
      *(("BENU-SUB-TUNNEL-MIB", "bWagTunMaxNumOfTunnels"),
        ("BENU-SUB-TUNNEL-MIB", "bWagTunHighThreshold"))
)
if mibBuilder.loadTexts:
    bWagTunHighThresholdReached.setStatus(
        "current"
    )

bWagTunLowThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 0, 4)
)
bWagTunLowThresholdReached.setObjects(
      *(("BENU-SUB-TUNNEL-MIB", "bWagTunMaxNumOfTunnels"),
        ("BENU-SUB-TUNNEL-MIB", "bWagTunLowThreshold"))
)
if mibBuilder.loadTexts:
    bWagTunLowThresholdReached.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BENU-SUB-TUNNEL-MIB",
    **{"benuWagSubTunMIB": benuWagSubTunMIB,
       "bWagSubTunnelMIBNotifications": bWagSubTunnelMIBNotifications,
       "bWagSubHighThresholdReached": bWagSubHighThresholdReached,
       "bWagSubLowThresholdReached": bWagSubLowThresholdReached,
       "bWagTunHighThresholdReached": bWagTunHighThresholdReached,
       "bWagTunLowThresholdReached": bWagTunLowThresholdReached,
       "bWagSubMIBObjects": bWagSubMIBObjects,
       "bWagSubMaxNumOfSubscribers": bWagSubMaxNumOfSubscribers,
       "bWagSubMIBNotifObjects": bWagSubMIBNotifObjects,
       "bWagSubHighThreshold": bWagSubHighThreshold,
       "bWagSubLowThreshold": bWagSubLowThreshold,
       "bWagTunnelMIBObjects": bWagTunnelMIBObjects,
       "bWagTunMaxNumOfTunnels": bWagTunMaxNumOfTunnels,
       "bWagTunnelMIBNotifObjects": bWagTunnelMIBNotifObjects,
       "bWagTunHighThreshold": bWagTunHighThreshold,
       "bWagTunLowThreshold": bWagTunLowThreshold}
)
