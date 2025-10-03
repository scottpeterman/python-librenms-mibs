# SNMP MIB module (ALCATEL-IND1-LLDP-MED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-LLDP-MED-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:13:41 2025
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

(softentIND1LldpMed,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1LldpMed")

(Dscp,
 PolicyAppType) = mibBuilder.importSymbols(
    "LLDP-EXT-MED-MIB",
    "Dscp",
    "PolicyAppType")

(LldpPortNumber,) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpPortNumber")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1LLDPMEDMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 58, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1LLDPMEDMIB.setRevisions(
        ("2009-08-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1LLDPMEDMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1LLDPMEDMIBObjects = _AlcatelIND1LLDPMEDMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 58, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1LLDPMEDMIBObjects.setStatus("current")
_AlaLldpMedLocMediaPolicyAttributes_ObjectIdentity = ObjectIdentity
alaLldpMedLocMediaPolicyAttributes = _AlaLldpMedLocMediaPolicyAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 58, 1, 1, 1)
)
_AlaLldpXMedLocMediaPolicyTable_Object = MibTable
alaLldpXMedLocMediaPolicyTable = _AlaLldpXMedLocMediaPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 58, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaLldpXMedLocMediaPolicyTable.setStatus("current")
_AlaLldpXMedLocMediaPolicyEntry_Object = MibTableRow
alaLldpXMedLocMediaPolicyEntry = _AlaLldpXMedLocMediaPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 58, 1, 1, 1, 1, 1)
)
alaLldpXMedLocMediaPolicyEntry.setIndexNames(
    (0, "ALCATEL-IND1-LLDP-MED-MIB", "alaLldpXMedLocMediaPolicyId"),
)
if mibBuilder.loadTexts:
    alaLldpXMedLocMediaPolicyEntry.setStatus("current")
_AlaLldpXMedLocMediaPolicyId_Type = Integer32
_AlaLldpXMedLocMediaPolicyId_Object = MibTableColumn
alaLldpXMedLocMediaPolicyId = _AlaLldpXMedLocMediaPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 58, 1, 1, 1, 1, 1, 1),
    _AlaLldpXMedLocMediaPolicyId_Type()
)
alaLldpXMedLocMediaPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaLldpXMedLocMediaPolicyId.setStatus("current")
_AlaLldpXMedLocMediaPolicyAppType_Type = PolicyAppType
_AlaLldpXMedLocMediaPolicyAppType_Object = MibTableColumn
alaLldpXMedLocMediaPolicyAppType = _AlaLldpXMedLocMediaPolicyAppType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 58, 1, 1, 1, 1, 1, 2),
    _AlaLldpXMedLocMediaPolicyAppType_Type()
)
alaLldpXMedLocMediaPolicyAppType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaLldpXMedLocMediaPolicyAppType.setStatus("current")


class _AlaLldpXMedLocMediaPolicyVlanType_Type(Integer32):
    """Custom type alaLldpXMedLocMediaPolicyVlanType based on Integer32"""
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
        *(("tagged", 1),
          ("priorityTagged", 2),
          ("untagged", 3))
    )


_AlaLldpXMedLocMediaPolicyVlanType_Type.__name__ = "Integer32"
_AlaLldpXMedLocMediaPolicyVlanType_Object = MibTableColumn
alaLldpXMedLocMediaPolicyVlanType = _AlaLldpXMedLocMediaPolicyVlanType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 58, 1, 1, 1, 1, 1, 3),
    _AlaLldpXMedLocMediaPolicyVlanType_Type()
)
alaLldpXMedLocMediaPolicyVlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaLldpXMedLocMediaPolicyVlanType.setStatus("current")


class _AlaLldpXMedLocMediaPolicyVlanID_Type(Integer32):
    """Custom type alaLldpXMedLocMediaPolicyVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )


_AlaLldpXMedLocMediaPolicyVlanID_Type.__name__ = "Integer32"
_AlaLldpXMedLocMediaPolicyVlanID_Object = MibTableColumn
alaLldpXMedLocMediaPolicyVlanID = _AlaLldpXMedLocMediaPolicyVlanID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 58, 1, 1, 1, 1, 1, 4),
    _AlaLldpXMedLocMediaPolicyVlanID_Type()
)
alaLldpXMedLocMediaPolicyVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaLldpXMedLocMediaPolicyVlanID.setStatus("current")


class _AlaLldpXMedLocMediaPolicyPriority_Type(Integer32):
    """Custom type alaLldpXMedLocMediaPolicyPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaLldpXMedLocMediaPolicyPriority_Type.__name__ = "Integer32"
