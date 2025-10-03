# SNMP MIB module (TN-VLAN-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-VLAN-MGMT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:37 2025
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

(EightOTwoOui,) = mibBuilder.importSymbols(
    "DOT3-OAM-MIB",
    "EightOTwoOui")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(PortList,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnVlanQoSMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4)
)
if mibBuilder.loadTexts:
    tnVlanQoSMgmtMIB.setRevisions(
        ("2009-01-08 00:00",
         "2011-02-25 00:00",
         "2012-05-18 00:00",
         "2012-12-21 00:00",
         "2014-05-01 00:00",
         "2015-06-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TnVlanServiceTranslationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("noTranslation", 1),
          ("untaggedUntagged", 2),
          ("untaggedSingleTagged", 3),
          ("singleTaggedSingleTagged", 4),
          ("singleTaggedTranslation", 5),
          ("singleTaggedDoubleTagged", 6),
          ("doubleTaggedDoubleTagged", 7),
          ("doubleTaggedTranslation", 8),
          ("addProviderTag", 9))
    )



class TNVlanListQuarter(TextualConvention, OctetString):
    status = "current"
    displayHint = "128x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128



# MIB Managed Objects in the order of their OIDs

_TnVlanQoSMgmtNotifications_ObjectIdentity = ObjectIdentity
tnVlanQoSMgmtNotifications = _TnVlanQoSMgmtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 0)
)
_TnVlanQoSMgmtObjects_ObjectIdentity = ObjectIdentity
tnVlanQoSMgmtObjects = _TnVlanQoSMgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1)
)
_TnSysVlanMgmt_ObjectIdentity = ObjectIdentity
tnSysVlanMgmt = _TnSysVlanMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 1)
)
_TnSysManagmentVLANTable_Object = MibTable
tnSysManagmentVLANTable = _TnSysManagmentVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnSysManagmentVLANTable.setStatus("current")
_TnSysManagmentVLANEntry_Object = MibTableRow
tnSysManagmentVLANEntry = _TnSysManagmentVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 1, 1, 1)
)
tnSysManagmentVLANEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnSysManagmentVLANEntry.setStatus("current")


class _TnSysMgmtVLANStatus_Type(Integer32):
    """Custom type tnSysMgmtVLANStatus based on Integer32"""
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


_TnSysMgmtVLANStatus_Type.__name__ = "Integer32"
_TnSysMgmtVLANStatus_Object = MibTableColumn
tnSysMgmtVLANStatus = _TnSysMgmtVLANStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 1, 1, 1, 1),
    _TnSysMgmtVLANStatus_Type()
)
tnSysMgmtVLANStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysMgmtVLANStatus.setStatus("current")


class _TnSysMgmtVLANId_Type(Integer32):
    """Custom type tnSysMgmtVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TnSysMgmtVLANId_Type.__name__ = "Integer32"
_TnSysMgmtVLANId_Object = MibTableColumn
tnSysMgmtVLANId = _TnSysMgmtVLANId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 1, 1, 1, 2),
    _TnSysMgmtVLANId_Type()
)
tnSysMgmtVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysMgmtVLANId.setStatus("current")


class _TnSysMgmtMemberPorts_Type(Bits):
    """Custom type tnSysMgmtMemberPorts based on Bits"""
    namedValues = NamedValues(
        ("none", 0)
    )

_TnSysMgmtMemberPorts_Type.__name__ = "Bits"
_TnSysMgmtMemberPorts_Object = MibTableColumn
tnSysMgmtMemberPorts = _TnSysMgmtMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 1, 1, 1, 3),
    _TnSysMgmtMemberPorts_Type()
)
tnSysMgmtMemberPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysMgmtMemberPorts.setStatus("current")
_TnSysVLANExtTable_Object = MibTable
tnSysVLANExtTable = _TnSysVLANExtTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tnSysVLANExtTable.setStatus("current")
_TnSysVLANExtEntry_Object = MibTableRow
tnSysVLANExtEntry = _TnSysVLANExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 1, 2, 1)
)
tnSysVLANExtEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnSysVLANExtEntry.setStatus("current")


class _TnSysVlanExtMgmtPortType_Type(Integer32):
    """Custom type tnSysVlanExtMgmtPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unaware", 1),
          ("cPort", 2),
          ("sPort", 3),
          ("sCustomPort", 4))
    )


_TnSysVlanExtMgmtPortType_Type.__name__ = "Integer32"
_TnSysVlanExtMgmtPortType_Object = MibTableColumn
tnSysVlanExtMgmtPortType = _TnSysVlanExtMgmtPortType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 1, 2, 1, 1),
    _TnSysVlanExtMgmtPortType_Type()
)
tnSysVlanExtMgmtPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysVlanExtMgmtPortType.setStatus("current")


class _TnSysVLANExtCustomSTag_Type(OctetString):
    """Custom type tnSysVLANExtCustomSTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_TnSysVLANExtCustomSTag_Type.__name__ = "OctetString"
_TnSysVLANExtCustomSTag_Object = MibTableColumn
tnSysVLANExtCustomSTag = _TnSysVLANExtCustomSTag_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 1, 2, 1, 2),
    _TnSysVLANExtCustomSTag_Type()
)
tnSysVLANExtCustomSTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysVLANExtCustomSTag.setStatus("current")
_TnVlanConfigGlobalsMainAccessVlans0To1K_Type = TNVlanListQuarter
_TnVlanConfigGlobalsMainAccessVlans0To1K_Object = MibTableColumn
tnVlanConfigGlobalsMainAccessVlans0To1K = _TnVlanConfigGlobalsMainAccessVlans0To1K_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 1, 2, 1, 3),
    _TnVlanConfigGlobalsMainAccessVlans0To1K_Type()
)
tnVlanConfigGlobalsMainAccessVlans0To1K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVlanConfigGlobalsMainAccessVlans0To1K.setStatus("current")
_TnVlanConfigGlobalsMainAccessVlans1KTo2K_Type = TNVlanListQuarter
_TnVlanConfigGlobalsMainAccessVlans1KTo2K_Object = MibTableColumn
tnVlanConfigGlobalsMainAccessVlans1KTo2K = _TnVlanConfigGlobalsMainAccessVlans1KTo2K_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 1, 2, 1, 4),
    _TnVlanConfigGlobalsMainAccessVlans1KTo2K_Type()
)
tnVlanConfigGlobalsMainAccessVlans1KTo2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVlanConfigGlobalsMainAccessVlans1KTo2K.setStatus("current")
_TnVlanConfigGlobalsMainAccessVlans2KTo3K_Type = TNVlanListQuarter
_TnVlanConfigGlobalsMainAccessVlans2KTo3K_Object = MibTableColumn
tnVlanConfigGlobalsMainAccessVlans2KTo3K = _TnVlanConfigGlobalsMainAccessVlans2KTo3K_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 1, 2, 1, 5),
    _TnVlanConfigGlobalsMainAccessVlans2KTo3K_Type()
)
tnVlanConfigGlobalsMainAccessVlans2KTo3K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVlanConfigGlobalsMainAccessVlans2KTo3K.setStatus("current")
_TnVlanConfigGlobalsMainAccessVlans3KTo4K_Type = TNVlanListQuarter
_TnVlanConfigGlobalsMainAccessVlans3KTo4K_Object = MibTableColumn
tnVlanConfigGlobalsMainAccessVlans3KTo4K = _TnVlanConfigGlobalsMainAccessVlans3KTo4K_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 1, 2, 1, 6),
    _TnVlanConfigGlobalsMainAccessVlans3KTo4K_Type()
)
tnVlanConfigGlobalsMainAccessVlans3KTo4K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVlanConfigGlobalsMainAccessVlans3KTo4K.setStatus("current")
_TnDevSysPriorityMgmt_ObjectIdentity = ObjectIdentity
tnDevSysPriorityMgmt = _TnDevSysPriorityMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 2)
)
_TnSwIPPrioTable_Object = MibTable
tnSwIPPrioTable = _TnSwIPPrioTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tnSwIPPrioTable.setStatus("current")
_TnSwIPPrioEntry_Object = MibTableRow
tnSwIPPrioEntry = _TnSwIPPrioEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 2, 1, 1)
)
tnSwIPPrioEntry.setIndexNames(
    (0, "TN-VLAN-MGMT-MIB", "tnSwIPPrioIndex"),
)
if mibBuilder.loadTexts:
    tnSwIPPrioEntry.setStatus("current")


class _TnSwIPPrioIndex_Type(Integer32):
    """Custom type tnSwIPPrioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11111),
    )


_TnSwIPPrioIndex_Type.__name__ = "Integer32"
_TnSwIPPrioIndex_Object = MibTableColumn
tnSwIPPrioIndex = _TnSwIPPrioIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 2, 1, 1, 1),
    _TnSwIPPrioIndex_Type()
)
tnSwIPPrioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwIPPrioIndex.setStatus("current")
_TnSwIPPrioTC_Type = Integer32
_TnSwIPPrioTC_Object = MibTableColumn
tnSwIPPrioTC = _TnSwIPPrioTC_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 2, 1, 1, 2),
    _TnSwIPPrioTC_Type()
)
tnSwIPPrioTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwIPPrioTC.setStatus("current")


