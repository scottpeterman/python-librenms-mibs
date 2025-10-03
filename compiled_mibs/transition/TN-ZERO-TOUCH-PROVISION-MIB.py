# SNMP MIB module (TN-ZERO-TOUCH-PROVISION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-ZERO-TOUCH-PROVISION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:41 2025
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

(entPhysicalDescr,
 entPhysicalHardwareRev,
 entPhysicalSerialNum,
 entPhysicalSoftwareRev) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalDescr",
    "entPhysicalHardwareRev",
    "entPhysicalSerialNum",
    "entPhysicalSoftwareRev")

(ifPhysAddress,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifPhysAddress")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysObjectID,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysObjectID")

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

(tnIpAddr,
 tnIpv6Addr) = mibBuilder.importSymbols(
    "TN-DEV-SYS-IPMGMT-MIB",
    "tnIpAddr",
    "tnIpv6Addr")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnZeroTouchProvisionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 12)
)
if mibBuilder.loadTexts:
    tnZeroTouchProvisionMIB.setRevisions(
        ("2014-02-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnZeroTouchProvisionNotifications_ObjectIdentity = ObjectIdentity
tnZeroTouchProvisionNotifications = _TnZeroTouchProvisionNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 12, 0)
)
_TnZeroTouchProvisionMIBObjects_ObjectIdentity = ObjectIdentity
tnZeroTouchProvisionMIBObjects = _TnZeroTouchProvisionMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 12, 1)
)


class _TnZTPAutoDiscoveryMode_Type(Integer32):
    """Custom type tnZTPAutoDiscoveryMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("dhcp", 1))
    )


_TnZTPAutoDiscoveryMode_Type.__name__ = "Integer32"
_TnZTPAutoDiscoveryMode_Object = MibScalar
tnZTPAutoDiscoveryMode = _TnZTPAutoDiscoveryMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 12, 1, 1),
    _TnZTPAutoDiscoveryMode_Type()
)
tnZTPAutoDiscoveryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnZTPAutoDiscoveryMode.setStatus("current")

# Managed Objects groups


# Notification objects

tnZTPAutoDiscoveryNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 12, 0, 1)
)
tnZTPAutoDiscoveryNotification.setObjects(
      *(("SNMPv2-MIB", "sysObjectID"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("TN-DEV-SYS-IPMGMT-MIB", "tnIpAddr"),
        ("TN-DEV-SYS-IPMGMT-MIB", "tnIpv6Addr"),
        ("ENTITY-MIB", "entPhysicalSoftwareRev"),
        ("ENTITY-MIB", "entPhysicalHardwareRev"),
        ("ENTITY-MIB", "entPhysicalSerialNum"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    tnZTPAutoDiscoveryNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-ZERO-TOUCH-PROVISION-MIB",
    **{"tnZeroTouchProvisionMIB": tnZeroTouchProvisionMIB,
       "tnZeroTouchProvisionNotifications": tnZeroTouchProvisionNotifications,
       "tnZTPAutoDiscoveryNotification": tnZTPAutoDiscoveryNotification,
       "tnZeroTouchProvisionMIBObjects": tnZeroTouchProvisionMIBObjects,
       "tnZTPAutoDiscoveryMode": tnZTPAutoDiscoveryMode}
)
