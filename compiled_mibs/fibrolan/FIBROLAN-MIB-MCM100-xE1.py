# SNMP MIB module (FIBROLAN-MIB-MCM100-xE1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fibrolan\FIBROLAN-MIB-MCM100-xE1
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:24 2025
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

(flMsChassisModuleMvEntry,
 flMsChassisModuleMvIndex,
 flMsChassisMvIndex) = mibBuilder.importSymbols(
    "FIBROLAN-MIB-METRO-STAR-MV",
    "flMsChassisModuleMvEntry",
    "flMsChassisModuleMvIndex",
    "flMsChassisMvIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

flMcm100xE1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 200)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fibrolan_ObjectIdentity = ObjectIdentity
fibrolan = _Fibrolan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467)
)
_FibrolanSNMP_ObjectIdentity = ObjectIdentity
fibrolanSNMP = _FibrolanSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100)
)
_FlMetroStarMv_ObjectIdentity = ObjectIdentity
flMetroStarMv = _FlMetroStarMv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500)
)
_FlMsChassisMv_ObjectIdentity = ObjectIdentity
flMsChassisMv = _FlMsChassisMv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10)
)
_FlMsModuleMv_ObjectIdentity = ObjectIdentity
flMsModuleMv = _FlMsModuleMv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30)
)
_FlMcm1xxMv_ObjectIdentity = ObjectIdentity
flMcm1xxMv = _FlMcm1xxMv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100)
)
_FlMcm100xE1MIBConformance_ObjectIdentity = ObjectIdentity
flMcm100xE1MIBConformance = _FlMcm100xE1MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 200, 1)
)
_FlMsMcm100xE1MIBCompliances_ObjectIdentity = ObjectIdentity
flMsMcm100xE1MIBCompliances = _FlMsMcm100xE1MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 200, 1, 1)
)
_FlMsMcm100xE1MIBGroups_ObjectIdentity = ObjectIdentity
flMsMcm100xE1MIBGroups = _FlMsMcm100xE1MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 200, 1, 2)
)
_FlMcm100xE1Ports_ObjectIdentity = ObjectIdentity
flMcm100xE1Ports = _FlMcm100xE1Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 200, 10)
)
_FlMcm100xE1PortsGeneralTable_Object = MibTable
flMcm100xE1PortsGeneralTable = _FlMcm100xE1PortsGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 200, 10, 1)
)
if mibBuilder.loadTexts:
    flMcm100xE1PortsGeneralTable.setStatus("current")
_FlMcm100xE1PortsEntry_Object = MibTableRow
flMcm100xE1PortsEntry = _FlMcm100xE1PortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 200, 10, 1, 1)
)
if mibBuilder.loadTexts:
    flMcm100xE1PortsEntry.setStatus("current")


class _FlMsMcm100xE1ResetPorts_Type(Integer32):
    """Custom type flMsMcm100xE1ResetPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_FlMsMcm100xE1ResetPorts_Type.__name__ = "Integer32"
_FlMsMcm100xE1ResetPorts_Object = MibTableColumn
flMsMcm100xE1ResetPorts = _FlMsMcm100xE1ResetPorts_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 200, 10, 1, 1, 1),
    _FlMsMcm100xE1ResetPorts_Type()
)
flMsMcm100xE1ResetPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsMcm100xE1ResetPorts.setStatus("current")


class _FlMsMcm100xE1RestorePortsDef_Type(Integer32):
    """Custom type flMsMcm100xE1RestorePortsDef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("restore", 2))
    )


_FlMsMcm100xE1RestorePortsDef_Type.__name__ = "Integer32"
_FlMsMcm100xE1RestorePortsDef_Object = MibTableColumn
flMsMcm100xE1RestorePortsDef = _FlMsMcm100xE1RestorePortsDef_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 200, 10, 1, 1, 2),
    _FlMsMcm100xE1RestorePortsDef_Type()
)
flMsMcm100xE1RestorePortsDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsMcm100xE1RestorePortsDef.setStatus("current")
_FlMcm100xE1PortsStatusTable_Object = MibTable
flMcm100xE1PortsStatusTable = _FlMcm100xE1PortsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 200, 10, 2)
)
if mibBuilder.loadTexts:
    flMcm100xE1PortsStatusTable.setStatus("current")