class _TnSwIPPrioRemap_Type(Integer32):
    """Custom type tnSwIPPrioRemap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("pri0", 1),
          ("pri1", 2),
          ("pri2", 3),
          ("pri3", 4))
    )


_TnSwIPPrioRemap_Type.__name__ = "Integer32"
_TnSwIPPrioRemap_Object = MibTableColumn
tnSwIPPrioRemap = _TnSwIPPrioRemap_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 2, 1, 1, 3),
    _TnSwIPPrioRemap_Type()
)
tnSwIPPrioRemap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwIPPrioRemap.setStatus("current")
_TnSwIEEEPrioTable_Object = MibTable
tnSwIEEEPrioTable = _TnSwIEEEPrioTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tnSwIEEEPrioTable.setStatus("current")
_TnSwIEEEPrioEntry_Object = MibTableRow
tnSwIEEEPrioEntry = _TnSwIEEEPrioEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 2, 2, 1)
)
tnSwIEEEPrioEntry.setIndexNames(
    (0, "TN-VLAN-MGMT-MIB", "tnSwIEEEPriority"),
)
if mibBuilder.loadTexts:
    tnSwIEEEPrioEntry.setStatus("current")


class _TnSwIEEEPriority_Type(Integer32):
    """Custom type tnSwIEEEPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnSwIEEEPriority_Type.__name__ = "Integer32"
_TnSwIEEEPriority_Object = MibTableColumn
tnSwIEEEPriority = _TnSwIEEEPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 2, 2, 1, 1),
    _TnSwIEEEPriority_Type()
)
tnSwIEEEPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwIEEEPriority.setStatus("current")


class _TnSwIEEEPriorityRemap_Type(Integer32):
    """Custom type tnSwIEEEPriorityRemap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("pri0", 1),
          ("pri1", 2),
          ("pri2", 3),
          ("pri3", 4))
    )


_TnSwIEEEPriorityRemap_Type.__name__ = "Integer32"
_TnSwIEEEPriorityRemap_Object = MibTableColumn
tnSwIEEEPriorityRemap = _TnSwIEEEPriorityRemap_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 2, 2, 1, 2),
    _TnSwIEEEPriorityRemap_Type()
)
tnSwIEEEPriorityRemap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwIEEEPriorityRemap.setStatus("current")
_TnInterfaceQoSMgmt_ObjectIdentity = ObjectIdentity
tnInterfaceQoSMgmt = _TnInterfaceQoSMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 3)
)
_TnIfPriorityTable_Object = MibTable
tnIfPriorityTable = _TnIfPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tnIfPriorityTable.setStatus("current")
_TnIfPriorityEntry_Object = MibTableRow
tnIfPriorityEntry = _TnIfPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 3, 1, 1)
)
tnIfPriorityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnIfPriorityEntry.setStatus("current")


class _TnIfDefaultPriority_Type(Integer32):
    """Custom type tnIfDefaultPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnIfDefaultPriority_Type.__name__ = "Integer32"
_TnIfDefaultPriority_Object = MibTableColumn
tnIfDefaultPriority = _TnIfDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 3, 1, 1, 1),
    _TnIfDefaultPriority_Type()
)
tnIfDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfDefaultPriority.setStatus("current")
_TnIfUseIEEEPriority_Type = TruthValue
_TnIfUseIEEEPriority_Object = MibTableColumn
tnIfUseIEEEPriority = _TnIfUseIEEEPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 3, 1, 1, 2),
    _TnIfUseIEEEPriority_Type()
)
tnIfUseIEEEPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfUseIEEEPriority.setStatus("current")
_TnIfUseIPPriority_Type = TruthValue
_TnIfUseIPPriority_Object = MibTableColumn
tnIfUseIPPriority = _TnIfUseIPPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 3, 1, 1, 3),
    _TnIfUseIPPriority_Type()
)
tnIfUseIPPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfUseIPPriority.setStatus("current")


class _TnIfUseIPOrIEEEPriority_Type(Integer32):
    """Custom type tnIfUseIPOrIEEEPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("useIEEE", 1),
          ("useIP", 2))
    )


_TnIfUseIPOrIEEEPriority_Type.__name__ = "Integer32"
_TnIfUseIPOrIEEEPriority_Object = MibTableColumn
tnIfUseIPOrIEEEPriority = _TnIfUseIPOrIEEEPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 3, 1, 1, 4),
    _TnIfUseIPOrIEEEPriority_Type()
)
tnIfUseIPOrIEEEPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfUseIPOrIEEEPriority.setStatus("current")
_TnIfSrcMACPriorityRemap_Type = TruthValue
_TnIfSrcMACPriorityRemap_Object = MibTableColumn
tnIfSrcMACPriorityRemap = _TnIfSrcMACPriorityRemap_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 3, 1, 1, 5),
    _TnIfSrcMACPriorityRemap_Type()
)
tnIfSrcMACPriorityRemap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfSrcMACPriorityRemap.setStatus("current")
_TnIfDstMACPriorityRemap_Type = TruthValue
_TnIfDstMACPriorityRemap_Object = MibTableColumn
tnIfDstMACPriorityRemap = _TnIfDstMACPriorityRemap_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 3, 1, 1, 6),
    _TnIfDstMACPriorityRemap_Type()
)
tnIfDstMACPriorityRemap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfDstMACPriorityRemap.setStatus("current")
_TnIfVIDPriorityRemap_Type = TruthValue
_TnIfVIDPriorityRemap_Object = MibTableColumn
tnIfVIDPriorityRemap = _TnIfVIDPriorityRemap_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 3, 1, 1, 7),
    _TnIfVIDPriorityRemap_Type()
)
tnIfVIDPriorityRemap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfVIDPriorityRemap.setStatus("current")
_TnIfPriorityRemapTable_Object = MibTable
tnIfPriorityRemapTable = _TnIfPriorityRemapTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tnIfPriorityRemapTable.setStatus("current")
_TnIfPriorityRemapEntry_Object = MibTableRow
tnIfPriorityRemapEntry = _TnIfPriorityRemapEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 3, 2, 1)
)
tnIfPriorityRemapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TN-VLAN-MGMT-MIB", "tnIfUserPriority"),
)
if mibBuilder.loadTexts:
    tnIfPriorityRemapEntry.setStatus("current")


class _TnIfUserPriority_Type(Integer32):
    """Custom type tnIfUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnIfUserPriority_Type.__name__ = "Integer32"
_TnIfUserPriority_Object = MibTableColumn
tnIfUserPriority = _TnIfUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 3, 2, 1, 1),
    _TnIfUserPriority_Type()
)
tnIfUserPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfUserPriority.setStatus("current")


class _TnIfRemappedPriority_Type(Integer32):
    """Custom type tnIfRemappedPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnIfRemappedPriority_Type.__name__ = "Integer32"
_TnIfRemappedPriority_Object = MibTableColumn
tnIfRemappedPriority = _TnIfRemappedPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 3, 2, 1, 2),
    _TnIfRemappedPriority_Type()
)
tnIfRemappedPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfRemappedPriority.setStatus("current")
_TnInterfaceVlanMgmt_ObjectIdentity = ObjectIdentity
tnInterfaceVlanMgmt = _TnInterfaceVlanMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4)
)
_TnIfVLANTable_Object = MibTable
tnIfVLANTable = _TnIfVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tnIfVLANTable.setStatus("current")
_TnIfVLANEntry_Object = MibTableRow
tnIfVLANEntry = _TnIfVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 1, 1)
)
tnIfVLANEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnIfVLANEntry.setStatus("current")


class _TnIfDot1qState_Type(Integer32):
    """Custom type tnIfDot1qState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlanEnabled", 1),
          ("vlanDisabled", 2))
    )


_TnIfDot1qState_Type.__name__ = "Integer32"
_TnIfDot1qState_Object = MibTableColumn
tnIfDot1qState = _TnIfDot1qState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 1, 1, 1),
    _TnIfDot1qState_Type()
)
tnIfDot1qState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfDot1qState.setStatus("current")
_TnIfDiscardTagged_Type = TruthValue
_TnIfDiscardTagged_Object = MibTableColumn
tnIfDiscardTagged = _TnIfDiscardTagged_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 1, 1, 2),
    _TnIfDiscardTagged_Type()
)
tnIfDiscardTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfDiscardTagged.setStatus("current")
_TnIfDiscardUntagged_Type = TruthValue
_TnIfDiscardUntagged_Object = MibTableColumn
tnIfDiscardUntagged = _TnIfDiscardUntagged_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 1, 1, 3),
    _TnIfDiscardUntagged_Type()
)
tnIfDiscardUntagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfDiscardUntagged.setStatus("current")


class _TnIfDefaultVlanId_Type(Integer32):
    """Custom type tnIfDefaultVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_TnIfDefaultVlanId_Type.__name__ = "Integer32"
_TnIfDefaultVlanId_Object = MibTableColumn
tnIfDefaultVlanId = _TnIfDefaultVlanId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 1, 1, 4),
    _TnIfDefaultVlanId_Type()
)
tnIfDefaultVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfDefaultVlanId.setStatus("current")
_TnIfForceDefaultVlanId_Type = TruthValue
_TnIfForceDefaultVlanId_Object = MibTableColumn
tnIfForceDefaultVlanId = _TnIfForceDefaultVlanId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 1, 1, 5),
    _TnIfForceDefaultVlanId_Type()
)
tnIfForceDefaultVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfForceDefaultVlanId.setStatus("current")
_TnIfVLANTagMgmtTable_Object = MibTable
tnIfVLANTagMgmtTable = _TnIfVLANTagMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 2)
)
if mibBuilder.loadTexts:
    tnIfVLANTagMgmtTable.setStatus("current")
_TnIfVLANTagMgmtEntry_Object = MibTableRow
tnIfVLANTagMgmtEntry = _TnIfVLANTagMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 2, 1)
)
tnIfVLANTagMgmtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnIfVLANTagMgmtEntry.setStatus("current")


class _TnIfFrameTagMode_Type(Integer32):
    """Custom type tnIfFrameTagMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("provider", 2),
          ("customer", 3))
    )


