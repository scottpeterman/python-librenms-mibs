# SNMP MIB module (TN-LACP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-LACP
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:44 2025
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

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(TNInterfaceIndex,
 TNUnsigned16,
 TNUnsigned8) = mibBuilder.importSymbols(
    "TN-TC",
    "TNInterfaceIndex",
    "TNUnsigned16",
    "TNUnsigned8")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnLacpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35)
)
if mibBuilder.loadTexts:
    tnLacpMib.setRevisions(
        ("2015-07-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnLacpConfigPortTable_Object = MibTable
tnLacpConfigPortTable = _TnLacpConfigPortTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 1)
)
if mibBuilder.loadTexts:
    tnLacpConfigPortTable.setStatus("current")
_TnLacpConfigPortEntry_Object = MibTableRow
tnLacpConfigPortEntry = _TnLacpConfigPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 1, 1)
)
tnLacpConfigPortEntry.setIndexNames(
    (0, "TN-LACP-MIB", "tnLacpConfigPortInterfaceNo"),
)
if mibBuilder.loadTexts:
    tnLacpConfigPortEntry.setStatus("current")
_TnLacpConfigPortInterfaceNo_Type = TNInterfaceIndex
_TnLacpConfigPortInterfaceNo_Object = MibTableColumn
tnLacpConfigPortInterfaceNo = _TnLacpConfigPortInterfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 1, 1, 1),
    _TnLacpConfigPortInterfaceNo_Type()
)
tnLacpConfigPortInterfaceNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLacpConfigPortInterfaceNo.setStatus("current")


class _TnLacpConfigPortDot3adAggrActorAdminMode_Type(Integer32):
    """Custom type tnLacpConfigPortDot3adAggrActorAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TnLacpConfigPortDot3adAggrActorAdminMode_Type.__name__ = "Integer32"
_TnLacpConfigPortDot3adAggrActorAdminMode_Object = MibTableColumn
tnLacpConfigPortDot3adAggrActorAdminMode = _TnLacpConfigPortDot3adAggrActorAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 1, 1, 2),
    _TnLacpConfigPortDot3adAggrActorAdminMode_Type()
)
tnLacpConfigPortDot3adAggrActorAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLacpConfigPortDot3adAggrActorAdminMode.setStatus("current")


class _TnLacpConfigPortDot3adAggrActorKeyMode_Type(Integer32):
    """Custom type tnLacpConfigPortDot3adAggrActorKeyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("specific", 1))
    )


_TnLacpConfigPortDot3adAggrActorKeyMode_Type.__name__ = "Integer32"
_TnLacpConfigPortDot3adAggrActorKeyMode_Object = MibTableColumn
tnLacpConfigPortDot3adAggrActorKeyMode = _TnLacpConfigPortDot3adAggrActorKeyMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 1, 1, 3),
    _TnLacpConfigPortDot3adAggrActorKeyMode_Type()
)
tnLacpConfigPortDot3adAggrActorKeyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLacpConfigPortDot3adAggrActorKeyMode.setStatus("current")
_TnLacpConfigPortDot3adAggrActorAdminKey_Type = Unsigned32
_TnLacpConfigPortDot3adAggrActorAdminKey_Object = MibTableColumn
tnLacpConfigPortDot3adAggrActorAdminKey = _TnLacpConfigPortDot3adAggrActorAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 1, 1, 4),
    _TnLacpConfigPortDot3adAggrActorAdminKey_Type()
)
tnLacpConfigPortDot3adAggrActorAdminKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLacpConfigPortDot3adAggrActorAdminKey.setStatus("current")


class _TnLacpConfigPortDot3adAggrRole_Type(Integer32):
    """Custom type tnLacpConfigPortDot3adAggrRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("passive", 0),
          ("active", 1))
    )


_TnLacpConfigPortDot3adAggrRole_Type.__name__ = "Integer32"
_TnLacpConfigPortDot3adAggrRole_Object = MibTableColumn
tnLacpConfigPortDot3adAggrRole = _TnLacpConfigPortDot3adAggrRole_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 1, 1, 5),
    _TnLacpConfigPortDot3adAggrRole_Type()
)
tnLacpConfigPortDot3adAggrRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLacpConfigPortDot3adAggrRole.setStatus("current")


class _TnLacpConfigPortDot3adAggrTimeout_Type(Integer32):
    """Custom type tnLacpConfigPortDot3adAggrTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("slow", 0),
          ("fast", 1))
    )


