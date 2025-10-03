# SNMP MIB module (TN-TT-LOOP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-TT-LOOP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:33 2025
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

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnTtLoopMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 149)
)
if mibBuilder.loadTexts:
    tnTtLoopMib.setRevisions(
        ("2015-07-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TNTtLoopInstanceAdminState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("adminDisabled", 0),
          ("adminEnabled", 1))
    )



class TNTtLoopInstanceDomain(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 0),
          ("evc", 1),
          ("vlan", 2))
    )



class TNTtLoopInstanceDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("facility", 0),
          ("terminal", 1))
    )



class TNTtLoopInstanceSubscriber(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("all", 1),
          ("test", 2))
    )



class TNTtLoopInstanceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("macLoop", 0),
          ("oamLoop", 1))
    )



class TNTtLoopInstanceOperState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("operDown", 0),
          ("operUp", 1))
    )



# MIB Managed Objects in the order of their OIDs

_TnTtLoopCapabilitiesInstanceMax_Type = Unsigned32
_TnTtLoopCapabilitiesInstanceMax_Object = MibScalar
tnTtLoopCapabilitiesInstanceMax = _TnTtLoopCapabilitiesInstanceMax_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 149, 1),
    _TnTtLoopCapabilitiesInstanceMax_Type()
)
tnTtLoopCapabilitiesInstanceMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTtLoopCapabilitiesInstanceMax.setStatus("current")
_TnTtLoopCapabilitiesNameMax_Type = Unsigned32
_TnTtLoopCapabilitiesNameMax_Object = MibScalar
tnTtLoopCapabilitiesNameMax = _TnTtLoopCapabilitiesNameMax_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 149, 2),
    _TnTtLoopCapabilitiesNameMax_Type()
)
tnTtLoopCapabilitiesNameMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTtLoopCapabilitiesNameMax.setStatus("current")
_TnTtLoopConfigInstanceTable_Object = MibTable
tnTtLoopConfigInstanceTable = _TnTtLoopConfigInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 149, 3)
)
if mibBuilder.loadTexts:
    tnTtLoopConfigInstanceTable.setStatus("current")
_TnTtLoopConfigInstanceEntry_Object = MibTableRow
tnTtLoopConfigInstanceEntry = _TnTtLoopConfigInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 149, 3, 1)
)
tnTtLoopConfigInstanceEntry.setIndexNames(
    (0, "TN-TT-LOOP-MIB", "tnTtLoopConfigInstanceId"),
)
if mibBuilder.loadTexts:
    tnTtLoopConfigInstanceEntry.setStatus("current")


class _TnTtLoopConfigInstanceName_Type(DisplayString):
    """Custom type tnTtLoopConfigInstanceName based on DisplayString"""
    defaultValue = OctetString("TRAFFIC_TEST_LOOP_INSTANCE")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnTtLoopConfigInstanceName_Type.__name__ = "DisplayString"
_TnTtLoopConfigInstanceName_Object = MibTableColumn
tnTtLoopConfigInstanceName = _TnTtLoopConfigInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 149, 3, 1, 1),
    _TnTtLoopConfigInstanceName_Type()
)
tnTtLoopConfigInstanceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTtLoopConfigInstanceName.setStatus("current")
_TnTtLoopConfigInstanceDomain_Type = TNTtLoopInstanceDomain
_TnTtLoopConfigInstanceDomain_Object = MibTableColumn
tnTtLoopConfigInstanceDomain = _TnTtLoopConfigInstanceDomain_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 149, 3, 1, 2),
    _TnTtLoopConfigInstanceDomain_Type()
)
tnTtLoopConfigInstanceDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTtLoopConfigInstanceDomain.setStatus("current")
_TnTtLoopConfigInstanceType_Type = TNTtLoopInstanceType
_TnTtLoopConfigInstanceType_Object = MibTableColumn
tnTtLoopConfigInstanceType = _TnTtLoopConfigInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 149, 3, 1, 3),
    _TnTtLoopConfigInstanceType_Type()
)
tnTtLoopConfigInstanceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTtLoopConfigInstanceType.setStatus("current")
_TnTtLoopConfigInstanceDirection_Type = TNTtLoopInstanceDirection
_TnTtLoopConfigInstanceDirection_Object = MibTableColumn
tnTtLoopConfigInstanceDirection = _TnTtLoopConfigInstanceDirection_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 149, 3, 1, 4),
    _TnTtLoopConfigInstanceDirection_Type()
)
tnTtLoopConfigInstanceDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTtLoopConfigInstanceDirection.setStatus("current")


class _TnTtLoopConfigInstanceFlow_Type(InterfaceIndex):
    """Custom type tnTtLoopConfigInstanceFlow based on InterfaceIndex"""
    defaultValue = 1


_TnTtLoopConfigInstanceFlow_Type.__name__ = "InterfaceIndex"
_TnTtLoopConfigInstanceFlow_Object = MibTableColumn
tnTtLoopConfigInstanceFlow = _TnTtLoopConfigInstanceFlow_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 149, 3, 1, 5),
    _TnTtLoopConfigInstanceFlow_Type()
)
tnTtLoopConfigInstanceFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTtLoopConfigInstanceFlow.setStatus("current")