_TnIfFrameTagMode_Type.__name__ = "Integer32"
_TnIfFrameTagMode_Object = MibTableColumn
tnIfFrameTagMode = _TnIfFrameTagMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 2, 1, 1),
    _TnIfFrameTagMode_Type()
)
tnIfFrameTagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfFrameTagMode.setStatus("current")


class _TnIfProviderEtherType_Type(Integer32):
    """Custom type tnIfProviderEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("x8100", 1),
          ("x9100", 2),
          ("x88a8", 3))
    )


_TnIfProviderEtherType_Type.__name__ = "Integer32"
_TnIfProviderEtherType_Object = MibTableColumn
tnIfProviderEtherType = _TnIfProviderEtherType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 2, 1, 2),
    _TnIfProviderEtherType_Type()
)
tnIfProviderEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfProviderEtherType.setStatus("current")


class _TnIfNetworkModeTagging_Type(Integer32):
    """Custom type tnIfNetworkModeTagging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unmodified", 1),
          ("removeTag", 2),
          ("addTag", 3))
    )


_TnIfNetworkModeTagging_Type.__name__ = "Integer32"
_TnIfNetworkModeTagging_Object = MibTableColumn
tnIfNetworkModeTagging = _TnIfNetworkModeTagging_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 2, 1, 3),
    _TnIfNetworkModeTagging_Type()
)
tnIfNetworkModeTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfNetworkModeTagging.setStatus("current")
_TnIfVLANTagMgmt2Table_Object = MibTable
tnIfVLANTagMgmt2Table = _TnIfVLANTagMgmt2Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 3)
)
if mibBuilder.loadTexts:
    tnIfVLANTagMgmt2Table.setStatus("current")
_TnIfVLANTagMgmt2Entry_Object = MibTableRow
tnIfVLANTagMgmt2Entry = _TnIfVLANTagMgmt2Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 3, 1)
)
tnIfVLANTagMgmt2Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnIfVLANTagMgmt2Entry.setStatus("current")


class _TnIfVLANTagMgmt2PortType_Type(Integer32):
    """Custom type tnIfVLANTagMgmt2PortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unaware", 1),
          ("cPort", 2),
          ("sPort", 3),
          ("sCustomPort", 4))
    )


_TnIfVLANTagMgmt2PortType_Type.__name__ = "Integer32"
_TnIfVLANTagMgmt2PortType_Object = MibTableColumn
tnIfVLANTagMgmt2PortType = _TnIfVLANTagMgmt2PortType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 3, 1, 1),
    _TnIfVLANTagMgmt2PortType_Type()
)
tnIfVLANTagMgmt2PortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfVLANTagMgmt2PortType.setStatus("current")


class _TnIfVLANTagMgmt2TxTagType_Type(Integer32):
    """Custom type tnIfVLANTagMgmt2TxTagType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("untagPvid", 1),
          ("tagAll", 2),
          ("untagAll", 3))
    )


_TnIfVLANTagMgmt2TxTagType_Type.__name__ = "Integer32"
_TnIfVLANTagMgmt2TxTagType_Object = MibTableColumn
tnIfVLANTagMgmt2TxTagType = _TnIfVLANTagMgmt2TxTagType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 3, 1, 2),
    _TnIfVLANTagMgmt2TxTagType_Type()
)
tnIfVLANTagMgmt2TxTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfVLANTagMgmt2TxTagType.setStatus("current")


class _TnIfVLANTagMgmt2ConfigConflicts_Type(Integer32):
    """Custom type tnIfVLANTagMgmt2ConfigConflicts based on Integer32"""
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


_TnIfVLANTagMgmt2ConfigConflicts_Type.__name__ = "Integer32"
_TnIfVLANTagMgmt2ConfigConflicts_Object = MibTableColumn
tnIfVLANTagMgmt2ConfigConflicts = _TnIfVLANTagMgmt2ConfigConflicts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 3, 1, 3),
    _TnIfVLANTagMgmt2ConfigConflicts_Type()
)
tnIfVLANTagMgmt2ConfigConflicts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfVLANTagMgmt2ConfigConflicts.setStatus("current")


class _TnVlanConfigInterfaceMode_Type(Integer32):
    """Custom type tnVlanConfigInterfaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("trunk", 2),
          ("hybrid", 3))
    )


_TnVlanConfigInterfaceMode_Type.__name__ = "Integer32"
_TnVlanConfigInterfaceMode_Object = MibTableColumn
tnVlanConfigInterfaceMode = _TnVlanConfigInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 3, 1, 4),
    _TnVlanConfigInterfaceMode_Type()
)
tnVlanConfigInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVlanConfigInterfaceMode.setStatus("current")
_TnVlanConfigInterfaceAllowVlans0KTo1K_Type = TNVlanListQuarter
_TnVlanConfigInterfaceAllowVlans0KTo1K_Object = MibTableColumn
tnVlanConfigInterfaceAllowVlans0KTo1K = _TnVlanConfigInterfaceAllowVlans0KTo1K_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 3, 1, 5),
    _TnVlanConfigInterfaceAllowVlans0KTo1K_Type()
)
tnVlanConfigInterfaceAllowVlans0KTo1K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVlanConfigInterfaceAllowVlans0KTo1K.setStatus("current")
_TnVlanConfigInterfaceAllowVlans1KTo2K_Type = TNVlanListQuarter
_TnVlanConfigInterfaceAllowVlans1KTo2K_Object = MibTableColumn
tnVlanConfigInterfaceAllowVlans1KTo2K = _TnVlanConfigInterfaceAllowVlans1KTo2K_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 3, 1, 6),
    _TnVlanConfigInterfaceAllowVlans1KTo2K_Type()
)
tnVlanConfigInterfaceAllowVlans1KTo2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVlanConfigInterfaceAllowVlans1KTo2K.setStatus("current")
_TnVlanConfigInterfaceAllowVlans2KTo3K_Type = TNVlanListQuarter
_TnVlanConfigInterfaceAllowVlans2KTo3K_Object = MibTableColumn
tnVlanConfigInterfaceAllowVlans2KTo3K = _TnVlanConfigInterfaceAllowVlans2KTo3K_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 3, 1, 7),
    _TnVlanConfigInterfaceAllowVlans2KTo3K_Type()
)
tnVlanConfigInterfaceAllowVlans2KTo3K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVlanConfigInterfaceAllowVlans2KTo3K.setStatus("current")
_TnVlanConfigInterfaceAllowVlans3KTo4K_Type = TNVlanListQuarter
_TnVlanConfigInterfaceAllowVlans3KTo4K_Object = MibTableColumn
tnVlanConfigInterfaceAllowVlans3KTo4K = _TnVlanConfigInterfaceAllowVlans3KTo4K_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 3, 1, 8),
    _TnVlanConfigInterfaceAllowVlans3KTo4K_Type()
)
tnVlanConfigInterfaceAllowVlans3KTo4K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVlanConfigInterfaceAllowVlans3KTo4K.setStatus("current")
_TnVlanConfigInterfaceForbiddenVlans0KTo1K_Type = TNVlanListQuarter
_TnVlanConfigInterfaceForbiddenVlans0KTo1K_Object = MibTableColumn
tnVlanConfigInterfaceForbiddenVlans0KTo1K = _TnVlanConfigInterfaceForbiddenVlans0KTo1K_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 3, 1, 9),
    _TnVlanConfigInterfaceForbiddenVlans0KTo1K_Type()
)
tnVlanConfigInterfaceForbiddenVlans0KTo1K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVlanConfigInterfaceForbiddenVlans0KTo1K.setStatus("current")
_TnVlanConfigInterfaceForbiddenVlans1KTo2K_Type = TNVlanListQuarter
_TnVlanConfigInterfaceForbiddenVlans1KTo2K_Object = MibTableColumn
tnVlanConfigInterfaceForbiddenVlans1KTo2K = _TnVlanConfigInterfaceForbiddenVlans1KTo2K_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 3, 1, 10),
    _TnVlanConfigInterfaceForbiddenVlans1KTo2K_Type()
)
tnVlanConfigInterfaceForbiddenVlans1KTo2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVlanConfigInterfaceForbiddenVlans1KTo2K.setStatus("current")
_TnVlanConfigInterfaceForbiddenVlans2KTo3K_Type = TNVlanListQuarter
_TnVlanConfigInterfaceForbiddenVlans2KTo3K_Object = MibTableColumn
tnVlanConfigInterfaceForbiddenVlans2KTo3K = _TnVlanConfigInterfaceForbiddenVlans2KTo3K_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 3, 1, 11),
    _TnVlanConfigInterfaceForbiddenVlans2KTo3K_Type()
)
tnVlanConfigInterfaceForbiddenVlans2KTo3K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVlanConfigInterfaceForbiddenVlans2KTo3K.setStatus("current")
_TnVlanConfigInterfaceForbiddenVlans3KTo4K_Type = TNVlanListQuarter
_TnVlanConfigInterfaceForbiddenVlans3KTo4K_Object = MibTableColumn
tnVlanConfigInterfaceForbiddenVlans3KTo4K = _TnVlanConfigInterfaceForbiddenVlans3KTo4K_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 4, 3, 1, 12),
    _TnVlanConfigInterfaceForbiddenVlans3KTo4K_Type()
)
tnVlanConfigInterfaceForbiddenVlans3KTo4K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVlanConfigInterfaceForbiddenVlans3KTo4K.setStatus("current")
_TnVlanServiceMgmt_ObjectIdentity = ObjectIdentity
tnVlanServiceMgmt = _TnVlanServiceMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 5)
)


class _TnVlanServiceConnType_Type(Integer32):
    """Custom type tnVlanServiceConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("customerProvider", 1),
          ("providerCustomer", 2))
    )


