# SNMP MIB module (ARUBAWIRED-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-INTERFACE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:08 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

arubaWiredInterfaceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24)
)
if mibBuilder.loadTexts:
    arubaWiredInterfaceMIB.setRevisions(
        ("2023-09-13 00:00",
         "2021-11-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArubaWiredInterfaceSettings_ObjectIdentity = ObjectIdentity
arubaWiredInterfaceSettings = _ArubaWiredInterfaceSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1)
)
_ArubaWiredInterfaceTable_Object = MibTable
arubaWiredInterfaceTable = _ArubaWiredInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 1)
)
if mibBuilder.loadTexts:
    arubaWiredInterfaceTable.setStatus("current")
_ArubaWiredInterfaceEntry_Object = MibTableRow
arubaWiredInterfaceEntry = _ArubaWiredInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 1, 1)
)
arubaWiredInterfaceEntry.setIndexNames(
    (0, "ARUBAWIRED-INTERFACE-MIB", "arubaWiredInterfaceIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredInterfaceEntry.setStatus("current")
_ArubaWiredInterfaceIndex_Type = InterfaceIndex
_ArubaWiredInterfaceIndex_Object = MibTableColumn
arubaWiredInterfaceIndex = _ArubaWiredInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 1, 1, 1),
    _ArubaWiredInterfaceIndex_Type()
)
arubaWiredInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredInterfaceIndex.setStatus("current")


class _ArubaWiredInterfaceAutoneg_Type(Integer32):
    """Custom type arubaWiredInterfaceAutoneg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_ArubaWiredInterfaceAutoneg_Type.__name__ = "Integer32"
_ArubaWiredInterfaceAutoneg_Object = MibTableColumn
arubaWiredInterfaceAutoneg = _ArubaWiredInterfaceAutoneg_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 1, 1, 2),
    _ArubaWiredInterfaceAutoneg_Type()
)
arubaWiredInterfaceAutoneg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredInterfaceAutoneg.setStatus("current")


class _ArubaWiredInterfaceDuplex_Type(Integer32):
    """Custom type arubaWiredInterfaceDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_ArubaWiredInterfaceDuplex_Type.__name__ = "Integer32"
_ArubaWiredInterfaceDuplex_Object = MibTableColumn
arubaWiredInterfaceDuplex = _ArubaWiredInterfaceDuplex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 1, 1, 3),
    _ArubaWiredInterfaceDuplex_Type()
)
arubaWiredInterfaceDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredInterfaceDuplex.setStatus("current")


class _ArubaWiredInterfaceSpeeds_Type(Bits):
    """Custom type arubaWiredInterfaceSpeeds based on Bits"""
    namedValues = NamedValues(
        *(("speed10M", 0),
          ("speed100M", 1),
          ("speed1G", 2),
          ("speed2p5G", 3),
          ("speed5G", 4),
          ("speed10G", 5),
          ("speed25G", 6),
          ("speed40G", 7),
          ("speed50G", 8),
          ("speed100G", 9),
          ("speed200G", 10),
          ("speed400G", 11),
          ("speed800G", 12))
    )

_ArubaWiredInterfaceSpeeds_Type.__name__ = "Bits"
_ArubaWiredInterfaceSpeeds_Object = MibTableColumn
arubaWiredInterfaceSpeeds = _ArubaWiredInterfaceSpeeds_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 1, 1, 4),
    _ArubaWiredInterfaceSpeeds_Type()
)
arubaWiredInterfaceSpeeds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredInterfaceSpeeds.setStatus("current")
_ArubaWiredIfRateTable_Object = MibTable
arubaWiredIfRateTable = _ArubaWiredIfRateTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 2)
)
if mibBuilder.loadTexts:
    arubaWiredIfRateTable.setStatus("current")
