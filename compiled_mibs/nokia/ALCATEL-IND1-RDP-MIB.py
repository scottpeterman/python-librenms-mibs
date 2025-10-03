# SNMP MIB module (ALCATEL-IND1-RDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-RDP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:14:00 2025
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

(routingIND1RDP,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1RDP")

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

alcatelIND1RouterDiscoveryProtocolMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 11, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1RouterDiscoveryProtocolMIB.setRevisions(
        ("2007-04-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1RDPMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1RDPMIBObjects = _AlcatelIND1RDPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 11, 1, 1)
)
_AlaRDPConfig_ObjectIdentity = ObjectIdentity
alaRDPConfig = _AlaRDPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 11, 1, 1, 1)
)


class _AlaRDPStatus_Type(Integer32):
    """Custom type alaRDPStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AlaRDPStatus_Type.__name__ = "Integer32"
_AlaRDPStatus_Object = MibScalar
alaRDPStatus = _AlaRDPStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 11, 1, 1, 1, 1),
    _AlaRDPStatus_Type()
)
alaRDPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRDPStatus.setStatus("current")
_AlaRDPIfTable_Object = MibTable
alaRDPIfTable = _AlaRDPIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 11, 1, 1, 1, 20)
)
if mibBuilder.loadTexts:
    alaRDPIfTable.setStatus("current")
_AlaRDPIfEntry_Object = MibTableRow
alaRDPIfEntry = _AlaRDPIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 11, 1, 1, 1, 20, 1)
)
alaRDPIfEntry.setIndexNames(
    (0, "ALCATEL-IND1-RDP-MIB", "alaRDPIfAddr"),
)
if mibBuilder.loadTexts:
    alaRDPIfEntry.setStatus("current")
_AlaRDPIfAddr_Type = IpAddress
_AlaRDPIfAddr_Object = MibTableColumn
alaRDPIfAddr = _AlaRDPIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 11, 1, 1, 1, 20, 1, 1),
    _AlaRDPIfAddr_Type()
)
alaRDPIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRDPIfAddr.setStatus("current")


class _AlaRDPIfStatus_Type(Integer32):
    """Custom type alaRDPIfStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AlaRDPIfStatus_Type.__name__ = "Integer32"
_AlaRDPIfStatus_Object = MibTableColumn
alaRDPIfStatus = _AlaRDPIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 11, 1, 1, 1, 20, 1, 2),
    _AlaRDPIfStatus_Type()
)
alaRDPIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRDPIfStatus.setStatus("current")
_AlaRDPIfAdvtAddress_Type = IpAddress
_AlaRDPIfAdvtAddress_Object = MibTableColumn
alaRDPIfAdvtAddress = _AlaRDPIfAdvtAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 11, 1, 1, 1, 20, 1, 3),
    _AlaRDPIfAdvtAddress_Type()
)
alaRDPIfAdvtAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRDPIfAdvtAddress.setStatus("current")


class _AlaRDPIfMaxAdvtInterval_Type(Unsigned32):
    """Custom type alaRDPIfMaxAdvtInterval based on Unsigned32"""
    defaultValue = 600


_AlaRDPIfMaxAdvtInterval_Type.__name__ = "Unsigned32"
_AlaRDPIfMaxAdvtInterval_Object = MibTableColumn
alaRDPIfMaxAdvtInterval = _AlaRDPIfMaxAdvtInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 11, 1, 1, 1, 20, 1, 4),
    _AlaRDPIfMaxAdvtInterval_Type()
)
alaRDPIfMaxAdvtInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRDPIfMaxAdvtInterval.setStatus("current")
_AlaRDPIfMinAdvtInterval_Type = Unsigned32
_AlaRDPIfMinAdvtInterval_Object = MibTableColumn
alaRDPIfMinAdvtInterval = _AlaRDPIfMinAdvtInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 11, 1, 1, 1, 20, 1, 5),
    _AlaRDPIfMinAdvtInterval_Type()
)
alaRDPIfMinAdvtInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRDPIfMinAdvtInterval.setStatus("current")
_AlaRDPIfAdvLifeTime_Type = Unsigned32
_AlaRDPIfAdvLifeTime_Object = MibTableColumn
alaRDPIfAdvLifeTime = _AlaRDPIfAdvLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 11, 1, 1, 1, 20, 1, 6),
    _AlaRDPIfAdvLifeTime_Type()
)
alaRDPIfAdvLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRDPIfAdvLifeTime.setStatus("current")


class _AlaRDPIfPrefLevel_Type(Integer32):
    """Custom type alaRDPIfPrefLevel based on Integer32"""
    defaultValue = 0


_AlaRDPIfPrefLevel_Type.__name__ = "Integer32"
_AlaRDPIfPrefLevel_Object = MibTableColumn
alaRDPIfPrefLevel = _AlaRDPIfPrefLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 11, 1, 1, 1, 20, 1, 7),
    _AlaRDPIfPrefLevel_Type()
)
alaRDPIfPrefLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRDPIfPrefLevel.setStatus("current")


class _AlaRDPIfRowStatus_Type(RowStatus):
    """Custom type alaRDPIfRowStatus based on RowStatus"""
    defaultValue = 2