_TnVlanServiceConnType_Type.__name__ = "Integer32"
_TnVlanServiceConnType_Object = MibScalar
tnVlanServiceConnType = _TnVlanServiceConnType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 5, 1),
    _TnVlanServiceConnType_Type()
)
tnVlanServiceConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVlanServiceConnType.setStatus("current")


class _TnVlanServiceVIDForTag_Type(Integer32):
    """Custom type tnVlanServiceVIDForTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TnVlanServiceVIDForTag_Type.__name__ = "Integer32"
_TnVlanServiceVIDForTag_Object = MibScalar
tnVlanServiceVIDForTag = _TnVlanServiceVIDForTag_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 5, 2),
    _TnVlanServiceVIDForTag_Type()
)
tnVlanServiceVIDForTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVlanServiceVIDForTag.setStatus("current")
_TnVlanServiceEtherTypeForTag_Type = Integer32
_TnVlanServiceEtherTypeForTag_Object = MibScalar
tnVlanServiceEtherTypeForTag = _TnVlanServiceEtherTypeForTag_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 5, 3),
    _TnVlanServiceEtherTypeForTag_Type()
)
tnVlanServiceEtherTypeForTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVlanServiceEtherTypeForTag.setStatus("current")
_TnVlanServiceTranslation_Type = TnVlanServiceTranslationType
_TnVlanServiceTranslation_Object = MibScalar
tnVlanServiceTranslation = _TnVlanServiceTranslation_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 5, 4),
    _TnVlanServiceTranslation_Type()
)
tnVlanServiceTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVlanServiceTranslation.setStatus("current")
_TnVlanDbMgmt_ObjectIdentity = ObjectIdentity
tnVlanDbMgmt = _TnVlanDbMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 6)
)
_TnVLANDbTable_Object = MibTable
tnVLANDbTable = _TnVLANDbTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tnVLANDbTable.setStatus("current")
_TnVLANDbEntry_Object = MibTableRow
tnVLANDbEntry = _TnVLANDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 6, 1, 1)
)
tnVLANDbEntry.setIndexNames(
    (0, "TN-VLAN-MGMT-MIB", "tnVlanDbVID"),
)
if mibBuilder.loadTexts:
    tnVLANDbEntry.setStatus("current")
_TnVlanDbVID_Type = VlanIndex
_TnVlanDbVID_Object = MibTableColumn
tnVlanDbVID = _TnVlanDbVID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 6, 1, 1, 1),
    _TnVlanDbVID_Type()
)
tnVlanDbVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVlanDbVID.setStatus("current")


class _TnVlanDbFID_Type(Integer32):
    """Custom type tnVlanDbFID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnVlanDbFID_Type.__name__ = "Integer32"
_TnVlanDbFID_Object = MibTableColumn
tnVlanDbFID = _TnVlanDbFID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 6, 1, 1, 2),
    _TnVlanDbFID_Type()
)
tnVlanDbFID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVlanDbFID.setStatus("current")


class _TnVlanDbVIDPriOverride_Type(Integer32):
    """Custom type tnVlanDbVIDPriOverride based on Integer32"""
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


_TnVlanDbVIDPriOverride_Type.__name__ = "Integer32"
_TnVlanDbVIDPriOverride_Object = MibTableColumn
tnVlanDbVIDPriOverride = _TnVlanDbVIDPriOverride_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 6, 1, 1, 3),
    _TnVlanDbVIDPriOverride_Type()
)
tnVlanDbVIDPriOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVlanDbVIDPriOverride.setStatus("current")
_TnVlanDbVIDPriority_Type = Integer32
_TnVlanDbVIDPriority_Object = MibTableColumn
tnVlanDbVIDPriority = _TnVlanDbVIDPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 6, 1, 1, 4),
    _TnVlanDbVIDPriority_Type()
)
tnVlanDbVIDPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVlanDbVIDPriority.setStatus("current")


class _TnVlanDbMemTagPort1_Type(Integer32):
    """Custom type tnVlanDbMemTagPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("memEgressNoMod", 1),
          ("memEgressNoTag", 2),
          ("memEgressTag", 3),
          ("notMember", 4),
          ("notApplicable", 5))
    )


_TnVlanDbMemTagPort1_Type.__name__ = "Integer32"
_TnVlanDbMemTagPort1_Object = MibTableColumn
tnVlanDbMemTagPort1 = _TnVlanDbMemTagPort1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 6, 1, 1, 5),
    _TnVlanDbMemTagPort1_Type()
)
tnVlanDbMemTagPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVlanDbMemTagPort1.setStatus("current")


class _TnVlanDbMemTagPort2_Type(Integer32):
    """Custom type tnVlanDbMemTagPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("memEgressNoMod", 1),
          ("memEgressNoTag", 2),
          ("memEgressTag", 3),
          ("notMember", 4),
          ("notApplicable", 5))
    )


_TnVlanDbMemTagPort2_Type.__name__ = "Integer32"
_TnVlanDbMemTagPort2_Object = MibTableColumn
tnVlanDbMemTagPort2 = _TnVlanDbMemTagPort2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 6, 1, 1, 6),
    _TnVlanDbMemTagPort2_Type()
)
tnVlanDbMemTagPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVlanDbMemTagPort2.setStatus("current")


class _TnVlanDbMemTagPort3_Type(Integer32):
    """Custom type tnVlanDbMemTagPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("memEgressNoMod", 1),
          ("memEgressNoTag", 2),
          ("memEgressTag", 3),
          ("notMember", 4),
          ("notApplicable", 5))
    )


_TnVlanDbMemTagPort3_Type.__name__ = "Integer32"
_TnVlanDbMemTagPort3_Object = MibTableColumn
tnVlanDbMemTagPort3 = _TnVlanDbMemTagPort3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 6, 1, 1, 7),
    _TnVlanDbMemTagPort3_Type()
)
tnVlanDbMemTagPort3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVlanDbMemTagPort3.setStatus("current")


class _TnVlanDbMemTagPort4_Type(Integer32):
    """Custom type tnVlanDbMemTagPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("memEgressNoMod", 1),
          ("memEgressNoTag", 2),
          ("memEgressTag", 3),
          ("notMember", 4),
          ("notApplicable", 5))
    )


_TnVlanDbMemTagPort4_Type.__name__ = "Integer32"
_TnVlanDbMemTagPort4_Object = MibTableColumn
tnVlanDbMemTagPort4 = _TnVlanDbMemTagPort4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 6, 1, 1, 8),
    _TnVlanDbMemTagPort4_Type()
)
tnVlanDbMemTagPort4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVlanDbMemTagPort4.setStatus("current")


class _TnVlanDbMemTagPort5_Type(Integer32):
    """Custom type tnVlanDbMemTagPort5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("memEgressNoMod", 1),
          ("memEgressNoTag", 2),
          ("memEgressTag", 3),
          ("notMember", 4),
          ("notApplicable", 5))
    )


_TnVlanDbMemTagPort5_Type.__name__ = "Integer32"
_TnVlanDbMemTagPort5_Object = MibTableColumn
tnVlanDbMemTagPort5 = _TnVlanDbMemTagPort5_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 6, 1, 1, 9),
    _TnVlanDbMemTagPort5_Type()
)
tnVlanDbMemTagPort5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVlanDbMemTagPort5.setStatus("current")


class _TnVlanDbMemTagPort6_Type(Integer32):
    """Custom type tnVlanDbMemTagPort6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("memEgressNoMod", 1),
          ("memEgressNoTag", 2),
          ("memEgressTag", 3),
          ("notMember", 4),
          ("notApplicable", 5))
    )


_TnVlanDbMemTagPort6_Type.__name__ = "Integer32"
_TnVlanDbMemTagPort6_Object = MibTableColumn
tnVlanDbMemTagPort6 = _TnVlanDbMemTagPort6_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 6, 1, 1, 10),
    _TnVlanDbMemTagPort6_Type()
)
tnVlanDbMemTagPort6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVlanDbMemTagPort6.setStatus("current")