_TnLacpConfigPortDot3adAggrTimeout_Type.__name__ = "Integer32"
_TnLacpConfigPortDot3adAggrTimeout_Object = MibTableColumn
tnLacpConfigPortDot3adAggrTimeout = _TnLacpConfigPortDot3adAggrTimeout_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 1, 1, 6),
    _TnLacpConfigPortDot3adAggrTimeout_Type()
)
tnLacpConfigPortDot3adAggrTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLacpConfigPortDot3adAggrTimeout.setStatus("current")


class _TnLacpConfigPortDot3adAggrPortPriority_Type(Unsigned32):
    """Custom type tnLacpConfigPortDot3adAggrPortPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnLacpConfigPortDot3adAggrPortPriority_Type.__name__ = "Unsigned32"
_TnLacpConfigPortDot3adAggrPortPriority_Object = MibTableColumn
tnLacpConfigPortDot3adAggrPortPriority = _TnLacpConfigPortDot3adAggrPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 1, 1, 7),
    _TnLacpConfigPortDot3adAggrPortPriority_Type()
)
tnLacpConfigPortDot3adAggrPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLacpConfigPortDot3adAggrPortPriority.setStatus("current")
_TnLacpStatusSystemTable_Object = MibTable
tnLacpStatusSystemTable = _TnLacpStatusSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 2)
)
if mibBuilder.loadTexts:
    tnLacpStatusSystemTable.setStatus("current")
_TnLacpStatusSystemEntry_Object = MibTableRow
tnLacpStatusSystemEntry = _TnLacpStatusSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 2, 1)
)
tnLacpStatusSystemEntry.setIndexNames(
    (0, "TN-LACP-MIB", "tnLacpStatusSystemDot3adAggrID"),
)
if mibBuilder.loadTexts:
    tnLacpStatusSystemEntry.setStatus("current")


class _TnLacpStatusSystemDot3adAggrID_Type(DisplayString):
    """Custom type tnLacpStatusSystemDot3adAggrID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TnLacpStatusSystemDot3adAggrID_Type.__name__ = "DisplayString"
_TnLacpStatusSystemDot3adAggrID_Object = MibTableColumn
tnLacpStatusSystemDot3adAggrID = _TnLacpStatusSystemDot3adAggrID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 2, 1, 1),
    _TnLacpStatusSystemDot3adAggrID_Type()
)
tnLacpStatusSystemDot3adAggrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLacpStatusSystemDot3adAggrID.setStatus("current")
_TnLacpStatusSystemDot3adAggrPartnerSystemID_Type = MacAddress
_TnLacpStatusSystemDot3adAggrPartnerSystemID_Object = MibTableColumn
tnLacpStatusSystemDot3adAggrPartnerSystemID = _TnLacpStatusSystemDot3adAggrPartnerSystemID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 2, 1, 2),
    _TnLacpStatusSystemDot3adAggrPartnerSystemID_Type()
)
tnLacpStatusSystemDot3adAggrPartnerSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLacpStatusSystemDot3adAggrPartnerSystemID.setStatus("current")
_TnLacpStatusSystemDot3adAggrPartnerOperKey_Type = TNUnsigned16
_TnLacpStatusSystemDot3adAggrPartnerOperKey_Object = MibTableColumn
tnLacpStatusSystemDot3adAggrPartnerOperKey = _TnLacpStatusSystemDot3adAggrPartnerOperKey_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 2, 1, 3),
    _TnLacpStatusSystemDot3adAggrPartnerOperKey_Type()
)
tnLacpStatusSystemDot3adAggrPartnerOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLacpStatusSystemDot3adAggrPartnerOperKey.setStatus("current")
_TnLacpStatusSystemDot3adAggrPartnerOperSystemPriority_Type = TNUnsigned16
_TnLacpStatusSystemDot3adAggrPartnerOperSystemPriority_Object = MibTableColumn
tnLacpStatusSystemDot3adAggrPartnerOperSystemPriority = _TnLacpStatusSystemDot3adAggrPartnerOperSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 2, 1, 4),
    _TnLacpStatusSystemDot3adAggrPartnerOperSystemPriority_Type()
)
tnLacpStatusSystemDot3adAggrPartnerOperSystemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLacpStatusSystemDot3adAggrPartnerOperSystemPriority.setStatus("current")
_TnLacpStatusSystemDot3adAggrPartnerStateLastChanged_Type = Unsigned32
_TnLacpStatusSystemDot3adAggrPartnerStateLastChanged_Object = MibTableColumn
tnLacpStatusSystemDot3adAggrPartnerStateLastChanged = _TnLacpStatusSystemDot3adAggrPartnerStateLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 2, 1, 5),
    _TnLacpStatusSystemDot3adAggrPartnerStateLastChanged_Type()
)
tnLacpStatusSystemDot3adAggrPartnerStateLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLacpStatusSystemDot3adAggrPartnerStateLastChanged.setStatus("current")
_TnLacpStatusSystemDot3adAggrLocalPorts_Type = PortList
_TnLacpStatusSystemDot3adAggrLocalPorts_Object = MibTableColumn
tnLacpStatusSystemDot3adAggrLocalPorts = _TnLacpStatusSystemDot3adAggrLocalPorts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 2, 1, 6),
    _TnLacpStatusSystemDot3adAggrLocalPorts_Type()
)
tnLacpStatusSystemDot3adAggrLocalPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLacpStatusSystemDot3adAggrLocalPorts.setStatus("current")
_TnLacpStatusPortTable_Object = MibTable
tnLacpStatusPortTable = _TnLacpStatusPortTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 3)
)
if mibBuilder.loadTexts:
    tnLacpStatusPortTable.setStatus("current")