_FlMcm100xE1PortsStatusEntry_Object = MibTableRow
flMcm100xE1PortsStatusEntry = _FlMcm100xE1PortsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 200, 10, 2, 1)
)
flMcm100xE1PortsStatusEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MCM100-xE1", "flMsMcm100xE1PortIndex"),
)
if mibBuilder.loadTexts:
    flMcm100xE1PortsStatusEntry.setStatus("current")


class _FlMsMcm100xE1PortIndex_Type(Integer32):
    """Custom type flMsMcm100xE1PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FlMsMcm100xE1PortIndex_Type.__name__ = "Integer32"
_FlMsMcm100xE1PortIndex_Object = MibTableColumn
flMsMcm100xE1PortIndex = _FlMsMcm100xE1PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 200, 10, 2, 1, 1),
    _FlMsMcm100xE1PortIndex_Type()
)
flMsMcm100xE1PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsMcm100xE1PortIndex.setStatus("current")


class _FlMsMcm100xE1Signal_Type(Integer32):
    """Custom type flMsMcm100xE1Signal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("los", 1),
          ("on", 2))
    )


_FlMsMcm100xE1Signal_Type.__name__ = "Integer32"
_FlMsMcm100xE1Signal_Object = MibTableColumn
flMsMcm100xE1Signal = _FlMsMcm100xE1Signal_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 200, 10, 2, 1, 2),
    _FlMsMcm100xE1Signal_Type()
)
flMsMcm100xE1Signal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsMcm100xE1Signal.setStatus("current")


class _FlMsMcm100xE1RemoteSignal_Type(Integer32):
    """Custom type flMsMcm100xE1RemoteSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("los", 1),
          ("on", 2))
    )


_FlMsMcm100xE1RemoteSignal_Type.__name__ = "Integer32"
_FlMsMcm100xE1RemoteSignal_Object = MibTableColumn
flMsMcm100xE1RemoteSignal = _FlMsMcm100xE1RemoteSignal_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 200, 10, 2, 1, 3),
    _FlMsMcm100xE1RemoteSignal_Type()
)
flMsMcm100xE1RemoteSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsMcm100xE1RemoteSignal.setStatus("current")


class _FlMsMcm100xE1Ais_Type(Integer32):
    """Custom type flMsMcm100xE1Ais based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FlMsMcm100xE1Ais_Type.__name__ = "Integer32"
_FlMsMcm100xE1Ais_Object = MibTableColumn
flMsMcm100xE1Ais = _FlMsMcm100xE1Ais_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 200, 10, 2, 1, 4),
    _FlMsMcm100xE1Ais_Type()
)
flMsMcm100xE1Ais.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsMcm100xE1Ais.setStatus("current")


class _FlMsMcm100xE1Output_Type(Integer32):
    """Custom type flMsMcm100xE1Output based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlMsMcm100xE1Output_Type.__name__ = "Integer32"
_FlMsMcm100xE1Output_Object = MibTableColumn
flMsMcm100xE1Output = _FlMsMcm100xE1Output_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 200, 10, 2, 1, 5),
    _FlMsMcm100xE1Output_Type()
)
flMsMcm100xE1Output.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsMcm100xE1Output.setStatus("current")


class _FlMsMcm100xE1Input_Type(Integer32):
    """Custom type flMsMcm100xE1Input based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlMsMcm100xE1Input_Type.__name__ = "Integer32"
_FlMsMcm100xE1Input_Object = MibTableColumn
flMsMcm100xE1Input = _FlMsMcm100xE1Input_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 200, 10, 2, 1, 6),
    _FlMsMcm100xE1Input_Type()
)
flMsMcm100xE1Input.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsMcm100xE1Input.setStatus("current")


