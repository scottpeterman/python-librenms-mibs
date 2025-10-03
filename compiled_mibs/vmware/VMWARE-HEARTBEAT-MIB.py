# SNMP MIB module (VMWARE-HEARTBEAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\vmware\VMWARE-HEARTBEAT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:19 2025
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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

(vmwProductSpecific,) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwProductSpecific")


# MODULE-IDENTITY

vmwHBMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 190, 66)
)
if mibBuilder.loadTexts:
    vmwHBMIB.setRevisions(
        ("2016-02-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwHb_ObjectIdentity = ObjectIdentity
vmwHb = _VmwHb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 190)
)
_VmwHbNotifications_ObjectIdentity = ObjectIdentity
vmwHbNotifications = _VmwHbNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 190, 0)
)
_VmwHbMIBConformance_ObjectIdentity = ObjectIdentity
vmwHbMIBConformance = _VmwHbMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 190, 2)
)
_VmwHbMIBCompliances_ObjectIdentity = ObjectIdentity
vmwHbMIBCompliances = _VmwHbMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 190, 2, 1)
)
_VmwHbMIBGroups_ObjectIdentity = ObjectIdentity
vmwHbMIBGroups = _VmwHbMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 190, 2, 2)
)

# Managed Objects groups


# Notification objects

vmwHbHeartbeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 190, 0, 401)
)
vmwHbHeartbeat.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    vmwHbHeartbeat.setStatus(
        "current"
    )


# Notifications groups

vmwHbNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 4, 190, 2, 2, 2)
)
vmwHbNotificationGroup.setObjects(
    ("VMWARE-HEARTBEAT-MIB", "vmwHbHeartbeat")
)
if mibBuilder.loadTexts:
    vmwHbNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vmwHbMIBBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 4, 190, 2, 1, 4)
)
vmwHbMIBBasicCompliance.setObjects(
      *(("VMWARE-HEARTBEAT-MIB", "vmwHbNotificationGroup"),
        ("VMWARE-HEARTBEAT-MIB", "vmwHbNotificationGroup"))
)
if mibBuilder.loadTexts:
    vmwHbMIBBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-HEARTBEAT-MIB",
    **{"vmwHb": vmwHb,
       "vmwHbNotifications": vmwHbNotifications,
       "vmwHbHeartbeat": vmwHbHeartbeat,
       "vmwHbMIBConformance": vmwHbMIBConformance,
       "vmwHbMIBCompliances": vmwHbMIBCompliances,
       "vmwHbMIBBasicCompliance": vmwHbMIBBasicCompliance,
       "vmwHbMIBGroups": vmwHbMIBGroups,
       "vmwHbNotificationGroup": vmwHbNotificationGroup,
       "vmwHBMIB": vmwHBMIB}
)