class _TnVlanDbMemTagPort7_Type(Integer32):
    """Custom type tnVlanDbMemTagPort7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("memEgressNoMod", 1),
          ("memEgressNoTag", 2),
          ("memEgressTag", 3),
          ("notMember", 4),
          ("notApplicable", 5))
    )


_TnVlanDbMemTagPort7_Type.__name__ = "Integer32"
_TnVlanDbMemTagPort7_Object = MibTableColumn
tnVlanDbMemTagPort7 = _TnVlanDbMemTagPort7_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 6, 1, 1, 11),
    _TnVlanDbMemTagPort7_Type()
)
tnVlanDbMemTagPort7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVlanDbMemTagPort7.setStatus("current")


class _TnVlanDbMemTagPort8_Type(Integer32):
    """Custom type tnVlanDbMemTagPort8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("memEgressNoMod", 1),
          ("memEgressNoTag", 2),
          ("memEgressTag", 3),
          ("notMember", 4),
          ("notApplicable", 5))
    )


_TnVlanDbMemTagPort8_Type.__name__ = "Integer32"
_TnVlanDbMemTagPort8_Object = MibTableColumn
tnVlanDbMemTagPort8 = _TnVlanDbMemTagPort8_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 6, 1, 1, 12),
    _TnVlanDbMemTagPort8_Type()
)
tnVlanDbMemTagPort8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVlanDbMemTagPort8.setStatus("current")


class _TnVlanDbMemTagPort9_Type(Integer32):
    """Custom type tnVlanDbMemTagPort9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("memEgressNoMod", 1),
          ("memEgressNoTag", 2),
          ("memEgressTag", 3),
          ("notMember", 4),
          ("notApplicable", 5))
    )


_TnVlanDbMemTagPort9_Type.__name__ = "Integer32"
_TnVlanDbMemTagPort9_Object = MibTableColumn
tnVlanDbMemTagPort9 = _TnVlanDbMemTagPort9_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 6, 1, 1, 13),
    _TnVlanDbMemTagPort9_Type()
)
tnVlanDbMemTagPort9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVlanDbMemTagPort9.setStatus("current")


class _TnVlanDbMemTagPort10_Type(Integer32):
    """Custom type tnVlanDbMemTagPort10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("memEgressNoMod", 1),
          ("memEgressNoTag", 2),
          ("memEgressTag", 3),
          ("notMember", 4),
          ("notApplicable", 5))
    )


_TnVlanDbMemTagPort10_Type.__name__ = "Integer32"
_TnVlanDbMemTagPort10_Object = MibTableColumn
tnVlanDbMemTagPort10 = _TnVlanDbMemTagPort10_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 6, 1, 1, 14),
    _TnVlanDbMemTagPort10_Type()
)
tnVlanDbMemTagPort10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVlanDbMemTagPort10.setStatus("current")
_TnVlanDbRowStatus_Type = RowStatus
_TnVlanDbRowStatus_Object = MibTableColumn
tnVlanDbRowStatus = _TnVlanDbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 6, 1, 1, 15),
    _TnVlanDbRowStatus_Type()
)
tnVlanDbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVlanDbRowStatus.setStatus("current")
_TnVLANDbFlush_ObjectIdentity = ObjectIdentity
tnVLANDbFlush = _TnVLANDbFlush_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 6, 2)
)


class _TnVLANDbFlushOperation_Type(Integer32):
    """Custom type tnVLANDbFlushOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 1),
          ("flushAll", 2))
    )


_TnVLANDbFlushOperation_Type.__name__ = "Integer32"
_TnVLANDbFlushOperation_Object = MibScalar
tnVLANDbFlushOperation = _TnVLANDbFlushOperation_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 6, 2, 1),
    _TnVLANDbFlushOperation_Type()
)
tnVLANDbFlushOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVLANDbFlushOperation.setStatus("current")


class _TnVLANDbFlushOperationStatus_Type(Integer32):
    """Custom type tnVLANDbFlushOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("success", 2),
          ("failure", 3),
          ("inProgress", 4))
    )


_TnVLANDbFlushOperationStatus_Type.__name__ = "Integer32"
_TnVLANDbFlushOperationStatus_Object = MibScalar
tnVLANDbFlushOperationStatus = _TnVLANDbFlushOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 6, 2, 2),
    _TnVLANDbFlushOperationStatus_Type()
)
tnVLANDbFlushOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVLANDbFlushOperationStatus.setStatus("current")


class _TnVLANDbFlushOperationFailureReason_Type(DisplayString):
    """Custom type tnVLANDbFlushOperationFailureReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TnVLANDbFlushOperationFailureReason_Type.__name__ = "DisplayString"
_TnVLANDbFlushOperationFailureReason_Object = MibScalar
tnVLANDbFlushOperationFailureReason = _TnVLANDbFlushOperationFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 6, 2, 3),
    _TnVLANDbFlushOperationFailureReason_Type()
)
tnVLANDbFlushOperationFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVLANDbFlushOperationFailureReason.setStatus("current")
_TnFIDDbMgmt_ObjectIdentity = ObjectIdentity
tnFIDDbMgmt = _TnFIDDbMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 7)
)
_TnFIDDbTable_Object = MibTable
tnFIDDbTable = _TnFIDDbTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 7, 1)
)
if mibBuilder.loadTexts:
    tnFIDDbTable.setStatus("current")
_TnFIDDbEntry_Object = MibTableRow
tnFIDDbEntry = _TnFIDDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 7, 1, 1)
)
tnFIDDbEntry.setIndexNames(
    (0, "TN-VLAN-MGMT-MIB", "tnFIDDbID"),
    (0, "TN-VLAN-MGMT-MIB", "tnFIDDbMacAddress"),
)
if mibBuilder.loadTexts:
    tnFIDDbEntry.setStatus("current")


class _TnFIDDbID_Type(Integer32):
    """Custom type tnFIDDbID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnFIDDbID_Type.__name__ = "Integer32"
_TnFIDDbID_Object = MibTableColumn
tnFIDDbID = _TnFIDDbID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 7, 1, 1, 2),
    _TnFIDDbID_Type()
)
tnFIDDbID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFIDDbID.setStatus("current")
_TnFIDDbMacAddress_Type = MacAddress
_TnFIDDbMacAddress_Object = MibTableColumn
tnFIDDbMacAddress = _TnFIDDbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 7, 1, 1, 3),
    _TnFIDDbMacAddress_Type()
)
tnFIDDbMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFIDDbMacAddress.setStatus("current")
_TnFIDDbConnPort_Type = Integer32
_TnFIDDbConnPort_Object = MibTableColumn
tnFIDDbConnPort = _TnFIDDbConnPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 7, 1, 1, 4),
    _TnFIDDbConnPort_Type()
)
tnFIDDbConnPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnFIDDbConnPort.setStatus("current")
_TnFIDDbPriority_Type = Integer32
_TnFIDDbPriority_Object = MibTableColumn
tnFIDDbPriority = _TnFIDDbPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 7, 1, 1, 5),
    _TnFIDDbPriority_Type()
)
tnFIDDbPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnFIDDbPriority.setStatus("current")


class _TnFIDDbEntryType_Type(Integer32):
    """Custom type tnFIDDbEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("staticNRL", 2),
          ("staticPA", 3),
          ("dynamic", 4))
    )


_TnFIDDbEntryType_Type.__name__ = "Integer32"
_TnFIDDbEntryType_Object = MibTableColumn
tnFIDDbEntryType = _TnFIDDbEntryType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 7, 1, 1, 6),
    _TnFIDDbEntryType_Type()
)
tnFIDDbEntryType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnFIDDbEntryType.setStatus("current")
_TnFIDDbEntryStatus_Type = RowStatus
_TnFIDDbEntryStatus_Object = MibTableColumn
tnFIDDbEntryStatus = _TnFIDDbEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 7, 1, 1, 7),
    _TnFIDDbEntryStatus_Type()
)
tnFIDDbEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnFIDDbEntryStatus.setStatus("current")
_TnFIDDbFlush_ObjectIdentity = ObjectIdentity
tnFIDDbFlush = _TnFIDDbFlush_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 7, 2)
)


class _TnFIDDbFlushFID_Type(Integer32):
    """Custom type tnFIDDbFlushFID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_TnFIDDbFlushFID_Type.__name__ = "Integer32"
_TnFIDDbFlushFID_Object = MibScalar
tnFIDDbFlushFID = _TnFIDDbFlushFID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 7, 2, 1),
    _TnFIDDbFlushFID_Type()
)
tnFIDDbFlushFID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnFIDDbFlushFID.setStatus("current")


class _TnFIDDbFlushOperation_Type(Integer32):
    """Custom type tnFIDDbFlushOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 1),
          ("flushAll", 2),
          ("flushAllDynamic", 3),
          ("flushAllFID", 4),
          ("flushAllDynamicFID", 5))
    )


_TnFIDDbFlushOperation_Type.__name__ = "Integer32"
_TnFIDDbFlushOperation_Object = MibScalar
tnFIDDbFlushOperation = _TnFIDDbFlushOperation_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 7, 2, 2),
    _TnFIDDbFlushOperation_Type()
)
tnFIDDbFlushOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnFIDDbFlushOperation.setStatus("current")


class _TnFIDDbFlushOperationStatus_Type(Integer32):
    """Custom type tnFIDDbFlushOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("success", 2),
          ("failure", 3),
          ("inProgress", 4))
    )