_TnLacpStatusPortEntry_Object = MibTableRow
tnLacpStatusPortEntry = _TnLacpStatusPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 3, 1)
)
tnLacpStatusPortEntry.setIndexNames(
    (0, "TN-LACP-MIB", "tnLacpStatusPortInterfaceNo"),
)
if mibBuilder.loadTexts:
    tnLacpStatusPortEntry.setStatus("current")
_TnLacpStatusPortInterfaceNo_Type = TNInterfaceIndex
_TnLacpStatusPortInterfaceNo_Object = MibTableColumn
tnLacpStatusPortInterfaceNo = _TnLacpStatusPortInterfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 3, 1, 1),
    _TnLacpStatusPortInterfaceNo_Type()
)
tnLacpStatusPortInterfaceNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLacpStatusPortInterfaceNo.setStatus("current")


class _TnLacpStatusPortDot3adAggrActorAdminMode_Type(Integer32):
    """Custom type tnLacpStatusPortDot3adAggrActorAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TnLacpStatusPortDot3adAggrActorAdminMode_Type.__name__ = "Integer32"
_TnLacpStatusPortDot3adAggrActorAdminMode_Object = MibTableColumn
tnLacpStatusPortDot3adAggrActorAdminMode = _TnLacpStatusPortDot3adAggrActorAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 3, 1, 2),
    _TnLacpStatusPortDot3adAggrActorAdminMode_Type()
)
tnLacpStatusPortDot3adAggrActorAdminMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLacpStatusPortDot3adAggrActorAdminMode.setStatus("current")
_TnLacpStatusPortDot3adAggrActorAdminKey_Type = Integer32
_TnLacpStatusPortDot3adAggrActorAdminKey_Object = MibTableColumn
tnLacpStatusPortDot3adAggrActorAdminKey = _TnLacpStatusPortDot3adAggrActorAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 3, 1, 3),
    _TnLacpStatusPortDot3adAggrActorAdminKey_Type()
)
tnLacpStatusPortDot3adAggrActorAdminKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLacpStatusPortDot3adAggrActorAdminKey.setStatus("current")


class _TnLacpStatusPortDot3adAggrActorID_Type(DisplayString):
    """Custom type tnLacpStatusPortDot3adAggrActorID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TnLacpStatusPortDot3adAggrActorID_Type.__name__ = "DisplayString"
