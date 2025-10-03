# SNMP MIB module (DLINKSW-SWITCHPORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-SWITCHPORT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:57 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwSwitchPortMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 11)
)
if mibBuilder.loadTexts:
    dlinkSwSwitchPortMIB.setRevisions(
        ("2013-03-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DSwPortNotifications_ObjectIdentity = ObjectIdentity
dSwPortNotifications = _DSwPortNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 11, 0)
)
_DSwPortObjects_ObjectIdentity = ObjectIdentity
dSwPortObjects = _DSwPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 11, 1)
)
_DSwPortIfTable_Object = MibTable
dSwPortIfTable = _DSwPortIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 11, 1, 1)
)
if mibBuilder.loadTexts:
    dSwPortIfTable.setStatus("current")
_DSwPortIfEntry_Object = MibTableRow
dSwPortIfEntry = _DSwPortIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 11, 1, 1, 1)
)
dSwPortIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dSwPortIfEntry.setStatus("current")


class _DSwPortIfB1000baseTCtrl_Type(Integer32):
    """Custom type dSwPortIfB1000baseTCtrl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("b1000baseTMaster", 2),
          ("b1000baseTSlave", 3))
    )


_DSwPortIfB1000baseTCtrl_Type.__name__ = "Integer32"
_DSwPortIfB1000baseTCtrl_Object = MibTableColumn
dSwPortIfB1000baseTCtrl = _DSwPortIfB1000baseTCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 11, 1, 1, 1, 1),
    _DSwPortIfB1000baseTCtrl_Type()
)
dSwPortIfB1000baseTCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSwPortIfB1000baseTCtrl.setStatus("current")


class _DSwPortIfB10GbaseTCtrl_Type(Integer32):
    """Custom type dSwPortIfB10GbaseTCtrl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("b10GbaseTMaster", 2),
          ("b10GbaseTSlave", 3))
    )


_DSwPortIfB10GbaseTCtrl_Type.__name__ = "Integer32"
_DSwPortIfB10GbaseTCtrl_Object = MibTableColumn
dSwPortIfB10GbaseTCtrl = _DSwPortIfB10GbaseTCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 11, 1, 1, 1, 2),
    _DSwPortIfB10GbaseTCtrl_Type()
)
dSwPortIfB10GbaseTCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSwPortIfB10GbaseTCtrl.setStatus("current")


class _DSwPortIfMdix_Type(Integer32):
    """Custom type dSwPortIfMdix based on Integer32"""
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
        *(("auto", 1),
          ("normal", 2),
          ("cross", 3))
    )


_DSwPortIfMdix_Type.__name__ = "Integer32"
_DSwPortIfMdix_Object = MibTableColumn
dSwPortIfMdix = _DSwPortIfMdix_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 11, 1, 1, 1, 3),
    _DSwPortIfMdix_Type()
)
dSwPortIfMdix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSwPortIfMdix.setStatus("current")


class _DSwPortIfJumboFrameSize_Type(Unsigned32):
    """Custom type dSwPortIfJumboFrameSize based on Unsigned32"""
    defaultValue = 1536


_DSwPortIfJumboFrameSize_Type.__name__ = "Unsigned32"
_DSwPortIfJumboFrameSize_Object = MibTableColumn
dSwPortIfJumboFrameSize = _DSwPortIfJumboFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 11, 1, 1, 1, 4),
    _DSwPortIfJumboFrameSize_Type()
)
dSwPortIfJumboFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSwPortIfJumboFrameSize.setStatus("current")


class _DSwPortIfSpeedAutoDowngrade_Type(TruthValue):
    """Custom type dSwPortIfSpeedAutoDowngrade based on TruthValue"""
    defaultValue = 2


_DSwPortIfSpeedAutoDowngrade_Type.__name__ = "TruthValue"
_DSwPortIfSpeedAutoDowngrade_Object = MibTableColumn
dSwPortIfSpeedAutoDowngrade = _DSwPortIfSpeedAutoDowngrade_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 11, 1, 1, 1, 5),
    _DSwPortIfSpeedAutoDowngrade_Type()
)
dSwPortIfSpeedAutoDowngrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSwPortIfSpeedAutoDowngrade.setStatus("current")
_DSwPortConformance_ObjectIdentity = ObjectIdentity
dSwPortConformance = _DSwPortConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 11, 2)
)
_DSwPortCompliances_ObjectIdentity = ObjectIdentity
dSwPortCompliances = _DSwPortCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 11, 2, 1)
)
_DSwPortGroups_ObjectIdentity = ObjectIdentity
dSwPortGroups = _DSwPortGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 11, 2, 2)
)

# Managed Objects groups

dSwPortBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 11, 2, 2, 1)
)
dSwPortBasicGroup.setObjects(
      *(("DLINKSW-SWITCHPORT-MIB", "dSwPortIfB1000baseTCtrl"),
        ("DLINKSW-SWITCHPORT-MIB", "dSwPortIfB10GbaseTCtrl"),
        ("DLINKSW-SWITCHPORT-MIB", "dSwPortIfMdix"),
        ("DLINKSW-SWITCHPORT-MIB", "dSwPortIfJumboFrameSize"),
        ("DLINKSW-SWITCHPORT-MIB", "dSwPortIfSpeedAutoDowngrade"))
)
if mibBuilder.loadTexts:
    dSwPortBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dSwPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 11, 2, 1, 1)
)
dSwPortCompliance.setObjects(
    ("DLINKSW-SWITCHPORT-MIB", "dSwPortBasicGroup")
)
if mibBuilder.loadTexts:
    dSwPortCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-SWITCHPORT-MIB",
    **{"dlinkSwSwitchPortMIB": dlinkSwSwitchPortMIB,
       "dSwPortNotifications": dSwPortNotifications,
       "dSwPortObjects": dSwPortObjects,
       "dSwPortIfTable": dSwPortIfTable,
       "dSwPortIfEntry": dSwPortIfEntry,
       "dSwPortIfB1000baseTCtrl": dSwPortIfB1000baseTCtrl,
       "dSwPortIfB10GbaseTCtrl": dSwPortIfB10GbaseTCtrl,
       "dSwPortIfMdix": dSwPortIfMdix,
       "dSwPortIfJumboFrameSize": dSwPortIfJumboFrameSize,
       "dSwPortIfSpeedAutoDowngrade": dSwPortIfSpeedAutoDowngrade,
       "dSwPortConformance": dSwPortConformance,
       "dSwPortCompliances": dSwPortCompliances,
       "dSwPortCompliance": dSwPortCompliance,
       "dSwPortGroups": dSwPortGroups,
       "dSwPortBasicGroup": dSwPortBasicGroup}
)