_TnFIDDbFlushOperationStatus_Type.__name__ = "Integer32"
_TnFIDDbFlushOperationStatus_Object = MibScalar
tnFIDDbFlushOperationStatus = _TnFIDDbFlushOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 7, 2, 3),
    _TnFIDDbFlushOperationStatus_Type()
)
tnFIDDbFlushOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFIDDbFlushOperationStatus.setStatus("current")


class _TnFIDDbFlushOperationFailureReason_Type(DisplayString):
    """Custom type tnFIDDbFlushOperationFailureReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TnFIDDbFlushOperationFailureReason_Type.__name__ = "DisplayString"
_TnFIDDbFlushOperationFailureReason_Object = MibScalar
tnFIDDbFlushOperationFailureReason = _TnFIDDbFlushOperationFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 7, 2, 4),
    _TnFIDDbFlushOperationFailureReason_Type()
)
tnFIDDbFlushOperationFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFIDDbFlushOperationFailureReason.setStatus("current")
_TnVclMgmt_ObjectIdentity = ObjectIdentity
tnVclMgmt = _TnVclMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8)
)
_TnVclMacBasedMgmt_ObjectIdentity = ObjectIdentity
tnVclMacBasedMgmt = _TnVclMacBasedMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 1)
)
_TnVclMacBasedTable_Object = MibTable
tnVclMacBasedTable = _TnVclMacBasedTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    tnVclMacBasedTable.setStatus("current")
_TnVclMacBasedEntry_Object = MibTableRow
tnVclMacBasedEntry = _TnVclMacBasedEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 1, 1, 1)
)
tnVclMacBasedEntry.setIndexNames(
    (0, "TN-VLAN-MGMT-MIB", "tnVclMacBasedMacAddr"),
)
if mibBuilder.loadTexts:
    tnVclMacBasedEntry.setStatus("current")
_TnVclMacBasedMacAddr_Type = MacAddress
_TnVclMacBasedMacAddr_Object = MibTableColumn
tnVclMacBasedMacAddr = _TnVclMacBasedMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 1, 1, 1, 1),
    _TnVclMacBasedMacAddr_Type()
)
tnVclMacBasedMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVclMacBasedMacAddr.setStatus("current")
_TnVclMacBasedVlanId_Type = VlanIndex
_TnVclMacBasedVlanId_Object = MibTableColumn
tnVclMacBasedVlanId = _TnVclMacBasedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 1, 1, 1, 2),
    _TnVclMacBasedVlanId_Type()
)
tnVclMacBasedVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVclMacBasedVlanId.setStatus("current")
_TnVclMacBasedPortMember_Type = PortList
_TnVclMacBasedPortMember_Object = MibTableColumn
tnVclMacBasedPortMember = _TnVclMacBasedPortMember_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 1, 1, 1, 3),
    _TnVclMacBasedPortMember_Type()
)
tnVclMacBasedPortMember.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVclMacBasedPortMember.setStatus("current")


class _TnVclMacBasedUser_Type(Integer32):
    """Custom type tnVclMacBasedUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("nas", 2))
    )


_TnVclMacBasedUser_Type.__name__ = "Integer32"
_TnVclMacBasedUser_Object = MibTableColumn
tnVclMacBasedUser = _TnVclMacBasedUser_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 1, 1, 1, 4),
    _TnVclMacBasedUser_Type()
)
tnVclMacBasedUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVclMacBasedUser.setStatus("current")
_TnVclMacBasedRowStatus_Type = RowStatus
_TnVclMacBasedRowStatus_Object = MibTableColumn
tnVclMacBasedRowStatus = _TnVclMacBasedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 1, 1, 1, 5),
    _TnVclMacBasedRowStatus_Type()
)
tnVclMacBasedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVclMacBasedRowStatus.setStatus("current")
_TnVclProtoBasedMgmt_ObjectIdentity = ObjectIdentity
tnVclProtoBasedMgmt = _TnVclProtoBasedMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 2)
)
_TnVclProtoBasedGroupMapTable_Object = MibTable
tnVclProtoBasedGroupMapTable = _TnVclProtoBasedGroupMapTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    tnVclProtoBasedGroupMapTable.setStatus("current")
_TnVclProtoBasedGroupMapEntry_Object = MibTableRow
tnVclProtoBasedGroupMapEntry = _TnVclProtoBasedGroupMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 2, 1, 1)
)
tnVclProtoBasedGroupMapEntry.setIndexNames(
    (0, "TN-VLAN-MGMT-MIB", "tnVclProtoBasedGroupMapName"),
)
if mibBuilder.loadTexts:
    tnVclProtoBasedGroupMapEntry.setStatus("current")
_TnVclProtoBasedGroupMapName_Type = SnmpAdminString
_TnVclProtoBasedGroupMapName_Object = MibTableColumn
tnVclProtoBasedGroupMapName = _TnVclProtoBasedGroupMapName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 2, 1, 1, 1),
    _TnVclProtoBasedGroupMapName_Type()
)
tnVclProtoBasedGroupMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVclProtoBasedGroupMapName.setStatus("current")


class _TnVclProtoBasedGroupMapProtocol_Type(Integer32):
    """Custom type tnVclProtoBasedGroupMapProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("snap", 2),
          ("llc", 3))
    )


_TnVclProtoBasedGroupMapProtocol_Type.__name__ = "Integer32"
_TnVclProtoBasedGroupMapProtocol_Object = MibTableColumn
tnVclProtoBasedGroupMapProtocol = _TnVclProtoBasedGroupMapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 2, 1, 1, 2),
    _TnVclProtoBasedGroupMapProtocol_Type()
)
tnVclProtoBasedGroupMapProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVclProtoBasedGroupMapProtocol.setStatus("current")


class _TnVclProtoBasedGroupMapEtherTypeVal_Type(Integer32):
    """Custom type tnVclProtoBasedGroupMapEtherTypeVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_TnVclProtoBasedGroupMapEtherTypeVal_Type.__name__ = "Integer32"
_TnVclProtoBasedGroupMapEtherTypeVal_Object = MibTableColumn
tnVclProtoBasedGroupMapEtherTypeVal = _TnVclProtoBasedGroupMapEtherTypeVal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 2, 1, 1, 3),
    _TnVclProtoBasedGroupMapEtherTypeVal_Type()
)
tnVclProtoBasedGroupMapEtherTypeVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVclProtoBasedGroupMapEtherTypeVal.setStatus("current")
_TnVclProtoBasedGroupMapSnapOui_Type = EightOTwoOui
_TnVclProtoBasedGroupMapSnapOui_Object = MibTableColumn
tnVclProtoBasedGroupMapSnapOui = _TnVclProtoBasedGroupMapSnapOui_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 2, 1, 1, 4),
    _TnVclProtoBasedGroupMapSnapOui_Type()
)
tnVclProtoBasedGroupMapSnapOui.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVclProtoBasedGroupMapSnapOui.setStatus("current")
_TnVclProtoBasedGroupMapSnapPid_Type = Integer32
_TnVclProtoBasedGroupMapSnapPid_Object = MibTableColumn
tnVclProtoBasedGroupMapSnapPid = _TnVclProtoBasedGroupMapSnapPid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 2, 1, 1, 5),
    _TnVclProtoBasedGroupMapSnapPid_Type()
)
tnVclProtoBasedGroupMapSnapPid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVclProtoBasedGroupMapSnapPid.setStatus("current")
_TnVclProtoBasedGroupMapLlcDsap_Type = Integer32
_TnVclProtoBasedGroupMapLlcDsap_Object = MibTableColumn
tnVclProtoBasedGroupMapLlcDsap = _TnVclProtoBasedGroupMapLlcDsap_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 2, 1, 1, 6),
    _TnVclProtoBasedGroupMapLlcDsap_Type()
)
tnVclProtoBasedGroupMapLlcDsap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVclProtoBasedGroupMapLlcDsap.setStatus("current")
_TnVclProtoBasedGroupMapLlcSsap_Type = Integer32
_TnVclProtoBasedGroupMapLlcSsap_Object = MibTableColumn
tnVclProtoBasedGroupMapLlcSsap = _TnVclProtoBasedGroupMapLlcSsap_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 2, 1, 1, 7),
    _TnVclProtoBasedGroupMapLlcSsap_Type()
)
tnVclProtoBasedGroupMapLlcSsap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVclProtoBasedGroupMapLlcSsap.setStatus("current")
_TnVclProtoBasedGroupMapRowStatus_Type = RowStatus
_TnVclProtoBasedGroupMapRowStatus_Object = MibTableColumn
tnVclProtoBasedGroupMapRowStatus = _TnVclProtoBasedGroupMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 2, 1, 1, 8),
    _TnVclProtoBasedGroupMapRowStatus_Type()
)
tnVclProtoBasedGroupMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVclProtoBasedGroupMapRowStatus.setStatus("current")
_TnVclProtoBasedVlanMapTable_Object = MibTable
tnVclProtoBasedVlanMapTable = _TnVclProtoBasedVlanMapTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 2, 2)
)
if mibBuilder.loadTexts:
    tnVclProtoBasedVlanMapTable.setStatus("current")
_TnVclProtoBasedVlanMapEntry_Object = MibTableRow
tnVclProtoBasedVlanMapEntry = _TnVclProtoBasedVlanMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 2, 2, 1)
)
tnVclProtoBasedVlanMapEntry.setIndexNames(
    (1, "TN-VLAN-MGMT-MIB", "tnVclProtoBasedGroupMapName"),
    (0, "TN-VLAN-MGMT-MIB", "tnVclProtoBasedVlanMapVlanId"),
)
if mibBuilder.loadTexts:
    tnVclProtoBasedVlanMapEntry.setStatus("current")