_TnLacpStatusPortDot3adAggrActorID_Object = MibTableColumn
tnLacpStatusPortDot3adAggrActorID = _TnLacpStatusPortDot3adAggrActorID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 3, 1, 4),
    _TnLacpStatusPortDot3adAggrActorID_Type()
)
tnLacpStatusPortDot3adAggrActorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLacpStatusPortDot3adAggrActorID.setStatus("current")
_TnLacpStatusPortDot3adAggrPartnerSystemID_Type = MacAddress
_TnLacpStatusPortDot3adAggrPartnerSystemID_Object = MibTableColumn
tnLacpStatusPortDot3adAggrPartnerSystemID = _TnLacpStatusPortDot3adAggrPartnerSystemID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 3, 1, 5),
    _TnLacpStatusPortDot3adAggrPartnerSystemID_Type()
)
tnLacpStatusPortDot3adAggrPartnerSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLacpStatusPortDot3adAggrPartnerSystemID.setStatus("current")
_TnLacpStatusPortDot3adAggrPartnerOperPortIndex_Type = Integer32
_TnLacpStatusPortDot3adAggrPartnerOperPortIndex_Object = MibTableColumn
tnLacpStatusPortDot3adAggrPartnerOperPortIndex = _TnLacpStatusPortDot3adAggrPartnerOperPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 3, 1, 6),
    _TnLacpStatusPortDot3adAggrPartnerOperPortIndex_Type()
)
tnLacpStatusPortDot3adAggrPartnerOperPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLacpStatusPortDot3adAggrPartnerOperPortIndex.setStatus("current")
_TnLacpStatusPortDot3adAggrPartnerOperPortPriority_Type = TNUnsigned16
_TnLacpStatusPortDot3adAggrPartnerOperPortPriority_Object = MibTableColumn
tnLacpStatusPortDot3adAggrPartnerOperPortPriority = _TnLacpStatusPortDot3adAggrPartnerOperPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 3, 1, 7),
    _TnLacpStatusPortDot3adAggrPartnerOperPortPriority_Type()
)
tnLacpStatusPortDot3adAggrPartnerOperPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLacpStatusPortDot3adAggrPartnerOperPortPriority.setStatus("current")
_TnLacpStatisticsPortTable_Object = MibTable
tnLacpStatisticsPortTable = _TnLacpStatisticsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 4)
)
if mibBuilder.loadTexts:
    tnLacpStatisticsPortTable.setStatus("current")
_TnLacpStatisticsPortEntry_Object = MibTableRow
tnLacpStatisticsPortEntry = _TnLacpStatisticsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 4, 1)
)
tnLacpStatisticsPortEntry.setIndexNames(
    (0, "TN-LACP-MIB", "tnLacpStatisticsPortInterfaceNo"),
)
if mibBuilder.loadTexts:
    tnLacpStatisticsPortEntry.setStatus("current")