_AlaLldpXMedLocMediaPolicyPriority_Object = MibTableColumn
alaLldpXMedLocMediaPolicyPriority = _AlaLldpXMedLocMediaPolicyPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 58, 1, 1, 1, 1, 1, 5),
    _AlaLldpXMedLocMediaPolicyPriority_Type()
)
alaLldpXMedLocMediaPolicyPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaLldpXMedLocMediaPolicyPriority.setStatus("current")
_AlaLldpXMedLocMediaPolicyDscp_Type = Dscp
_AlaLldpXMedLocMediaPolicyDscp_Object = MibTableColumn
alaLldpXMedLocMediaPolicyDscp = _AlaLldpXMedLocMediaPolicyDscp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 58, 1, 1, 1, 1, 1, 6),
    _AlaLldpXMedLocMediaPolicyDscp_Type()
)
alaLldpXMedLocMediaPolicyDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaLldpXMedLocMediaPolicyDscp.setStatus("current")
_AlaLldpXMedLocMediaPolicyUnknown_Type = TruthValue
_AlaLldpXMedLocMediaPolicyUnknown_Object = MibTableColumn
alaLldpXMedLocMediaPolicyUnknown = _AlaLldpXMedLocMediaPolicyUnknown_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 58, 1, 1, 1, 1, 1, 7),
    _AlaLldpXMedLocMediaPolicyUnknown_Type()
)
alaLldpXMedLocMediaPolicyUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLldpXMedLocMediaPolicyUnknown.setStatus("current")
_AlaLldpXMedLocMediaPolicyTagged_Type = TruthValue
_AlaLldpXMedLocMediaPolicyTagged_Object = MibTableColumn
alaLldpXMedLocMediaPolicyTagged = _AlaLldpXMedLocMediaPolicyTagged_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 58, 1, 1, 1, 1, 1, 8),
    _AlaLldpXMedLocMediaPolicyTagged_Type()
)
alaLldpXMedLocMediaPolicyTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLldpXMedLocMediaPolicyTagged.setStatus("current")
_AlaLldpXMedLocMediaPolicyRowStatus_Type = RowStatus
_AlaLldpXMedLocMediaPolicyRowStatus_Object = MibTableColumn
alaLldpXMedLocMediaPolicyRowStatus = _AlaLldpXMedLocMediaPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 58, 1, 1, 1, 1, 1, 9),
    _AlaLldpXMedLocMediaPolicyRowStatus_Type()
)
alaLldpXMedLocMediaPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaLldpXMedLocMediaPolicyRowStatus.setStatus("current")
_AlaLldpXMedLocMediaPolicyPortTable_Object = MibTable
alaLldpXMedLocMediaPolicyPortTable = _AlaLldpXMedLocMediaPolicyPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 58, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaLldpXMedLocMediaPolicyPortTable.setStatus("current")
_AlaLldpXMedLocMediaPolicyPortEntry_Object = MibTableRow
alaLldpXMedLocMediaPolicyPortEntry = _AlaLldpXMedLocMediaPolicyPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 58, 1, 1, 1, 2, 1)
)
alaLldpXMedLocMediaPolicyPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-LLDP-MED-MIB", "alaLldpXMedLocMediaPolicyId"),
    (0, "ALCATEL-IND1-LLDP-MED-MIB", "alaLldpXMedLocMediaPolicyPortNumber"),
)
if mibBuilder.loadTexts:
    alaLldpXMedLocMediaPolicyPortEntry.setStatus("current")
_AlaLldpXMedLocMediaPolicyPortNumber_Type = LldpPortNumber
_AlaLldpXMedLocMediaPolicyPortNumber_Object = MibTableColumn
alaLldpXMedLocMediaPolicyPortNumber = _AlaLldpXMedLocMediaPolicyPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 58, 1, 1, 1, 2, 1, 1),
    _AlaLldpXMedLocMediaPolicyPortNumber_Type()
)
alaLldpXMedLocMediaPolicyPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaLldpXMedLocMediaPolicyPortNumber.setStatus("current")
_AlaLldpXMedLocMediaPolicyPortRowStatus_Type = RowStatus
_AlaLldpXMedLocMediaPolicyPortRowStatus_Object = MibTableColumn
alaLldpXMedLocMediaPolicyPortRowStatus = _AlaLldpXMedLocMediaPolicyPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 58, 1, 1, 1, 2, 1, 2),
    _AlaLldpXMedLocMediaPolicyPortRowStatus_Type()
)
alaLldpXMedLocMediaPolicyPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaLldpXMedLocMediaPolicyPortRowStatus.setStatus("current")
_AlcatelIND1LLDPMEDMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1LLDPMEDMIBConformance = _AlcatelIND1LLDPMEDMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 58, 1, 2)
)
_AlcatelIND1LLDPMEDMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1LLDPMEDMIBCompliances = _AlcatelIND1LLDPMEDMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 58, 1, 2, 1)
)
_AlcatelIND1LLDPMEDMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1LLDPMEDMIBGroups = _AlcatelIND1LLDPMEDMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 58, 1, 2, 2)
)