_TnVclProtoBasedVlanMapVlanId_Type = VlanIndex
_TnVclProtoBasedVlanMapVlanId_Object = MibTableColumn
tnVclProtoBasedVlanMapVlanId = _TnVclProtoBasedVlanMapVlanId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 2, 2, 1, 1),
    _TnVclProtoBasedVlanMapVlanId_Type()
)
tnVclProtoBasedVlanMapVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVclProtoBasedVlanMapVlanId.setStatus("current")
_TnVclProtoBasedVlanMapPortMember_Type = PortList
_TnVclProtoBasedVlanMapPortMember_Object = MibTableColumn
tnVclProtoBasedVlanMapPortMember = _TnVclProtoBasedVlanMapPortMember_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 2, 2, 1, 2),
    _TnVclProtoBasedVlanMapPortMember_Type()
)
tnVclProtoBasedVlanMapPortMember.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVclProtoBasedVlanMapPortMember.setStatus("current")
_TnVclProtoBasedVlanMapRowStatus_Type = RowStatus
_TnVclProtoBasedVlanMapRowStatus_Object = MibTableColumn
tnVclProtoBasedVlanMapRowStatus = _TnVclProtoBasedVlanMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 2, 2, 1, 3),
    _TnVclProtoBasedVlanMapRowStatus_Type()
)
tnVclProtoBasedVlanMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVclProtoBasedVlanMapRowStatus.setStatus("current")
_TnVclIpSubnetBasedMgmt_ObjectIdentity = ObjectIdentity
tnVclIpSubnetBasedMgmt = _TnVclIpSubnetBasedMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 3)
)
_TnVclIpSubnetBasedTable_Object = MibTable
tnVclIpSubnetBasedTable = _TnVclIpSubnetBasedTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 3, 1)
)
if mibBuilder.loadTexts:
    tnVclIpSubnetBasedTable.setStatus("current")
_TnVclIpSubnetBasedEntry_Object = MibTableRow
tnVclIpSubnetBasedEntry = _TnVclIpSubnetBasedEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 3, 1, 1)
)
tnVclIpSubnetBasedEntry.setIndexNames(
    (0, "TN-VLAN-MGMT-MIB", "tnVclIpSubnetBasedVceId"),
)
if mibBuilder.loadTexts:
    tnVclIpSubnetBasedEntry.setStatus("current")


