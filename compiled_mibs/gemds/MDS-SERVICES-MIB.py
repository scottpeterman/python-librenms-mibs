# SNMP MIB module (MDS-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\gemds\MDS-SERVICES-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:47:37 2025
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

(mdsServices,) = mibBuilder.importSymbols(
    "MDS-ORBIT-SMI-MIB",
    "mdsServices")

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

mdsServicesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 1)
)
if mibBuilder.loadTexts:
    mdsServicesMIB.setRevisions(
        ("2018-05-16 00:00",
         "2014-10-20 00:00",
         "2014-05-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MServMIBObjects_ObjectIdentity = ObjectIdentity
mServMIBObjects = _MServMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 1)
)
_MServConfig_ObjectIdentity = ObjectIdentity
mServConfig = _MServConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 1, 1)
)
_MServStatus_ObjectIdentity = ObjectIdentity
mServStatus = _MServStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 1, 2)
)
_MServStatusTable_Object = MibTable
mServStatusTable = _MServStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mServStatusTable.setStatus("current")
_MServStatusEntry_Object = MibTableRow
mServStatusEntry = _MServStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 1, 2, 1, 1)
)
mServStatusEntry.setIndexNames(
    (0, "MDS-SERVICES-MIB", "mServServiceName"),
)
if mibBuilder.loadTexts:
    mServStatusEntry.setStatus("current")
_MServServiceName_Type = OctetString
_MServServiceName_Object = MibTableColumn
mServServiceName = _MServServiceName_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 1, 2, 1, 1, 1),
    _MServServiceName_Type()
)
mServServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mServServiceName.setStatus("current")


class _MServServiceStatus_Type(Integer32):
    """Custom type mServServiceStatus based on Integer32"""
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
        *(("running", 0),
          ("disabled", 1),
          ("error", 2),
          ("notRunning", 3))
    )


_MServServiceStatus_Type.__name__ = "Integer32"
_MServServiceStatus_Object = MibTableColumn
mServServiceStatus = _MServServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 1, 2, 1, 1, 2),
    _MServServiceStatus_Type()
)
mServServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mServServiceStatus.setStatus("current")
_MdsServMIBConformance_ObjectIdentity = ObjectIdentity
mdsServMIBConformance = _MdsServMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 3)
)
_MdsServMIBCompliances_ObjectIdentity = ObjectIdentity
mdsServMIBCompliances = _MdsServMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 3, 1)
)
_MdsServMIBGroups_ObjectIdentity = ObjectIdentity
mdsServMIBGroups = _MdsServMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 3, 2)
)

# Managed Objects groups

mServStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 3, 2, 1)
)
mServStatusGroup.setObjects(
      *(("MDS-SERVICES-MIB", "mServServiceName"),
        ("MDS-SERVICES-MIB", "mServServiceStatus"))
)
if mibBuilder.loadTexts:
    mServStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mServCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 3, 1, 1)
)
mServCompliance.setObjects(
    ("MDS-SERVICES-MIB", "mServStatusGroup")
)
if mibBuilder.loadTexts:
    mServCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MDS-SERVICES-MIB",
    **{"mdsServicesMIB": mdsServicesMIB,
       "mServMIBObjects": mServMIBObjects,
       "mServConfig": mServConfig,
       "mServStatus": mServStatus,
       "mServStatusTable": mServStatusTable,
       "mServStatusEntry": mServStatusEntry,
       "mServServiceName": mServServiceName,
       "mServServiceStatus": mServServiceStatus,
       "mdsServMIBConformance": mdsServMIBConformance,
       "mdsServMIBCompliances": mdsServMIBCompliances,
       "mServCompliance": mServCompliance,
       "mdsServMIBGroups": mdsServMIBGroups,
       "mServStatusGroup": mServStatusGroup}
)
