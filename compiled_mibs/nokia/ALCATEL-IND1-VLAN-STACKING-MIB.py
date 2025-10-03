# SNMP MIB module (ALCATEL-IND1-VLAN-STACKING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-VLAN-STACKING-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:14:26 2025
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

(softentIND1VlanStackingMgt,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1VlanStackingMgt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1VLANStackingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1VLANStackingMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1VLANStackingMIBObjects = _AlcatelIND1VLANStackingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1VLANStackingMIBObjects.setStatus("current")
_AlaVlanStackingPort_ObjectIdentity = ObjectIdentity
alaVlanStackingPort = _AlaVlanStackingPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 1, 1)
)
_AlaVstkPortTable_Object = MibTable
alaVstkPortTable = _AlaVstkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaVstkPortTable.setStatus("current")
_AlaVstkPortEntry_Object = MibTableRow
alaVstkPortEntry = _AlaVstkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 1, 1, 1, 1)
)
alaVstkPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkPortNumber"),
)
if mibBuilder.loadTexts:
    alaVstkPortEntry.setStatus("current")
_AlaVstkPortNumber_Type = InterfaceIndex
_AlaVstkPortNumber_Object = MibTableColumn
alaVstkPortNumber = _AlaVstkPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 1, 1, 1, 1, 1),
    _AlaVstkPortNumber_Type()
)
alaVstkPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVstkPortNumber.setStatus("current")


class _AlaVstkPortType_Type(Integer32):
    """Custom type alaVstkPortType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("userCustomer", 1),
          ("userProvider", 2),
          ("network", 3))
    )


_AlaVstkPortType_Type.__name__ = "Integer32"
_AlaVstkPortType_Object = MibTableColumn
alaVstkPortType = _AlaVstkPortType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 1, 1, 1, 1, 2),
    _AlaVstkPortType_Type()
)
alaVstkPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVstkPortType.setStatus("current")


class _AlaVstkPortVendorTpid_Type(Integer32):
    """Custom type alaVstkPortVendorTpid based on Integer32"""
    defaultValue = 34984


_AlaVstkPortVendorTpid_Type.__name__ = "Integer32"
_AlaVstkPortVendorTpid_Object = MibTableColumn
alaVstkPortVendorTpid = _AlaVstkPortVendorTpid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 1, 1, 1, 1, 3),
    _AlaVstkPortVendorTpid_Type()
)
alaVstkPortVendorTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVstkPortVendorTpid.setStatus("current")


class _AlaVstkPortBpduTreatment_Type(Integer32):
    """Custom type alaVstkPortBpduTreatment based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flooded", 1),
          ("dropped", 2))
    )


_AlaVstkPortBpduTreatment_Type.__name__ = "Integer32"
_AlaVstkPortBpduTreatment_Object = MibTableColumn
alaVstkPortBpduTreatment = _AlaVstkPortBpduTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 1, 1, 1, 1, 4),
    _AlaVstkPortBpduTreatment_Type()
)
alaVstkPortBpduTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVstkPortBpduTreatment.setStatus("current")


class _AlaVstkPortAcceptFrameType_Type(Integer32):
    """Custom type alaVstkPortAcceptFrameType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 1),
          ("untagged", 2),
          ("all", 3))
    )


_AlaVstkPortAcceptFrameType_Type.__name__ = "Integer32"
_AlaVstkPortAcceptFrameType_Object = MibTableColumn
alaVstkPortAcceptFrameType = _AlaVstkPortAcceptFrameType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 1, 1, 1, 1, 5),
    _AlaVstkPortAcceptFrameType_Type()
)
alaVstkPortAcceptFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVstkPortAcceptFrameType.setStatus("current")


class _AlaVstkPortLookupMiss_Type(Integer32):
    """Custom type alaVstkPortLookupMiss based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("default", 2))
    )


_AlaVstkPortLookupMiss_Type.__name__ = "Integer32"
_AlaVstkPortLookupMiss_Object = MibTableColumn
alaVstkPortLookupMiss = _AlaVstkPortLookupMiss_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 1, 1, 1, 1, 6),
    _AlaVstkPortLookupMiss_Type()
)
alaVstkPortLookupMiss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVstkPortLookupMiss.setStatus("current")