class _TnVclIpSubnetBasedVceId_Type(Integer32):
    """Custom type tnVclIpSubnetBasedVceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11111),
    )


_TnVclIpSubnetBasedVceId_Type.__name__ = "Integer32"
_TnVclIpSubnetBasedVceId_Object = MibTableColumn
tnVclIpSubnetBasedVceId = _TnVclIpSubnetBasedVceId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 3, 1, 1, 1),
    _TnVclIpSubnetBasedVceId_Type()
)
tnVclIpSubnetBasedVceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVclIpSubnetBasedVceId.setStatus("current")
_TnVclIpSubnetBasedIpAddr_Type = IpAddress
_TnVclIpSubnetBasedIpAddr_Object = MibTableColumn
tnVclIpSubnetBasedIpAddr = _TnVclIpSubnetBasedIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 3, 1, 1, 2),
    _TnVclIpSubnetBasedIpAddr_Type()
)
tnVclIpSubnetBasedIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVclIpSubnetBasedIpAddr.setStatus("current")
_TnVclIpSubnetBasedMaskLen_Type = Integer32
_TnVclIpSubnetBasedMaskLen_Object = MibTableColumn
tnVclIpSubnetBasedMaskLen = _TnVclIpSubnetBasedMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 3, 1, 1, 3),
    _TnVclIpSubnetBasedMaskLen_Type()
)
tnVclIpSubnetBasedMaskLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVclIpSubnetBasedMaskLen.setStatus("current")
_TnVclIpSubnetBasedVlanId_Type = VlanIndex
_TnVclIpSubnetBasedVlanId_Object = MibTableColumn
tnVclIpSubnetBasedVlanId = _TnVclIpSubnetBasedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 3, 1, 1, 4),
    _TnVclIpSubnetBasedVlanId_Type()
)
tnVclIpSubnetBasedVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVclIpSubnetBasedVlanId.setStatus("current")
_TnVclIpSubnetBasedPortMember_Type = PortList
_TnVclIpSubnetBasedPortMember_Object = MibTableColumn
tnVclIpSubnetBasedPortMember = _TnVclIpSubnetBasedPortMember_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 3, 1, 1, 5),
    _TnVclIpSubnetBasedPortMember_Type()
)
tnVclIpSubnetBasedPortMember.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVclIpSubnetBasedPortMember.setStatus("current")
_TnVclIpSubnetBasedRowStatus_Type = RowStatus
_TnVclIpSubnetBasedRowStatus_Object = MibTableColumn
tnVclIpSubnetBasedRowStatus = _TnVclIpSubnetBasedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 1, 8, 3, 1, 1, 6),
    _TnVclIpSubnetBasedRowStatus_Type()
)
tnVclIpSubnetBasedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVclIpSubnetBasedRowStatus.setStatus("current")
_TnVlanMQoSgmtConformance_ObjectIdentity = ObjectIdentity
tnVlanMQoSgmtConformance = _TnVlanMQoSgmtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 2)
)

# Managed Objects groups


# Notification objects

tnIfSourceAddrChangeEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 4, 0, 1)
)
tnIfSourceAddrChangeEvt.setObjects(
      *(("TN-VLAN-MGMT-MIB", "tnFIDDbMacAddress"),
        ("TN-VLAN-MGMT-MIB", "tnFIDDbConnPort"))
)
if mibBuilder.loadTexts:
    tnIfSourceAddrChangeEvt.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-VLAN-MGMT-MIB",
    **{"TnVlanServiceTranslationType": TnVlanServiceTranslationType,
       "TNVlanListQuarter": TNVlanListQuarter,
       "tnVlanQoSMgmtMIB": tnVlanQoSMgmtMIB,
       "tnVlanQoSMgmtNotifications": tnVlanQoSMgmtNotifications,
       "tnIfSourceAddrChangeEvt": tnIfSourceAddrChangeEvt,
       "tnVlanQoSMgmtObjects": tnVlanQoSMgmtObjects,
       "tnSysVlanMgmt": tnSysVlanMgmt,
       "tnSysManagmentVLANTable": tnSysManagmentVLANTable,
       "tnSysManagmentVLANEntry": tnSysManagmentVLANEntry,
       "tnSysMgmtVLANStatus": tnSysMgmtVLANStatus,
       "tnSysMgmtVLANId": tnSysMgmtVLANId,
       "tnSysMgmtMemberPorts": tnSysMgmtMemberPorts,
       "tnSysVLANExtTable": tnSysVLANExtTable,
       "tnSysVLANExtEntry": tnSysVLANExtEntry,
       "tnSysVlanExtMgmtPortType": tnSysVlanExtMgmtPortType,
       "tnSysVLANExtCustomSTag": tnSysVLANExtCustomSTag,
       "tnVlanConfigGlobalsMainAccessVlans0To1K": tnVlanConfigGlobalsMainAccessVlans0To1K,
       "tnVlanConfigGlobalsMainAccessVlans1KTo2K": tnVlanConfigGlobalsMainAccessVlans1KTo2K,
       "tnVlanConfigGlobalsMainAccessVlans2KTo3K": tnVlanConfigGlobalsMainAccessVlans2KTo3K,
       "tnVlanConfigGlobalsMainAccessVlans3KTo4K": tnVlanConfigGlobalsMainAccessVlans3KTo4K,
       "tnDevSysPriorityMgmt": tnDevSysPriorityMgmt,
       "tnSwIPPrioTable": tnSwIPPrioTable,
       "tnSwIPPrioEntry": tnSwIPPrioEntry,
       "tnSwIPPrioIndex": tnSwIPPrioIndex,
       "tnSwIPPrioTC": tnSwIPPrioTC,
       "tnSwIPPrioRemap": tnSwIPPrioRemap,
       "tnSwIEEEPrioTable": tnSwIEEEPrioTable,
       "tnSwIEEEPrioEntry": tnSwIEEEPrioEntry,
       "tnSwIEEEPriority": tnSwIEEEPriority,
       "tnSwIEEEPriorityRemap": tnSwIEEEPriorityRemap,
       "tnInterfaceQoSMgmt": tnInterfaceQoSMgmt,
       "tnIfPriorityTable": tnIfPriorityTable,
       "tnIfPriorityEntry": tnIfPriorityEntry,
       "tnIfDefaultPriority": tnIfDefaultPriority,
       "tnIfUseIEEEPriority": tnIfUseIEEEPriority,
       "tnIfUseIPPriority": tnIfUseIPPriority,
       "tnIfUseIPOrIEEEPriority": tnIfUseIPOrIEEEPriority,
       "tnIfSrcMACPriorityRemap": tnIfSrcMACPriorityRemap,
       "tnIfDstMACPriorityRemap": tnIfDstMACPriorityRemap,
       "tnIfVIDPriorityRemap": tnIfVIDPriorityRemap,
       "tnIfPriorityRemapTable": tnIfPriorityRemapTable,
       "tnIfPriorityRemapEntry": tnIfPriorityRemapEntry,
       "tnIfUserPriority": tnIfUserPriority,
       "tnIfRemappedPriority": tnIfRemappedPriority,
       "tnInterfaceVlanMgmt": tnInterfaceVlanMgmt,
       "tnIfVLANTable": tnIfVLANTable,
       "tnIfVLANEntry": tnIfVLANEntry,
       "tnIfDot1qState": tnIfDot1qState,
       "tnIfDiscardTagged": tnIfDiscardTagged,
       "tnIfDiscardUntagged": tnIfDiscardUntagged,
       "tnIfDefaultVlanId": tnIfDefaultVlanId,
       "tnIfForceDefaultVlanId": tnIfForceDefaultVlanId,
       "tnIfVLANTagMgmtTable": tnIfVLANTagMgmtTable,
       "tnIfVLANTagMgmtEntry": tnIfVLANTagMgmtEntry,
       "tnIfFrameTagMode": tnIfFrameTagMode,
       "tnIfProviderEtherType": tnIfProviderEtherType,
       "tnIfNetworkModeTagging": tnIfNetworkModeTagging,
       "tnIfVLANTagMgmt2Table": tnIfVLANTagMgmt2Table,
       "tnIfVLANTagMgmt2Entry": tnIfVLANTagMgmt2Entry,
       "tnIfVLANTagMgmt2PortType": tnIfVLANTagMgmt2PortType,
       "tnIfVLANTagMgmt2TxTagType": tnIfVLANTagMgmt2TxTagType,
       "tnIfVLANTagMgmt2ConfigConflicts": tnIfVLANTagMgmt2ConfigConflicts,
       "tnVlanConfigInterfaceMode": tnVlanConfigInterfaceMode,
       "tnVlanConfigInterfaceAllowVlans0KTo1K": tnVlanConfigInterfaceAllowVlans0KTo1K,
       "tnVlanConfigInterfaceAllowVlans1KTo2K": tnVlanConfigInterfaceAllowVlans1KTo2K,
       "tnVlanConfigInterfaceAllowVlans2KTo3K": tnVlanConfigInterfaceAllowVlans2KTo3K,
       "tnVlanConfigInterfaceAllowVlans3KTo4K": tnVlanConfigInterfaceAllowVlans3KTo4K,
       "tnVlanConfigInterfaceForbiddenVlans0KTo1K": tnVlanConfigInterfaceForbiddenVlans0KTo1K,
       "tnVlanConfigInterfaceForbiddenVlans1KTo2K": tnVlanConfigInterfaceForbiddenVlans1KTo2K,
       "tnVlanConfigInterfaceForbiddenVlans2KTo3K": tnVlanConfigInterfaceForbiddenVlans2KTo3K,
       "tnVlanConfigInterfaceForbiddenVlans3KTo4K": tnVlanConfigInterfaceForbiddenVlans3KTo4K,
       "tnVlanServiceMgmt": tnVlanServiceMgmt,
       "tnVlanServiceConnType": tnVlanServiceConnType,
       "tnVlanServiceVIDForTag": tnVlanServiceVIDForTag,
       "tnVlanServiceEtherTypeForTag": tnVlanServiceEtherTypeForTag,
       "tnVlanServiceTranslation": tnVlanServiceTranslation,
       "tnVlanDbMgmt": tnVlanDbMgmt,
       "tnVLANDbTable": tnVLANDbTable,
       "tnVLANDbEntry": tnVLANDbEntry,
       "tnVlanDbVID": tnVlanDbVID,
       "tnVlanDbFID": tnVlanDbFID,
       "tnVlanDbVIDPriOverride": tnVlanDbVIDPriOverride,
       "tnVlanDbVIDPriority": tnVlanDbVIDPriority,
       "tnVlanDbMemTagPort1": tnVlanDbMemTagPort1,
       "tnVlanDbMemTagPort2": tnVlanDbMemTagPort2,
       "tnVlanDbMemTagPort3": tnVlanDbMemTagPort3,
       "tnVlanDbMemTagPort4": tnVlanDbMemTagPort4,
       "tnVlanDbMemTagPort5": tnVlanDbMemTagPort5,
       "tnVlanDbMemTagPort6": tnVlanDbMemTagPort6,
       "tnVlanDbMemTagPort7": tnVlanDbMemTagPort7,
       "tnVlanDbMemTagPort8": tnVlanDbMemTagPort8,
       "tnVlanDbMemTagPort9": tnVlanDbMemTagPort9,
       "tnVlanDbMemTagPort10": tnVlanDbMemTagPort10,
       "tnVlanDbRowStatus": tnVlanDbRowStatus,
       "tnVLANDbFlush": tnVLANDbFlush,
       "tnVLANDbFlushOperation": tnVLANDbFlushOperation,
       "tnVLANDbFlushOperationStatus": tnVLANDbFlushOperationStatus,
       "tnVLANDbFlushOperationFailureReason": tnVLANDbFlushOperationFailureReason,
       "tnFIDDbMgmt": tnFIDDbMgmt,
       "tnFIDDbTable": tnFIDDbTable,
       "tnFIDDbEntry": tnFIDDbEntry,
       "tnFIDDbID": tnFIDDbID,
       "tnFIDDbMacAddress": tnFIDDbMacAddress,
       "tnFIDDbConnPort": tnFIDDbConnPort,
       "tnFIDDbPriority": tnFIDDbPriority,
       "tnFIDDbEntryType": tnFIDDbEntryType,
       "tnFIDDbEntryStatus": tnFIDDbEntryStatus,
       "tnFIDDbFlush": tnFIDDbFlush,
       "tnFIDDbFlushFID": tnFIDDbFlushFID,
       "tnFIDDbFlushOperation": tnFIDDbFlushOperation,
       "tnFIDDbFlushOperationStatus": tnFIDDbFlushOperationStatus,
       "tnFIDDbFlushOperationFailureReason": tnFIDDbFlushOperationFailureReason,
       "tnVclMgmt": tnVclMgmt,
       "tnVclMacBasedMgmt": tnVclMacBasedMgmt,
       "tnVclMacBasedTable": tnVclMacBasedTable,
       "tnVclMacBasedEntry": tnVclMacBasedEntry,
       "tnVclMacBasedMacAddr": tnVclMacBasedMacAddr,
       "tnVclMacBasedVlanId": tnVclMacBasedVlanId,
       "tnVclMacBasedPortMember": tnVclMacBasedPortMember,
       "tnVclMacBasedUser": tnVclMacBasedUser,
       "tnVclMacBasedRowStatus": tnVclMacBasedRowStatus,
       "tnVclProtoBasedMgmt": tnVclProtoBasedMgmt,
       "tnVclProtoBasedGroupMapTable": tnVclProtoBasedGroupMapTable,
       "tnVclProtoBasedGroupMapEntry": tnVclProtoBasedGroupMapEntry,
       "tnVclProtoBasedGroupMapName": tnVclProtoBasedGroupMapName,
       "tnVclProtoBasedGroupMapProtocol": tnVclProtoBasedGroupMapProtocol,
       "tnVclProtoBasedGroupMapEtherTypeVal": tnVclProtoBasedGroupMapEtherTypeVal,
       "tnVclProtoBasedGroupMapSnapOui": tnVclProtoBasedGroupMapSnapOui,
       "tnVclProtoBasedGroupMapSnapPid": tnVclProtoBasedGroupMapSnapPid,
       "tnVclProtoBasedGroupMapLlcDsap": tnVclProtoBasedGroupMapLlcDsap,
       "tnVclProtoBasedGroupMapLlcSsap": tnVclProtoBasedGroupMapLlcSsap,
       "tnVclProtoBasedGroupMapRowStatus": tnVclProtoBasedGroupMapRowStatus,
       "tnVclProtoBasedVlanMapTable": tnVclProtoBasedVlanMapTable,
       "tnVclProtoBasedVlanMapEntry": tnVclProtoBasedVlanMapEntry,
       "tnVclProtoBasedVlanMapVlanId": tnVclProtoBasedVlanMapVlanId,
       "tnVclProtoBasedVlanMapPortMember": tnVclProtoBasedVlanMapPortMember,
       "tnVclProtoBasedVlanMapRowStatus": tnVclProtoBasedVlanMapRowStatus,
       "tnVclIpSubnetBasedMgmt": tnVclIpSubnetBasedMgmt,
       "tnVclIpSubnetBasedTable": tnVclIpSubnetBasedTable,
       "tnVclIpSubnetBasedEntry": tnVclIpSubnetBasedEntry,
       "tnVclIpSubnetBasedVceId": tnVclIpSubnetBasedVceId,
       "tnVclIpSubnetBasedIpAddr": tnVclIpSubnetBasedIpAddr,
       "tnVclIpSubnetBasedMaskLen": tnVclIpSubnetBasedMaskLen,
       "tnVclIpSubnetBasedVlanId": tnVclIpSubnetBasedVlanId,
       "tnVclIpSubnetBasedPortMember": tnVclIpSubnetBasedPortMember,
       "tnVclIpSubnetBasedRowStatus": tnVclIpSubnetBasedRowStatus,
       "tnVlanMQoSgmtConformance": tnVlanMQoSgmtConformance}
)