class _TnTtLoopConfigInstancePort_Type(InterfaceIndex):
    """Custom type tnTtLoopConfigInstancePort based on InterfaceIndex"""
    defaultValue = 1


_TnTtLoopConfigInstancePort_Type.__name__ = "InterfaceIndex"
_TnTtLoopConfigInstancePort_Object = MibTableColumn
tnTtLoopConfigInstancePort = _TnTtLoopConfigInstancePort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 149, 3, 1, 6),
    _TnTtLoopConfigInstancePort_Type()
)
tnTtLoopConfigInstancePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTtLoopConfigInstancePort.setStatus("current")
_TnTtLoopConfigInstanceLevel_Type = Unsigned32
_TnTtLoopConfigInstanceLevel_Object = MibTableColumn
tnTtLoopConfigInstanceLevel = _TnTtLoopConfigInstanceLevel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 149, 3, 1, 7),
    _TnTtLoopConfigInstanceLevel_Type()
)
tnTtLoopConfigInstanceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTtLoopConfigInstanceLevel.setStatus("current")
_TnTtLoopConfigInstanceSubscriber_Type = TNTtLoopInstanceSubscriber
_TnTtLoopConfigInstanceSubscriber_Object = MibTableColumn
tnTtLoopConfigInstanceSubscriber = _TnTtLoopConfigInstanceSubscriber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 149, 3, 1, 8),
    _TnTtLoopConfigInstanceSubscriber_Type()
)
tnTtLoopConfigInstanceSubscriber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTtLoopConfigInstanceSubscriber.setStatus("current")
_TnTtLoopStatusInstanceOperState_Type = TNTtLoopInstanceOperState
_TnTtLoopStatusInstanceOperState_Object = MibTableColumn
tnTtLoopStatusInstanceOperState = _TnTtLoopStatusInstanceOperState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 149, 3, 1, 9),
    _TnTtLoopStatusInstanceOperState_Type()
)
tnTtLoopStatusInstanceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTtLoopStatusInstanceOperState.setStatus("current")
_TnTtLoopConfigInstanceAdminState_Type = TNTtLoopInstanceAdminState
_TnTtLoopConfigInstanceAdminState_Object = MibTableColumn
tnTtLoopConfigInstanceAdminState = _TnTtLoopConfigInstanceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 149, 3, 1, 10),
    _TnTtLoopConfigInstanceAdminState_Type()
)
tnTtLoopConfigInstanceAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTtLoopConfigInstanceAdminState.setStatus("current")


class _TnTtLoopConfigInstanceAction_Type(Integer32):
    """Custom type tnTtLoopConfigInstanceAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("save", 1),
          ("delete", 2))
    )


_TnTtLoopConfigInstanceAction_Type.__name__ = "Integer32"
_TnTtLoopConfigInstanceAction_Object = MibTableColumn
tnTtLoopConfigInstanceAction = _TnTtLoopConfigInstanceAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 149, 3, 1, 11),
    _TnTtLoopConfigInstanceAction_Type()
)
tnTtLoopConfigInstanceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTtLoopConfigInstanceAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-TT-LOOP-MIB",
    **{"TNTtLoopInstanceAdminState": TNTtLoopInstanceAdminState,
       "TNTtLoopInstanceDomain": TNTtLoopInstanceDomain,
       "TNTtLoopInstanceDirection": TNTtLoopInstanceDirection,
       "TNTtLoopInstanceSubscriber": TNTtLoopInstanceSubscriber,
       "TNTtLoopInstanceType": TNTtLoopInstanceType,
       "TNTtLoopInstanceOperState": TNTtLoopInstanceOperState,
       "tnTtLoopMib": tnTtLoopMib,
       "tnTtLoopCapabilitiesInstanceMax": tnTtLoopCapabilitiesInstanceMax,
       "tnTtLoopCapabilitiesNameMax": tnTtLoopCapabilitiesNameMax,
       "tnTtLoopConfigInstanceTable": tnTtLoopConfigInstanceTable,
       "tnTtLoopConfigInstanceEntry": tnTtLoopConfigInstanceEntry,
       "tnTtLoopConfigInstanceName": tnTtLoopConfigInstanceName,
       "tnTtLoopConfigInstanceDomain": tnTtLoopConfigInstanceDomain,
       "tnTtLoopConfigInstanceType": tnTtLoopConfigInstanceType,
       "tnTtLoopConfigInstanceDirection": tnTtLoopConfigInstanceDirection,
       "tnTtLoopConfigInstanceFlow": tnTtLoopConfigInstanceFlow,
       "tnTtLoopConfigInstancePort": tnTtLoopConfigInstancePort,
       "tnTtLoopConfigInstanceLevel": tnTtLoopConfigInstanceLevel,
       "tnTtLoopConfigInstanceSubscriber": tnTtLoopConfigInstanceSubscriber,
       "tnTtLoopStatusInstanceOperState": tnTtLoopStatusInstanceOperState,
       "tnTtLoopConfigInstanceAdminState": tnTtLoopConfigInstanceAdminState,
       "tnTtLoopConfigInstanceAction": tnTtLoopConfigInstanceAction}
)