class _AlaVstkPortDefaultSvlan_Type(Integer32):
    """Custom type alaVstkPortDefaultSvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaVstkPortDefaultSvlan_Type.__name__ = "Integer32"
_AlaVstkPortDefaultSvlan_Object = MibTableColumn
alaVstkPortDefaultSvlan = _AlaVstkPortDefaultSvlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 1, 1, 1, 1, 7),
    _AlaVstkPortDefaultSvlan_Type()
)
alaVstkPortDefaultSvlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVstkPortDefaultSvlan.setStatus("current")
_AlaVstkPortRowStatus_Type = RowStatus
_AlaVstkPortRowStatus_Object = MibTableColumn
alaVstkPortRowStatus = _AlaVstkPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 1, 1, 1, 1, 8),
    _AlaVstkPortRowStatus_Type()
)
alaVstkPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVstkPortRowStatus.setStatus("current")


class _AlaVstkPortLegacyStpBpdu_Type(Integer32):
    """Custom type alaVstkPortLegacyStpBpdu based on Integer32"""
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


_AlaVstkPortLegacyStpBpdu_Type.__name__ = "Integer32"
_AlaVstkPortLegacyStpBpdu_Object = MibTableColumn
alaVstkPortLegacyStpBpdu = _AlaVstkPortLegacyStpBpdu_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 1, 1, 1, 1, 9),
    _AlaVstkPortLegacyStpBpdu_Type()
)
alaVstkPortLegacyStpBpdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVstkPortLegacyStpBpdu.setStatus("current")
_AlaVlanStackingSvlanPort_ObjectIdentity = ObjectIdentity
alaVlanStackingSvlanPort = _AlaVlanStackingSvlanPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 1, 2)
)
_AlaVstkSvlanPortTable_Object = MibTable
alaVstkSvlanPortTable = _AlaVstkSvlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaVstkSvlanPortTable.setStatus("current")
_AlaVstkSvlanPortEntry_Object = MibTableRow
alaVstkSvlanPortEntry = _AlaVstkSvlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 1, 2, 1, 1)
)
alaVstkSvlanPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkSvlanPortSvlanNumber"),
    (0, "ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkSvlanPortPortNumber"),
    (0, "ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkSvlanPortCvlanNumber"),
)
if mibBuilder.loadTexts:
    alaVstkSvlanPortEntry.setStatus("current")


class _AlaVstkSvlanPortSvlanNumber_Type(Integer32):
    """Custom type alaVstkSvlanPortSvlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaVstkSvlanPortSvlanNumber_Type.__name__ = "Integer32"
_AlaVstkSvlanPortSvlanNumber_Object = MibTableColumn
alaVstkSvlanPortSvlanNumber = _AlaVstkSvlanPortSvlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 1, 2, 1, 1, 1),
    _AlaVstkSvlanPortSvlanNumber_Type()
)
alaVstkSvlanPortSvlanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVstkSvlanPortSvlanNumber.setStatus("current")
_AlaVstkSvlanPortPortNumber_Type = InterfaceIndex
_AlaVstkSvlanPortPortNumber_Object = MibTableColumn
alaVstkSvlanPortPortNumber = _AlaVstkSvlanPortPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 1, 2, 1, 1, 2),
    _AlaVstkSvlanPortPortNumber_Type()
)
alaVstkSvlanPortPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVstkSvlanPortPortNumber.setStatus("current")


class _AlaVstkSvlanPortCvlanNumber_Type(Integer32):
    """Custom type alaVstkSvlanPortCvlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaVstkSvlanPortCvlanNumber_Type.__name__ = "Integer32"
_AlaVstkSvlanPortCvlanNumber_Object = MibTableColumn
alaVstkSvlanPortCvlanNumber = _AlaVstkSvlanPortCvlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 1, 2, 1, 1, 3),
    _AlaVstkSvlanPortCvlanNumber_Type()
)
alaVstkSvlanPortCvlanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVstkSvlanPortCvlanNumber.setStatus("current")


class _AlaVstkSvlanPortMode_Type(Integer32):
    """Custom type alaVstkSvlanPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doubleTag", 1),
          ("translate", 2))
    )


