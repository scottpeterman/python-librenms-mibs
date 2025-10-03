# SNMP MIB module (CORERO-CMS-CLUSTERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\corero\CORERO-CMS-CLUSTERS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:31 2025
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

(coreroCMSMIBCompliances,
 coreroCMSMIBGroups,
 coreroCMSMIBObjects) = mibBuilder.importSymbols(
    "CORERO-CMS-MIB",
    "coreroCMSMIBCompliances",
    "coreroCMSMIBGroups",
    "coreroCMSMIBObjects")

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
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

clusters = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 3)
)
if mibBuilder.loadTexts:
    clusters.setRevisions(
        ("2017-08-24 00:00",
         "2018-05-03 00:00",
         "2018-05-23 00:00",
         "2018-06-29 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ClusterTable_Object = MibTable
clusterTable = _ClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    clusterTable.setStatus("current")
_ClusterEntry_Object = MibTableRow
clusterEntry = _ClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 3, 1, 1)
)
clusterEntry.setIndexNames(
    (0, "CORERO-CMS-CLUSTERS-MIB", "clusterIndex"),
)
if mibBuilder.loadTexts:
    clusterEntry.setStatus("current")


class _ClusterIndex_Type(Integer32):
    """Custom type clusterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClusterIndex_Type.__name__ = "Integer32"
_ClusterIndex_Object = MibTableColumn
clusterIndex = _ClusterIndex_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 3, 1, 1, 1),
    _ClusterIndex_Type()
)
clusterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterIndex.setStatus("current")


class _ClusterName_Type(OctetString):
    """Custom type clusterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ClusterName_Type.__name__ = "OctetString"
_ClusterName_Object = MibTableColumn
clusterName = _ClusterName_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 3, 1, 1, 2),
    _ClusterName_Type()
)
clusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterName.setStatus("current")
_ClusterDescription_Type = OctetString
_ClusterDescription_Object = MibTableColumn
clusterDescription = _ClusterDescription_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 3, 1, 1, 3),
    _ClusterDescription_Type()
)
clusterDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterDescription.setStatus("current")
_ClusterProtectionProfile_Type = OctetString
_ClusterProtectionProfile_Object = MibTableColumn
clusterProtectionProfile = _ClusterProtectionProfile_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 3, 1, 1, 4),
    _ClusterProtectionProfile_Type()
)
clusterProtectionProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterProtectionProfile.setStatus("current")


class _ClusterIngressSampleRate_Type(Integer32):
    """Custom type clusterIngressSampleRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_ClusterIngressSampleRate_Type.__name__ = "Integer32"
_ClusterIngressSampleRate_Object = MibTableColumn
clusterIngressSampleRate = _ClusterIngressSampleRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 3, 1, 1, 5),
    _ClusterIngressSampleRate_Type()
)
clusterIngressSampleRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterIngressSampleRate.setStatus("current")


class _ClusterOptimizeForScrubbing_Type(Integer32):
    """Custom type clusterOptimizeForScrubbing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_ClusterOptimizeForScrubbing_Type.__name__ = "Integer32"
_ClusterOptimizeForScrubbing_Object = MibTableColumn
clusterOptimizeForScrubbing = _ClusterOptimizeForScrubbing_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 3, 1, 1, 6),
    _ClusterOptimizeForScrubbing_Type()
)
clusterOptimizeForScrubbing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterOptimizeForScrubbing.setStatus("current")

# Managed Objects groups

coreroClusterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 41036, 4, 2, 2, 3)
)
coreroClusterGroup.setObjects(
      *(("CORERO-CMS-CLUSTERS-MIB", "clusterIndex"),
        ("CORERO-CMS-CLUSTERS-MIB", "clusterName"),
        ("CORERO-CMS-CLUSTERS-MIB", "clusterDescription"),
        ("CORERO-CMS-CLUSTERS-MIB", "clusterProtectionProfile"),
        ("CORERO-CMS-CLUSTERS-MIB", "clusterIngressSampleRate"),
        ("CORERO-CMS-CLUSTERS-MIB", "clusterOptimizeForScrubbing"))
)
if mibBuilder.loadTexts:
    coreroClusterGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

coreroCMSMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 41036, 4, 2, 1, 3)
)
coreroCMSMIBCompliance.setObjects(
    ("CORERO-CMS-CLUSTERS-MIB", "coreroClusterGroup")
)
if mibBuilder.loadTexts:
    coreroCMSMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CORERO-CMS-CLUSTERS-MIB",
    **{"clusters": clusters,
       "clusterTable": clusterTable,
       "clusterEntry": clusterEntry,
       "clusterIndex": clusterIndex,
       "clusterName": clusterName,
       "clusterDescription": clusterDescription,
       "clusterProtectionProfile": clusterProtectionProfile,
       "clusterIngressSampleRate": clusterIngressSampleRate,
       "clusterOptimizeForScrubbing": clusterOptimizeForScrubbing,
       "coreroCMSMIBCompliance": coreroCMSMIBCompliance,
       "coreroClusterGroup": coreroClusterGroup}
)