_ArubaWiredIfRateEntry_Object = MibTableRow
arubaWiredIfRateEntry = _ArubaWiredIfRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 2, 1)
)
arubaWiredIfRateEntry.setIndexNames(
    (0, "ARUBAWIRED-INTERFACE-MIB", "arubaWiredIfRateIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredIfRateEntry.setStatus("current")
_ArubaWiredIfRateIndex_Type = InterfaceIndex
_ArubaWiredIfRateIndex_Object = MibTableColumn
arubaWiredIfRateIndex = _ArubaWiredIfRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 2, 1, 1),
    _ArubaWiredIfRateIndex_Type()
)
arubaWiredIfRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredIfRateIndex.setStatus("current")
_ArubaWiredIfRateInterval_Type = TimeTicks
_ArubaWiredIfRateInterval_Object = MibTableColumn
arubaWiredIfRateInterval = _ArubaWiredIfRateInterval_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 2, 1, 2),
    _ArubaWiredIfRateInterval_Type()
)
arubaWiredIfRateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredIfRateInterval.setStatus("current")
_ArubaWiredIfRateInBytes_Type = Gauge32
_ArubaWiredIfRateInBytes_Object = MibTableColumn
arubaWiredIfRateInBytes = _ArubaWiredIfRateInBytes_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 2, 1, 3),
    _ArubaWiredIfRateInBytes_Type()
)
arubaWiredIfRateInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredIfRateInBytes.setStatus("current")
_ArubaWiredIfRateOutBytes_Type = Gauge32
_ArubaWiredIfRateOutBytes_Object = MibTableColumn
arubaWiredIfRateOutBytes = _ArubaWiredIfRateOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 2, 1, 4),
    _ArubaWiredIfRateOutBytes_Type()
)
arubaWiredIfRateOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredIfRateOutBytes.setStatus("current")
_ArubaWiredIfRateInBcastPkts_Type = Gauge32
_ArubaWiredIfRateInBcastPkts_Object = MibTableColumn
arubaWiredIfRateInBcastPkts = _ArubaWiredIfRateInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 2, 1, 5),
    _ArubaWiredIfRateInBcastPkts_Type()
)
arubaWiredIfRateInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredIfRateInBcastPkts.setStatus("current")
_ArubaWiredIfRateInMcastPkts_Type = Gauge32
_ArubaWiredIfRateInMcastPkts_Object = MibTableColumn
arubaWiredIfRateInMcastPkts = _ArubaWiredIfRateInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 2, 1, 6),
    _ArubaWiredIfRateInMcastPkts_Type()
)
arubaWiredIfRateInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredIfRateInMcastPkts.setStatus("current")
_ArubaWiredIfRateInUcastPkts_Type = Gauge32
_ArubaWiredIfRateInUcastPkts_Object = MibTableColumn
arubaWiredIfRateInUcastPkts = _ArubaWiredIfRateInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 2, 1, 7),
    _ArubaWiredIfRateInUcastPkts_Type()
)
arubaWiredIfRateInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredIfRateInUcastPkts.setStatus("current")
_ArubaWiredIfRateInTotalPkts_Type = Gauge32
_ArubaWiredIfRateInTotalPkts_Object = MibTableColumn
arubaWiredIfRateInTotalPkts = _ArubaWiredIfRateInTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 2, 1, 8),
    _ArubaWiredIfRateInTotalPkts_Type()
)
arubaWiredIfRateInTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredIfRateInTotalPkts.setStatus("current")
_ArubaWiredIfRateOutBcastPkts_Type = Gauge32
_ArubaWiredIfRateOutBcastPkts_Object = MibTableColumn
arubaWiredIfRateOutBcastPkts = _ArubaWiredIfRateOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 2, 1, 9),
    _ArubaWiredIfRateOutBcastPkts_Type()
)
arubaWiredIfRateOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredIfRateOutBcastPkts.setStatus("current")
_ArubaWiredIfRateOutMcastPkts_Type = Gauge32
_ArubaWiredIfRateOutMcastPkts_Object = MibTableColumn
arubaWiredIfRateOutMcastPkts = _ArubaWiredIfRateOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 2, 1, 10),
    _ArubaWiredIfRateOutMcastPkts_Type()
)
arubaWiredIfRateOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredIfRateOutMcastPkts.setStatus("current")
_ArubaWiredIfRateOutUcastPkts_Type = Gauge32
_ArubaWiredIfRateOutUcastPkts_Object = MibTableColumn
arubaWiredIfRateOutUcastPkts = _ArubaWiredIfRateOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 2, 1, 11),
    _ArubaWiredIfRateOutUcastPkts_Type()
)
arubaWiredIfRateOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredIfRateOutUcastPkts.setStatus("current")
_ArubaWiredIfRateOutTotalPkts_Type = Gauge32
_ArubaWiredIfRateOutTotalPkts_Object = MibTableColumn
arubaWiredIfRateOutTotalPkts = _ArubaWiredIfRateOutTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 2, 1, 12),
    _ArubaWiredIfRateOutTotalPkts_Type()
)
arubaWiredIfRateOutTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredIfRateOutTotalPkts.setStatus("current")