_AlaVstkSvlanPortMode_Type.__name__ = "Integer32"
_AlaVstkSvlanPortMode_Object = MibTableColumn
alaVstkSvlanPortMode = _AlaVstkSvlanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 1, 2, 1, 1, 4),
    _AlaVstkSvlanPortMode_Type()
)
alaVstkSvlanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVstkSvlanPortMode.setStatus("current")
_AlaVstkSvlanPortRowStatus_Type = RowStatus
_AlaVstkSvlanPortRowStatus_Object = MibTableColumn
alaVstkSvlanPortRowStatus = _AlaVstkSvlanPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 1, 2, 1, 1, 5),
    _AlaVstkSvlanPortRowStatus_Type()
)
alaVstkSvlanPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVstkSvlanPortRowStatus.setStatus("current")
_AlcatelIND1VLANStackingMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1VLANStackingMIBConformance = _AlcatelIND1VLANStackingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1VLANStackingMIBConformance.setStatus("current")
_AlcatelIND1VLANStackingMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1VLANStackingMIBGroups = _AlcatelIND1VLANStackingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1VLANStackingMIBGroups.setStatus("current")
_AlcatelIND1VLANStackingMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1VLANStackingMIBCompliances = _AlcatelIND1VLANStackingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1VLANStackingMIBCompliances.setStatus("current")

# Managed Objects groups

vlanStackingPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 2, 1, 1)
)
vlanStackingPortGroup.setObjects(
      *(("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkPortNumber"),
        ("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkPortType"),
        ("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkPortVendorTpid"),
        ("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkPortBpduTreatment"),
        ("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkPortAcceptFrameType"),
        ("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkPortLookupMiss"),
        ("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkPortDefaultSvlan"),
        ("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkPortRowStatus"))
)
if mibBuilder.loadTexts:
    vlanStackingPortGroup.setStatus("current")

vlanStackingSvlanPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 2, 1, 2)
)
vlanStackingSvlanPortGroup.setObjects(
      *(("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkSvlanPortSvlanNumber"),
        ("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkSvlanPortPortNumber"),
        ("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkSvlanPortCvlanNumber"),
        ("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkSvlanPortMode"),
        ("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkSvlanPortRowStatus"))
)
if mibBuilder.loadTexts:
    vlanStackingSvlanPortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1VLANStackingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 37, 1, 2, 2, 1)
)
alcatelIND1VLANStackingMIBCompliance.setObjects(
      *(("ALCATEL-IND1-VLAN-STACKING-MIB", "vlanStackingPortGroup"),
        ("ALCATEL-IND1-VLAN-STACKING-MIB", "vlanStackingSvlanPortGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1VLANStackingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-VLAN-STACKING-MIB",
    **{"alcatelIND1VLANStackingMIB": alcatelIND1VLANStackingMIB,
       "alcatelIND1VLANStackingMIBObjects": alcatelIND1VLANStackingMIBObjects,
       "alaVlanStackingPort": alaVlanStackingPort,
       "alaVstkPortTable": alaVstkPortTable,
       "alaVstkPortEntry": alaVstkPortEntry,
       "alaVstkPortNumber": alaVstkPortNumber,
       "alaVstkPortType": alaVstkPortType,
       "alaVstkPortVendorTpid": alaVstkPortVendorTpid,
       "alaVstkPortBpduTreatment": alaVstkPortBpduTreatment,
       "alaVstkPortAcceptFrameType": alaVstkPortAcceptFrameType,
       "alaVstkPortLookupMiss": alaVstkPortLookupMiss,
       "alaVstkPortDefaultSvlan": alaVstkPortDefaultSvlan,
       "alaVstkPortRowStatus": alaVstkPortRowStatus,
       "alaVstkPortLegacyStpBpdu": alaVstkPortLegacyStpBpdu,
       "alaVlanStackingSvlanPort": alaVlanStackingSvlanPort,
       "alaVstkSvlanPortTable": alaVstkSvlanPortTable,
       "alaVstkSvlanPortEntry": alaVstkSvlanPortEntry,
       "alaVstkSvlanPortSvlanNumber": alaVstkSvlanPortSvlanNumber,
       "alaVstkSvlanPortPortNumber": alaVstkSvlanPortPortNumber,
       "alaVstkSvlanPortCvlanNumber": alaVstkSvlanPortCvlanNumber,
       "alaVstkSvlanPortMode": alaVstkSvlanPortMode,
       "alaVstkSvlanPortRowStatus": alaVstkSvlanPortRowStatus,
       "alcatelIND1VLANStackingMIBConformance": alcatelIND1VLANStackingMIBConformance,
       "alcatelIND1VLANStackingMIBGroups": alcatelIND1VLANStackingMIBGroups,
       "vlanStackingPortGroup": vlanStackingPortGroup,
       "vlanStackingSvlanPortGroup": vlanStackingSvlanPortGroup,
       "alcatelIND1VLANStackingMIBCompliances": alcatelIND1VLANStackingMIBCompliances,
       "alcatelIND1VLANStackingMIBCompliance": alcatelIND1VLANStackingMIBCompliance}
)
