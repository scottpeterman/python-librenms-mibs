# SNMP MIB module (ARUBAWIRED-MACNOTIFY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-MACNOTIFY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:12 2025
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

(wndFeatures,) = mibBuilder.importSymbols(
    "ARUBAWIRED-NETWORKING-OID",
    "wndFeatures")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

macNotify = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19)
)
if mibBuilder.loadTexts:
    macNotify.setRevisions(
        ("2021-03-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArubaWiredMacNotifyNotificationObjects_ObjectIdentity = ObjectIdentity
arubaWiredMacNotifyNotificationObjects = _ArubaWiredMacNotifyNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19, 0)
)
_ArubaWiredMacNotifyConfigObjects_ObjectIdentity = ObjectIdentity
arubaWiredMacNotifyConfigObjects = _ArubaWiredMacNotifyConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19, 1)
)


class _ArubaWiredMacNotifyEnable_Type(Integer32):
    """Custom type arubaWiredMacNotifyEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ArubaWiredMacNotifyEnable_Type.__name__ = "Integer32"
_ArubaWiredMacNotifyEnable_Object = MibScalar
arubaWiredMacNotifyEnable = _ArubaWiredMacNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19, 1, 1),
    _ArubaWiredMacNotifyEnable_Type()
)
arubaWiredMacNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMacNotifyEnable.setStatus("current")
_ArubaWiredMacNotifyConformance_ObjectIdentity = ObjectIdentity
arubaWiredMacNotifyConformance = _ArubaWiredMacNotifyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19, 2)
)
_ArubaWiredMacNotify_ObjectIdentity = ObjectIdentity
arubaWiredMacNotify = _ArubaWiredMacNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19, 3)
)
_MacNotifyChangeTable_Object = MibTable
macNotifyChangeTable = _MacNotifyChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19, 3, 1)
)
if mibBuilder.loadTexts:
    macNotifyChangeTable.setStatus("current")
_MacNotifyChangeTableEntry_Object = MibTableRow
macNotifyChangeTableEntry = _MacNotifyChangeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19, 3, 1, 1)
)
macNotifyChangeTableEntry.setIndexNames(
    (0, "ARUBAWIRED-MACNOTIFY-MIB", "arubaWiredMacNotifyMacAddress"),
)
if mibBuilder.loadTexts:
    macNotifyChangeTableEntry.setStatus("current")


class _ArubaWiredMacNotifyAction_Type(Integer32):
    """Custom type arubaWiredMacNotifyAction based on Integer32"""
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
        *(("aged", 0),
          ("learned", 1),
          ("moved", 2),
          ("removed", 3))
    )


_ArubaWiredMacNotifyAction_Type.__name__ = "Integer32"
_ArubaWiredMacNotifyAction_Object = MibTableColumn
arubaWiredMacNotifyAction = _ArubaWiredMacNotifyAction_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19, 3, 1, 1, 1),
    _ArubaWiredMacNotifyAction_Type()
)
arubaWiredMacNotifyAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredMacNotifyAction.setStatus("current")
_ArubaWiredMacNotifyMacAddress_Type = MacAddress
_ArubaWiredMacNotifyMacAddress_Object = MibTableColumn
arubaWiredMacNotifyMacAddress = _ArubaWiredMacNotifyMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19, 3, 1, 1, 2),
    _ArubaWiredMacNotifyMacAddress_Type()
)
arubaWiredMacNotifyMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredMacNotifyMacAddress.setStatus("current")
_ArubaWiredMacNotifyFromPortId_Type = Integer32
_ArubaWiredMacNotifyFromPortId_Object = MibTableColumn
arubaWiredMacNotifyFromPortId = _ArubaWiredMacNotifyFromPortId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19, 3, 1, 1, 3),
    _ArubaWiredMacNotifyFromPortId_Type()
)
arubaWiredMacNotifyFromPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredMacNotifyFromPortId.setStatus("current")
_ArubaWiredMacNotifyToPortId_Type = Integer32
_ArubaWiredMacNotifyToPortId_Object = MibTableColumn
arubaWiredMacNotifyToPortId = _ArubaWiredMacNotifyToPortId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19, 3, 1, 1, 4),
    _ArubaWiredMacNotifyToPortId_Type()
)
arubaWiredMacNotifyToPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredMacNotifyToPortId.setStatus("current")
_ArubaWiredMacNotifyVlanId_Type = Integer32
_ArubaWiredMacNotifyVlanId_Object = MibTableColumn
arubaWiredMacNotifyVlanId = _ArubaWiredMacNotifyVlanId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19, 3, 1, 1, 5),
    _ArubaWiredMacNotifyVlanId_Type()
)
arubaWiredMacNotifyVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredMacNotifyVlanId.setStatus("current")
_ArubaWiredMacNotifyFromDest_Type = DisplayString
_ArubaWiredMacNotifyFromDest_Object = MibTableColumn
arubaWiredMacNotifyFromDest = _ArubaWiredMacNotifyFromDest_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19, 3, 1, 1, 6),
    _ArubaWiredMacNotifyFromDest_Type()
)
arubaWiredMacNotifyFromDest.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredMacNotifyFromDest.setStatus("current")
_ArubaWiredMacNotifyToDest_Type = DisplayString
_ArubaWiredMacNotifyToDest_Object = MibTableColumn
arubaWiredMacNotifyToDest = _ArubaWiredMacNotifyToDest_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19, 3, 1, 1, 7),
    _ArubaWiredMacNotifyToDest_Type()
)
arubaWiredMacNotifyToDest.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredMacNotifyToDest.setStatus("current")
_MacNotifyConformance_ObjectIdentity = ObjectIdentity
macNotifyConformance = _MacNotifyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19, 4)
)
_MacNotifyDataGroups_ObjectIdentity = ObjectIdentity
macNotifyDataGroups = _MacNotifyDataGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19, 4, 1)
)
_MacNotifyTrapsGroups_ObjectIdentity = ObjectIdentity
macNotifyTrapsGroups = _MacNotifyTrapsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19, 4, 2)
)
_MacNotifySystemGroups_ObjectIdentity = ObjectIdentity
macNotifySystemGroups = _MacNotifySystemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19, 4, 3)
)
_MacNotifyCompliance_ObjectIdentity = ObjectIdentity
macNotifyCompliance = _MacNotifyCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19, 4, 4)
)

# Managed Objects groups

macNotifyDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19, 4, 1, 1)
)
macNotifyDataGroup.setObjects(
      *(("ARUBAWIRED-MACNOTIFY-MIB", "arubaWiredMacNotifyAction"),
        ("ARUBAWIRED-MACNOTIFY-MIB", "arubaWiredMacNotifyMacAddress"),
        ("ARUBAWIRED-MACNOTIFY-MIB", "arubaWiredMacNotifyFromPortId"),
        ("ARUBAWIRED-MACNOTIFY-MIB", "arubaWiredMacNotifyToPortId"),
        ("ARUBAWIRED-MACNOTIFY-MIB", "arubaWiredMacNotifyVlanId"),
        ("ARUBAWIRED-MACNOTIFY-MIB", "arubaWiredMacNotifyFromDest"),
        ("ARUBAWIRED-MACNOTIFY-MIB", "arubaWiredMacNotifyToDest"))
)
if mibBuilder.loadTexts:
    macNotifyDataGroup.setStatus("current")

macNotifySystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19, 4, 1, 3)
)
macNotifySystemGroup.setObjects(
    ("ARUBAWIRED-MACNOTIFY-MIB", "arubaWiredMacNotifyEnable")
)
if mibBuilder.loadTexts:
    macNotifySystemGroup.setStatus("current")


# Notification objects

arubaWiredMacNotifyMacAddressTableChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19, 0, 1)
)
arubaWiredMacNotifyMacAddressTableChange.setObjects(
      *(("ARUBAWIRED-MACNOTIFY-MIB", "arubaWiredMacNotifyAction"),
        ("ARUBAWIRED-MACNOTIFY-MIB", "arubaWiredMacNotifyMacAddress"),
        ("ARUBAWIRED-MACNOTIFY-MIB", "arubaWiredMacNotifyFromPortId"),
        ("ARUBAWIRED-MACNOTIFY-MIB", "arubaWiredMacNotifyToPortId"),
        ("ARUBAWIRED-MACNOTIFY-MIB", "arubaWiredMacNotifyVlanId"),
        ("ARUBAWIRED-MACNOTIFY-MIB", "arubaWiredMacNotifyFromDest"),
        ("ARUBAWIRED-MACNOTIFY-MIB", "arubaWiredMacNotifyToDest"))
)
if mibBuilder.loadTexts:
    arubaWiredMacNotifyMacAddressTableChange.setStatus(
        "current"
    )


# Notifications groups

macNotifyTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19, 4, 1, 2)
)
macNotifyTrapsGroup.setObjects(
    ("ARUBAWIRED-MACNOTIFY-MIB", "arubaWiredMacNotifyMacAddressTableChange")
)
if mibBuilder.loadTexts:
    macNotifyTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

macNotifyComplianceGroups = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19, 4, 4, 1)
)
macNotifyComplianceGroups.setObjects(
      *(("ARUBAWIRED-MACNOTIFY-MIB", "macNotifyDataGroup"),
        ("ARUBAWIRED-MACNOTIFY-MIB", "macNotifyTrapsGroup"),
        ("ARUBAWIRED-MACNOTIFY-MIB", "macNotifySystemGroup"))
)
if mibBuilder.loadTexts:
    macNotifyComplianceGroups.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-MACNOTIFY-MIB",
    **{"macNotify": macNotify,
       "arubaWiredMacNotifyNotificationObjects": arubaWiredMacNotifyNotificationObjects,
       "arubaWiredMacNotifyMacAddressTableChange": arubaWiredMacNotifyMacAddressTableChange,
       "arubaWiredMacNotifyConfigObjects": arubaWiredMacNotifyConfigObjects,
       "arubaWiredMacNotifyEnable": arubaWiredMacNotifyEnable,
       "arubaWiredMacNotifyConformance": arubaWiredMacNotifyConformance,
       "arubaWiredMacNotify": arubaWiredMacNotify,
       "macNotifyChangeTable": macNotifyChangeTable,
       "macNotifyChangeTableEntry": macNotifyChangeTableEntry,
       "arubaWiredMacNotifyAction": arubaWiredMacNotifyAction,
       "arubaWiredMacNotifyMacAddress": arubaWiredMacNotifyMacAddress,
       "arubaWiredMacNotifyFromPortId": arubaWiredMacNotifyFromPortId,
       "arubaWiredMacNotifyToPortId": arubaWiredMacNotifyToPortId,
       "arubaWiredMacNotifyVlanId": arubaWiredMacNotifyVlanId,
       "arubaWiredMacNotifyFromDest": arubaWiredMacNotifyFromDest,
       "arubaWiredMacNotifyToDest": arubaWiredMacNotifyToDest,
       "macNotifyConformance": macNotifyConformance,
       "macNotifyDataGroups": macNotifyDataGroups,
       "macNotifyDataGroup": macNotifyDataGroup,
       "macNotifyTrapsGroup": macNotifyTrapsGroup,
       "macNotifySystemGroup": macNotifySystemGroup,
       "macNotifyTrapsGroups": macNotifyTrapsGroups,
       "macNotifySystemGroups": macNotifySystemGroups,
       "macNotifyCompliance": macNotifyCompliance,
       "macNotifyComplianceGroups": macNotifyComplianceGroups}
)