class _ArubaWiredIfRateInUtilization_Type(Integer32):
    """Custom type arubaWiredIfRateInUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ArubaWiredIfRateInUtilization_Type.__name__ = "Integer32"
_ArubaWiredIfRateInUtilization_Object = MibTableColumn
arubaWiredIfRateInUtilization = _ArubaWiredIfRateInUtilization_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 2, 1, 13),
    _ArubaWiredIfRateInUtilization_Type()
)
arubaWiredIfRateInUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredIfRateInUtilization.setStatus("current")


class _ArubaWiredIfRateOutUtilization_Type(Integer32):
    """Custom type arubaWiredIfRateOutUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ArubaWiredIfRateOutUtilization_Type.__name__ = "Integer32"
_ArubaWiredIfRateOutUtilization_Object = MibTableColumn
arubaWiredIfRateOutUtilization = _ArubaWiredIfRateOutUtilization_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 2, 1, 14),
    _ArubaWiredIfRateOutUtilization_Type()
)
arubaWiredIfRateOutUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredIfRateOutUtilization.setStatus("current")
_ArubaWiredInterfaceConformance_ObjectIdentity = ObjectIdentity
arubaWiredInterfaceConformance = _ArubaWiredInterfaceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 2)
)
_ArubaWiredInterfaceGroups_ObjectIdentity = ObjectIdentity
arubaWiredInterfaceGroups = _ArubaWiredInterfaceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 2, 1)
)
_ArubaWiredInterfaceCompliances_ObjectIdentity = ObjectIdentity
arubaWiredInterfaceCompliances = _ArubaWiredInterfaceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 2, 2)
)

# Managed Objects groups

arubaWiredInterfaceConfig = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 2, 1, 1)
)
arubaWiredInterfaceConfig.setObjects(
      *(("ARUBAWIRED-INTERFACE-MIB", "arubaWiredInterfaceAutoneg"),
        ("ARUBAWIRED-INTERFACE-MIB", "arubaWiredInterfaceDuplex"),
        ("ARUBAWIRED-INTERFACE-MIB", "arubaWiredInterfaceSpeeds"))
)
if mibBuilder.loadTexts:
    arubaWiredInterfaceConfig.setStatus("current")

arubaWiredIfRateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 2, 1, 2)
)
arubaWiredIfRateGroup.setObjects(
      *(("ARUBAWIRED-INTERFACE-MIB", "arubaWiredIfRateInterval"),
        ("ARUBAWIRED-INTERFACE-MIB", "arubaWiredIfRateInBytes"),
        ("ARUBAWIRED-INTERFACE-MIB", "arubaWiredIfRateOutBytes"),
        ("ARUBAWIRED-INTERFACE-MIB", "arubaWiredIfRateInBcastPkts"),
        ("ARUBAWIRED-INTERFACE-MIB", "arubaWiredIfRateInMcastPkts"),
        ("ARUBAWIRED-INTERFACE-MIB", "arubaWiredIfRateInUcastPkts"),
        ("ARUBAWIRED-INTERFACE-MIB", "arubaWiredIfRateInTotalPkts"),
        ("ARUBAWIRED-INTERFACE-MIB", "arubaWiredIfRateOutBcastPkts"),
        ("ARUBAWIRED-INTERFACE-MIB", "arubaWiredIfRateOutMcastPkts"),
        ("ARUBAWIRED-INTERFACE-MIB", "arubaWiredIfRateOutUcastPkts"),
        ("ARUBAWIRED-INTERFACE-MIB", "arubaWiredIfRateOutTotalPkts"),
        ("ARUBAWIRED-INTERFACE-MIB", "arubaWiredIfRateInUtilization"),
        ("ARUBAWIRED-INTERFACE-MIB", "arubaWiredIfRateOutUtilization"))
)
if mibBuilder.loadTexts:
    arubaWiredIfRateGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

arubaWiredInterfaceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 2, 2, 1)
)
arubaWiredInterfaceCompliance.setObjects(
    ("ARUBAWIRED-INTERFACE-MIB", "arubaWiredInterfaceConfig")
)
if mibBuilder.loadTexts:
    arubaWiredInterfaceCompliance.setStatus(
        "current"
    )

arubaWiredIfRateCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 2, 2, 2)
)
arubaWiredIfRateCompliance.setObjects(
    ("ARUBAWIRED-INTERFACE-MIB", "arubaWiredIfRateGroup")
)
if mibBuilder.loadTexts:
    arubaWiredIfRateCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-INTERFACE-MIB",
    **{"arubaWiredInterfaceMIB": arubaWiredInterfaceMIB,
       "arubaWiredInterfaceSettings": arubaWiredInterfaceSettings,
       "arubaWiredInterfaceTable": arubaWiredInterfaceTable,
       "arubaWiredInterfaceEntry": arubaWiredInterfaceEntry,
       "arubaWiredInterfaceIndex": arubaWiredInterfaceIndex,
       "arubaWiredInterfaceAutoneg": arubaWiredInterfaceAutoneg,
       "arubaWiredInterfaceDuplex": arubaWiredInterfaceDuplex,
       "arubaWiredInterfaceSpeeds": arubaWiredInterfaceSpeeds,
       "arubaWiredIfRateTable": arubaWiredIfRateTable,
       "arubaWiredIfRateEntry": arubaWiredIfRateEntry,
       "arubaWiredIfRateIndex": arubaWiredIfRateIndex,
       "arubaWiredIfRateInterval": arubaWiredIfRateInterval,
       "arubaWiredIfRateInBytes": arubaWiredIfRateInBytes,
       "arubaWiredIfRateOutBytes": arubaWiredIfRateOutBytes,
       "arubaWiredIfRateInBcastPkts": arubaWiredIfRateInBcastPkts,
       "arubaWiredIfRateInMcastPkts": arubaWiredIfRateInMcastPkts,
       "arubaWiredIfRateInUcastPkts": arubaWiredIfRateInUcastPkts,
       "arubaWiredIfRateInTotalPkts": arubaWiredIfRateInTotalPkts,
       "arubaWiredIfRateOutBcastPkts": arubaWiredIfRateOutBcastPkts,
       "arubaWiredIfRateOutMcastPkts": arubaWiredIfRateOutMcastPkts,
       "arubaWiredIfRateOutUcastPkts": arubaWiredIfRateOutUcastPkts,
       "arubaWiredIfRateOutTotalPkts": arubaWiredIfRateOutTotalPkts,
       "arubaWiredIfRateInUtilization": arubaWiredIfRateInUtilization,
       "arubaWiredIfRateOutUtilization": arubaWiredIfRateOutUtilization,
       "arubaWiredInterfaceConformance": arubaWiredInterfaceConformance,
       "arubaWiredInterfaceGroups": arubaWiredInterfaceGroups,
       "arubaWiredInterfaceConfig": arubaWiredInterfaceConfig,
       "arubaWiredIfRateGroup": arubaWiredIfRateGroup,
       "arubaWiredInterfaceCompliances": arubaWiredInterfaceCompliances,
       "arubaWiredInterfaceCompliance": arubaWiredInterfaceCompliance,
       "arubaWiredIfRateCompliance": arubaWiredIfRateCompliance}
)