class _FlMsMcm100xE1Taos_Type(Integer32):
    """Custom type flMsMcm100xE1Taos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FlMsMcm100xE1Taos_Type.__name__ = "Integer32"
_FlMsMcm100xE1Taos_Object = MibTableColumn
flMsMcm100xE1Taos = _FlMsMcm100xE1Taos_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 200, 10, 2, 1, 7),
    _FlMsMcm100xE1Taos_Type()
)
flMsMcm100xE1Taos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsMcm100xE1Taos.setStatus("current")


class _FlMsMcm100xE1LocalLoopback_Type(Integer32):
    """Custom type flMsMcm100xE1LocalLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FlMsMcm100xE1LocalLoopback_Type.__name__ = "Integer32"
_FlMsMcm100xE1LocalLoopback_Object = MibTableColumn
flMsMcm100xE1LocalLoopback = _FlMsMcm100xE1LocalLoopback_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 200, 10, 2, 1, 8),
    _FlMsMcm100xE1LocalLoopback_Type()
)
flMsMcm100xE1LocalLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsMcm100xE1LocalLoopback.setStatus("current")


class _FlMsMcm100xE1UserAnalogLB_Type(Integer32):
    """Custom type flMsMcm100xE1UserAnalogLB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FlMsMcm100xE1UserAnalogLB_Type.__name__ = "Integer32"
_FlMsMcm100xE1UserAnalogLB_Object = MibTableColumn
flMsMcm100xE1UserAnalogLB = _FlMsMcm100xE1UserAnalogLB_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 200, 10, 2, 1, 9),
    _FlMsMcm100xE1UserAnalogLB_Type()
)
flMsMcm100xE1UserAnalogLB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsMcm100xE1UserAnalogLB.setStatus("current")


class _FlMsMcm100xE1UserDigitalLB_Type(Integer32):
    """Custom type flMsMcm100xE1UserDigitalLB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FlMsMcm100xE1UserDigitalLB_Type.__name__ = "Integer32"
_FlMsMcm100xE1UserDigitalLB_Object = MibTableColumn
flMsMcm100xE1UserDigitalLB = _FlMsMcm100xE1UserDigitalLB_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 200, 10, 2, 1, 10),
    _FlMsMcm100xE1UserDigitalLB_Type()
)
flMsMcm100xE1UserDigitalLB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsMcm100xE1UserDigitalLB.setStatus("current")
_FlMsMcm100xE1PortDescription_Type = DisplayString
_FlMsMcm100xE1PortDescription_Object = MibTableColumn
flMsMcm100xE1PortDescription = _FlMsMcm100xE1PortDescription_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 200, 10, 2, 1, 11),
    _FlMsMcm100xE1PortDescription_Type()
)
flMsMcm100xE1PortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsMcm100xE1PortDescription.setStatus("current")
flMsChassisModuleMvEntry.registerAugmentions(
    ("FIBROLAN-MIB-MCM100-xE1",
     "flMcm100xE1PortsEntry")
)
flMcm100xE1PortsEntry.setIndexNames(*flMsChassisModuleMvEntry.getIndexNames())

# Managed Objects groups

flMsMcm100xE1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 200, 1, 2, 1)
)
flMsMcm100xE1Group.setObjects(
      *(("FIBROLAN-MIB-MCM100-xE1", "flMsMcm100xE1ResetPorts"),
        ("FIBROLAN-MIB-MCM100-xE1", "flMsMcm100xE1RestorePortsDef"))
)
if mibBuilder.loadTexts:
    flMsMcm100xE1Group.setStatus("current")