_TnLacpStatisticsPortInterfaceNo_Type = TNInterfaceIndex
_TnLacpStatisticsPortInterfaceNo_Object = MibTableColumn
tnLacpStatisticsPortInterfaceNo = _TnLacpStatisticsPortInterfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 4, 1, 1),
    _TnLacpStatisticsPortInterfaceNo_Type()
)
tnLacpStatisticsPortInterfaceNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLacpStatisticsPortInterfaceNo.setStatus("current")
_TnLacpStatisticsPortDot3adAggrRxFrames_Type = Unsigned32
_TnLacpStatisticsPortDot3adAggrRxFrames_Object = MibTableColumn
tnLacpStatisticsPortDot3adAggrRxFrames = _TnLacpStatisticsPortDot3adAggrRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 4, 1, 2),
    _TnLacpStatisticsPortDot3adAggrRxFrames_Type()
)
tnLacpStatisticsPortDot3adAggrRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLacpStatisticsPortDot3adAggrRxFrames.setStatus("current")
_TnLacpStatisticsPortDot3adAggrTxFrames_Type = Unsigned32
_TnLacpStatisticsPortDot3adAggrTxFrames_Object = MibTableColumn
tnLacpStatisticsPortDot3adAggrTxFrames = _TnLacpStatisticsPortDot3adAggrTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 4, 1, 3),
    _TnLacpStatisticsPortDot3adAggrTxFrames_Type()
)
tnLacpStatisticsPortDot3adAggrTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLacpStatisticsPortDot3adAggrTxFrames.setStatus("current")
_TnLacpStatisticsPortDot3adAggrRxUnknownFrames_Type = Unsigned32
_TnLacpStatisticsPortDot3adAggrRxUnknownFrames_Object = MibTableColumn
tnLacpStatisticsPortDot3adAggrRxUnknownFrames = _TnLacpStatisticsPortDot3adAggrRxUnknownFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 4, 1, 4),
    _TnLacpStatisticsPortDot3adAggrRxUnknownFrames_Type()
)
tnLacpStatisticsPortDot3adAggrRxUnknownFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLacpStatisticsPortDot3adAggrRxUnknownFrames.setStatus("current")
_TnLacpStatisticsPortDot3adAggrRxIllegalFrames_Type = Unsigned32
_TnLacpStatisticsPortDot3adAggrRxIllegalFrames_Object = MibTableColumn
tnLacpStatisticsPortDot3adAggrRxIllegalFrames = _TnLacpStatisticsPortDot3adAggrRxIllegalFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 35, 4, 1, 5),
    _TnLacpStatisticsPortDot3adAggrRxIllegalFrames_Type()
)
tnLacpStatisticsPortDot3adAggrRxIllegalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLacpStatisticsPortDot3adAggrRxIllegalFrames.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-LACP-MIB",
    **{"tnLacpMib": tnLacpMib,
       "tnLacpConfigPortTable": tnLacpConfigPortTable,
       "tnLacpConfigPortEntry": tnLacpConfigPortEntry,
       "tnLacpConfigPortInterfaceNo": tnLacpConfigPortInterfaceNo,
       "tnLacpConfigPortDot3adAggrActorAdminMode": tnLacpConfigPortDot3adAggrActorAdminMode,
       "tnLacpConfigPortDot3adAggrActorKeyMode": tnLacpConfigPortDot3adAggrActorKeyMode,
       "tnLacpConfigPortDot3adAggrActorAdminKey": tnLacpConfigPortDot3adAggrActorAdminKey,
       "tnLacpConfigPortDot3adAggrRole": tnLacpConfigPortDot3adAggrRole,
       "tnLacpConfigPortDot3adAggrTimeout": tnLacpConfigPortDot3adAggrTimeout,
       "tnLacpConfigPortDot3adAggrPortPriority": tnLacpConfigPortDot3adAggrPortPriority,
       "tnLacpStatusSystemTable": tnLacpStatusSystemTable,
       "tnLacpStatusSystemEntry": tnLacpStatusSystemEntry,
       "tnLacpStatusSystemDot3adAggrID": tnLacpStatusSystemDot3adAggrID,
       "tnLacpStatusSystemDot3adAggrPartnerSystemID": tnLacpStatusSystemDot3adAggrPartnerSystemID,
       "tnLacpStatusSystemDot3adAggrPartnerOperKey": tnLacpStatusSystemDot3adAggrPartnerOperKey,
       "tnLacpStatusSystemDot3adAggrPartnerOperSystemPriority": tnLacpStatusSystemDot3adAggrPartnerOperSystemPriority,
       "tnLacpStatusSystemDot3adAggrPartnerStateLastChanged": tnLacpStatusSystemDot3adAggrPartnerStateLastChanged,
       "tnLacpStatusSystemDot3adAggrLocalPorts": tnLacpStatusSystemDot3adAggrLocalPorts,
       "tnLacpStatusPortTable": tnLacpStatusPortTable,
       "tnLacpStatusPortEntry": tnLacpStatusPortEntry,
       "tnLacpStatusPortInterfaceNo": tnLacpStatusPortInterfaceNo,
       "tnLacpStatusPortDot3adAggrActorAdminMode": tnLacpStatusPortDot3adAggrActorAdminMode,
       "tnLacpStatusPortDot3adAggrActorAdminKey": tnLacpStatusPortDot3adAggrActorAdminKey,
       "tnLacpStatusPortDot3adAggrActorID": tnLacpStatusPortDot3adAggrActorID,
       "tnLacpStatusPortDot3adAggrPartnerSystemID": tnLacpStatusPortDot3adAggrPartnerSystemID,
       "tnLacpStatusPortDot3adAggrPartnerOperPortIndex": tnLacpStatusPortDot3adAggrPartnerOperPortIndex,
       "tnLacpStatusPortDot3adAggrPartnerOperPortPriority": tnLacpStatusPortDot3adAggrPartnerOperPortPriority,
       "tnLacpStatisticsPortTable": tnLacpStatisticsPortTable,
       "tnLacpStatisticsPortEntry": tnLacpStatisticsPortEntry,
       "tnLacpStatisticsPortInterfaceNo": tnLacpStatisticsPortInterfaceNo,
       "tnLacpStatisticsPortDot3adAggrRxFrames": tnLacpStatisticsPortDot3adAggrRxFrames,
       "tnLacpStatisticsPortDot3adAggrTxFrames": tnLacpStatisticsPortDot3adAggrTxFrames,
       "tnLacpStatisticsPortDot3adAggrRxUnknownFrames": tnLacpStatisticsPortDot3adAggrRxUnknownFrames,
       "tnLacpStatisticsPortDot3adAggrRxIllegalFrames": tnLacpStatisticsPortDot3adAggrRxIllegalFrames}
)