_AlaRDPIfRowStatus_Type.__name__ = "RowStatus"
_AlaRDPIfRowStatus_Object = MibTableColumn
alaRDPIfRowStatus = _AlaRDPIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 11, 1, 1, 1, 20, 1, 8),
    _AlaRDPIfRowStatus_Type()
)
alaRDPIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRDPIfRowStatus.setStatus("current")
_AlaRDPIfName_Type = DisplayString
_AlaRDPIfName_Object = MibTableColumn
alaRDPIfName = _AlaRDPIfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 11, 1, 1, 1, 20, 1, 9),
    _AlaRDPIfName_Type()
)
alaRDPIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRDPIfName.setStatus("current")


class _AlaRDPIPIfStatus_Type(Integer32):
    """Custom type alaRDPIPIfStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AlaRDPIPIfStatus_Type.__name__ = "Integer32"
_AlaRDPIPIfStatus_Object = MibTableColumn
alaRDPIPIfStatus = _AlaRDPIPIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 11, 1, 1, 1, 20, 1, 10),
    _AlaRDPIPIfStatus_Type()
)
alaRDPIPIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRDPIPIfStatus.setStatus("current")


class _AlaRDPVrrpStatus_Type(Integer32):
    """Custom type alaRDPVrrpStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AlaRDPVrrpStatus_Type.__name__ = "Integer32"
_AlaRDPVrrpStatus_Object = MibTableColumn
alaRDPVrrpStatus = _AlaRDPVrrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 11, 1, 1, 1, 20, 1, 11),
    _AlaRDPVrrpStatus_Type()
)
alaRDPVrrpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRDPVrrpStatus.setStatus("current")
_AlcatelIND1RDPMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1RDPMIBConformance = _AlcatelIND1RDPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 11, 1, 2)
)
_AlcatelIND1RDPMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1RDPMIBCompliances = _AlcatelIND1RDPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 11, 1, 2, 1)
)
_AlcatelIND1RDPMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1RDPMIBGroups = _AlcatelIND1RDPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 11, 1, 2, 2)
)

# Managed Objects groups

alaRDPConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 11, 1, 2, 2, 1)
)
alaRDPConfigMIBGroup.setObjects(
      *(("ALCATEL-IND1-RDP-MIB", "alaRDPStatus"),
        ("ALCATEL-IND1-RDP-MIB", "alaRDPIfAddr"),
        ("ALCATEL-IND1-RDP-MIB", "alaRDPIfStatus"),
        ("ALCATEL-IND1-RDP-MIB", "alaRDPIfAdvtAddress"),
        ("ALCATEL-IND1-RDP-MIB", "alaRDPIfMaxAdvtInterval"),
        ("ALCATEL-IND1-RDP-MIB", "alaRDPIfMinAdvtInterval"),
        ("ALCATEL-IND1-RDP-MIB", "alaRDPIfAdvLifeTime"),
        ("ALCATEL-IND1-RDP-MIB", "alaRDPIfPrefLevel"),
        ("ALCATEL-IND1-RDP-MIB", "alaRDPIfRowStatus"),
        ("ALCATEL-IND1-RDP-MIB", "alaRDPIfName"),
        ("ALCATEL-IND1-RDP-MIB", "alaRDPIPIfStatus"),
        ("ALCATEL-IND1-RDP-MIB", "alaRDPVrrpStatus"))
)
if mibBuilder.loadTexts:
    alaRDPConfigMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1RDPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 11, 1, 2, 1, 1)
)
alcatelIND1RDPMIBCompliance.setObjects(
    ("ALCATEL-IND1-RDP-MIB", "alaRDPConfigMIBGroup")
)
if mibBuilder.loadTexts:
    alcatelIND1RDPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-RDP-MIB",
    **{"alcatelIND1RouterDiscoveryProtocolMIB": alcatelIND1RouterDiscoveryProtocolMIB,
       "alcatelIND1RDPMIBObjects": alcatelIND1RDPMIBObjects,
       "alaRDPConfig": alaRDPConfig,
       "alaRDPStatus": alaRDPStatus,
       "alaRDPIfTable": alaRDPIfTable,
       "alaRDPIfEntry": alaRDPIfEntry,
       "alaRDPIfAddr": alaRDPIfAddr,
       "alaRDPIfStatus": alaRDPIfStatus,
       "alaRDPIfAdvtAddress": alaRDPIfAdvtAddress,
       "alaRDPIfMaxAdvtInterval": alaRDPIfMaxAdvtInterval,
       "alaRDPIfMinAdvtInterval": alaRDPIfMinAdvtInterval,
       "alaRDPIfAdvLifeTime": alaRDPIfAdvLifeTime,
       "alaRDPIfPrefLevel": alaRDPIfPrefLevel,
       "alaRDPIfRowStatus": alaRDPIfRowStatus,
       "alaRDPIfName": alaRDPIfName,
       "alaRDPIPIfStatus": alaRDPIPIfStatus,
       "alaRDPVrrpStatus": alaRDPVrrpStatus,
       "alcatelIND1RDPMIBConformance": alcatelIND1RDPMIBConformance,
       "alcatelIND1RDPMIBCompliances": alcatelIND1RDPMIBCompliances,
       "alcatelIND1RDPMIBCompliance": alcatelIND1RDPMIBCompliance,
       "alcatelIND1RDPMIBGroups": alcatelIND1RDPMIBGroups,
       "alaRDPConfigMIBGroup": alaRDPConfigMIBGroup}
)