flMsMcm100xE1PortsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 200, 1, 2, 2)
)
flMsMcm100xE1PortsGroup.setObjects(
      *(("FIBROLAN-MIB-MCM100-xE1", "flMsMcm100xE1PortIndex"),
        ("FIBROLAN-MIB-MCM100-xE1", "flMsMcm100xE1Signal"),
        ("FIBROLAN-MIB-MCM100-xE1", "flMsMcm100xE1RemoteSignal"),
        ("FIBROLAN-MIB-MCM100-xE1", "flMsMcm100xE1Ais"),
        ("FIBROLAN-MIB-MCM100-xE1", "flMsMcm100xE1Output"),
        ("FIBROLAN-MIB-MCM100-xE1", "flMsMcm100xE1Input"),
        ("FIBROLAN-MIB-MCM100-xE1", "flMsMcm100xE1Taos"),
        ("FIBROLAN-MIB-MCM100-xE1", "flMsMcm100xE1LocalLoopback"),
        ("FIBROLAN-MIB-MCM100-xE1", "flMsMcm100xE1UserAnalogLB"),
        ("FIBROLAN-MIB-MCM100-xE1", "flMsMcm100xE1UserDigitalLB"),
        ("FIBROLAN-MIB-MCM100-xE1", "flMsMcm100xE1PortDescription"))
)
if mibBuilder.loadTexts:
    flMsMcm100xE1PortsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

flMcm100xE1MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 200, 1, 1, 1)
)
flMcm100xE1MIBCompliance.setObjects(
      *(("FIBROLAN-MIB-MCM1xx", "flMsMcm1xxMvGroup"),
        ("FIBROLAN-MIB-MCM100-xE1", "flMsMcm100xE1Group"),
        ("FIBROLAN-MIB-MCM100-xE1", "flMsMcm100xE1PortsGroup"))
)
if mibBuilder.loadTexts:
    flMcm100xE1MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIBROLAN-MIB-MCM100-xE1",
    **{"fibrolan": fibrolan,
       "fibrolanSNMP": fibrolanSNMP,
       "flMetroStarMv": flMetroStarMv,
       "flMsChassisMv": flMsChassisMv,
       "flMsModuleMv": flMsModuleMv,
       "flMcm1xxMv": flMcm1xxMv,
       "flMcm100xE1": flMcm100xE1,
       "flMcm100xE1MIBConformance": flMcm100xE1MIBConformance,
       "flMsMcm100xE1MIBCompliances": flMsMcm100xE1MIBCompliances,
       "flMcm100xE1MIBCompliance": flMcm100xE1MIBCompliance,
       "flMsMcm100xE1MIBGroups": flMsMcm100xE1MIBGroups,
       "flMsMcm100xE1Group": flMsMcm100xE1Group,
       "flMsMcm100xE1PortsGroup": flMsMcm100xE1PortsGroup,
       "flMcm100xE1Ports": flMcm100xE1Ports,
       "flMcm100xE1PortsGeneralTable": flMcm100xE1PortsGeneralTable,
       "flMcm100xE1PortsEntry": flMcm100xE1PortsEntry,
       "flMsMcm100xE1ResetPorts": flMsMcm100xE1ResetPorts,
       "flMsMcm100xE1RestorePortsDef": flMsMcm100xE1RestorePortsDef,
       "flMcm100xE1PortsStatusTable": flMcm100xE1PortsStatusTable,
       "flMcm100xE1PortsStatusEntry": flMcm100xE1PortsStatusEntry,
       "flMsMcm100xE1PortIndex": flMsMcm100xE1PortIndex,
       "flMsMcm100xE1Signal": flMsMcm100xE1Signal,
       "flMsMcm100xE1RemoteSignal": flMsMcm100xE1RemoteSignal,
       "flMsMcm100xE1Ais": flMsMcm100xE1Ais,
       "flMsMcm100xE1Output": flMsMcm100xE1Output,
       "flMsMcm100xE1Input": flMsMcm100xE1Input,
       "flMsMcm100xE1Taos": flMsMcm100xE1Taos,
       "flMsMcm100xE1LocalLoopback": flMsMcm100xE1LocalLoopback,
       "flMsMcm100xE1UserAnalogLB": flMsMcm100xE1UserAnalogLB,
       "flMsMcm100xE1UserDigitalLB": flMsMcm100xE1UserDigitalLB,
       "flMsMcm100xE1PortDescription": flMsMcm100xE1PortDescription}
)