# Managed Objects groups

alaLldpXMedLocMediaPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 58, 1, 2, 2, 1)
)
alaLldpXMedLocMediaPolicyGroup.setObjects(
      *(("ALCATEL-IND1-LLDP-MED-MIB", "alaLldpXMedLocMediaPolicyAppType"),
        ("ALCATEL-IND1-LLDP-MED-MIB", "alaLldpXMedLocMediaPolicyVlanType"),
        ("ALCATEL-IND1-LLDP-MED-MIB", "alaLldpXMedLocMediaPolicyVlanID"),
        ("ALCATEL-IND1-LLDP-MED-MIB", "alaLldpXMedLocMediaPolicyPriority"),
        ("ALCATEL-IND1-LLDP-MED-MIB", "alaLldpXMedLocMediaPolicyDscp"),
        ("ALCATEL-IND1-LLDP-MED-MIB", "alaLldpXMedLocMediaPolicyUnknown"),
        ("ALCATEL-IND1-LLDP-MED-MIB", "alaLldpXMedLocMediaPolicyTagged"),
        ("ALCATEL-IND1-LLDP-MED-MIB", "alaLldpXMedLocMediaPolicyRowStatus"),
        ("ALCATEL-IND1-LLDP-MED-MIB", "alaLldpXMedLocMediaPolicyPortRowStatus"))
)
if mibBuilder.loadTexts:
    alaLldpXMedLocMediaPolicyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1LLDPMEDMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 58, 1, 2, 1, 1)
)
alcatelIND1LLDPMEDMIBCompliance.setObjects(
    ("ALCATEL-IND1-LLDP-MED-MIB", "alaLldpXMedLocMediaPolicyGroup")
)
if mibBuilder.loadTexts:
    alcatelIND1LLDPMEDMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-LLDP-MED-MIB",
    **{"alcatelIND1LLDPMEDMIB": alcatelIND1LLDPMEDMIB,
       "alcatelIND1LLDPMEDMIBObjects": alcatelIND1LLDPMEDMIBObjects,
       "alaLldpMedLocMediaPolicyAttributes": alaLldpMedLocMediaPolicyAttributes,
       "alaLldpXMedLocMediaPolicyTable": alaLldpXMedLocMediaPolicyTable,
       "alaLldpXMedLocMediaPolicyEntry": alaLldpXMedLocMediaPolicyEntry,
       "alaLldpXMedLocMediaPolicyId": alaLldpXMedLocMediaPolicyId,
       "alaLldpXMedLocMediaPolicyAppType": alaLldpXMedLocMediaPolicyAppType,
       "alaLldpXMedLocMediaPolicyVlanType": alaLldpXMedLocMediaPolicyVlanType,
       "alaLldpXMedLocMediaPolicyVlanID": alaLldpXMedLocMediaPolicyVlanID,
       "alaLldpXMedLocMediaPolicyPriority": alaLldpXMedLocMediaPolicyPriority,
       "alaLldpXMedLocMediaPolicyDscp": alaLldpXMedLocMediaPolicyDscp,
       "alaLldpXMedLocMediaPolicyUnknown": alaLldpXMedLocMediaPolicyUnknown,
       "alaLldpXMedLocMediaPolicyTagged": alaLldpXMedLocMediaPolicyTagged,
       "alaLldpXMedLocMediaPolicyRowStatus": alaLldpXMedLocMediaPolicyRowStatus,
       "alaLldpXMedLocMediaPolicyPortTable": alaLldpXMedLocMediaPolicyPortTable,
       "alaLldpXMedLocMediaPolicyPortEntry": alaLldpXMedLocMediaPolicyPortEntry,
       "alaLldpXMedLocMediaPolicyPortNumber": alaLldpXMedLocMediaPolicyPortNumber,
       "alaLldpXMedLocMediaPolicyPortRowStatus": alaLldpXMedLocMediaPolicyPortRowStatus,
       "alcatelIND1LLDPMEDMIBConformance": alcatelIND1LLDPMEDMIBConformance,
       "alcatelIND1LLDPMEDMIBCompliances": alcatelIND1LLDPMEDMIBCompliances,
       "alcatelIND1LLDPMEDMIBCompliance": alcatelIND1LLDPMEDMIBCompliance,
       "alcatelIND1LLDPMEDMIBGroups": alcatelIND1LLDPMEDMIBGroups,
       "alaLldpXMedLocMediaPolicyGroup": alaLldpXMedLocMediaPolicyGroup}
)
