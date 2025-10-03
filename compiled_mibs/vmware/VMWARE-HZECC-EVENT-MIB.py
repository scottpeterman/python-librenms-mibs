# SNMP MIB module (VMWARE-HZECC-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\vmware\VMWARE-HZECC-EVENT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:21 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(vmwHzecc,) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwHzecc")


# MODULE-IDENTITY

vmwHzeccMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 140, 1)
)
if mibBuilder.loadTexts:
    vmwHzeccMIB.setRevisions(
        ("2021-05-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VmwHzeccLifecycleEventType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10,
              20,
              21,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("paired", 1),
          ("unplug", 2),
          ("bluepreupgrade", 10),
          ("bluepostupgradesuccess", 20),
          ("bluepostupgradefailure", 21),
          ("greenpostupgradesuccess", 30),
          ("greenpostupgradefailure", 31))
    )



# MIB Managed Objects in the order of their OIDs

_VmwHzeccNotifications_ObjectIdentity = ObjectIdentity
vmwHzeccNotifications = _VmwHzeccNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 140, 0)
)
_VmwHzeccMIBConformance_ObjectIdentity = ObjectIdentity
vmwHzeccMIBConformance = _VmwHzeccMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 140, 1, 1)
)
_VmwHzeccMIBCompliances_ObjectIdentity = ObjectIdentity
vmwHzeccMIBCompliances = _VmwHzeccMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 140, 1, 1, 1)
)
_VmwHzeccMIBGroups_ObjectIdentity = ObjectIdentity
vmwHzeccMIBGroups = _VmwHzeccMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 140, 1, 1, 2)
)
_VmwHzeccLifecycleEvents_ObjectIdentity = ObjectIdentity
vmwHzeccLifecycleEvents = _VmwHzeccLifecycleEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 140, 4)
)
_VmwHzeccLCEventName_Type = VmwHzeccLifecycleEventType
_VmwHzeccLCEventName_Object = MibScalar
vmwHzeccLCEventName = _VmwHzeccLCEventName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 140, 4, 1),
    _VmwHzeccLCEventName_Type()
)
vmwHzeccLCEventName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwHzeccLCEventName.setStatus("current")
_VmwHzeccSubscriptionLicenseEvents_ObjectIdentity = ObjectIdentity
vmwHzeccSubscriptionLicenseEvents = _VmwHzeccSubscriptionLicenseEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 140, 5)
)
_VmwHzeccSubscriptionLicenseFailStatus_Type = SnmpAdminString
_VmwHzeccSubscriptionLicenseFailStatus_Object = MibScalar
vmwHzeccSubscriptionLicenseFailStatus = _VmwHzeccSubscriptionLicenseFailStatus_Object(
    (1, 3, 6, 1, 4, 1, 6876, 140, 5, 1),
    _VmwHzeccSubscriptionLicenseFailStatus_Type()
)
vmwHzeccSubscriptionLicenseFailStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwHzeccSubscriptionLicenseFailStatus.setStatus("current")

# Managed Objects groups

vmwHzeccObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 140, 1, 1, 2, 1)
)
vmwHzeccObjectGroup.setObjects(
      *(("VMWARE-HZECC-EVENT-MIB", "vmwHzeccLCEventName"),
        ("VMWARE-HZECC-EVENT-MIB", "vmwHzeccSubscriptionLicenseFailStatus"))
)
if mibBuilder.loadTexts:
    vmwHzeccObjectGroup.setStatus("current")


# Notification objects

vmwHzeccLifecycleEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 140, 0, 1)
)
vmwHzeccLifecycleEventTrap.setObjects(
    ("VMWARE-HZECC-EVENT-MIB", "vmwHzeccLCEventName")
)
if mibBuilder.loadTexts:
    vmwHzeccLifecycleEventTrap.setStatus(
        "current"
    )

vmwHzeccSubscriptionLicenseEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 140, 0, 2)
)
vmwHzeccSubscriptionLicenseEventTrap.setObjects(
    ("VMWARE-HZECC-EVENT-MIB", "vmwHzeccSubscriptionLicenseFailStatus")
)
if mibBuilder.loadTexts:
    vmwHzeccSubscriptionLicenseEventTrap.setStatus(
        "current"
    )


# Notifications groups

vmwHzeccNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 140, 1, 1, 2, 2)
)
vmwHzeccNotificationGroup.setObjects(
      *(("VMWARE-HZECC-EVENT-MIB", "vmwHzeccLifecycleEventTrap"),
        ("VMWARE-HZECC-EVENT-MIB", "vmwHzeccSubscriptionLicenseEventTrap"))
)
if mibBuilder.loadTexts:
    vmwHzeccNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vmwHzeccMIBBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 140, 1, 1, 1, 1)
)
vmwHzeccMIBBasicCompliance.setObjects(
      *(("VMWARE-HZECC-EVENT-MIB", "vmwHzeccNotificationGroup"),
        ("VMWARE-HZECC-EVENT-MIB", "vmwHzeccObjectGroup"))
)
if mibBuilder.loadTexts:
    vmwHzeccMIBBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-HZECC-EVENT-MIB",
    **{"VmwHzeccLifecycleEventType": VmwHzeccLifecycleEventType,
       "vmwHzeccNotifications": vmwHzeccNotifications,
       "vmwHzeccLifecycleEventTrap": vmwHzeccLifecycleEventTrap,
       "vmwHzeccSubscriptionLicenseEventTrap": vmwHzeccSubscriptionLicenseEventTrap,
       "vmwHzeccMIB": vmwHzeccMIB,
       "vmwHzeccMIBConformance": vmwHzeccMIBConformance,
       "vmwHzeccMIBCompliances": vmwHzeccMIBCompliances,
       "vmwHzeccMIBBasicCompliance": vmwHzeccMIBBasicCompliance,
       "vmwHzeccMIBGroups": vmwHzeccMIBGroups,
       "vmwHzeccObjectGroup": vmwHzeccObjectGroup,
       "vmwHzeccNotificationGroup": vmwHzeccNotificationGroup,
       "vmwHzeccLifecycleEvents": vmwHzeccLifecycleEvents,
       "vmwHzeccLCEventName": vmwHzeccLCEventName,
       "vmwHzeccSubscriptionLicenseEvents": vmwHzeccSubscriptionLicenseEvents,
       "vmwHzeccSubscriptionLicenseFailStatus": vmwHzeccSubscriptionLicenseFailStatus}
)
